#!/usr/bin/env python3
"""Tests for erasure_helper.py, using small mock data packages.

Run from this folder:  python3 -m unittest test_erasure_helper -v
Uses only the standard library. Nothing here touches real data.
"""

import csv
import json
import os
import subprocess
import sys
import tempfile
import unittest
import zipfile

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "erasure_helper.py")

DM = "111111111111111111"
SERVER = "222222222222222222"
GROUP = "333333333333333333"


def run(*args):
    """Run the script and return (exit code, stdout, stderr)."""
    p = subprocess.run([sys.executable, SCRIPT, *args],
                       capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def json_files(channels, folder="Messages"):
    """{channel_id: (type, [ids])} -> {path: bytes} in the current JSON layout."""
    files = {f"{folder}/index.json": json.dumps({c: f"name-{c}" for c in channels}).encode()}
    for cid, (ctype, ids) in channels.items():
        files[f"{folder}/c{cid}/channel.json"] = json.dumps({"id": cid, "type": ctype}).encode()
        files[f"{folder}/c{cid}/messages.json"] = json.dumps(
            [{"ID": int(m), "Timestamp": "2026-01-01", "Contents": "x", "Attachments": ""}
             for m in ids]).encode()
    return files


def make_zip(path, files):
    with zipfile.ZipFile(path, "w") as z:
        for name, data in files.items():
            z.writestr(name, data)
    return path


def make_dir(path, files):
    for name, data in files.items():
        full = os.path.join(path, *name.split("/"))
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "wb") as fh:
            fh.write(data)
    return path


def read_bytes(path):
    with open(path, "rb") as fh:
        return fh.read()


def read_rows(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.reader(fh))


class HelperTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.d = self.tmp.name
        self.old = make_zip(os.path.join(self.d, "old.zip"), json_files({
            DM: (1, ["1001", "1002", "1003"]),
            SERVER: (0, ["2001", "2002"]),
            GROUP: (3, ["3001"]),
        }))
        self.new = make_zip(os.path.join(self.d, "new.zip"), json_files({
            DM: (1, ["1001", "1002", "1003", "1004"]),
            SERVER: (0, []),
        }))

    def tearDown(self):
        self.tmp.cleanup()

    def p(self, name):
        return os.path.join(self.d, name)

    # --- reading packages -------------------------------------------------

    def test_json_package_csv(self):
        code, out, _ = run("csv", self.old, "-o", self.p("out.csv"))
        self.assertEqual(code, 0)
        rows = read_rows(self.p("out.csv"))
        self.assertEqual(rows[0], ["channel_id", "message_id"])
        self.assertEqual(len(rows) - 1, 6)
        self.assertIn([DM, "1001"], rows)

    def test_summary_counts(self):
        code, out, _ = run("summary", self.new)
        self.assertEqual(code, 0)
        self.assertIn("DM", out)
        self.assertRegex(out, r"GUILD_TEXT\s+1\s+0")   # empty channel still listed
        self.assertRegex(out, r"TOTAL\s+2\s+4")

    def test_older_csv_layout(self):
        files = {
            "messages/index.json": json.dumps({DM: "x"}).encode(),
            f"messages/{DM}/channel.json": json.dumps({"id": DM, "type": 1}).encode(),
            f"messages/{DM}/messages.csv": b"ID,Timestamp,Contents,Attachments\n5001,t,\"a, b\",\n5002,t,c,\n",
        }
        pkg = make_zip(self.p("oldformat.zip"), files)
        code, _, _ = run("csv", pkg, "-o", self.p("o.csv"))
        self.assertEqual(code, 0)
        self.assertEqual(read_rows(self.p("o.csv"))[1:], [[DM, "5001"], [DM, "5002"]])

    def test_extracted_folder_with_extra_root(self):
        folder = make_dir(self.p("extracted"), {f"package/{k}": v for k, v in
                                               json_files({DM: (1, ["1"])}).items()})
        code, out, _ = run("summary", folder)
        self.assertEqual(code, 0)
        self.assertRegex(out, r"TOTAL\s+1\s+1")

    def test_lowercase_messages_folder(self):
        pkg = make_zip(self.p("lower.zip"), json_files({DM: (1, ["1"])}, folder="messages"))
        code, out, _ = run("summary", pkg)
        self.assertEqual(code, 0)

    # --- failing visibly --------------------------------------------------

    def test_malformed_json_is_an_error(self):
        files = json_files({DM: (1, ["1"])})
        files[f"Messages/c{DM}/messages.json"] = b"[{not json"
        pkg = make_zip(self.p("bad.zip"), files)
        code, _, err = run("summary", pkg)
        self.assertNotEqual(code, 0)
        self.assertIn("isn't valid JSON", err)

    def test_unexpected_structure_is_an_error(self):
        files = json_files({DM: (1, ["1"])})
        files[f"Messages/c{DM}/messages.json"] = json.dumps({"messages": [{"ID": 1}]}).encode()
        pkg = make_zip(self.p("dict.zip"), files)
        code, _, err = run("csv", pkg, "-o", self.p("x.csv"))
        self.assertNotEqual(code, 0)
        self.assertIn("doesn't contain a list", err)
        self.assertFalse(os.path.exists(self.p("x.csv")))

    def test_records_without_ids_are_an_error(self):
        files = json_files({DM: (1, ["1"])})
        files[f"Messages/c{DM}/messages.json"] = json.dumps([{"MessageId": 1}]).encode()
        pkg = make_zip(self.p("noid.zip"), files)
        code, _, err = run("summary", pkg)
        self.assertNotEqual(code, 0)
        self.assertIn("has a message ID", err)

    def test_skipped_records_stop_the_run(self):
        files = json_files({DM: (1, ["1"])})
        files[f"Messages/c{DM}/messages.json"] = json.dumps([{"ID": 1}, {"x": 2}]).encode()
        pkg = make_zip(self.p("partial.zip"), files)
        for args in (["summary", pkg], ["csv", pkg, "-o", self.p("p.csv")]):
            code, _, err = run(*args)
            self.assertNotEqual(code, 0)
            self.assertIn("would be incomplete", err)
        self.assertFalse(os.path.exists(self.p("p.csv")))

    def test_allow_incomplete_continues_and_says_so(self):
        files = json_files({DM: (1, ["1"])})
        files[f"Messages/c{DM}/messages.json"] = json.dumps([{"ID": 1}, {"x": 2}]).encode()
        pkg = make_zip(self.p("partial.zip"), files)
        code, out, err = run("summary", pkg, "--allow-incomplete")
        self.assertEqual(code, 0)
        self.assertIn("INCOMPLETE", out)
        code, _, err = run("csv", pkg, "-o", self.p("p.csv"), "--allow-incomplete")
        self.assertEqual(code, 0)
        self.assertIn("INCOMPLETE", err)
        self.assertEqual(read_rows(self.p("p.csv"))[1:], [[DM, "1"]])

    def test_failed_run_leaves_no_partial_csv(self):
        files = json_files({DM: (1, ["1", "2"]), SERVER: (0, ["3"])})
        files[f"Messages/c{SERVER}/messages.json"] = b"[{broken"
        pkg = make_zip(self.p("late.zip"), files)
        code, _, _ = run("csv", pkg, "-o", self.p("late.csv"))
        self.assertNotEqual(code, 0)
        self.assertFalse(os.path.exists(self.p("late.csv")))
        # With --force, an existing file is left exactly as it was.
        with open(self.p("late.csv"), "w") as fh:
            fh.write("previous\n")
        code, _, _ = run("csv", pkg, "-o", self.p("late.csv"), "--force")
        self.assertNotEqual(code, 0)
        self.assertEqual(read_bytes(self.p("late.csv")), b"previous\n")
        self.assertEqual([f for f in os.listdir(self.d) if f.endswith(".tmp")], [])

    def test_failed_compare_keeps_existing_report(self):
        files = json_files({DM: (1, ["1"])})
        files[f"Messages/c{DM}/messages.json"] = b"[{broken"
        bad = make_zip(self.p("bad.zip"), files)
        with open(self.p("rep.csv"), "w") as fh:
            fh.write("previous\n")
        code, _, _ = run("compare", self.old, bad, "--report", self.p("rep.csv"), "--force")
        self.assertNotEqual(code, 0)
        self.assertEqual(read_bytes(self.p("rep.csv")), b"previous\n")

    def test_csv_header_with_spaces(self):
        files = {
            "messages/index.json": json.dumps({DM: "x"}).encode(),
            f"messages/{DM}/channel.json": json.dumps({"id": DM, "type": 1}).encode(),
            f"messages/{DM}/messages.csv": b" ID ,Timestamp,Contents,Attachments\n5001,t,a,\n",
        }
        pkg = make_zip(self.p("spaces.zip"), files)
        code, _, err = run("csv", pkg, "-o", self.p("sp.csv"))
        self.assertEqual(code, 0, err)
        self.assertEqual(read_rows(self.p("sp.csv"))[1:], [[DM, "5001"]])

    def test_unrecognised_message_file_is_an_error(self):
        files = json_files({DM: (1, ["1"])})
        files[f"Messages/c{SERVER}/channel.json"] = json.dumps({"id": SERVER, "type": 0}).encode()
        files[f"Messages/c{SERVER}/messages.ndjson"] = b"{}"
        pkg = make_zip(self.p("unknown.zip"), files)
        code, _, err = run("summary", pkg)
        self.assertNotEqual(code, 0)
        self.assertIn("doesn't recognise", err)

    def test_messages_without_channel_id_is_an_error(self):
        files = json_files({DM: (1, ["1"])})
        files["Messages/oddfolder/messages.json"] = json.dumps([{"ID": 5}]).encode()
        pkg = make_zip(self.p("odd.zip"), files)
        code, _, err = run("summary", pkg)
        self.assertNotEqual(code, 0)
        self.assertIn("no readable channel ID", err)

    def test_other_folders_are_reported(self):
        files = json_files({DM: (1, ["1"])})
        files["Messages/notes/readme.txt"] = b"hi"
        pkg = make_zip(self.p("other.zip"), files)
        code, _, err = run("summary", pkg)
        self.assertEqual(code, 0)
        self.assertIn("aren't channel folders", err)

    def test_corrupt_zip_gives_clean_error(self):
        pkg = self.p("corrupt.zip")
        with zipfile.ZipFile(pkg, "w", zipfile.ZIP_STORED) as z:
            for name, data in json_files({DM: (1, ["1" * 18])}).items():
                z.writestr(name, data)
        raw = bytearray(read_bytes(pkg))
        i = raw.find(b'"Timestamp"')
        raw[i:i + 3] = b"XXX"                    # damage a file's contents (CRC mismatch)
        with open(pkg, "wb") as fh:
            fh.write(raw)
        code, _, err = run("summary", pkg)
        self.assertNotEqual(code, 0)
        self.assertIn("error:", err)
        self.assertNotIn("Traceback", err)

    def test_missing_message_file_is_reported(self):
        files = json_files({DM: (1, ["1"])})
        files[f"Messages/c{SERVER}/channel.json"] = json.dumps({"id": SERVER, "type": 0}).encode()
        pkg = make_zip(self.p("missing.zip"), files)
        code, _, err = run("summary", pkg)
        self.assertEqual(code, 0)
        self.assertIn("have no messages.json or messages.csv", err)

    def test_duplicates_counted_once_and_reported(self):
        pkg = make_zip(self.p("dup.zip"), json_files({DM: (1, ["1", "1", "2"])}))
        code, _, err = run("csv", pkg, "-o", self.p("d.csv"))
        self.assertEqual(code, 0)
        self.assertEqual(len(read_rows(self.p("d.csv"))) - 1, 2)
        self.assertIn("1 repeated message IDs", err)

    # --- comparison -------------------------------------------------------

    def test_compare_counts_and_outputs(self):
        code, out, _ = run("compare", self.old, self.new,
                           "--report", self.p("r.csv"), "--remaining", self.p("rem.csv"))
        self.assertEqual(code, 0)
        self.assertIn("No longer in export (in old, not in new): 3", out)
        self.assertIn("Present in both exports:                  3", out)
        self.assertIn("New in newer export:                      1", out)
        self.assertEqual(read_rows(self.p("rem.csv"))[1:],
                         [[DM, "1001"], [DM, "1002"], [DM, "1003"]])
        report = {r[0]: r for r in read_rows(self.p("r.csv"))[1:]}
        self.assertEqual(report[SERVER][5], "2")   # no_longer_in_export

    def test_compare_uses_channel_and_message_pairs(self):
        a = make_zip(self.p("a.zip"), json_files({DM: (1, ["9"])}))
        b = make_zip(self.p("b.zip"), json_files({SERVER: (0, ["9"])}))
        code, out, err = run("compare", a, b)
        self.assertEqual(code, 0)
        self.assertIn("No longer in export (in old, not in new): 1", out)
        self.assertIn("different channel", err)

    # --- options and output safety -----------------------------------------

    def test_split(self):
        code, out, _ = run("csv", self.old, "-o", self.p("s.csv"), "--split", "4")
        self.assertEqual(code, 0)
        self.assertEqual(len(read_rows(self.p("s_part1.csv"))) - 1, 4)
        self.assertEqual(len(read_rows(self.p("s_part2.csv"))) - 1, 2)

    def test_split_not_needed_keeps_name(self):
        code, _, _ = run("csv", self.old, "-o", self.p("one.csv"), "--split", "100")
        self.assertEqual(code, 0)
        self.assertTrue(os.path.exists(self.p("one.csv")))

    def test_split_zero_or_negative_is_an_error(self):
        for n in ("0", "-5"):
            code, _, err = run("csv", self.old, "-o", self.p("z.csv"), "--split", n)
            self.assertNotEqual(code, 0)
            self.assertIn("positive", err)

    def test_exclude_and_only(self):
        with open(self.p("keep.txt"), "w") as fh:
            fh.write(f'"{DM}",note\n')          # quoted CSV field
        code, _, _ = run("csv", self.old, "-o", self.p("e.csv"), "--exclude", self.p("keep.txt"))
        self.assertEqual(code, 0)
        self.assertNotIn(DM, {r[0] for r in read_rows(self.p("e.csv"))})
        code, _, _ = run("csv", self.old, "-o", self.p("o.csv"), "--only", self.p("keep.txt"))
        self.assertEqual({r[0] for r in read_rows(self.p("o.csv"))[1:]}, {DM})

    def test_refuses_to_overwrite_package_zip(self):
        before = read_bytes(self.old)
        code, _, err = run("csv", self.old, "-o", self.old, "--force")
        self.assertNotEqual(code, 0)
        self.assertIn("is the package itself", err)
        self.assertEqual(read_bytes(self.old), before)
        code, _, _ = run("compare", self.old, self.new, "--report", self.new, "--force")
        self.assertNotEqual(code, 0)

    def test_refuses_to_write_inside_package_folder(self):
        folder = make_dir(self.p("pkgdir"), json_files({DM: (1, ["1"])}))
        target = os.path.join(folder, "Messages", f"c{DM}", "messages.json")
        code, _, err = run("csv", folder, "-o", target, "--force")
        self.assertNotEqual(code, 0)
        self.assertIn("inside the package folder", err)

    def test_refuses_same_report_and_remaining(self):
        code, _, err = run("compare", self.old, self.new,
                           "--report", self.p("same.csv"), "--remaining", self.p("same.csv"))
        self.assertNotEqual(code, 0)
        self.assertIn("more than one output", err)

    def test_refuses_to_overwrite_input_list(self):
        with open(self.p("keep.txt"), "w") as fh:
            fh.write(DM + "\n")
        code, _, err = run("csv", self.old, "--exclude", self.p("keep.txt"),
                           "-o", self.p("keep.txt"), "--force")
        self.assertNotEqual(code, 0)
        self.assertIn("also an input file", err)
        self.assertEqual(read_bytes(self.p("keep.txt")), (DM + "\n").encode())

    def test_existing_output_needs_force(self):
        open(self.p("exists.csv"), "w").close()
        code, _, err = run("csv", self.old, "-o", self.p("exists.csv"))
        self.assertNotEqual(code, 0)
        self.assertIn("--force", err)
        code, _, _ = run("csv", self.old, "-o", self.p("exists.csv"), "--force")
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main()

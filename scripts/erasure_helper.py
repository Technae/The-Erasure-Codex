#!/usr/bin/env python3
"""
erasure_helper.py - work with a Discord data package for an erasure request.

Reads the package straight from the .zip (or from an extracted folder) and
never changes it: it refuses to write output over the package or into an
extracted package folder. Uses only the Python standard library.

Commands
  summary  PACKAGE                 Count your messages per channel type.
  csv      PACKAGE -o OUT.csv      Write channel_id,message_id for every message.
  compare  OLD_PACKAGE NEW_PACKAGE Show what is no longer in the newer export.

Run "python3 erasure_helper.py COMMAND --help" for the options of each command.

If the package isn't in a format the script recognises, it stops with an
error instead of reporting fewer messages than the package contains.
"""

import argparse
import csv
import io
import json
import os
import re
import sys
import zipfile
from collections import Counter, OrderedDict

# Numeric channel types used in older packages, mapped to readable names.
CHANNEL_TYPES = {
    0: "GUILD_TEXT", 1: "DM", 2: "GUILD_VOICE", 3: "GROUP_DM",
    4: "GUILD_CATEGORY", 5: "GUILD_ANNOUNCEMENT", 10: "ANNOUNCEMENT_THREAD",
    11: "PUBLIC_THREAD", 12: "PRIVATE_THREAD", 13: "GUILD_STAGE_VOICE",
    14: "GUILD_DIRECTORY", 15: "GUILD_FORUM", 16: "GUILD_MEDIA",
}


class PackageError(Exception):
    """The package isn't in a format this script can read reliably."""


def warn(msg):
    print(f"warning: {msg}", file=sys.stderr)


class Package:
    """Read-only view of a data package, from a .zip file or a folder."""

    def __init__(self, path):
        self.path = path
        self.skipped_records = 0      # message records without a usable ID
        self.duplicates = 0           # repeated (channel, message) pairs
        self.missing_files = []       # channel folders with no message file
        if os.path.isdir(path):
            self._zip = None
            names = []
            for root, _dirs, files in os.walk(path):
                for f in files:
                    full = os.path.join(root, f)
                    names.append(os.path.relpath(full, path).replace(os.sep, "/"))
            self._names = names
        elif zipfile.is_zipfile(path):
            self._zip = zipfile.ZipFile(path)
            self._names = [n for n in self._zip.namelist() if not n.endswith("/")]
        else:
            raise PackageError(f"{path} is neither a folder nor a .zip file")

        # Find the messages folder, whatever its capitalisation, and allow for
        # a package that was extracted into an extra top-level folder.
        self._prefix = None
        for n in self._names:
            parts = n.split("/")
            for i, p in enumerate(parts[:-1]):
                if p.lower() == "messages":
                    self._prefix = "/".join(parts[: i + 1]) + "/"
                    break
            if self._prefix:
                break
        if self._prefix is None:
            self.close()
            raise PackageError(f"no Messages folder found in {path}")

    def close(self):
        if self._zip is not None:
            self._zip.close()
            self._zip = None

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()

    def _read(self, name):
        if self._zip is not None:
            return self._zip.read(name)
        with open(os.path.join(self.path, name), "rb") as fh:
            return fh.read()

    def _read_json(self, name):
        try:
            return json.loads(self._read(name).decode("utf-8-sig"))
        except (ValueError, UnicodeDecodeError) as e:
            raise PackageError(f"{name} in {self.path} isn't valid JSON ({e})")

    def channel_names(self):
        """Channel ID -> name, from the index file if there is one."""
        idx = self._prefix + "index.json"
        if idx in self._names:
            try:
                data = self._read_json(idx)
            except PackageError:
                warn(f"couldn't read {idx}; channel names will be blank")
                return {}
            if isinstance(data, dict):
                return {str(k): (v or "") for k, v in data.items()}
        return {}

    def _message_ids(self, name, kind):
        """Return the message IDs in one channel's message file."""
        ids = []
        if kind == "json":
            data = self._read_json(name)
            if not isinstance(data, list):
                raise PackageError(
                    f"{name} in {self.path} doesn't contain a list of messages "
                    f"(found {type(data).__name__}). The export format may have "
                    "changed; please open an issue so the script can be updated")
            for msg in data:
                mid = msg.get("ID", msg.get("id")) if isinstance(msg, dict) else None
                if mid is not None and str(mid).strip().isdigit():
                    ids.append(str(mid).strip())
                else:
                    self.skipped_records += 1
            if data and not ids:
                raise PackageError(
                    f"none of the {len(data)} records in {name} has a message ID. "
                    "The export format may have changed; please open an issue")
        else:
            try:
                text = self._read(name).decode("utf-8-sig")
            except UnicodeDecodeError as e:
                raise PackageError(f"{name} in {self.path} isn't valid text ({e})")
            reader = csv.DictReader(io.StringIO(text))
            fields = [f.strip() for f in (reader.fieldnames or [])]
            if not any(f in ("ID", "id") for f in fields):
                if text.strip():
                    raise PackageError(
                        f"{name} in {self.path} has no ID column (columns: "
                        f"{', '.join(fields) or 'none'}). Please open an issue")
                return ids
            for row in reader:
                mid = (row.get("ID") or row.get("id") or "").strip()
                if mid.isdigit():
                    ids.append(mid)
                else:
                    self.skipped_records += 1
        return ids

    def channels(self):
        """Yield (channel_id, channel_type, [message_ids]) for each channel.

        Message IDs are unique within each channel: repeats are dropped and
        counted in self.duplicates.
        """
        self.skipped_records, self.duplicates, self.missing_files = 0, 0, []
        folders = OrderedDict()
        for n in self._names:
            if not n.startswith(self._prefix):
                continue
            rest = n[len(self._prefix):].split("/")
            if len(rest) == 2:
                folders.setdefault(rest[0], []).append(rest[1])

        for folder, files in folders.items():
            base = self._prefix + folder + "/"
            channel_id, channel_type = None, "UNKNOWN"
            if "channel.json" in files:
                try:
                    info = self._read_json(base + "channel.json")
                    if isinstance(info, dict):
                        if info.get("id") is not None:
                            channel_id = str(info["id"])
                        t = info.get("type")
                        if isinstance(t, int):
                            channel_type = CHANNEL_TYPES.get(t, str(t))
                        elif t:
                            channel_type = str(t)
                except PackageError:
                    warn(f"couldn't read {base}channel.json; using the folder name")
            if channel_id is None:
                m = re.fullmatch(r"c?(\d{15,21})", folder)
                if not m:
                    continue
                channel_id = m.group(1)

            if "messages.json" in files:
                ids = self._message_ids(base + "messages.json", "json")
            elif "messages.csv" in files:
                ids = self._message_ids(base + "messages.csv", "csv")
            else:
                self.missing_files.append(folder)
                ids = []

            seen, unique = set(), []
            for mid in ids:
                if mid in seen:
                    self.duplicates += 1
                else:
                    seen.add(mid)
                    unique.append(mid)
            yield channel_id, channel_type, unique

    def report_problems(self):
        """Print warnings about anything that was skipped. Call after reading."""
        if self.skipped_records:
            warn(f"{self.path}: skipped {self.skipped_records} message records "
                 "without a valid ID. The counts don't include them")
        if self.duplicates:
            warn(f"{self.path}: {self.duplicates} repeated message IDs were "
                 "counted once")
        if self.missing_files:
            warn(f"{self.path}: {len(self.missing_files)} channel folders have no "
                 f"messages.json or messages.csv (e.g. {self.missing_files[0]}). "
                 "They're counted as empty")


def _real(path):
    return os.path.realpath(os.path.abspath(path))


def check_outputs(outputs, packages, force):
    """Refuse to write over a package, into a package folder, or twice."""
    seen = set()
    for out in outputs:
        r = _real(out)
        if r in seen:
            sys.exit(f"error: {out} is given for more than one output")
        seen.add(r)
        for pkg in packages:
            p = _real(pkg)
            if os.path.isdir(p):
                if r == p or r.startswith(p.rstrip(os.sep) + os.sep):
                    sys.exit(f"error: {out} is inside the package folder {pkg}. "
                             "Write it somewhere else, so the package isn't changed")
            elif r == p:
                sys.exit(f"error: {out} is the package itself. Choose another "
                         "output name, so the package isn't overwritten")
        if os.path.exists(r) and not force:
            sys.exit(f"error: {out} already exists. Use --force to overwrite it")


def load_id_set(path):
    """Read channel IDs: one per line, or the first column of a CSV."""
    ids = set()
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for row in csv.reader(fh):
            if row and row[0].strip().isdigit():
                ids.add(row[0].strip())
    return ids


def cmd_summary(args):
    with Package(args.package) as pkg:
        per_type, chans = Counter(), Counter()
        for _cid, ctype, ids in pkg.channels():
            per_type[ctype] += len(ids)
            chans[ctype] += 1
        pkg.report_problems()
    print(f"Package: {args.package}")
    print(f"{'Channel type':<22}{'Channels':>10}{'Messages':>12}")
    for ctype in sorted(chans, key=lambda t: (-per_type[t], t)):
        print(f"{ctype:<22}{chans[ctype]:>10}{per_type[ctype]:>12}")
    print(f"{'TOTAL':<22}{sum(chans.values()):>10}{sum(per_type.values()):>12}")


def cmd_csv(args):
    if args.split is not None and args.split <= 0:
        sys.exit("error: --split needs a positive number of rows")
    only = load_id_set(args.only) if args.only else None
    exclude = load_id_set(args.exclude) if args.exclude else set()
    stem, ext = os.path.splitext(args.output)
    ext = ext or ".csv"

    def part_name(n):
        return f"{stem}_part{n}{ext}"

    # Check every file this run might write before writing anything.
    with Package(args.package) as pkg:
        total = 0
        if args.split:
            # Count first, so the output names are known in advance.
            for cid, _ctype, ids in pkg.channels():
                if (only is None or cid in only) and cid not in exclude:
                    total += len(ids)
            if total == 0:
                sys.exit("error: no messages matched, so nothing was written")
            parts = -(-total // args.split)
            planned = [args.output] if parts == 1 else [part_name(n) for n in range(1, parts + 1)]
        else:
            planned = [args.output]
        check_outputs(planned, [args.package], args.force)

        written, rows_written, channels = [], 0, set()
        fh = w = None
        in_part = 0
        try:
            for cid, _ctype, ids in pkg.channels():
                if (only is not None and cid not in only) or cid in exclude:
                    continue
                for mid in ids:
                    if fh is None or (args.split and in_part >= args.split):
                        if fh is not None:
                            fh.close()
                        out = planned[len(written)]
                        fh = open(out, "w", newline="", encoding="utf-8")
                        w = csv.writer(fh, lineterminator="\n")
                        if not args.no_header:
                            w.writerow(["channel_id", "message_id"])
                        written.append(out)
                        in_part = 0
                    w.writerow([cid, mid])
                    in_part += 1
                    rows_written += 1
                    channels.add(cid)
        finally:
            if fh is not None:
                fh.close()
        pkg.report_problems()

    if rows_written == 0:
        sys.exit("error: no messages matched, so nothing was written")
    print(f"Wrote {rows_written} messages from {len(channels)} channels to: "
          f"{', '.join(written)}")


def cmd_compare(args):
    outputs = [o for o in (args.report, args.remaining) if o]
    check_outputs(outputs, [args.old, args.new], args.force)

    with Package(args.old) as old, Package(args.new) as new:
        names = old.channel_names()
        names.update(new.channel_names())

        old_by_chan, types = {}, {}
        for cid, ctype, ids in old.channels():
            old_by_chan.setdefault(cid, set()).update(ids)
            types[cid] = ctype
        new_by_chan = {}
        for cid, ctype, ids in new.channels():
            new_by_chan.setdefault(cid, set()).update(ids)
            types.setdefault(cid, ctype)
        old.report_problems()
        new.report_problems()

    # Compare (channel_id, message_id) pairs, the same unit as the CSV.
    old_all = {(c, m) for c, ids in old_by_chan.items() for m in ids}
    new_all = {(c, m) for c, ids in new_by_chan.items() for m in ids}
    gone = old_all - new_all
    both = old_all & new_all
    added = new_all - old_all

    print(f"Old export: {len(old_all)} messages")
    print(f"New export: {len(new_all)} messages")
    print(f"No longer in export (in old, not in new): {len(gone)}")
    print(f"Present in both exports:                  {len(both)}")
    print(f"New in newer export:                      {len(added)}")
    if old_all:
        print(f"Share of old messages no longer exported: {len(gone) / len(old_all):.1%}")

    # A message ID that appears under a different channel in each export
    # would count as gone and new. Flag it rather than hide it.
    moved = {m for _c, m in gone} & {m for _c, m in added}
    if moved:
        warn(f"{len(moved)} message IDs appear under a different channel in each "
             "export, so they're counted as both 'no longer in export' and 'new'")
    print("Note: this shows what Discord's export no longer includes.")
    print("It can't show whether every copy, including backups, has been erased.")

    if args.report:
        with open(args.report, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh, lineterminator="\n")
            w.writerow(["channel_id", "channel_name", "channel_type", "old_count",
                        "new_count", "no_longer_in_export", "in_both"])
            for cid in sorted(set(old_by_chan) | set(new_by_chan), key=lambda c: (len(c), c)):
                o, n = old_by_chan.get(cid, set()), new_by_chan.get(cid, set())
                w.writerow([cid, names.get(cid, ""), types.get(cid, ""),
                            len(o), len(n), len(o - n), len(o & n)])
        print(f"Per-channel report written to {args.report} "
              "(it contains channel names, so don't share it publicly)")

    if args.remaining:
        with open(args.remaining, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh, lineterminator="\n")
            w.writerow(["channel_id", "message_id"])
            for cid, mid in sorted(both, key=lambda p: (len(p[0]), p[0], len(p[1]), p[1])):
                w.writerow([cid, mid])
        print(f"IDs present in both exports written to {args.remaining}")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("summary", help="count your messages per channel type")
    s.add_argument("package", help="the data package .zip, or the extracted folder")
    s.set_defaults(func=cmd_summary)

    c = sub.add_parser("csv", help="write a channel_id,message_id CSV")
    c.add_argument("package", help="the data package .zip, or the extracted folder")
    c.add_argument("-o", "--output", default="messages_to_delete.csv",
                   help="output file (default: messages_to_delete.csv)")
    c.add_argument("--only", metavar="FILE",
                   help="only include channel IDs listed in FILE (one per line)")
    c.add_argument("--exclude", metavar="FILE",
                   help="leave out channel IDs listed in FILE (one per line)")
    c.add_argument("--split", type=int, metavar="N",
                   help="split into files of at most N rows each (named _part1, _part2…)")
    c.add_argument("--no-header", action="store_true",
                   help="don't write the channel_id,message_id header line")
    c.add_argument("--force", action="store_true",
                   help="overwrite output files that already exist")
    c.set_defaults(func=cmd_csv)

    m = sub.add_parser("compare", help="compare an older and a newer package")
    m.add_argument("old", help="the older package (.zip or folder)")
    m.add_argument("new", help="the newer package (.zip or folder)")
    m.add_argument("--report", metavar="FILE",
                   help="write a per-channel CSV report to FILE")
    m.add_argument("--remaining", metavar="FILE",
                   help="write the IDs present in both exports to FILE, ready for a "
                        "follow-up request")
    m.add_argument("--force", action="store_true",
                   help="overwrite output files that already exist")
    m.set_defaults(func=cmd_compare)

    args = p.parse_args()
    try:
        args.func(args)
    except PackageError as e:
        sys.exit(f"error: {e}")


if __name__ == "__main__":
    main()

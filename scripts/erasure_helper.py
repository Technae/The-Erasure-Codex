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

If the package isn't in a format the script recognises, or some message
records can't be read, it stops with an error instead of reporting fewer
messages than the package contains (--allow-incomplete overrides this for
skipped records, and says so). Output files are written to a temporary name
first and only put in place once the whole run has succeeded.
"""

import argparse
import csv
import io
import json
import os
import re
import sys
import tempfile
import zipfile
import zlib
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


_warned = set()


def warn(msg):
    if msg not in _warned:              # the csv command can read a package twice
        _warned.add(msg)
        print(f"warning: {msg}", file=sys.stderr)


def is_id(s):
    """A Discord ID: ASCII digits only (str.isdigit() also accepts other scripts)."""
    return bool(re.fullmatch(r"[0-9]+", s))


def is_channel_id(s):
    """A channel ID, with the same rule as for channel folder names."""
    return bool(re.fullmatch(r"[0-9]{15,21}", s))


class Package:
    """Read-only view of a data package, from a .zip file or a folder."""

    def __init__(self, path):
        self.path = path
        self.skipped_records = 0      # message records without a usable ID
        self.duplicates = 0           # repeated (channel, message) pairs
        self.missing_files = []       # channel folders with no message file
        self._zip = None
        if os.path.isdir(path):
            def walk_error(err):
                raise PackageError(f"couldn't read {err.filename}: {err.strerror}")
            names = []
            for root, _dirs, files in os.walk(path, onerror=walk_error):
                for f in files:
                    full = os.path.join(root, f)
                    names.append(os.path.relpath(full, path).replace(os.sep, "/"))
            self._names = names
        elif zipfile.is_zipfile(path):
            try:
                self._zip = zipfile.ZipFile(path)
            except (zipfile.BadZipFile, OSError) as e:
                raise PackageError(f"couldn't open {path} as a .zip file ({e})")
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
        try:
            if self._zip is not None:
                return self._zip.read(name)
            with open(os.path.join(self.path, name), "rb") as fh:
                return fh.read()
        except (zipfile.BadZipFile, zlib.error, OSError, KeyError,
                RuntimeError, NotImplementedError, EOFError) as e:
            raise PackageError(f"couldn't read {name} from {self.path} ({e})")

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
                if mid is not None and is_id(str(mid).strip()):
                    ids.append(str(mid).strip())
                else:
                    self.skipped_records += 1
            if data and not ids:
                self.unreadable_files.append(name)    # no record had an ID
        else:
            try:
                text = self._read(name).decode("utf-8-sig")
            except UnicodeDecodeError as e:
                raise PackageError(f"{name} in {self.path} isn't valid text ({e})")
            reader = csv.DictReader(io.StringIO(text))
            fields = [f.strip() for f in (reader.fieldnames or [])]
            reader.fieldnames = fields      # so " ID " in the header still matches
            if not any(f in ("ID", "id") for f in fields):
                if text.strip():
                    raise PackageError(
                        f"{name} in {self.path} has no ID column (columns: "
                        f"{', '.join(fields) or 'none'}). Please open an issue")
                return ids
            rows = 0
            for row in reader:
                mid = (row.get("ID") or row.get("id") or "").strip()
                if is_id(mid):
                    ids.append(mid)
                else:
                    self.skipped_records += 1
                rows += 1
            if rows and not ids:
                self.unreadable_files.append(name)
        return ids

    def channels(self):
        """Yield (channel_id, channel_type, [message_ids]) for each channel.

        Message IDs are unique within each channel: repeats are dropped and
        counted in self.duplicates.
        """
        self.skipped_records, self.duplicates, self.missing_files = 0, 0, []
        self.unknown_folders, self.unreadable_files = [], []
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
                        raw = info.get("id")
                        if raw is not None and is_channel_id(str(raw).strip()):
                            channel_id = str(raw).strip()
                        elif raw is not None:
                            warn(f"{base}channel.json has an ID that isn't a valid "
                                 f"channel ID ({str(raw)[:40]!r}); using the folder name")
                        t = info.get("type")
                        if isinstance(t, int):
                            channel_type = CHANNEL_TYPES.get(t, str(t))
                        elif t:
                            channel_type = str(t)
                except PackageError:
                    warn(f"couldn't read {base}channel.json; using the folder name")
            has_messages = "messages.json" in files or "messages.csv" in files
            if channel_id is None:
                m = re.fullmatch(r"c?([0-9]{15,21})", folder)
                if not m:
                    if has_messages:
                        raise PackageError(
                            f"{base} has a message file but no readable channel ID "
                            "(no channel.json and the folder name isn't a channel ID). "
                            "Please open an issue")
                    self.unknown_folders.append(folder)
                    continue
                channel_id = m.group(1)

            if "messages.json" in files:
                ids = self._message_ids(base + "messages.json", "json")
            elif "messages.csv" in files:
                ids = self._message_ids(base + "messages.csv", "csv")
            elif [f for f in files if f != "channel.json"]:
                raise PackageError(
                    f"{base} has files the script doesn't recognise "
                    f"({', '.join(sorted(f for f in files if f != 'channel.json'))}) "
                    "but no messages.json or messages.csv. The export format may "
                    "have changed; please open an issue")
            else:
                self.missing_files.append(folder)    # channel.json only: no messages
                ids = []

            seen, unique = set(), []
            for mid in ids:
                if mid in seen:
                    self.duplicates += 1
                else:
                    seen.add(mid)
                    unique.append(mid)
            yield channel_id, channel_type, unique

    def report_problems(self, allow_incomplete=False):
        """Warn about anything unusual, and stop if records were skipped.

        Call after reading. Skipped records make the result incomplete, so
        they're an error unless allow_incomplete is set.
        """
        if self.unreadable_files:
            n, first = len(self.unreadable_files), self.unreadable_files[0]
            if not allow_incomplete:
                raise PackageError(
                    f"{self.path}: no message ID could be read in {n} message "
                    f"files (e.g. {first}). The export format may have changed. "
                    "Nothing was written. Please open an issue; or rerun with "
                    "--allow-incomplete to continue without those channels")
            warn(f"{self.path}: INCOMPLETE: no message ID could be read in {n} "
                 f"message files (e.g. {first}), so those channels are left out "
                 "entirely. The export format may have changed; please open an issue")
        if self.skipped_records:
            if not allow_incomplete:
                raise PackageError(
                    f"{self.path}: {self.skipped_records} message records have no "
                    "valid ID, so the result would be incomplete. Nothing was "
                    "written. Please open an issue; or rerun with --allow-incomplete "
                    "to continue without them")
            warn(f"{self.path}: INCOMPLETE: skipped {self.skipped_records} message "
                 "records without a valid ID. The counts and files don't include them")
        if self.duplicates:
            warn(f"{self.path}: {self.duplicates} repeated message IDs were "
                 "counted once")
        if self.missing_files:
            warn(f"{self.path}: {len(self.missing_files)} channel folders have no "
                 f"messages.json or messages.csv (e.g. {self.missing_files[0]}). "
                 "They're counted as empty")
        if self.unknown_folders:
            warn(f"{self.path}: ignored {len(self.unknown_folders)} folders that "
                 f"aren't channel folders (e.g. {self.unknown_folders[0]})")


def _real(path):
    return os.path.realpath(os.path.abspath(path))


def check_outputs(outputs, packages, force, inputs=()):
    """Refuse to write over a package, an input file, into a package folder,
    or to the same file twice."""
    seen = set()
    protected = {_real(i) for i in inputs if i}
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
        if r in protected:
            sys.exit(f"error: {out} is also an input file. Choose another output name")
        if os.path.isdir(r):
            sys.exit(f"error: {out} is a folder. Give a file name for the output")
        if os.path.exists(r) and not force:
            sys.exit(f"error: {out} already exists. Use --force to overwrite it")


class Outputs:
    """Write output files under temporary names, and only move them into
    place when commit() is called. If anything fails, before or during the
    commit, the temporary files are removed and existing files are left as
    they were."""

    def __init__(self):
        self._files = []        # (final path, temp path, file handle)

    def open(self, final):
        folder = os.path.dirname(os.path.abspath(final))
        fd, tmp = tempfile.mkstemp(dir=folder, prefix="." + os.path.basename(final) + ".",
                                   suffix=".tmp")
        fh = os.fdopen(fd, "w", newline="", encoding="utf-8")
        self._files.append((final, tmp, fh))
        return fh

    def commit(self):
        """Move every file into place, or none of them.

        Existing files are first moved aside to backup names. If any step
        fails, the new files already installed are removed, the backups are
        put back, and a PackageError is raised.
        """
        for _final, _tmp, fh in self._files:
            fh.close()
        done = []                       # (final, backup or None), installed so far
        try:
            for final, tmp, _fh in self._files:
                backup = None
                if os.path.lexists(final):
                    if os.path.isdir(final):
                        raise OSError(f"{final} is a folder")
                    fd, backup = tempfile.mkstemp(
                        dir=os.path.dirname(os.path.abspath(final)),
                        prefix="." + os.path.basename(final) + ".", suffix=".bak")
                    os.close(fd)
                    os.replace(final, backup)
                try:
                    os.replace(tmp, final)
                except OSError:
                    if backup:
                        os.replace(backup, final)
                    raise
                done.append((final, backup))
        except OSError as e:
            for final, backup in reversed(done):
                try:
                    if backup:
                        os.replace(backup, final)
                    else:
                        os.remove(final)
                except OSError:
                    warn(f"couldn't restore {final}"
                         + (f"; the earlier version is in {backup}" if backup else ""))
            raise PackageError(f"couldn't write the output files ({e}). "
                               "No output files were changed")
        for _final, backup in done:
            if backup:
                try:
                    os.remove(backup)
                except OSError:
                    warn(f"couldn't remove the backup file {backup}")
        self._files = []

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        for _final, tmp, fh in self._files:     # only left if commit() wasn't reached
            fh.close()
            try:
                os.remove(tmp)
            except OSError:
                pass
        self._files = []


def load_id_set(path):
    """Read channel IDs: one per line, or the first column of a CSV."""
    ids = set()
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for row in csv.reader(fh):
            if row and is_id(row[0].strip()):
                ids.add(row[0].strip())
    return ids


def cmd_summary(args):
    with Package(args.package) as pkg:
        per_type, chans = Counter(), Counter()
        for _cid, ctype, ids in pkg.channels():
            per_type[ctype] += len(ids)
            chans[ctype] += 1
        pkg.report_problems(args.allow_incomplete)
    print(f"Package: {args.package}")
    print(f"{'Channel type':<22}{'Channels':>10}{'Messages':>12}")
    for ctype in sorted(chans, key=lambda t: (-per_type[t], t)):
        print(f"{ctype:<22}{chans[ctype]:>10}{per_type[ctype]:>12}")
    print(f"{'TOTAL':<22}{sum(chans.values()):>10}{sum(per_type.values()):>12}")
    if pkg.skipped_records:
        print(f"INCOMPLETE: {pkg.skipped_records} message records without a valid ID "
              "aren't counted")


def cmd_csv(args):
    if args.split is not None and args.split <= 0:
        sys.exit("error: --split needs a positive number of messages")
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
        check_outputs(planned, [args.package], args.force,
                      inputs=[args.only, args.exclude])

        written, rows_written, channels = [], 0, set()
        w = None
        in_part = 0
        with Outputs() as outs:
            for cid, _ctype, ids in pkg.channels():
                if (only is not None and cid not in only) or cid in exclude:
                    continue
                for mid in ids:
                    if w is None or (args.split and in_part >= args.split):
                        out = planned[len(written)]
                        w = csv.writer(outs.open(out), lineterminator="\n")
                        if not args.no_header:
                            w.writerow(["channel_id", "message_id"])
                        written.append(out)
                        in_part = 0
                    w.writerow([cid, mid])
                    in_part += 1
                    rows_written += 1
                    channels.add(cid)
            pkg.report_problems(args.allow_incomplete)
            if rows_written == 0:
                sys.exit("error: no messages matched, so nothing was written")
            outs.commit()

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
        old.report_problems(args.allow_incomplete)
        new.report_problems(args.allow_incomplete)

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

    with Outputs() as outs:
        write_compare_files(args, outs, old_by_chan, new_by_chan, names, types, both)
        outs.commit()
    if args.report:
        print(f"Per-channel report written to {args.report} "
              "(it contains channel names, so don't share it publicly)")
    if args.remaining:
        print(f"IDs present in both exports written to {args.remaining}")


def write_compare_files(args, outs, old_by_chan, new_by_chan, names, types, both):
    """Write the optional --report and --remaining files (via Outputs)."""
    if args.report:
        w = csv.writer(outs.open(args.report), lineterminator="\n")
        w.writerow(["channel_id", "channel_name", "channel_type", "old_count",
                    "new_count", "no_longer_in_export", "in_both"])
        for cid in sorted(set(old_by_chan) | set(new_by_chan), key=lambda c: (len(c), c)):
            o, n = old_by_chan.get(cid, set()), new_by_chan.get(cid, set())
            w.writerow([cid, names.get(cid, ""), types.get(cid, ""),
                        len(o), len(n), len(o - n), len(o & n)])
    if args.remaining:
        w = csv.writer(outs.open(args.remaining), lineterminator="\n")
        w.writerow(["channel_id", "message_id"])
        for cid, mid in sorted(both, key=lambda p: (len(p[0]), p[0], len(p[1]), p[1])):
            w.writerow([cid, mid])


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("summary", help="count your messages per channel type")
    s.add_argument("package", help="the data package .zip, or the extracted folder")
    s.add_argument("--allow-incomplete", action="store_true",
                   help="continue if some message records can't be read, and say so")
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
                   help="split into files of at most N messages each, plus the header "
                        "line (named _part1, _part2…)")
    c.add_argument("--no-header", action="store_true",
                   help="don't write the channel_id,message_id header line")
    c.add_argument("--force", action="store_true",
                   help="overwrite output files that already exist")
    c.add_argument("--allow-incomplete", action="store_true",
                   help="write the CSV even if some message records can't be read, "
                        "leaving them out (a warning says how many)")
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
    m.add_argument("--allow-incomplete", action="store_true",
                   help="compare even if some message records can't be read, "
                        "leaving them out (a warning says how many)")
    m.set_defaults(func=cmd_compare)

    args = p.parse_args()
    try:
        args.func(args)
    except PackageError as e:
        sys.exit(f"error: {e}")
    except OSError as e:                # e.g. the output folder doesn't exist
        sys.exit(f"error: {e}")


if __name__ == "__main__":
    main()

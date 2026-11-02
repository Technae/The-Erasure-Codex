#!/usr/bin/env python3
"""
erasure_helper.py - work with a Discord data package for an erasure request.

Reads the package straight from the .zip (or from an extracted folder) and
never changes it. Uses only the Python standard library.

Commands
  summary  PACKAGE                 Count your messages per channel type.
  csv      PACKAGE -o OUT.csv      Write channel_id,message_id for every message.
  compare  OLD_PACKAGE NEW_PACKAGE Show what was removed between two packages.

Run "python3 erasure_helper.py COMMAND --help" for the options of each command.
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
    15: "GUILD_FORUM", 16: "GUILD_MEDIA",
}


class Package:
    """Read-only view of a data package, from a .zip file or a folder."""

    def __init__(self, path):
        self.path = path
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
            sys.exit(f"error: {path} is neither a folder nor a .zip file")

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
            sys.exit(f"error: no Messages folder found in {path}")

    def _read(self, name):
        if self._zip is not None:
            return self._zip.read(name)
        with open(os.path.join(self.path, name), "rb") as fh:
            return fh.read()

    def _read_json(self, name):
        return json.loads(self._read(name).decode("utf-8-sig"))

    def channel_names(self):
        """Channel ID -> name, from the index file if there is one."""
        idx = self._prefix + "index.json"
        if idx in self._names:
            try:
                data = self._read_json(idx)
                if isinstance(data, dict):
                    return {str(k): (v or "") for k, v in data.items()}
            except (ValueError, UnicodeDecodeError):
                pass
        return {}

    def channels(self):
        """Yield (channel_id, channel_type, [message_ids]) for each channel."""
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
                    if info.get("id") is not None:
                        channel_id = str(info["id"])
                    t = info.get("type")
                    if isinstance(t, int):
                        channel_type = CHANNEL_TYPES.get(t, str(t))
                    elif t:
                        channel_type = str(t)
                except (ValueError, UnicodeDecodeError, AttributeError):
                    pass
            if channel_id is None:
                m = re.fullmatch(r"c?(\d{15,21})", folder)
                if not m:
                    continue
                channel_id = m.group(1)

            ids = []
            if "messages.json" in files:
                data = self._read_json(base + "messages.json")
                for msg in data if isinstance(data, list) else []:
                    mid = msg.get("ID", msg.get("id")) if isinstance(msg, dict) else None
                    if mid is not None and str(mid).isdigit():
                        ids.append(str(mid))
            elif "messages.csv" in files:
                text = self._read(base + "messages.csv").decode("utf-8-sig")
                for row in csv.DictReader(io.StringIO(text)):
                    mid = row.get("ID") or row.get("id")
                    if mid and mid.strip().isdigit():
                        ids.append(mid.strip())
            yield channel_id, channel_type, ids


def load_id_set(path):
    """Read channel IDs, one per line (or the first column of a CSV)."""
    ids = set()
    with open(path, encoding="utf-8-sig") as fh:
        for line in fh:
            first = line.split(",")[0].strip()
            if first.isdigit():
                ids.add(first)
    return ids


def cmd_summary(args):
    pkg = Package(args.package)
    per_type, chans = Counter(), Counter()
    total = 0
    for _cid, ctype, ids in pkg.channels():
        per_type[ctype] += len(ids)
        chans[ctype] += 1
        total += len(ids)
    print(f"Package: {args.package}")
    print(f"{'Channel type':<22}{'Channels':>10}{'Messages':>12}")
    for ctype, count in per_type.most_common():
        print(f"{ctype:<22}{chans[ctype]:>10}{count:>12}")
    print(f"{'TOTAL':<22}{sum(chans.values()):>10}{total:>12}")


def cmd_csv(args):
    pkg = Package(args.package)
    only = load_id_set(args.only) if args.only else None
    exclude = load_id_set(args.exclude) if args.exclude else set()
    rows = []
    for cid, _ctype, ids in pkg.channels():
        if only is not None and cid not in only:
            continue
        if cid in exclude:
            continue
        rows.extend((cid, mid) for mid in ids)

    if not rows:
        sys.exit("error: no messages matched, so nothing was written")

    chunk = args.split if args.split and args.split > 0 else len(rows)
    stem, ext = os.path.splitext(args.output)
    written = []
    for n, start in enumerate(range(0, len(rows), chunk), start=1):
        out = args.output if chunk >= len(rows) else f"{stem}_part{n}{ext or '.csv'}"
        with open(out, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh, lineterminator="\n")
            if not args.no_header:
                w.writerow(["channel_id", "message_id"])
            w.writerows(rows[start:start + chunk])
        written.append(out)

    channels = len({c for c, _ in rows})
    print(f"Wrote {len(rows)} messages from {channels} channels to: {', '.join(written)}")


def cmd_compare(args):
    old, new = Package(args.old), Package(args.new)
    names = old.channel_names()
    names.update(new.channel_names())

    old_by_chan, types = {}, {}
    for cid, ctype, ids in old.channels():
        old_by_chan[cid] = set(ids)
        types[cid] = ctype
    new_by_chan = {}
    for cid, ctype, ids in new.channels():
        new_by_chan[cid] = set(ids)
        types.setdefault(cid, ctype)

    old_all = set().union(*old_by_chan.values()) if old_by_chan else set()
    new_all = set().union(*new_by_chan.values()) if new_by_chan else set()
    removed = old_all - new_all
    kept = old_all & new_all
    added = new_all - old_all

    print(f"Old package: {len(old_all)} messages")
    print(f"New package: {len(new_all)} messages")
    print(f"Removed (in old, not in new):   {len(removed)}")
    print(f"Still present (in both):        {len(kept)}")
    print(f"New since the old package:      {len(added)}")
    if old_all:
        print(f"Share of old messages removed:  {len(removed) / len(old_all):.1%}")

    if args.report:
        with open(args.report, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh, lineterminator="\n")
            w.writerow(["channel_id", "channel_name", "channel_type",
                        "old_count", "new_count", "removed", "still_present"])
            for cid in sorted(set(old_by_chan) | set(new_by_chan)):
                o, n = old_by_chan.get(cid, set()), new_by_chan.get(cid, set())
                w.writerow([cid, names.get(cid, ""), types.get(cid, ""),
                            len(o), len(n), len(o - n), len(o & n)])
        print(f"Per-channel report written to {args.report} "
              "(it contains channel names, so don't share it publicly)")

    if args.remaining:
        with open(args.remaining, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh, lineterminator="\n")
            w.writerow(["channel_id", "message_id"])
            for cid in sorted(old_by_chan):
                for mid in sorted(old_by_chan[cid] & new_by_chan.get(cid, set()), key=int):
                    w.writerow([cid, mid])
        print(f"IDs still present written to {args.remaining}")


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
                   help="split into files of at most N rows each")
    c.add_argument("--no-header", action="store_true",
                   help="don't write the channel_id,message_id header line")
    c.set_defaults(func=cmd_csv)

    m = sub.add_parser("compare", help="compare an older and a newer package")
    m.add_argument("old", help="the older package (.zip or folder)")
    m.add_argument("new", help="the newer package (.zip or folder)")
    m.add_argument("--report", metavar="FILE",
                   help="write a per-channel CSV report to FILE")
    m.add_argument("--remaining", metavar="FILE",
                   help="write the IDs still present to FILE, ready for a follow-up request")
    m.set_defaults(func=cmd_compare)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

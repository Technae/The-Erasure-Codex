#!/usr/bin/env python3
"""Build CODEX-FULL.md: the whole Erasure Codex in one file.

Run from the repository root after changing any page:

    python3 scripts/build_full.py

It joins AI-GUIDE.md, README.md, docs/01-12 and scripts/README.md, rewrites
relative links as full GitHub links so they work from a single file, and
drops the per-page navigation lines. Uses only the standard library.
"""

import posixpath
import re
from pathlib import Path

REPO = "https://github.com/Technae/The-Erasure-Codex/blob/main/"
ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "CODEX-FULL.md"

LINK = re.compile(r"\]\(([^)\s]+)\)")
NAV = re.compile(r"^\[← .*\]\(.*\)|^\[Contents\]\(|· \[Contents\]\(")


def sources():
    files = [ROOT / "AI-GUIDE.md", ROOT / "README.md"]
    files += sorted((ROOT / "docs").glob("[0-9][0-9]-*.md"))
    files.append(ROOT / "scripts" / "README.md")
    return files


def absolute(target, base_dir):
    if re.match(r"^[a-z]+:", target) or target.startswith("#"):
        return target
    path, _, anchor = target.partition("#")
    full = posixpath.normpath(posixpath.join(base_dir, path)) if path else base_dir
    return REPO + full + ("#" + anchor if anchor else "")


def convert(path):
    rel = path.relative_to(ROOT).as_posix()
    base_dir = posixpath.dirname(rel)
    lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if NAV.search(line):
            continue
        lines.append(LINK.sub(lambda m: "](" + absolute(m.group(1), base_dir) + ")", line))
    body = "\n".join(lines).strip()
    return f"<!-- file: {rel} -->\n\n{body}\n"


def main():
    parts = [
        "# The Erasure Codex: the whole guide in one file\n\n"
        "This file joins every page of the guide so it can be read, or given to an "
        "AI assistant, in one go. It is generated from the individual pages by "
        "`scripts/build_full.py`; edit those pages, not this file. Each page starts "
        "with a `<!-- file: ... -->` marker.\n\n"
        f"Source: {REPO.replace('/blob/main/', '')}\n"
    ]
    parts += [convert(p) for p in sources()]
    OUTPUT.write_text("\n---\n\n".join(parts), encoding="utf-8")
    print(f"Wrote {OUTPUT.name} from {len(parts) - 1} pages")


if __name__ == "__main__":
    main()

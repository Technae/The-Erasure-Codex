#!/usr/bin/env python3
"""Build CODEX-FULL.md: the whole Erasure Codex in one file.

Run from the repository root after changing any page:

    python3 scripts/build_full.py

It joins docs/ai-instructions.md, README.md, docs/01-12 and scripts/README.md,
rewrites relative links as full GitHub links so they work from a single file,
and drops the per-page navigation lines and any line marked
<!-- source only -->. Uses only the standard library.
"""

import posixpath
import re
from pathlib import Path

REPO = "https://github.com/Technae/The-Erasure-Codex/blob/main/"
ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "CODEX-FULL.md"

LINK = re.compile(r"\]\(([^)\s]+)\)")
NAV = re.compile(r"^\[← .*\]\(.*\)|^\[Contents\]\(|· \[Contents\]\(|<!-- source only -->")


def sources():
    files = [ROOT / "docs" / "ai-instructions.md", ROOT / "README.md"]
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
    body = re.sub(r"\n{3,}", "\n\n", body)    # where a dropped line leaves a gap
    return f"<!-- file: {rel} -->\n\n{body}\n"


RAW = "https://raw.githubusercontent.com/Technae/The-Erasure-Codex/main/CODEX-FULL.md"


def version():
    """The date of the newest changelog entry, so rebuilding gives the same file."""
    for line in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            return line[3:].strip()
    return "unknown"


def main():
    parts = [
        "# The Erasure Codex: the whole guide in one file\n\n"
        f"**Version: {version()}** (the newest entry in the changelog). The guide is "
        "updated often. If you downloaded this file a while ago, get the latest copy: "
        f"{RAW}\n\n"
        "> **AI assistants: read this first.** The person has given you this file so "
        "you can help them use the guide. Before you answer, read the first section, "
        "\"For AI assistants\", and follow it: start with its questions, take the person "
        "through only the pages that apply to them, and use the templates in this file "
        "word for word. Don't write your own request, follow-up or complaint wording, "
        "and don't answer from general memory where the guide covers the point. If the "
        "version date above is more than a few weeks old, tell the person to download "
        "the latest copy.\n\n"
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

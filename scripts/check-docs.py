#!/usr/bin/env python3
"""Check that relative Markdown links in the Kettle product home resolve."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SKIP_DIRS = {".git", ".local", "planning"}


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)
    )


def main() -> int:
    failures: list[str] = []
    for source in markdown_files():
        for raw in LINK.findall(source.read_text(encoding="utf-8")):
            target = raw.strip().split(maxsplit=1)[0].strip("<>")
            if (
                not target
                or target.startswith(("#", "http://", "https://", "mailto:"))
            ):
                continue
            path_text = unquote(target.split("#", 1)[0])
            destination = (source.parent / path_text).resolve()
            try:
                destination.relative_to(ROOT)
            except ValueError:
                failures.append(
                    f"{source.relative_to(ROOT)}: link escapes repository: {raw}"
                )
                continue
            if not destination.exists():
                failures.append(
                    f"{source.relative_to(ROOT)}: missing relative link: {raw}"
                )

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"check-docs: {len(markdown_files())} Markdown files passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

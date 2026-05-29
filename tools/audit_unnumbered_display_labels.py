#!/usr/bin/env python3
r"""Reject labels inside unnumbered display-math delimiters.

LaTeX does not step an equation counter for ``\[...\]``.  A ``\label`` inside
such a display therefore cannot define an equation number, even though later
``\eqref`` commands may appear to compile.  This audit deliberately ignores
row-spacing commands such as ``\\[1mm]`` and TeX comments before scanning.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


DISPLAY_PATTERN = re.compile(r"(?<!\\)\\\[(.*?)(?<!\\)\\\]", re.DOTALL)
LABEL_PATTERN = re.compile(r"\\label\{[^}]+\}")


def strip_comments_preserving_offsets(text: str) -> str:
    """Replace TeX comments by spaces while preserving byte positions."""

    chars = list(text)
    i = 0
    while i < len(chars):
        if chars[i] == "%":
            backslashes = 0
            j = i - 1
            while j >= 0 and chars[j] == "\\":
                backslashes += 1
                j -= 1
            if backslashes % 2 == 0:
                while i < len(chars) and chars[i] != "\n":
                    chars[i] = " "
                    i += 1
                continue
        i += 1
    return "".join(chars)


def source_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.tex"):
        if "build" in path.parts:
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    tex_root = repo_root / "monograph" / "tex"
    failures: list[str] = []

    for path in source_files(tex_root):
        text = path.read_text()
        stripped = strip_comments_preserving_offsets(text)
        for match in DISPLAY_PATTERN.finditer(stripped):
            labels = LABEL_PATTERN.findall(match.group(1))
            if not labels:
                continue
            line = stripped.count("\n", 0, match.start()) + 1
            label_list = ", ".join(labels)
            failures.append(f"{path.relative_to(repo_root)}:{line}: {label_list}")

    if failures:
        print("Labels inside unnumbered display math were found:", file=sys.stderr)
        for failure in failures:
            print(failure, file=sys.stderr)
        print(
            "\nUse an equation/align/gather environment for any displayed formula "
            "that carries a label.",
            file=sys.stderr,
        )
        return 1

    print("No labels inside unnumbered display math.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

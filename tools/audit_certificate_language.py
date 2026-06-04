#!/usr/bin/env python3
"""Reject loose certificate language in reader-facing TeX.

The monograph reserves certificate language for a declared proof object with
an independent verification procedure.  Ordinary bounds, residual ledgers,
finite-window estimates, and diagnostics should use their actual mathematical
status instead.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "monograph" / "tex"
PATTERN = re.compile(
    r"\b("
    r"certificate|certificates|certification|certifications|"
    r"certify|certifies|certified|certifying"
    r")\b",
    re.IGNORECASE,
)
ALLOW_MARKER = "proof-object-ok:"


def strip_comment(line: str) -> str:
    escaped = False
    for index, char in enumerate(line):
        if char == "\\" and not escaped:
            escaped = True
            continue
        if char == "%" and not escaped:
            return line[:index]
        escaped = False
    return line


def nearby_allow_marker(lines: list[str], index: int) -> bool:
    start = max(0, index - 2)
    for line in lines[start : index + 1]:
        comment = line.split("%", 1)[1] if "%" in line else ""
        if ALLOW_MARKER in comment:
            return True
    return False


def main() -> int:
    failures: list[str] = []
    for path in sorted(ROOT.rglob("*.tex")):
        lines = path.read_text(encoding="utf-8").splitlines()
        for index, line in enumerate(lines):
            reader_facing = strip_comment(line)
            if PATTERN.search(reader_facing) and not nearby_allow_marker(lines, index):
                failures.append(f"{path}:{index + 1}: {line.strip()}")

    if failures:
        print("Loose certificate language found in reader-facing TeX:")
        for failure in failures:
            print(f"  {failure}")
        print(
            "Use residual bound, diagnostic, check, estimate, or another exact "
            "status term. For a genuine technical proof object, add a nearby "
            f"% {ALLOW_MARKER} comment explaining the verifier."
        )
        return 1

    print("Certificate-language audit clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

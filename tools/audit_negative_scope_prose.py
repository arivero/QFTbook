#!/usr/bin/env python3
"""Reject backward corrective prose in reader-facing TeX.

The monograph should state the positive scope of a construction directly.  A
sentence of the form "This is not ..." or "X is not a substitute for Y" often
signals that the preceding definition did not state its own scope cleanly.
Precise mathematical negations remain allowed; this audit is deliberately
narrow and targets the recurring soft phrases identified in issue #641.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "monograph" / "tex" / "volumes"

PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("this-is-not", re.compile(r"\b[Tt]his is not\b")),
    ("it-is-not-by-itself", re.compile(r"\b[Ii]t is not, by itself\b")),
    (
        "should-not-be-read-confused",
        re.compile(r"\bshould not be (?:confused|read|interpreted)\b", re.I),
    ),
    ("not-be-confused-with", re.compile(r"\bnot be confused with\b", re.I)),
    ("not-a-substitute", re.compile(r"\bnot a substitute\b", re.I)),
    ("not-merely", re.compile(r"\bnot merely\b", re.I)),
    ("not-cosmetic", re.compile(r"\bnot cosmetic\b", re.I)),
    ("not-a-choice-of-notation", re.compile(r"\bnot a choice of notation\b", re.I)),
]


def main() -> int:
    failures: list[str] = []
    for path in sorted(ROOT.rglob("*.tex")):
        text = path.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), 1):
            for name, pattern in PATTERNS:
                if pattern.search(line):
                    failures.append(f"{path}:{line_no}: {name}: {line.strip()}")

    if failures:
        print("Backward corrective prose found:", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        return 1

    print("Negative-scope prose audit clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

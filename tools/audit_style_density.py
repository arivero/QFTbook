#!/usr/bin/env python3
"""Report high-density prose tics in reader-facing TeX files.

This audit is intentionally narrower than ``audit_monograph_text.sh``.  The
terms here are not forbidden words.  The goal is to expose clusters where a
single definition template has started to dominate the prose.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


TERMS = ("datum", "ledger", "certification", "certified")
PATTERN = re.compile(r"\b(" + "|".join(re.escape(t) for t in TERMS) + r")\b", re.I)


def iter_windows(path: Path, window: int, stride: int):
    lines = path.read_text(errors="ignore").splitlines()
    for start in range(0, len(lines), stride):
        stop = min(start + window, len(lines))
        if start >= stop:
            continue
        text = "\n".join(lines[start:stop])
        matches = PATTERN.findall(text)
        if matches:
            yield start + 1, stop, matches


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default="monograph/tex",
        help="TeX root to audit, relative to the repository root.",
    )
    parser.add_argument(
        "--window",
        type=int,
        default=200,
        help="Number of lines in each density window.",
    )
    parser.add_argument(
        "--stride",
        type=int,
        default=50,
        help="Line stride between adjacent windows.",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=5,
        help="Report windows with more than this many marked terms.",
    )
    parser.add_argument(
        "--fail",
        action="store_true",
        help="Return nonzero if any high-density window is found.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=80,
        help="Maximum number of windows to print.",
    )
    args = parser.parse_args()

    root = Path(args.root)
    findings: list[tuple[int, str, int, int, dict[str, int]]] = []
    for path in root.rglob("*.tex"):
        for start, stop, matches in iter_windows(path, args.window, args.stride):
            if len(matches) <= args.threshold:
                continue
            counts = {term: 0 for term in TERMS}
            for match in matches:
                counts[match.lower()] += 1
            findings.append((len(matches), str(path), start, stop, counts))

    findings.sort(key=lambda item: (-item[0], item[1], item[2]))
    if not findings:
        print("Style-density audit clean.")
        return 0

    for total, path, start, stop, counts in findings[: args.limit]:
        count_text = ", ".join(f"{term}={counts[term]}" for term in TERMS if counts[term])
        print(f"{path}:{start}-{stop}: {total} marked terms ({count_text})")
    if len(findings) > args.limit:
        print(f"... {len(findings) - args.limit} additional high-density windows omitted.")

    return 1 if args.fail else 0


if __name__ == "__main__":
    raise SystemExit(main())

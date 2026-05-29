#!/usr/bin/env python3
"""Audit theorem-family headings and proof-environment placement.

This is deliberately narrow.  It catches theorem/proposition/lemma/corollary
titles of the form "X is not Y" or "X does not prove Y", which should usually
be a remark or status paragraph unless a genuine counterexample or obstruction
is being proved.  It also rejects a proof environment attached directly to a
definition, since convention checks and definitional consequences must be
written in prose or stated as separate theorem-family claims.

It does not try to judge proof quality; it flags presentation patterns that
create fake-looking proofs.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "monograph" / "tex" / "volumes"

THEOREM_ENV_RE = re.compile(
    r"\\begin\{(theorem|proposition|lemma|corollary)\}(?:\[([^\]]*)\])?",
)

NEGATIVE_SCOPE_TITLE_RE = re.compile(
    r"\b("
    r"does not|do not|is not|are not|cannot|"
    r"not a|not an|not the|not supply|not imply|not prove|no baseline"
    r")\b",
    re.IGNORECASE,
)


def main() -> int:
    failures: list[str] = []
    for path in sorted(ROOT.rglob("*.tex")):
        text = path.read_text(encoding="utf-8")
        for match in THEOREM_ENV_RE.finditer(text):
            title = match.group(2) or ""
            if not title:
                continue
            if NEGATIVE_SCOPE_TITLE_RE.search(title):
                line = text.count("\n", 0, match.start()) + 1
                failures.append(f"{path}:{line}: {match.group(1)} [{title}]")

        lines = text.splitlines()
        for idx, line_text in enumerate(lines):
            if not re.search(r"\\begin\{proof\}", line_text):
                continue
            prev = idx - 1
            while prev >= 0 and not lines[prev].strip():
                prev -= 1
            if prev >= 0 and lines[prev].strip() == r"\end{definition}":
                failures.append(
                    f"{path}:{idx + 1}: proof environment follows a definition"
                )

    if failures:
        print("Theorem-form audit failures:", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        return 1

    print("Theorem-form audit clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

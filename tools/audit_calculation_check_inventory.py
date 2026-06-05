#!/usr/bin/env python3
"""Audit the published calculation-check inventory count against the runner."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "calculation-checks" / "INDEX.md"
RUNNER_PATH = ROOT / "tools" / "run_calculation_checks.sh"

INDEX_COUNT_RE = re.compile(
    r"contains\s+(\d+)\s+active check scripts:\s+"
    r"(\d+)\s+Python checks\s+and\s+(\d+)\s+Wolfram Language",
    re.IGNORECASE,
)
PYTHON_COUNT_RE = re.compile(r"selected Python checks:\s+(\d+)")
WOLFRAM_COUNT_RE = re.compile(r"selected Wolfram Language checks:\s+(\d+)")


def parse_single_count(pattern: re.Pattern[str], text: str, label: str) -> int:
    matches = pattern.findall(text)
    if len(matches) != 1:
        raise AssertionError(f"expected exactly one {label} count, found {len(matches)}")
    match = matches[0]
    if isinstance(match, tuple):
        raise AssertionError(f"internal parser error for scalar {label} count")
    return int(match)


def published_counts() -> tuple[int, int, int]:
    text = INDEX_PATH.read_text()
    matches = INDEX_COUNT_RE.findall(text)
    if len(matches) != 1:
        raise AssertionError(
            f"{INDEX_PATH}: expected exactly one published active-check count line, found {len(matches)}"
        )
    total_text, python_text, wolfram_text = matches[0]
    return int(total_text), int(python_text), int(wolfram_text)


def runner_counts() -> tuple[int, int, int]:
    completed = subprocess.run(
        [str(RUNNER_PATH), "--list"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        raise AssertionError(
            "runner inventory command failed:\n"
            f"stdout:\n{completed.stdout}\n"
            f"stderr:\n{completed.stderr}"
        )
    python_count = parse_single_count(PYTHON_COUNT_RE, completed.stdout, "runner Python")
    wolfram_count = parse_single_count(WOLFRAM_COUNT_RE, completed.stdout, "runner Wolfram")
    return python_count + wolfram_count, python_count, wolfram_count


def main() -> int:
    try:
        published = published_counts()
        runner = runner_counts()
        if published != runner:
            raise AssertionError(
                "calculation-check inventory count is stale: "
                f"INDEX.md publishes total/python/wolfram={published}, "
                f"runner reports {runner}"
            )
    except AssertionError as exc:
        print(f"[calculation-check-inventory] FAILED: {exc}", file=sys.stderr)
        return 1

    total, python_count, wolfram_count = runner
    print(
        "[calculation-check-inventory] clean: "
        f"{total} active check scripts "
        f"({python_count} Python, {wolfram_count} Wolfram Language)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

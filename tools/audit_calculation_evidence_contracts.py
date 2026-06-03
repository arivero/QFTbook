#!/usr/bin/env python3
"""Audit evidence contracts for high-risk calculation companions."""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CHECK_ROOT = ROOT / "calculation-checks"
DEFAULT_MANIFEST = CHECK_ROOT / "evidence_contracts.json"
RISK_TERMS = re.compile(
    r"\b("
    r"anomaly|continuum|descent|existence|inflow|OS|Osterwalder|positivity|"
    r"reconstruction|sewing|theorem|thermodynamic|uniform"
    r")\b",
    re.IGNORECASE,
)


def module_docstring(path: Path) -> str:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except SyntaxError as exc:
        raise AssertionError(f"{path}: cannot parse Python source: {exc}") from exc
    return ast.get_docstring(tree) or ""


def load_manifest(path: Path) -> tuple[list[str], list[Path]]:
    data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    required = data.get("required_sections")
    if not isinstance(required, list) or not all(isinstance(item, str) for item in required):
        raise AssertionError(f"{path}: required_sections must be a list of strings")

    files = data.get("files")
    if not isinstance(files, list):
        raise AssertionError(f"{path}: files must be a list")

    paths: list[Path] = []
    for entry in files:
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), str):
            raise AssertionError(f"{path}: every file entry needs a string path")
        rel = Path(entry["path"])
        if rel.is_absolute() or ".." in rel.parts:
            raise AssertionError(f"{path}: invalid relative path {entry['path']!r}")
        full = CHECK_ROOT / rel
        if not full.exists():
            raise AssertionError(f"{path}: missing required companion {entry['path']!r}")
        paths.append(full)
    return required, paths


def missing_sections(doc: str, required_sections: list[str]) -> list[str]:
    return [section for section in required_sections if section not in doc]


def risky_without_contract(required_paths: set[Path]) -> list[str]:
    warnings: list[str] = []
    for path in sorted(CHECK_ROOT.glob("*.py")):
        if path.name in {"check_utils.py", "check_utils_checks.py"}:
            continue
        if path in required_paths:
            continue
        doc = module_docstring(path)
        if "Evidence contract." in doc:
            continue
        match = RISK_TERMS.search(doc)
        if match is not None:
            first = doc.splitlines()[0] if doc else "<no module docstring>"
            warnings.append(f"{path.relative_to(ROOT)}: {match.group(0)}: {first}")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help="evidence-contract manifest to audit",
    )
    parser.add_argument(
        "--fail-on-risk-report",
        action="store_true",
        help="also fail when nonmanifest risky docstrings lack contracts",
    )
    args = parser.parse_args()

    required_sections, required_paths = load_manifest(args.manifest)
    offenders: list[str] = []
    for path in required_paths:
        doc = module_docstring(path)
        missing = missing_sections(doc, required_sections)
        if missing:
            rel = path.relative_to(ROOT)
            offenders.append(f"{rel}: missing evidence-contract fields: {', '.join(missing)}")

    risk_warnings = risky_without_contract(set(required_paths))
    if args.fail_on_risk_report and risk_warnings:
        offenders.extend(
            f"{warning} [risk report lacks manifest evidence contract]"
            for warning in risk_warnings
        )

    if offenders:
        print("Calculation evidence-contract audit failed:", file=sys.stderr)
        for offender in offenders:
            print(f"  {offender}", file=sys.stderr)
        return 1

    print("Calculation evidence-contract audit clean.")
    if risk_warnings:
        print("Non-blocking risk report:")
        for warning in risk_warnings:
            print(f"  {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

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
SELF_CONFIRMING_TARGET = re.compile(
    r"(benchmark|datum|expected|physical|reference|target|truth)",
    re.IGNORECASE,
)
SELF_CONFIRMING_SOURCE = re.compile(
    r"(actual|computed|extracted|prediction|predicted|reconstructed|result)",
    re.IGNORECASE,
)


def module_docstring(path: Path) -> str:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except SyntaxError as exc:
        raise AssertionError(f"{path}: cannot parse Python source: {exc}") from exc
    return ast.get_docstring(tree) or ""


def load_manifest(path: Path) -> tuple[list[str], list[str], list[dict[str, Any]]]:
    data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    required = data.get("required_sections")
    if not isinstance(required, list) or not all(isinstance(item, str) for item in required):
        raise AssertionError(f"{path}: required_sections must be a list of strings")

    extended_required = data.get("extended_required_sections", [])
    if not isinstance(extended_required, list) or not all(
        isinstance(item, str) for item in extended_required
    ):
        raise AssertionError(f"{path}: extended_required_sections must be a list of strings")

    files = data.get("files")
    if not isinstance(files, list):
        raise AssertionError(f"{path}: files must be a list")

    entries: list[dict[str, Any]] = []
    for entry in files:
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), str):
            raise AssertionError(f"{path}: every file entry needs a string path")
        rel = Path(entry["path"])
        if rel.is_absolute() or ".." in rel.parts:
            raise AssertionError(f"{path}: invalid relative path {entry['path']!r}")
        full = CHECK_ROOT / rel
        if not full.exists():
            raise AssertionError(f"{path}: missing required companion {entry['path']!r}")
        tier = entry.get("contract_tier", "standard")
        if tier not in {"standard", "extended"}:
            raise AssertionError(f"{path}: invalid contract_tier {tier!r} for {entry['path']!r}")
        convention_tags = entry.get("convention_tags", [])
        if tier == "extended" and (
            not isinstance(convention_tags, list)
            or not convention_tags
            or not all(isinstance(item, str) and item for item in convention_tags)
        ):
            raise AssertionError(
                f"{path}: extended contract {entry['path']!r} needs convention_tags"
            )
        enriched = dict(entry)
        enriched["full_path"] = full
        entries.append(enriched)
    return required, extended_required, entries


def missing_sections(doc: str, required_sections: list[str]) -> list[str]:
    return [section for section in required_sections if section not in doc]


def target_names(target: ast.expr) -> list[str]:
    if isinstance(target, ast.Name):
        return [target.id]
    if isinstance(target, (ast.Tuple, ast.List)):
        names: list[str] = []
        for item in target.elts:
            names.extend(target_names(item))
        return names
    return []


def self_confirming_assignments(path: Path) -> list[str]:
    """Find exact assignments like physical_datum = reconstructed_datum."""

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    try:
        tree = ast.parse(text)
    except SyntaxError as exc:
        raise AssertionError(f"{path}: cannot parse Python source: {exc}") from exc

    offenders: list[str] = []
    for node in ast.walk(tree):
        assignment_pairs: list[tuple[list[str], ast.expr, int]] = []
        if isinstance(node, ast.Assign):
            for target in node.targets:
                assignment_pairs.append((target_names(target), node.value, node.lineno))
        elif isinstance(node, ast.AnnAssign):
            assignment_pairs.append((target_names(node.target), node.value, node.lineno))

        for names, value, lineno in assignment_pairs:
            if value is None or not isinstance(value, ast.Name):
                continue
            source = value.id
            if not SELF_CONFIRMING_SOURCE.search(source):
                continue
            line = lines[lineno - 1] if 0 <= lineno - 1 < len(lines) else ""
            if "evidence-audit: allow-self-confirming" in line:
                continue
            for name in names:
                if SELF_CONFIRMING_TARGET.search(name):
                    rel = path.relative_to(ROOT)
                    offenders.append(
                        f"{rel}:{lineno}: possible self-confirming evidence "
                        f"{name} = {source}"
                    )
    return offenders


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

    required_sections, extended_required_sections, entries = load_manifest(args.manifest)
    required_paths = [entry["full_path"] for entry in entries]
    offenders: list[str] = []
    for entry in entries:
        path = entry["full_path"]
        doc = module_docstring(path)
        required_for_entry = list(required_sections)
        if entry.get("contract_tier", "standard") == "extended":
            required_for_entry.extend(extended_required_sections)
        missing = missing_sections(doc, required_for_entry)
        if missing:
            rel = path.relative_to(ROOT)
            offenders.append(f"{rel}: missing evidence-contract fields: {', '.join(missing)}")

    for path in required_paths:
        offenders.extend(self_confirming_assignments(path))

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

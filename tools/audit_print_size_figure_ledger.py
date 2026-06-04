#!/usr/bin/env python3
"""Validate the issue-767 human print-size figure inspection ledger."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LEDGER = (
    ROOT
    / "planning"
    / "release_audits"
    / "2026-06-04_issue767_print_size_figure_ledger.tsv"
)
DEFAULT_RENDER_DIR = ROOT / "monograph" / "tex" / "build" / "figure_audit_current"

REQUIRED_COLUMNS = [
    "label",
    "number",
    "printed_page",
    "physical_page",
    "pdf_sha256",
    "page_png",
    "page_image_sha256",
    "machine_warnings",
    "review_status",
    "review_mode",
    "print_label_line_weight",
    "caption_separation",
    "grayscale_accessibility",
    "semantic_value",
    "theorem_evidence_scope",
    "higher_res_crop",
    "notes",
]
CRITERION_COLUMNS = [
    "print_label_line_weight",
    "caption_separation",
    "grayscale_accessibility",
    "semantic_value",
    "theorem_evidence_scope",
]
ALLOWED_STATUSES = {"pending", "pass", "needs-repair"}


def display_path(path: Path) -> str:
    return str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"missing required file: {display_path(path)}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"cannot parse JSON {display_path(path)}: {exc}") from exc


def load_ledger(path: Path) -> list[dict[str, str]]:
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            if reader.fieldnames != REQUIRED_COLUMNS:
                raise SystemExit(
                    "ledger columns do not match required schema:\n"
                    f"expected: {REQUIRED_COLUMNS}\n"
                    f"found: {reader.fieldnames}"
                )
            return list(reader)
    except FileNotFoundError as exc:
        raise SystemExit(f"missing ledger: {display_path(path)}") from exc


def expected_page_png(physical_page: int) -> str:
    return f"monograph/tex/build/figure_audit_current/pages/page-{physical_page:04d}.png"


def warning_map(audit: dict[str, Any]) -> dict[int, str]:
    return {
        int(page["physical_page"]): ";".join(page.get("warnings", []))
        for page in audit.get("pages", [])
    }


def validate(
    *,
    manifest: list[dict[str, Any]],
    audit: dict[str, Any],
    ledger_rows: list[dict[str, str]],
    require_complete: bool,
) -> list[str]:
    failures: list[str] = []
    if len(ledger_rows) != len(manifest):
        failures.append(
            f"ledger row count {len(ledger_rows)} does not match manifest {len(manifest)}"
        )

    manifest_labels = [row["label"] for row in manifest]
    ledger_labels = [row["label"] for row in ledger_rows]
    if len(set(ledger_labels)) != len(ledger_labels):
        failures.append("ledger contains duplicate labels")
    if ledger_labels != manifest_labels:
        missing = sorted(set(manifest_labels) - set(ledger_labels))
        extra = sorted(set(ledger_labels) - set(manifest_labels))
        failures.append(
            "ledger labels do not match manifest order/content"
            f"; missing={missing[:5]} extra={extra[:5]}"
        )

    warnings_by_page = warning_map(audit)
    manifest_by_label = {row["label"]: row for row in manifest}
    for row in ledger_rows:
        label = row["label"]
        item = manifest_by_label.get(label)
        if item is None:
            continue
        physical_page = int(item["physical_page"])
        checks = {
            "number": str(item["number"]),
            "printed_page": str(item["printed_page"]),
            "physical_page": str(physical_page),
            "pdf_sha256": str(item["pdf_sha256"]),
            "page_png": expected_page_png(physical_page),
            "page_image_sha256": str(item["page_image_sha256"]),
            "machine_warnings": warnings_by_page.get(physical_page, ""),
        }
        for key, expected in checks.items():
            if row[key] != expected:
                failures.append(
                    f"{label}: {key} is {row[key]!r}, expected {expected!r}"
                )

        status = row["review_status"]
        if status not in ALLOWED_STATUSES:
            failures.append(f"{label}: invalid review_status {status!r}")
            continue

        if status == "pass":
            if not row["review_mode"]:
                failures.append(f"{label}: pass row lacks review_mode")
            if not row["higher_res_crop"]:
                failures.append(f"{label}: pass row lacks crop decision")
            if not row["notes"]:
                failures.append(f"{label}: pass row lacks notes")
            for column in CRITERION_COLUMNS:
                if row[column] not in {"pass", "n/a"}:
                    failures.append(
                        f"{label}: pass row has {column}={row[column]!r}"
                    )
        elif status == "needs-repair":
            if not row["notes"]:
                failures.append(f"{label}: needs-repair row lacks notes")
        elif require_complete:
            failures.append(f"{label}: review_status is {status!r}, not complete")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--render-dir", type=Path, default=DEFAULT_RENDER_DIR)
    parser.add_argument(
        "--require-complete",
        action="store_true",
        help="Fail unless every ledger row is reviewed and passing.",
    )
    args = parser.parse_args()

    ledger_path = args.ledger if args.ledger.is_absolute() else ROOT / args.ledger
    render_dir = args.render_dir if args.render_dir.is_absolute() else ROOT / args.render_dir
    manifest = load_json(render_dir / "figure_pages_manifest.json")
    audit = load_json(render_dir / "rendered_figure_page_audit.json")
    if not isinstance(manifest, list):
        raise SystemExit("figure_pages_manifest.json must contain a list")
    if not isinstance(audit, dict):
        raise SystemExit("rendered_figure_page_audit.json must contain an object")

    rows = load_ledger(ledger_path)
    failures = validate(
        manifest=manifest,
        audit=audit,
        ledger_rows=rows,
        require_complete=args.require_complete,
    )
    pass_count = sum(row["review_status"] == "pass" for row in rows)
    repair_count = sum(row["review_status"] == "needs-repair" for row in rows)
    pending_count = sum(row["review_status"] == "pending" for row in rows)
    if failures:
        print("Print-size figure ledger audit failed:")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("Print-size figure ledger audit passed.")
    print(f"  rows: {len(rows)}")
    print(f"  pass: {pass_count}")
    print(f"  needs-repair: {repair_count}")
    print(f"  pending: {pending_count}")
    print(f"  ledger: {display_path(ledger_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

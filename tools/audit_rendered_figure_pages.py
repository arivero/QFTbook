#!/usr/bin/env python3
"""Audit rendered figure-page PNGs against their manifest and provenance."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "monograph" / "tex" / "build" / "figure_audit_current"
DEFAULT_PDF = ROOT / "monograph" / "tex" / "main.pdf"


def display_path(path: Path) -> str:
    return str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"missing required audit file: {display_path(path)}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"cannot parse JSON {display_path(path)}: {exc}") from exc


def percentile_from_histogram(histogram: list[int], fraction: float) -> int | None:
    total = sum(histogram)
    if total == 0:
        return None
    target = total * fraction
    seen = 0
    for value, count in enumerate(histogram):
        seen += count
        if seen >= target:
            return value
    return len(histogram) - 1


def analyze_page(
    image_path: Path,
    *,
    background_threshold: int,
    dark_threshold: int,
    edge_margin_px: int,
    min_ink_pixels: int,
    min_dark_pixels: int,
) -> dict[str, Any]:
    from PIL import Image, ImageChops

    with Image.open(image_path) as image:
        rgb = image.convert("RGB")
        gray = rgb.convert("L")
        width, height = rgb.size

        ink_mask = gray.point(
            lambda value: 255 if value < background_threshold else 0,
            "L",
        )
        dark_mask = gray.point(
            lambda value: 255 if value < dark_threshold else 0,
            "L",
        )
        ink_hist = ink_mask.histogram()
        dark_hist = dark_mask.histogram()
        ink_pixels = ink_hist[255]
        dark_pixels = dark_hist[255]
        bbox = ink_mask.getbbox()

        gray_as_rgb = gray.convert("RGB")
        color_diff = ImageChops.difference(rgb, gray_as_rgb).convert("L")
        color_mask = color_diff.point(lambda value: 255 if value > 18 else 0, "L")
        color_pixels = color_mask.histogram()[255]

        warnings: list[str] = []
        failures: list[str] = []
        if bbox is None or ink_pixels < min_ink_pixels:
            failures.append("blank_or_nearly_blank_page")
        if dark_pixels < min_dark_pixels:
            failures.append("no_dark_print_size_content")
        edge_distances: dict[str, int | None]
        if bbox is None:
            edge_distances = {"left": None, "top": None, "right": None, "bottom": None}
        else:
            left, top, right, bottom = bbox
            edge_distances = {
                "left": left,
                "top": top,
                "right": width - right,
                "bottom": height - bottom,
            }
            near_edges = [
                edge
                for edge, distance in edge_distances.items()
                if distance < edge_margin_px
            ]
            if near_edges:
                failures.append(f"ink_near_page_edge:{','.join(near_edges)}")
        if color_pixels > max(2000, ink_pixels // 20):
            warnings.append("substantial_color_pixels_check_grayscale_semantics")

        ink_luma_hist = [0] * 256
        if bbox is not None:
            gray_hist = gray.histogram()
            ink_luma_hist = [
                count if value < background_threshold else 0
                for value, count in enumerate(gray_hist)
            ]

    return {
        "image": display_path(image_path),
        "width": width,
        "height": height,
        "ink_pixels": ink_pixels,
        "dark_pixels": dark_pixels,
        "color_pixels": color_pixels,
        "ink_bbox": list(bbox) if bbox is not None else None,
        "edge_distances_px": edge_distances,
        "ink_luma_p50": percentile_from_histogram(ink_luma_hist, 0.5),
        "ink_luma_p95": percentile_from_histogram(ink_luma_hist, 0.95),
        "warnings": warnings,
        "failures": failures,
    }


def write_markdown_report(report: dict[str, Any], path: Path) -> None:
    summary = report["summary"]
    lines = [
        "# Rendered Figure Page Audit",
        "",
        f"- Status: `{summary['status']}`",
        f"- Figures: `{summary['figure_count']}`",
        f"- Unique physical pages: `{summary['unique_physical_pages']}`",
        f"- Rendered page PNGs: `{summary['rendered_page_pngs']}`",
        f"- Contact sheets: `{summary['contact_sheets']}`",
        f"- PDF SHA-256: `{summary['pdf_sha256']}`",
        f"- Renderer: `{summary['renderer']}`",
        f"- DPI: `{summary['dpi']}`",
        f"- Page failures: `{summary['page_failure_count']}`",
        f"- Page warnings: `{summary['page_warning_count']}`",
        "",
    ]
    if report["failures"]:
        lines.extend(["## Failures", ""])
        for failure in report["failures"]:
            lines.append(f"- {failure}")
        lines.append("")
    if report["warnings"]:
        lines.extend(["## Warnings", ""])
        for warning in report["warnings"]:
            lines.append(f"- {warning}")
        lines.append("")
    lines.extend(
        [
            "## Page Diagnostics",
            "",
            "| Page | Labels | Ink bbox | Edge px | Warnings | Failures |",
            "| ---: | --- | --- | --- | --- | --- |",
        ]
    )
    by_page = report["figures_by_page"]
    for page in sorted(report["pages"], key=lambda item: item["physical_page"]):
        labels = ", ".join(by_page[str(page["physical_page"])])
        edge = page["edge_distances_px"]
        edge_text = (
            "n/a"
            if edge["left"] is None
            else f"L{edge['left']} T{edge['top']} R{edge['right']} B{edge['bottom']}"
        )
        warnings = ", ".join(page["warnings"])
        failures = ", ".join(page["failures"])
        lines.append(
            f"| {page['physical_page']} | `{labels}` | `{page['ink_bbox']}` | "
            f"`{edge_text}` | {warnings} | {failures} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--background-threshold", type=int, default=250)
    parser.add_argument("--dark-threshold", type=int, default=175)
    parser.add_argument("--edge-margin-px", type=int, default=4)
    parser.add_argument("--min-ink-pixels", type=int, default=1000)
    parser.add_argument("--min-dark-pixels", type=int, default=250)
    args = parser.parse_args()

    out_dir = args.out_dir if args.out_dir.is_absolute() else ROOT / args.out_dir
    pdf_path = args.pdf if args.pdf.is_absolute() else ROOT / args.pdf
    manifest_path = out_dir / "figure_pages_manifest.json"
    provenance_path = out_dir / "render_provenance.json"
    manifest = load_json(manifest_path)
    provenance = load_json(provenance_path)
    if not isinstance(manifest, list):
        raise SystemExit(
            f"{display_path(manifest_path)} must contain a list of figure rows"
        )
    if not isinstance(provenance, dict):
        raise SystemExit(
            f"{display_path(provenance_path)} must contain a provenance object"
        )

    failures: list[str] = []
    warnings: list[str] = []
    current_pdf_sha = sha256_file(pdf_path)
    recorded_pdf_sha = provenance.get("pdf", {}).get("sha256")
    if recorded_pdf_sha != current_pdf_sha:
        failures.append(
            f"PDF digest mismatch: provenance={recorded_pdf_sha} current={current_pdf_sha}"
        )

    labels: list[str] = []
    figures_by_page: dict[int, list[str]] = {}
    for row in manifest:
        if not isinstance(row, dict):
            failures.append("manifest row is not an object")
            continue
        label = row.get("label")
        page = row.get("physical_page")
        if not isinstance(label, str) or not isinstance(page, int):
            failures.append(f"malformed manifest row: {row!r}")
            continue
        labels.append(label)
        figures_by_page.setdefault(page, []).append(label)

    duplicate_labels = [label for label, count in Counter(labels).items() if count > 1]
    if duplicate_labels:
        failures.append(
            f"duplicate manifest labels: {', '.join(sorted(duplicate_labels))}"
        )

    unique_pages = sorted(figures_by_page)
    provenance_pages = provenance.get("pages", {})
    if not isinstance(provenance_pages, dict):
        failures.append("provenance pages field is not an object")
        provenance_pages = {}

    page_results: list[dict[str, Any]] = []
    page_dir = out_dir / "pages"
    dimension_counts: Counter[tuple[int, int]] = Counter()
    for page in unique_pages:
        image_path = page_dir / f"page-{page:04d}.png"
        if not image_path.exists():
            failures.append(f"missing page image: {display_path(image_path)}")
            continue
        record = provenance_pages.get(str(page), {})
        recorded_sha = record.get("sha256") if isinstance(record, dict) else None
        actual_sha = sha256_file(image_path)
        if recorded_sha != actual_sha:
            failures.append(
                f"page {page}: digest mismatch provenance={recorded_sha} actual={actual_sha}"
            )
        result = analyze_page(
            image_path,
            background_threshold=args.background_threshold,
            dark_threshold=args.dark_threshold,
            edge_margin_px=args.edge_margin_px,
            min_ink_pixels=args.min_ink_pixels,
            min_dark_pixels=args.min_dark_pixels,
        )
        result["physical_page"] = page
        result["labels"] = figures_by_page[page]
        dimension_counts[(result["width"], result["height"])] += 1
        page_results.append(result)
        for failure in result["failures"]:
            failures.append(f"page {page}: {failure}")
        for warning in result["warnings"]:
            warnings.append(f"page {page}: {warning}")

    rendered_page_count = (
        len(list(page_dir.glob("page-*.png"))) if page_dir.exists() else 0
    )
    if rendered_page_count != len(unique_pages):
        failures.append(
            f"rendered page count mismatch: {rendered_page_count} PNGs for {len(unique_pages)} pages"
        )
    contact_dir = out_dir / "contact"
    contact_sheets = sorted(contact_dir.glob("sheet-*.png")) if contact_dir.exists() else []
    if not contact_sheets:
        failures.append("missing contact sheets")

    status = "passed" if not failures else "failed"
    report = {
        "schema": 1,
        "summary": {
            "status": status,
            "figure_count": len(manifest),
            "unique_physical_pages": len(unique_pages),
            "rendered_page_pngs": rendered_page_count,
            "contact_sheets": len(contact_sheets),
            "pdf_sha256": current_pdf_sha,
            "renderer": provenance.get("renderer", {}).get("version"),
            "dpi": provenance.get("options", {}).get("dpi"),
            "page_dimensions": {
                f"{width}x{height}": count
                for (width, height), count in sorted(dimension_counts.items())
            },
            "page_failure_count": sum(bool(page["failures"]) for page in page_results),
            "page_warning_count": sum(bool(page["warnings"]) for page in page_results),
        },
        "failures": failures,
        "warnings": warnings,
        "figures_by_page": {str(page): labels for page, labels in figures_by_page.items()},
        "pages": page_results,
    }
    json_path = out_dir / "rendered_figure_page_audit.json"
    md_path = out_dir / "rendered_figure_page_audit.md"
    json_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    write_markdown_report(report, md_path)

    print("Rendered figure page audit")
    print(f"  status: {status}")
    print(f"  figures: {len(manifest)}")
    print(f"  unique physical pages: {len(unique_pages)}")
    print(f"  rendered page PNGs: {rendered_page_count}")
    print(f"  contact sheets: {len(contact_sheets)}")
    print(f"  report: {display_path(md_path)}")
    if failures:
        print("  failures:")
        for failure in failures[:12]:
            print(f"    {failure}")
        if len(failures) > 12:
            print(f"    ... {len(failures) - 12} more")
    if warnings:
        print(f"  warnings: {len(warnings)}")
    return 0 if status == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())

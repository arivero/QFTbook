#!/usr/bin/env python3
"""Render current monograph pages that contain floated figures.

The structural figure audit checks labels and references.  This tool supports
the complementary rendered audit: it resolves hyperref figure destinations in
the compiled PDF, maps them to physical PDF pages, renders those pages with
``pdftoppm``, and writes a manifest that records every figure label, TeX
anchor, printed page, and physical page.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_AUX = ROOT / "monograph" / "tex" / "main.aux"
DEFAULT_PDF = ROOT / "monograph" / "tex" / "main.pdf"
DEFAULT_OUT = ROOT / "monograph" / "tex" / "build" / "figure_audit_current"


@dataclass(frozen=True)
class AuxFigure:
    label: str
    number: str
    printed_page: str
    anchor: str
    caption: str


@dataclass(frozen=True)
class FigureManifestRow:
    label: str
    number: str
    printed_page: str
    physical_page: int
    anchor: str
    caption: str


def read_group(text: str, start: int) -> tuple[str, int]:
    if start >= len(text) or text[start] != "{":
        raise ValueError(f"expected group at offset {start}")
    depth = 0
    out: list[str] = []
    i = start
    while i < len(text):
        ch = text[i]
        if ch == "\\" and i + 1 < len(text):
            if depth >= 1:
                out.append(ch)
                out.append(text[i + 1])
            i += 2
            continue
        if ch == "{":
            depth += 1
            if depth > 1:
                out.append(ch)
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return "".join(out), i + 1
            if depth < 0:
                raise ValueError(f"unbalanced group at offset {start}")
            out.append(ch)
        else:
            if depth >= 1:
                out.append(ch)
        i += 1
    raise ValueError(f"unterminated group at offset {start}")


def split_top_level_groups(group_text: str) -> list[str]:
    items: list[str] = []
    i = 0
    while i < len(group_text):
        if group_text[i].isspace():
            i += 1
            continue
        item, i = read_group(group_text, i)
        items.append(item)
    return items


def parse_aux_figures(aux_path: Path) -> list[AuxFigure]:
    figures: list[AuxFigure] = []
    for line_no, line in enumerate(aux_path.read_text(encoding="utf-8").splitlines(), start=1):
        marker = r"\newlabel{fig:"
        if marker not in line:
            continue
        label_start = line.index(r"\newlabel") + len(r"\newlabel")
        try:
            label, after_label = read_group(line, label_start)
            payload, _after_payload = read_group(line, after_label)
            fields = split_top_level_groups(payload)
        except ValueError as exc:
            raise SystemExit(f"{aux_path}:{line_no}: cannot parse figure label: {exc}") from exc
        if len(fields) < 4:
            raise SystemExit(f"{aux_path}:{line_no}: expected at least four newlabel fields")
        number, printed_page, caption, anchor = fields[:4]
        if not anchor.startswith("figure."):
            continue
        figures.append(
            AuxFigure(
                label=label,
                number=number,
                printed_page=printed_page,
                anchor=anchor,
                caption=caption,
            )
        )
    return figures


def run_json(command: list[str]) -> Any:
    try:
        proc = subprocess.run(command, check=True, text=True, capture_output=True)
    except FileNotFoundError as exc:
        raise SystemExit(f"required executable not found: {command[0]}") from exc
    except subprocess.CalledProcessError as exc:
        sys.stderr.write(exc.stderr)
        raise SystemExit(f"command failed: {' '.join(command)}") from exc
    return json.loads(proc.stdout)


def check_dependencies(*, render_page_images: bool, contact_sheets: bool) -> None:
    missing: list[str] = []
    if shutil.which("qpdf") is None:
        missing.append("qpdf (required to read PDF destination pages)")
    if render_page_images and shutil.which("pdftoppm") is None:
        missing.append("pdftoppm from Poppler (required to render page PNGs)")
    if contact_sheets and importlib.util.find_spec("PIL") is None:
        missing.append(
            "Pillow (required to write contact sheets; pass --no-contact-sheets "
            "only when page PNGs plus the manifest are the intended output)"
        )
    if missing:
        joined = "\n  - ".join(missing)
        raise SystemExit(f"missing required dependencies:\n  - {joined}")


def remove_unexpected_files(directory: Path, pattern: str, expected_names: set[str]) -> None:
    if not directory.exists():
        return
    for path in directory.glob(pattern):
        if path.name not in expected_names:
            path.unlink()


def pdf_destination_pages(pdf_path: Path) -> dict[str, int]:
    data = run_json(["qpdf", "--json", "--json-key=pages", "--json-key=qpdf", str(pdf_path)])
    page_by_object = {
        page["object"]: int(page["pageposfrom1"])
        for page in data.get("pages", [])
        if "object" in page and "pageposfrom1" in page
    }
    objects = data.get("qpdf", [{}])[1]

    figure_dest_objects: dict[str, str] = {}
    for value in objects.values():
        object_value = value.get("value")
        if not isinstance(object_value, dict):
            continue
        names = object_value.get("/Names")
        if not isinstance(names, list):
            continue
        if len(names) % 2:
            raise SystemExit("malformed PDF name tree: odd number of /Names entries")
        for name, dest_ref in zip(names[0::2], names[1::2]):
            if isinstance(name, str) and name.startswith("u:figure."):
                figure_dest_objects[name[2:]] = dest_ref

    figure_pages: dict[str, int] = {}
    for anchor, dest_ref in figure_dest_objects.items():
        key = f"obj:{dest_ref}"
        dest_object = objects.get(key, {})
        dest_value = dest_object.get("value")
        if not isinstance(dest_value, list) or not dest_value:
            continue
        page_ref = dest_value[0]
        page = page_by_object.get(page_ref)
        if page is not None:
            figure_pages[anchor] = page
    return figure_pages


def write_manifest(rows: list[FigureManifestRow], out_dir: Path) -> None:
    manifest_json = out_dir / "figure_pages_manifest.json"
    manifest_tsv = out_dir / "figure_pages_manifest.tsv"
    serializable = [
        {
            "label": row.label,
            "number": row.number,
            "printed_page": row.printed_page,
            "physical_page": row.physical_page,
            "anchor": row.anchor,
            "caption": row.caption,
        }
        for row in rows
    ]
    manifest_json.write_text(json.dumps(serializable, indent=2) + "\n", encoding="utf-8")
    with manifest_tsv.open("w", encoding="utf-8") as handle:
        handle.write("label\tnumber\tprinted_page\tphysical_page\tanchor\tcaption\n")
        for row in rows:
            caption = re.sub(r"\s+", " ", row.caption).replace("\t", " ")
            handle.write(
                f"{row.label}\t{row.number}\t{row.printed_page}\t"
                f"{row.physical_page}\t{row.anchor}\t{caption}\n"
            )


def render_pages(pdf_path: Path, pages: list[int], page_dir: Path, dpi: int, force: bool) -> None:
    page_dir.mkdir(parents=True, exist_ok=True)
    expected_names = {f"page-{page:04d}.png" for page in pages}
    remove_unexpected_files(page_dir, "page-*.png", expected_names)
    for page in pages:
        target = page_dir / f"page-{page:04d}.png"
        if target.exists() and not force:
            continue
        prefix = page_dir / f"page-{page:04d}"
        subprocess.run(
            [
                "pdftoppm",
                "-r",
                str(dpi),
                "-png",
                "-singlefile",
                "-f",
                str(page),
                "-l",
                str(page),
                str(pdf_path),
                str(prefix),
            ],
            check=True,
        )


def write_contact_sheets(
    rows: list[FigureManifestRow],
    out_dir: Path,
    columns: int,
    thumb_width: int,
) -> None:
    from PIL import Image, ImageDraw, ImageFont

    page_dir = out_dir / "pages"
    sheet_dir = out_dir / "contact"
    sheet_dir.mkdir(parents=True, exist_ok=True)

    by_page: dict[int, list[FigureManifestRow]] = {}
    for row in rows:
        by_page.setdefault(row.physical_page, []).append(row)

    font = ImageFont.load_default()
    entries = sorted(by_page.items())
    rows_per_sheet = 4
    max_cells = columns * rows_per_sheet
    sheet_count = (len(entries) + max_cells - 1) // max_cells
    expected_names = {f"sheet-{sheet_no:02d}.png" for sheet_no in range(1, sheet_count + 1)}
    remove_unexpected_files(sheet_dir, "sheet-*.png", expected_names)
    margin = 18
    label_height = 58

    for sheet_index in range(0, len(entries), max_cells):
        chunk = entries[sheet_index : sheet_index + max_cells]
        thumbs: list[tuple[Image.Image, str]] = []
        for page, page_rows in chunk:
            image_path = page_dir / f"page-{page:04d}.png"
            with Image.open(image_path) as img:
                img = img.convert("RGB")
                ratio = thumb_width / img.width
                thumb_height = int(img.height * ratio)
                thumb = img.resize((thumb_width, thumb_height))
            labels = ", ".join(row.number for row in page_rows)
            anchors = ", ".join(row.anchor.removeprefix("figure.") for row in page_rows[:3])
            if len(page_rows) > 3:
                anchors += f", +{len(page_rows) - 3}"
            text = f"PDF p.{page} | Fig. {labels}\n{anchors}"
            thumbs.append((thumb, text))

        cell_width = thumb_width + 2 * margin
        cell_height = max(thumb.height for thumb, _text in thumbs) + label_height + 2 * margin
        sheet_rows = (len(thumbs) + columns - 1) // columns
        sheet = Image.new("RGB", (columns * cell_width, sheet_rows * cell_height), "white")
        draw = ImageDraw.Draw(sheet)
        for idx, (thumb, text) in enumerate(thumbs):
            col = idx % columns
            row = idx // columns
            x = col * cell_width + margin
            y = row * cell_height + margin
            sheet.paste(thumb, (x, y))
            draw.rectangle([x, y, x + thumb.width - 1, y + thumb.height - 1], outline=(160, 160, 160))
            draw.multiline_text((x, y + thumb.height + 6), text, fill=(0, 0, 0), font=font, spacing=3)
        sheet_no = sheet_index // max_cells + 1
        sheet.save(sheet_dir / f"sheet-{sheet_no:02d}.png")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--aux", type=Path, default=DEFAULT_AUX)
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--dpi", type=int, default=120)
    parser.add_argument("--manifest-only", action="store_true")
    parser.add_argument("--force", action="store_true", help="re-render pages even if PNGs already exist")
    parser.add_argument("--no-contact-sheets", action="store_true")
    parser.add_argument("--columns", type=int, default=3)
    parser.add_argument("--thumb-width", type=int, default=360)
    args = parser.parse_args()

    aux_path = args.aux if args.aux.is_absolute() else ROOT / args.aux
    pdf_path = args.pdf if args.pdf.is_absolute() else ROOT / args.pdf
    out_dir = args.out_dir if args.out_dir.is_absolute() else ROOT / args.out_dir
    render_page_images = not args.manifest_only
    contact_sheets = render_page_images and not args.no_contact_sheets

    check_dependencies(render_page_images=render_page_images, contact_sheets=contact_sheets)

    figures = parse_aux_figures(aux_path)
    destination_pages = pdf_destination_pages(pdf_path)
    missing = [fig.anchor for fig in figures if fig.anchor not in destination_pages]
    if missing:
        preview = ", ".join(missing[:8])
        raise SystemExit(f"missing PDF destinations for {len(missing)} figures: {preview}")

    rows = [
        FigureManifestRow(
            label=fig.label,
            number=fig.number,
            printed_page=fig.printed_page,
            physical_page=destination_pages[fig.anchor],
            anchor=fig.anchor,
            caption=fig.caption,
        )
        for fig in figures
    ]
    rows.sort(key=lambda row: (row.physical_page, row.number, row.label))

    out_dir.mkdir(parents=True, exist_ok=True)
    write_manifest(rows, out_dir)
    unique_pages = sorted({row.physical_page for row in rows})

    if render_page_images:
        render_pages(pdf_path, unique_pages, out_dir / "pages", args.dpi, args.force)
        if contact_sheets:
            write_contact_sheets(rows, out_dir, args.columns, args.thumb_width)
        elif args.force:
            shutil.rmtree(out_dir / "contact", ignore_errors=True)

    print("Rendered figure-page audit data")
    print(f"  figures: {len(rows)}")
    print(f"  unique physical pages: {len(unique_pages)}")
    print(f"  PDF: {pdf_path.relative_to(ROOT) if pdf_path.is_relative_to(ROOT) else pdf_path}")
    print(f"  output: {out_dir.relative_to(ROOT) if out_dir.is_relative_to(ROOT) else out_dir}")
    print(f"  first physical page: {unique_pages[0] if unique_pages else 'n/a'}")
    print(f"  last physical page: {unique_pages[-1] if unique_pages else 'n/a'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

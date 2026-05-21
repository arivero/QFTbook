#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
TRANSCRIPTION_DIR = ROOT / "transcription"
BUILD_DIR = TRANSCRIPTION_DIR / "build"
SOURCE_DIR = TRANSCRIPTION_DIR / "source_pdfs"
OCR_DIR = TRANSCRIPTION_DIR / "ocr_json"
RENDER_DIR = BUILD_DIR / "rendered_pages"
VISION_SOURCE = ROOT / "tools" / "VisionOCR.swift"
VISION_EXE = BUILD_DIR / "vision_ocr"


@dataclass(frozen=True)
class Note:
    slug: str
    title: str
    pdf: Path


NOTES = [
    Note("253a", "253a lectures 2022", ROOT / "references" / "253a lectures 2022.pdf"),
    Note("253b", "253b lecture notes 2023", ROOT / "references" / "253b lecture notes 2023.pdf"),
    Note("253c", "253c 2023", ROOT / "references" / "253c 2023.pdf"),
]


def run(cmd: list[str], *, cwd: Path = ROOT, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=str(cwd),
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
    )


def pdf_page_count(pdf: Path) -> int:
    out = run(["pdfinfo", str(pdf)], capture=True).stdout
    match = re.search(r"^Pages:\s+(\d+)\s*$", out, re.MULTILINE)
    if not match:
        raise RuntimeError(f"Could not determine page count for {pdf}")
    return int(match.group(1))


def compile_vision_ocr() -> None:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    if VISION_EXE.exists() and VISION_EXE.stat().st_mtime >= VISION_SOURCE.stat().st_mtime:
        return
    run(["swiftc", str(VISION_SOURCE), "-o", str(VISION_EXE)])


def ensure_source_links() -> dict[str, str]:
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    tex_paths: dict[str, str] = {}
    for note in NOTES:
        target = SOURCE_DIR / f"{note.slug}.pdf"
        if target.exists() or target.is_symlink():
            target.unlink()
        target.symlink_to(note.pdf)
        tex_paths[note.slug] = f"source_pdfs/{note.slug}.pdf"
    return tex_paths


def render_page(note: Note, page: int, dpi: int) -> Path:
    note_render_dir = RENDER_DIR / note.slug
    note_render_dir.mkdir(parents=True, exist_ok=True)
    prefix = note_render_dir / f"p{page:03d}"
    image = prefix.with_suffix(".png")
    if image.exists():
        return image
    run([
        "pdftoppm",
        "-f",
        str(page),
        "-l",
        str(page),
        "-singlefile",
        "-png",
        "-r",
        str(dpi),
        str(note.pdf),
        str(prefix),
    ])
    return image


def ocr_json_path(note: Note, page: int) -> Path:
    return OCR_DIR / note.slug / f"p{page:03d}.json"


def run_ocr_batch(note: Note, pages: list[int], dpi: int, language_correction: bool, force: bool) -> None:
    missing = [p for p in pages if force or not ocr_json_path(note, p).exists()]
    if not missing:
        return

    images = [render_page(note, page, dpi) for page in missing]
    cmd = [str(VISION_EXE)]
    if language_correction:
        cmd.append("--language-correction")
    cmd.extend(str(image) for image in images)
    pages_json = json.loads(run(cmd, capture=True).stdout)

    note_ocr_dir = OCR_DIR / note.slug
    note_ocr_dir.mkdir(parents=True, exist_ok=True)
    for page_num, page_json in zip(missing, pages_json):
        out = ocr_json_path(note, page_num)
        page_json["pdf"] = str(note.pdf)
        page_json["pdf_page"] = page_num
        page_json["note_slug"] = note.slug
        page_json["note_title"] = note.title
        page_json["ocr_engine"] = "Apple Vision VNRecognizeTextRequest"
        page_json["ocr_language_correction"] = language_correction
        page_json["render_dpi"] = dpi
        out.write_text(json.dumps(page_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def clean_verbatim_text(text: str) -> str:
    text = text.replace("\x0c", "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\\end{Verbatim}", "\\textbackslash{}end\\{Verbatim\\}")
    return text


def tex_escape_text(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def page_review_summary(page_json: dict) -> tuple[float, int, int]:
    lines = page_json.get("lines", [])
    confidences = [float(line.get("confidence", 0.0)) for line in lines]
    avg = mean(confidences) if confidences else 0.0
    low = sum(1 for conf in confidences if conf < 0.45)
    very_low = sum(1 for conf in confidences if conf < 0.30)
    return avg, low, very_low


def write_main_tex(tex_paths: dict[str, str], page_counts: dict[str, int]) -> Path:
    out = TRANSCRIPTION_DIR / "qft_notes_transcription.tex"
    lines: list[str] = []
    lines.extend([
        r"\documentclass[10pt,oneside]{book}",
        r"\usepackage[margin=0.65in]{geometry}",
        r"\usepackage{graphicx}",
        r"\usepackage{fvextra}",
        r"\usepackage{xcolor}",
        r"\usepackage{hyperref}",
        r"\usepackage{bookmark}",
        r"\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue}",
        r"\setlength{\parindent}{0pt}",
        r"\setlength{\parskip}{0.45em}",
        r"\newcommand{\sourcefacsimile}[2]{%",
        r"  \begin{center}",
        r"  \fbox{\includegraphics[page=#2,width=0.96\linewidth,height=0.55\textheight,keepaspectratio]{#1}}",
        r"  \end{center}",
        r"}",
        r"\newcommand{\reviewflag}[1]{\textcolor{red!70!black}{#1}}",
        r"\begin{document}",
        r"\frontmatter",
        r"\begin{titlepage}",
        r"\centering",
        r"{\Huge QFT Lecture Notes Transcription\par}",
        r"\vspace{1em}",
        r"{\large OCR draft with embedded source-page facsimiles\par}",
        r"\vfill",
        r"\begin{minipage}{0.82\linewidth}",
        r"This TeX file is generated from image-only handwritten PDFs. Each page includes a rendered source facsimile so figures, diagrams, and handwritten formulas remain available as ground truth. The text block below each source page is OCR output and should be reviewed against the facsimile, especially for equations, Greek letters, spinor indices, and diagrams.",
        r"\end{minipage}",
        r"\end{titlepage}",
        r"\tableofcontents",
        r"\mainmatter",
    ])

    for note in NOTES:
        lines.append(rf"\chapter*{{{tex_escape_text(note.title)}}}")
        lines.append(rf"\addcontentsline{{toc}}{{chapter}}{{{tex_escape_text(note.title)}}}")
        for page in range(1, page_counts[note.slug] + 1):
            page_json = json.loads(ocr_json_path(note, page).read_text(encoding="utf-8"))
            avg_conf, low_count, very_low_count = page_review_summary(page_json)
            page_lines = [clean_verbatim_text(item.get("text", "")) for item in page_json.get("lines", [])]
            transcript = "\n".join(page_lines).strip()
            if not transcript:
                transcript = "[No OCR text detected on this page.]"

            title = f"{note.title}, page {page}"
            flag = ""
            if very_low_count:
                flag = rf"\reviewflag{{Review carefully: {very_low_count} very-low-confidence OCR lines.}}"
            elif low_count:
                flag = rf"\reviewflag{{Review: {low_count} low-confidence OCR lines.}}"
            else:
                flag = "No low-confidence OCR lines detected by the engine."

            lines.extend([
                r"\clearpage",
                rf"\section*{{{tex_escape_text(title)}}}",
                rf"\addcontentsline{{toc}}{{section}}{{{tex_escape_text(note.slug)} p. {page}}}",
                rf"\sourcefacsimile{{{tex_paths[note.slug]}}}{{{page}}}",
                rf"\textbf{{OCR metadata.}} Engine: Apple Vision; render DPI: {page_json.get('render_dpi')}; average confidence: {avg_conf:.3f}. {flag}",
                r"\subsection*{OCR transcription draft}",
                r"\begin{Verbatim}[breaklines=true,breakanywhere=true,fontsize=\small]",
                transcript,
                r"\end{Verbatim}",
            ])

    lines.append(r"\end{document}")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def write_report(page_counts: dict[str, int]) -> Path:
    out = TRANSCRIPTION_DIR / "ocr_review_report.md"
    lines = ["# OCR Review Report", ""]
    for note in NOTES:
        page_summaries = []
        for page in range(1, page_counts[note.slug] + 1):
            page_json = json.loads(ocr_json_path(note, page).read_text(encoding="utf-8"))
            avg, low, very_low = page_review_summary(page_json)
            page_summaries.append((page, avg, low, very_low, len(page_json.get("lines", []))))
        worst = sorted(page_summaries, key=lambda item: (item[1], -item[3], -item[2]))[:20]
        avg_all = mean(item[1] for item in page_summaries)
        lines.extend([
            f"## {note.title}",
            "",
            f"- Pages: {page_counts[note.slug]}",
            f"- Mean page OCR confidence: {avg_all:.3f}",
            "- Lowest-confidence pages:",
            "",
            "| Page | Avg conf | Low lines | Very low lines | OCR lines |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ])
        for page, avg, low, very_low, count in worst:
            lines.append(f"| {page} | {avg:.3f} | {low} | {very_low} | {count} |")
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build OCR-backed TeX transcription for QFT notes.")
    parser.add_argument("--dpi", type=int, default=300, help="DPI used when rendering pages for OCR.")
    parser.add_argument("--batch-size", type=int, default=12, help="Number of rendered page images per OCR call.")
    parser.add_argument("--force", action="store_true", help="Regenerate OCR JSON even if it already exists.")
    parser.add_argument("--language-correction", action="store_true", help="Enable Vision language correction.")
    parser.add_argument("--slugs", nargs="*", default=[note.slug for note in NOTES], help="Subset of notes to process.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    selected = [note for note in NOTES if note.slug in set(args.slugs)]
    if not selected:
        raise SystemExit("No notes selected.")

    for directory in [TRANSCRIPTION_DIR, BUILD_DIR, OCR_DIR, RENDER_DIR]:
        directory.mkdir(parents=True, exist_ok=True)

    compile_vision_ocr()
    tex_paths = ensure_source_links()
    page_counts = {note.slug: pdf_page_count(note.pdf) for note in NOTES}

    for note in selected:
        count = page_counts[note.slug]
        print(f"OCR {note.slug}: {count} pages at {args.dpi} DPI")
        for start in range(1, count + 1, args.batch_size):
            batch = list(range(start, min(start + args.batch_size, count + 1)))
            run_ocr_batch(note, batch, args.dpi, args.language_correction, args.force)
            print(f"  processed pages {batch[0]}-{batch[-1]}")

    missing = []
    for note in NOTES:
        for page in range(1, page_counts[note.slug] + 1):
            if not ocr_json_path(note, page).exists():
                missing.append(f"{note.slug} p.{page}")
    if missing:
        raise RuntimeError("Missing OCR output: " + ", ".join(missing[:20]))

    tex = write_main_tex(tex_paths, page_counts)
    report = write_report(page_counts)
    print(f"Wrote {tex}")
    print(f"Wrote {report}")


if __name__ == "__main__":
    main()

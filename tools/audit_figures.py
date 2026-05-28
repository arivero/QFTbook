#!/usr/bin/env python3
"""Audit figure anchoring and TikZ usage in the monograph TeX sources."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "monograph" / "tex" / "volumes"


FIGURE_RE = re.compile(r"\\begin\{figure\}(?:\[(?P<placement>[^\]]*)\])?(?P<body>.*?)\\end\{figure\}", re.S)
LABEL_RE = re.compile(r"\\label\{(?P<label>fig:[^}]+)\}")
REF_RE = re.compile(r"\\(?P<cmd>Cref|cref|autoref|pageref|ref)\s*\{(?P<body>[^}]*fig:[^}]*)\}")
TIKZ_RE = re.compile(r"\\begin\{tikzpicture\}")
TIKZ_BLOCK_RE = re.compile(r"\\begin\{tikzpicture\}(?P<body>.*?)\\end\{tikzpicture\}", re.S)


@dataclass(frozen=True)
class FigureRecord:
    path: Path
    line: int
    placement: str
    labels: tuple[str, ...]


@dataclass(frozen=True)
class InlineTikzRecord:
    path: Path
    line: int
    lines: int


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def strip_figure_blocks(text: str) -> tuple[str, list[tuple[int, int, re.Match[str]]]]:
    blocks: list[tuple[int, int, re.Match[str]]] = []
    pieces: list[str] = []
    last = 0
    for match in FIGURE_RE.finditer(text):
        blocks.append((match.start(), match.end(), match))
        pieces.append(text[last:match.start()])
        pieces.append(" " * (match.end() - match.start()))
        last = match.end()
    pieces.append(text[last:])
    return "".join(pieces), blocks


def refs_in_text(text: str) -> set[str]:
    refs: set[str] = set()
    for match in REF_RE.finditer(text):
        for item in match.group("body").split(","):
            label = item.strip()
            if label.startswith("fig:"):
                refs.add(label)
    return refs


def audit(
    paths: list[Path],
) -> tuple[list[FigureRecord], set[str], int, int, dict[str, int], list[InlineTikzRecord]]:
    figures: list[FigureRecord] = []
    inline_tikz: list[InlineTikzRecord] = []
    body_refs: set[str] = set()
    tikz_inside = 0
    tikz_outside = 0
    placements: dict[str, int] = {}

    for path in sorted(paths):
        text = path.read_text(encoding="utf-8")
        stripped, blocks = strip_figure_blocks(text)
        body_refs |= refs_in_text(stripped)
        tikz_outside += len(TIKZ_RE.findall(stripped))
        for tikz_match in TIKZ_BLOCK_RE.finditer(stripped):
            body = tikz_match.group("body")
            inline_tikz.append(
                InlineTikzRecord(
                    path=path.relative_to(ROOT),
                    line=line_number(stripped, tikz_match.start()),
                    lines=body.count("\n") + 2,
                )
            )
        for start, _end, match in blocks:
            body = match.group("body")
            labels = tuple(m.group("label") for m in LABEL_RE.finditer(body))
            placement = match.group("placement") or ""
            placements[placement] = placements.get(placement, 0) + 1
            tikz_inside += len(TIKZ_RE.findall(body))
            figures.append(
                FigureRecord(
                    path=path.relative_to(ROOT),
                    line=line_number(text, start),
                    placement=placement,
                    labels=labels,
                )
            )
    return figures, body_refs, tikz_inside, tikz_outside, placements, inline_tikz


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="TeX files or directories to audit; defaults to monograph/tex/volumes",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="return nonzero when any floated figure label lacks a body reference",
    )
    parser.add_argument(
        "--list-inline",
        action="store_true",
        help="list TikZ pictures that are not inside figure environments",
    )
    parser.add_argument(
        "--inline-long-threshold",
        type=int,
        default=30,
        help="line-count threshold for reporting large inline TikZ diagrams",
    )
    parser.add_argument(
        "--strict-inline-long",
        action="store_true",
        help="return nonzero when an inline TikZ diagram exceeds --inline-long-threshold",
    )
    args = parser.parse_args()

    roots = args.paths or [DEFAULT_SOURCE]
    tex_paths: list[Path] = []
    for root in roots:
        root = root if root.is_absolute() else ROOT / root
        if root.is_dir():
            tex_paths.extend(root.rglob("*.tex"))
        elif root.is_file():
            tex_paths.append(root)
        else:
            print(f"missing path: {root}", file=sys.stderr)
            return 2

    figures, body_refs, tikz_inside, tikz_outside, placements, inline_tikz = audit(tex_paths)
    labels = [label for fig in figures for label in fig.labels]
    missing_label = [fig for fig in figures if not fig.labels]
    duplicate_labels = sorted({label for label in labels if labels.count(label) > 1})
    unreferenced = [fig for fig in figures if fig.labels and not any(label in body_refs for label in fig.labels)]

    print("Figure audit")
    print(f"  TeX files scanned: {len(tex_paths)}")
    print(f"  figure environments: {len(figures)}")
    print(f"  figure labels: {len(labels)}")
    print(f"  figure labels referenced from body text: {len(set(labels) & body_refs)}")
    print(f"  unreferenced labeled figures: {len(unreferenced)}")
    print(f"  figure environments without fig: label: {len(missing_label)}")
    print(f"  duplicate fig: labels: {len(duplicate_labels)}")
    print(f"  TikZ inside figures: {tikz_inside}")
    print(f"  TikZ outside figures: {tikz_outside}")
    long_inline_tikz = [rec for rec in inline_tikz if rec.lines > args.inline_long_threshold]
    print(
        f"  inline TikZ above {args.inline_long_threshold} lines: "
        f"{len(long_inline_tikz)}"
    )
    if placements:
        print("  placement specifiers:")
        for key, value in sorted(placements.items(), key=lambda kv: (kv[0] != "H", kv[0])):
            shown = key or "<none>"
            print(f"    [{shown}]: {value}")

    if duplicate_labels:
        print("\nDuplicate figure labels:")
        for label in duplicate_labels:
            print(f"  {label}")

    if missing_label:
        print("\nFigures without fig: labels:")
        for fig in missing_label:
            print(f"  {fig.path}:{fig.line}")

    if unreferenced:
        print("\nUnreferenced labeled figures:")
        for fig in unreferenced:
            joined = ", ".join(fig.labels)
            print(f"  {fig.path}:{fig.line}: {joined}")

    if args.list_inline:
        print("\nInline TikZ outside figure environments:")
        for rec in sorted(inline_tikz, key=lambda item: (str(item.path), item.line)):
            marker = " large" if rec.lines > args.inline_long_threshold else ""
            print(f"  {rec.path}:{rec.line}: {rec.lines} lines{marker}")

    if long_inline_tikz and not args.list_inline:
        print("\nInline TikZ above threshold:")
        for rec in sorted(long_inline_tikz, key=lambda item: (str(item.path), item.line)):
            print(f"  {rec.path}:{rec.line}: {rec.lines} lines")

    if args.strict and (unreferenced or missing_label or duplicate_labels):
        return 1
    if args.strict_inline_long and long_inline_tikz:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Issue #767 Print-Size Figure Inspection Ledger

Scope: durable follow-up to issue #767.  This note records the current
per-figure inspection ledger and the first original-resolution review tranche.
It does not close the issue; most figures remain pending human print-size
inspection.

## Artifact Identity

- PDF: `monograph/tex/main.pdf`
- PDF SHA-256:
  `8671d9c77082d3cc1699ff2003ea578cd7e79f571d76a270463fca71baecebe3`
- Figure manifest:
  `monograph/tex/build/figure_audit_current/figure_pages_manifest.json`
- Render provenance:
  `monograph/tex/build/figure_audit_current/render_provenance.json`
- Machine page audit:
  `monograph/tex/build/figure_audit_current/rendered_figure_page_audit.md`
- Human inspection ledger:
  `planning/release_audits/2026-06-04_issue767_print_size_figure_ledger.tsv`
- Ledger verifier:
  `tools/audit_print_size_figure_ledger.py`

## Counts

- Floated figures represented in the ledger: 172
- Unique physical PDF pages containing figures: 168
- Rendered page PNGs: 168
- Contact sheets: 14
- Human-reviewed figures in this tranche: 10
- Pending human-reviewed figures after this tranche: 162

## Method

The rendered pages were regenerated with `tools/render_figure_pages.py --force`
after the current PDF build, then checked by
`tools/audit_rendered_figure_pages.py`.  The ledger was generated from the
current manifest and the structured rendered-page diagnostics so every figure
row carries the current PDF digest, physical page, page PNG path, page-image
digest, and machine warnings.

`tools/audit_print_size_figure_ledger.py` verifies that the ledger rows still
match the current rendered manifest and page diagnostics.  Its default mode
allows pending rows; `--require-complete` is the closure gate for the final
all-figure inspection.

The first tranche was inspected on the individual 120-dpi page PNGs at original
render size, not on reduced contact sheets.  Each reviewed row records the
following checks:

- print-size label and line-weight legibility;
- caption/figure separation;
- grayscale accessibility when the machine audit reports substantial color use;
- whether the figure has semantic value beyond restating prose;
- whether the figure is being overread as theorem-level evidence.

Higher-resolution crops were not needed for the ten reviewed figures; none has
dense small labels beyond the original page render.  Later dense figures should
receive crop review when the full-page PNG is insufficient.

## Reviewed Tranche

The following figures passed original-resolution review:

- `fig:wightman-fields-to-local-algebras`
- `fig:wightman-reconstruction`
- `fig:wightman-tube-analyticity`
- `fig:aqft-local-net`
- `fig:gns-representation`
- `fig:reeh-schlieder-cyclicity`
- `fig:dhr-localized-sector`
- `fig:split-property`
- `fig:modular-wedge-flow`
- `fig:translation-spectrum-mass-shell`

The color-warning pages in this tranche, pages 145 and 193, were checked
explicitly.  Their distinctions are carried by labels, geometry, arrows, and
line placement rather than by hue alone.

## Boundary

This pass establishes the durable ledger and audits the first ten figures only.
The older contact-sheet inspection remains useful for triage, but it is not
treated here as evidence for the remaining 162 pending figure rows.  Issue #767
should stay open until all rows are reviewed and any defects found in later
tranches are repaired and re-rendered.

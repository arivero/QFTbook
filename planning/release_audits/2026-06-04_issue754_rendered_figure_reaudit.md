# Issue #754 Rendered Figure Re-Audit

Scope: release-QA rendered figure pass after the post-#639 manuscript
expansion.  This note records audit evidence for rendered pages and visual
legibility; it is not a substitute for the theorem-boundary and derivation
audits tracked by the depth/proof-debt issues.

## Artifact Identity

- PDF: `monograph/tex/main.pdf`
- PDF SHA-256:
  `0171e0f3b86c6717cbb117f83e57c431cdfaba97c2d531188caa514d08a2a975`
- Figure manifest:
  `monograph/tex/build/figure_audit_current/figure_pages_manifest.json`
- Render provenance:
  `monograph/tex/build/figure_audit_current/render_provenance.json`
- Rendered-page QA report:
  `monograph/tex/build/figure_audit_current/rendered_figure_page_audit.md`

## Counts

- Floated figures: 172
- Unique physical PDF pages containing figures: 168
- Rendered page PNGs: 168
- Contact sheets: 14
- Multi-figure rendered pages: 4

The strict structural audit reports 172 figure environments, 172 labels, 172
body references, no missing labels, no duplicate labels, no unreferenced
labeled figures, and no inline TikZ above the 30-line threshold.

## Machine QA

`tools/audit_rendered_figure_pages.py` validates:

- current PDF digest against render provenance;
- per-page PNG digests against render provenance;
- rendered page count against the manifest's unique physical pages;
- contact-sheet presence;
- page dimensions;
- blank or nearly blank page failures;
- absence of dark print-size content;
- ink touching the physical page edge as a clipping proxy;
- substantial color usage as a warning for grayscale/accessibility inspection.

Current result: passed.  All 168 pages share dimensions `1020x1320`; no blank,
digest-mismatched, missing, or edge-clipped page was found.  The script emitted
27 color-use warnings.  The warned pages were visually inspected on larger
warning sheets; color distinctions were redundant with labels, arrows,
dash/solid style, geometry, or explicit text.

## Visual Sweep

All 14 contact sheets were inspected for:

- missing rendered content;
- clipping or ink at the physical page boundary;
- line weight and font-size failures visible at print scale;
- caption/figure collisions;
- page-placement crowding;
- color-only distinctions;
- diagrams that merely repeat nearby prose without contributing mathematical or
  physical structure;
- diagrams presented as evidence for theorem-level claims not established in
  the surrounding text.

No repair-worthy rendered defect was found.  Dense perturbative and RG figures
remain legible enough at the rendered page scale.  The color-heavy figures use
text labels and geometric or line-style separation, so grayscale loss does not
remove the mathematical distinction.  The instanton/profile diagrams are local
data aids; they are not treated here as substitutes for the deeper fluctuation
measure and amplitude derivations owed in the physics chapters.

## Verification Commands

```bash
tools/render_figure_pages.py --force
tools/audit_rendered_figure_pages.py
tools/audit_figures.py --strict
python3 -m py_compile tools/audit_rendered_figure_pages.py tools/test_audit_rendered_figure_pages.py
tools/test_audit_rendered_figure_pages.py
```

Release-candidate usage: `tools/verify_release.sh --rendered-figures` now runs
both forced rendered-page generation and the rendered-page QA audit.  The public
numerical smoke suite remains a separate explicit option:
`tools/verify_release.sh --qft-scripts-smoke`.

# Issue #767 Print-Size Figure Inspection Ledger

Scope: durable follow-up to issue #767.  This note records the current
per-figure inspection ledger and the original-resolution review tranches
completed so far.  It does not close the issue; most figures remain pending
human print-size inspection.

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
- Human-reviewed figures so far: 50
- Pending figures after these tranches: 122

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

The reviewed tranches were inspected on the individual 120-dpi page PNGs at
original render size, not on reduced contact sheets.  Each reviewed row records
the following checks:

- print-size label and line-weight legibility;
- caption/figure separation;
- grayscale accessibility when the machine audit reports substantial color use;
- whether the figure has semantic value beyond restating prose;
- whether the figure is being overread as theorem-level evidence.

Higher-resolution crops were not needed for the fifty reviewed figures; none has
dense small labels beyond the original page render.  Later dense figures should
receive crop review when the full-page PNG is insufficient.

## Reviewed Tranches

The following first-tranche figures passed original-resolution review:

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

The following second-tranche figures also passed original-resolution review:

- `fig:causal-lightcone-local-operation`
- `fig:anharmonic-second-order-vacuum-topologies`
- `fig:anharmonic-normalized-two-point-connected-diagrams`
- `fig:volume-i-derivative-interaction-contractions`
- `fig:scalar-mass-shell-branches`
- `fig:current-conservation-boundary-flux`
- `fig:complex-time-contour-ordering`
- `fig:uniform-wick-rotation-insertion-times`
- `fig:feynman-prescription-from-wick-rotation`
- `fig:os-reflection-positivity`

The second tranche includes the color-warning page 197.  It was checked
explicitly: the lightcone, local operation, and spacelike-signal distinctions
are carried by labels, geometry, dashed/solid arrows, and placement rather than
by hue alone.

The following third-tranche figures also passed original-resolution review:

- `fig:kallen-lehmann-feynman-contour-closures`
- `fig:standard-boost-positive-mass-shell`
- `fig:kallen-lehmann-pole-and-continuum`
- `fig:normalized-correlator-component-selection`
- `fig:euclidean-phi-four-feynman-rules`
- `fig:four-point-wick-connected-decomposition`
- `fig:bcfw-factorization`
- `fig:haag-ruelle-spectral-transfer`
- `fig:exchange-model-stu-tree-routings`
- `fig:resonance-k-plane-outgoing-growth`

The third tranche includes the color-warning page 451.  It was checked
explicitly: the positive mass-shell neighborhood, support region, reflected
transfer, and cone geometry are carried by labels, placement, filled regions,
and dashed reference lines rather than by hue alone.

The following fourth-tranche figures also passed original-resolution review:

- `fig:resonance-second-sheet-energy-plane`
- `fig:self-energy-cut-continuation`
- `fig:chain-amplitude-single-channel`
- `fig:bethe-salpeter-kernel-homogeneous-equation`
- `fig:fixed-t-physical-edge-cuts`
- `fig:triangle-landau-positive-parameter-data`
- `fig:triangle-landau-convex-hull-criterion`
- `fig:lehmann-ellipse-nearest-singularity`
- `fig:watson-elastic-form-factor-cut`
- `fig:eikonal-impact-parameter-exponentiation`

The fourth tranche includes the color-warning page 515.  It was checked
explicitly: first-sheet and second-sheet branch data, bound-state markers, cut
direction, and the resonance pole are carried by labels, placement, arrows, and
the caption rather than by hue alone.  Physical page 571 carries two reviewed
figures; both the Landau vector-closure figure and the convex-hull criterion
figure were checked on the full original page.

The following fifth-tranche figures also passed original-resolution review:

- `fig:regge-pole-contour`
- `fig:partial-wave-box-profile-lehmann-domain`
- `fig:subtracted-fixed-t-cauchy-contour`
- `fig:volume-ii-source-legendre`
- `fig:background-field-shifted-cubic-vertices`
- `fig:volume-ii-tadpoles-and-1pi`
- `fig:volume-ii-connected-from-1pi`
- `fig:volume-ii-branch-perturbation-condition`
- `fig:volume-ii-euclidean-convexity`
- `fig:volume-ii-counterterm-census`

The fifth tranche includes the color-warning pages 607, 638, and 639.  They
were checked explicitly: the Cauchy-contour figure distinguishes cuts,
subtraction points, and contour deformation by labels and geometry; the
branch-condition figure distinguishes the tangent, branch point, and shifted
exponent by labels, panels, and dashed/solid line style; the Euclidean convexity
figure distinguishes support lines, stationary branches, and the exact convex
effective action by labels and dashed/solid line style.  Physical page 624
carries two reviewed figures; both the shifted cubic-vertex expansion and the
tadpole/1PI mechanism figure were checked on the full original page.

## Boundary

This pass establishes the durable ledger and audits the first fifty figures.
The older contact-sheet inspection remains useful for triage, but it is not
treated here as evidence for the remaining 122 pending figure rows.  Issue #767
should stay open until all rows are reviewed and any defects found in later
tranches are repaired and re-rendered.

# 2026-05-25 Eleventh-Chapter And BV/Wilsonian Audit

## Scope

- Added eleventh chapters to Volumes VI--XII and included them in the
  corresponding volume manifests.
- Updated chapter dossiers and the systematic development matrix for the new
  special-volume material.
- Deepened Volume VII supersymmetric gauge theory with:
  - NSVZ coordinate beta function from holomorphic coupling, rescaling anomaly,
    and canonical normalization;
  - SQCD specialization in the chapter's trace and coupling conventions;
  - Witten index logic for pure supersymmetric Yang--Mills, including
    finite-volume pairing and the small-circle affine-Toda computation.
- Tightened the gauge-theory Wilsonian rule: continuum gauge-fixed Wilsonian
  path integrals are gauge-consistent through the quantum BV master equation
  before restriction to a gauge-fixing Lagrangian submanifold; the lattice
  construction is the companion finite-cutoff gauge-invariant route.
- Expanded the BV chapter so the formalism is introduced self-containedly:
  variational Euler operators, odd symplectic origin of the antibracket,
  Noether/Koszul--Tate construction of the minimal complex, component
  derivation of the quantum master equation, and gauge-fixed Wilsonian BV
  consistency.

## Verification

- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `rg -n -P '\\over(?![A-Za-z])' monograph/tex`: no matches.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean final log scan.
- `pdfinfo monograph/tex/main.pdf`: 1150 pages.

## Rendered PDF Spot Checks

Rendered PNGs were produced with `pdftoppm` at 1275 x 1650 resolution.
Physical PDF page numbers are used below; printed manuscript page numbers are
39 lower in main matter.

- BV variational derivatives and antibracket: physical pages 674 and 677,
  `/tmp/qft_bv_phys674.png`, `/tmp/qft_bv_phys677.png`.
- BV QME and gauge-fixed Wilsonian consistency: physical page 683,
  `/tmp/qft_bv_phys683.png`.
- Volume VI, Chapter 72 title page: physical page 937,
  `/tmp/qft_ch72_title_phys937.png`.
- Volume VII, Chapter 83 title page: physical page 981,
  `/tmp/qft_ch83_title_phys981.png`.
- Volume VIII, Chapter 94 title page: physical page 1014,
  `/tmp/qft_ch94_title_phys1014.png`.
- Volume IX, Chapter 105 title page: physical page 1046,
  `/tmp/qft_ch105_title_phys1046.png`.
- Volume X, Chapter 116 title page: physical page 1080,
  `/tmp/qft_ch116_title_phys1080.png`.
- Volume XI, Chapter 127 title page: physical page 1116,
  `/tmp/qft_ch127_title_phys1116.png`.
- Volume XII, Chapter 138 title page: physical page 1148,
  `/tmp/qft_ch138_title_phys1148.png`.

## Corrections During Verification

- Replaced undefined macros with explicit `\operatorname{...}` forms.
- Shortened an overfull BV paragraph after the self-contained BV expansion.
- Tightened supersymmetry wording around holomorphic claims and theorem status.
- Corrected the initial render-page audit after detecting the physical-page
  versus printed-page offset.

# 2026-05-24 Issue #341 Perturbative AQFT Audit

## Issue

GitHub issue #341 noted that perturbative AQFT was absent despite the
planning documents listing it among the comparison frameworks.  The requested
minimal fix was a remark that pAQFT is known but not developed.

## Edits

- Added `sec:perturbative-aqft-bridge` to the algebraic QFT chapter, titled
  "Perturbative Algebraic QFT and Interacting Examples."
- Defined microcausal functionals and their wavefront-set condition.
- Displayed the Hadamard star product and its Peierls-bracket semiclassical
  limit.
- Introduced Epstein--Glaser time-ordered products, diagonal extension,
  causal factorization, relative \(S\)-matrices, and the resulting formal
  perturbative local net.
- Stated the local nature of renormalization through
  Stueckelberg--Petermann redefinitions and identified the BV cohomological
  extension needed for gauge theories.
- Recorded that pAQFT should be developed as deep theory in later chapters,
  including time-ordered-product extensions, interacting fields, time-slice,
  BV cohomology, and the relation to 1PI/Wilsonian effective actions.
- Added an explicit mandate that AQFT objects must be developed in substantial
  interacting examples rather than treated only as abstract axioms.
- Added the frontier-development standard: the monograph should formulate and
  try to close genuine gaps exposed by comparing Wightman, Euclidean,
  Wilsonian, pAQFT, BV, and operator-algebraic formulations.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 750 pages.

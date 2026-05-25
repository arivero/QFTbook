# 2026-05-25 Issue 556: Wilson Gauge Reflection Positivity

## Scope

Issue #556 flagged that Volume XI Chapter 3 asserted Wilson plaquette
reflection positivity through a positive-character expansion without
displaying the Osterwalder-Seiler proof.

## Edits

- Replaced the gauge-field caveat paragraph by a finite-volume compact-group
  theorem.
- Defined the gauge link variables, plaquette holonomy, product Haar measure,
  reflection action, and positive algebra.
- Stated and proved the Osterwalder-Seiler character criterion: if the
  plaquette weight has an absolutely convergent nonnegative character
  expansion, crossing plaquettes decompose by Peter-Weyl into reflected
  squares.
- Proved Wilson plaquette reflection positivity for \(SU(N)\) and \(U(N)\)
  by expanding the exponential in defining and conjugate defining characters
  and decomposing tensor products into irreducibles with nonnegative
  multiplicities.
- Added the \(U(1)\) Bessel/Fourier expansion as the abelian version.
- Explained why negative rectangle coefficients in common improved actions
  fall outside the positive-character proof.
- Updated the Volume XI Chapter 3 dossier.

## Targeted Verification

No calculation script was edited for this text-only theorem/proof pass.

## Repository Verification

- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

The first build attempt correctly failed the final log scan because the new
text used TeX primitive `\over`; this was replaced by `\frac`.  The rerun
completed cleanly, and the rebuilt PDF has 1284 pages.

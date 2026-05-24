# 2026-05-24 Issue #286 Unitarity Shortening Theorem Pass

## Scope

- GitHub issue: #286, "[Vol V Ch 7] Unitarity bound saturation =
  conservation: not a labeled theorem".
- Manuscript target:
  `monograph/tex/volumes/volume_iii/chapter07_unitarity_bounds_and_short_multiplets.tex`.
- Dossier target:
  `planning/chapter_dossiers/volume_iii/chapter07_unitarity_bounds_short_multiplets.md`.

## Content Added

- Promoted the spinor bound from proposition to theorem:
  `thm:spinor-unitarity-bound`.
- Added Theorem `thm:basic-unitarity-bounds-short-multiplets`, collecting the
  basic positive-norm primary bounds in \(D\ge3\):
  scalar \(\Delta_\phi\ge(D-2)/2\), spinor
  \(\Delta_\psi\ge(D-1)/2\), and symmetric-traceless
  \(\Delta_{\mathcal O}\ge\ell+D-2\).
- Stated the equality conditions as null-descendant operator equations:
  \(\partial^2\phi=0\), \(\Gamma^\mu\partial_\mu\psi=0\), and
  \(\partial^{\mu_1}\mathcal O_{\mu_1\cdots\mu_\ell}=0\).
- The proof of the summary theorem points back to the explicit Gram-matrix
  derivations rather than replacing them with a citation or assertion.
- Updated the chapter dossier to preserve the labeled theorem and the
  connection between saturation and null quotient.

## Harness

- Passed: `git diff --check`
- Passed: `tools/audit_monograph_text.sh`
- Passed: `tools/audit_chapter_dossiers.sh`
- Passed: `tools/build_monograph.sh`

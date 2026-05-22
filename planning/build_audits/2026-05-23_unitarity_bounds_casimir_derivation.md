# Unitarity Bounds Casimir Derivation Audit

Date: 2026-05-23

This pass strengthens the unitarity-bounds chapter by replacing the asserted
spin-\(\ell\) level-one eigenvalues with a Casimir computation and by stating
the radial Hilbert-space convention underlying descendant positivity.

## Manuscript Changes

- Updated
  `monograph/tex/volumes/volume_iii/chapter07_unitarity_bounds_and_short_multiplets.tex`.
- Added the finite-energy domain and null-quotient convention for descendant
  Gram matrices.
- Reworked the level-one spin decomposition for symmetric traceless tensors.
- Computed the \(\mathcal H_{\ell+1}\), \(\mathcal H_{\ell,1}\), and
  \(\mathcal H_{\ell-1}\) eigenvalues from \(SO(D)\) quadratic Casimirs.
- Added the general first-level unitarity test for irreducible \(SO(D)\)
  representations.

## Planning Updates

- Added a Volume III chapter dossier for unitarity bounds and short
  multiplets.
- Updated the master architecture and dependency map so the next CFT target is
  carrying primary transformations and positivity normalizations into the
  correlation-function chapter.

## Verification

- `git diff --check` passed.
- Strict phrase scan on the edited manuscript found no manuscript-policy hits.
- `tools/build_monograph.sh` passed; the strict text audit, LaTeX build, and
  log scan were clean after latexmk resolved the expected cross-reference
  rerun.
- Rendered and inspected PDF pages 489--492, corresponding to printed pages
  471--474.  The new Hilbert-space convention and Casimir derivation typeset
  cleanly.

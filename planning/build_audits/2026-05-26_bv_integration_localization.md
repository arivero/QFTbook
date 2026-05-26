# 2026-05-26 BV Integration And Localization Pass

## Scope

- Deepened
  `monograph/tex/volumes/volume_viii/chapter10_bv_integration_and_localization.tex`.
- Added
  `calculation-checks/bv_localization_checks.py`.
- Updated the calculation-check index and the Volume VIII Chapter 10 dossier.

## Mathematical Content Added

- Rebuilt the finite-dimensional BV datum using odd symplectic graded
  manifolds, Hamiltonian vector fields, the BV bracket, and semidensities.
- Stated the semidensity quantum master equation and derived its action form
  in a Berezinian trivialization.
- Proved the BV product identity used in quantum observable equations.
- Proved finite-dimensional BV Stokes in Darboux coordinates and derived
  gauge-fixing independence for Lagrangian-cycle deformations.
- Proved BV pushforward preservation of the quantum master equation under
  explicit boundary or decay hypotheses.
- Proved finite-dimensional \(Q\)-exact deformation invariance with the
  hypothesis \(\int_M Q\beta=0\) stated as part of the theorem.
- Added the one-loop normal form, including the
  \(\operatorname{Pf}(B)/\sqrt{\det A}\) normal factor and determinant-line
  orientation dependence.
- Added a rank-one Mathai--Quillen normalization model whose integral is the
  local degree \(\operatorname{sign}(a)\).
- Spelled out boundary, noncompact, reducible-connection, small-instanton, and
  residue-prescription obligations for future infinite-dimensional
  localization claims.

## Verification

- Passed: `python3 calculation-checks/bv_localization_checks.py`.
- Passed: `git diff --check`.
- Passed: `tools/audit_monograph_text.sh`.
- Passed: `tools/audit_chapter_dossiers.sh`.
- Passed: `tools/build_monograph.sh`.
- Confirmed: `monograph/tex/main.pdf` builds to 1362 pages by `pdfinfo`.

# 2026-05-24 Issue #342 Threshold Bound-State Pole Audit

## Issue

GitHub issue #342 flagged that the bound-state chapter did not sufficiently
separate the physical condition \(M_B<2m\) from the mathematical hypothesis
that the amplitude has an isolated simple pole.  It requested a remark on
near-threshold and unitary-limit physics.

## Edits

- Added `rem:near-threshold-bound-state-poles` to Volume II, Chapter 3.
- The remark states that \(M_B<2m\) is a location statement, while the
  factorization theorem assumes an isolated finite-multiplicity spectral point
  with nonzero channel overlap and a gap from thresholds and other
  singularities.
- Added the relative-momentum parametrization
  \(s=4(m_1^2+k^2)\), \(k=i\kappa\), and the effective-range denominator
  \(-a^{-1}+r_e k^2/2-ik+\cdots\).
- Explained that as \(a^{-1}\to0\) the pole reaches the threshold branch
  point, so no fixed \(s\)-plane simple-pole neighborhood remains.
- Identified threshold bound states, virtual states, resonances, and Efimov
  accumulation as regimes requiring separate threshold analysis.
- Updated the chapter dossier with the same logical boundary.
- Added a follow-up framework paragraph to the AQFT chapter: no axiomatic
  framework is treated as sacred; frameworks are valued by the physical and
  mathematical insight they provide and by their performance on examples.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 751 pages.

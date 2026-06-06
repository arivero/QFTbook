# 2026-06-06 Issue 597 Source Cumulant Fluctuation Audit

## Scope

- Added `ca:instanton-first-source-cumulant-normal-modes` to Volume II
  Chapter 20D inside the normal-fluctuation source-data section.
- Extended `calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  with an exact finite Wick-pairing check for the first source cumulant.
- Updated the Chapter 20D dossier and calculation-check inventory.

## Depth Audit

- This pass targets the physical fluctuation response around the instanton,
  not moduli-space geometry.
- The new block computes the first source-dependent cumulant in normal
  coordinates: a linear source deformation has zero Gaussian mean but becomes
  nonzero through covariance with the cubic fluctuation action.
- This is one of the places where an instanton amplitude calculation is
  genuinely harder than a measure calculation: the source insertion and the
  fluctuation action must be expanded in the same zero-mode-deleted Gaussian
  coordinates.

## Scope Guard

- No planning directives, review commentary, or GitHub metadata were inserted
  into the monograph TeX.
- The finite Wick model is a companion for the local cumulant mechanism.  It
  does not compute the continuum determinant constant, prove the full
  Lorentzian amplitude, replace endpoint/IR control, or complete the
  instanton-pair/valley problem.

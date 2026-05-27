# Issue #494 Extrapolation Protocol Checkpoint

## Scope

This checkpoint strengthens the numerical-methods issue by adding theorem-level
finite-regulator extrapolation material to Volume XI, Chapter 10.

## Manuscript Changes

- Replaced the informal Rayleigh--Ritz discussion with a labeled proposition
  and proof at fixed self-adjoint Hamiltonian, including the form-norm
  eigenvector approximation hypothesis and the caveat that cutoff-dependent
  counterterms require separate estimates.
- Added the finite-regulator observable datum, separating finite objects,
  observables, statistical errors, and systematic cutoff errors.
- Proved that finitely many cutoff outputs do not determine a continuum value:
  for any proposed value, Lagrange interpolation constructs a compatible
  cutoff curve through the same finite data.
- Defined power-law cutoff expansions with explicit remainder bounds.
- Proved two-cutoff Richardson cancellation and integer-power multi-cutoff
  extrapolation with displayed constants.

## Companion Check

- Added `calculation-checks/numerical_extrapolation_checks.py`, using exact
  rational arithmetic to verify the interpolation obstruction, Richardson
  cancellation, and multi-cutoff extrapolation weights.

## Verification

- `python3 calculation-checks/numerical_extrapolation_checks.py`: passed.
- `python3 -m py_compile calculation-checks/numerical_extrapolation_checks.py`:
  passed.
- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed; final PDF at
  `monograph/tex/main.pdf` with 2083 pages.

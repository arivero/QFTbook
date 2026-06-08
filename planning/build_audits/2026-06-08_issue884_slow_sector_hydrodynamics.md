# Issue #884 Slow-Sector Hydrodynamics Audit

## Scope

- Volume X, Chapter 5 hydrodynamics from Ward identities.
- Volume X, Chapter 6 Schwinger-Keldysh hydrodynamic effective actions.
- `calculation-checks/hydrodynamic_modes_checks.py` and calculation-check
  inventory.
- Chapter dossiers for the touched chapters.

## Physics Repair

- Replaced the conserved-density-only foundation with a complete retained
  slow-sector criterion:
  `S_slow={O_a: gamma_a(lambda)->0 in the declared scaling limit}`.
- Scoped the existing deterministic Ward-identity derivation to an ordinary
  normal fluid with retained sector `{T00,T0i,J0_A}`.
- Added a complement-regularity controlled approximation: after projecting
  onto the retained slow sector, omitted retarded or memory kernels must
  remain uniformly expandable in the hydrodynamic window.
- Added compact extension data for superfluid phases, dynamic-critical order
  parameters, weakly relaxed charges, kinetic moments, and elastic/
  orientational/higher-form media.
- Replaced the microscopic theorem boundary with slow-sector completeness plus
  complement regularity.
- Updated the SK chapter so every retained slow field requires its own doubled
  variables, source normalization, symmetry/frame data, response/noise kernel,
  dynamical KMS transformation, and positivity constraints.

## Regression Guard

`hydrodynamic_modes_checks.py` now verifies that integrating out a sample
relaxational order parameter produces

`-lambda^2/(Gamma_phi+kappa_phi k^2-i omega)`.

It checks that fixed `Gamma_phi` gives finite analytic coefficients, while
`Gamma_phi`, `k^2`, and `omega` scaling together makes the memory term scale
as an inverse hydrodynamic denominator.  The same check records the
quasihydrodynamic weak-relaxation pole scaling.

## Re-Audit Notes

- The pass is an argument-architecture repair rather than a lemma-density
  increase.
- The added mathematics is only the finite memory-denominator algebra needed
  to expose the physical failure of integrating out an omitted slow channel.
- Directives and process notes remain in planning files, not monograph TeX.

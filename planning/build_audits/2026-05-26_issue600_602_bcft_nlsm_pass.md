# Issues #600 and #602 BCFT/NLSM Development Pass

Date: 2026-05-26.

## Scope

- GitHub issues: #600 (`[Block Q]` NLSM perturbative renormalization) and
  #602 (`[Block S]` 2D BCFT).
- Lane: `02_2d_cft_liouville_bcft_nlsm`.
- Files edited:
  - `monograph/tex/volumes/volume_v/volume_v_current.tex`
  - `monograph/tex/volumes/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.tex`
  - `monograph/tex/volumes/volume_v/chapter14_boundary_conformal_field_theory.tex`
  - `planning/chapter_dossiers/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.md`
  - `planning/chapter_dossiers/volume_v/chapter14_boundary_conformal_field_theory.md`
  - `calculation-checks/bcft_cardy_checks.py`
  - `calculation-checks/nlsm_buscher_checks.py`

## BCFT Content Added

- Added a dedicated compiled Volume V BCFT chapter.
- Defined BCFT data on bordered surfaces: boundary conditions, interval
  Hilbert spaces, boundary operators, bulk-to-boundary OPE maps, and sewing.
- Proved the preserved Virasoro algebra from the stress-tensor gluing
  condition.
- Defined boundary states and Ishibashi states; proved Ishibashi gluing.
- Derived Cardy's diagonal-rational annulus solution from the Verlinde
  formula.
- Worked out compact free-boson Neumann/Dirichlet oscillator and zero-mode
  boundary states, including T-duality exchange.
- Worked out Majorana/Ising boundary states, NS/R bookkeeping, and fixed/free
  annulus spectra.
- Stated Cardy-Lewellen sewing and the boundary `g`-theorem as theorem
  boundaries, plus a nonrational BCFT sewing open problem.

## NLSM Content Added

- Added a local-scheme definition for perturbative sigma-model
  renormalization as geometry on the coupling space `(G,B,Phi)`.
- Proved how hatted Weyl-anomaly coefficients differ from coordinate beta
  functions by target diffeomorphism and `B`-field gauge redundant
  directions.
- Recorded the pure-metric two-loop beta representative as a controlled
  large-radius/minimal-subtraction approximation.
- Added the flat linear-dilaton central-charge condition and distinguished it
  from nonconstant tensor beta functions.
- Derived Buscher rules by gauging a circle isometry and integrating out the
  gauge fields.
- Proved Buscher involutivity and stated beta-function covariance as an
  order-by-order perturbative statement.

## Calculation Checks

- Added `calculation-checks/bcft_cardy_checks.py` for Ising modular/Cardy
  annulus arithmetic, boundary entropy squares, and compact-boson boundary
  zero-mode T-duality.
- Added `calculation-checks/nlsm_buscher_checks.py` for Buscher algebra,
  component `G,B` rules, dilaton involutivity, and constant-curvature
  specialization of the two-loop coefficient.

## Remaining Obligations

- #602 remains open: needs explicit Cardy-Lewellen coefficient equations in a
  nontrivial rational model beyond annulus and boundary-condition-changing
  three-point constants.
- #600 remains open: needs fuller derivation of the one-loop `B` and dilaton
  beta functions, torsionful two-loop tensors, heterotic `(0,1)` gauge
  beta-functions, and supersymmetric higher-loop theorem boundaries.

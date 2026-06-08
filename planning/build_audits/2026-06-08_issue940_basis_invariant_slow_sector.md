# Issue #940 Basis-Invariant Slow-Sector Audit

## Scope

- Volume X, Chapter 5 hydrodynamic scaling-family definition.
- Volume X, Chapter 5 slow-sector completeness controlled approximation.
- Volume X, Chapter 5 omitted-mode memory-kernel section.
- Volume X, Chapter 6 SK hydrodynamic slow-field consistency language.
- `calculation-checks/hydrodynamic_modes_checks.py` and calculation-check
  inventory/evidence contracts.
- Chapter dossiers for Volume X Chapters 5 and 6.

## Physics Repair

- Replaced the named-operator/scalar-rate slow-sector definition with a
  quotient source/operator space and a basis-invariant retained spectral
  subspace.
- Declared the susceptibility or Kubo-Mori pairing and separated the
  relaxation/Liouvillian/memory generator whose spectral subspace is retained
  from the inverse-response or memory operator actually inverted in the
  Schur-complement test.
- Gave `P_slow` a Riesz-projector construction when the slow spectrum is
  isolated, and stated the thermodynamic-continuum replacement as a shrinking
  spectral window with a uniform resolvent criterion.
- Formulated complement regularity for the operator actually inverted when
  modes are integrated out, via the Schur complement
  `A_ss - A_sf A_ff^{-1} A_fs`.
- Stated explicitly that diagonal response or relaxation entries are not
  basis-invariant relaxation rates.
- Extended the omitted-mode discussion from a scalar pole to mixed
  multi-field Schur complements and kinetic/critical continuum lower edges.
- Synchronized the SK chapter language so additional slow data are coordinates
  on retained spectral subspaces rather than invariant operator-name members.

## Regression Guard

`hydrodynamic_modes_checks.py` now adds two issue #940 guards.

- A non-normal two-by-two relaxation operator is subjected to a nonsingular
  basis change.  Its diagonal entries change, while trace/determinant remain
  invariant and the slow Riesz projector transforms covariantly and remains
  idempotent.
- A continuum memory integral over relaxation rates `a in [a0,1]` is checked.
  Fixed `a0` gives finite analytic coefficients, while `a0` scaling to zero
  produces growing branch-cut memory rather than a finite-pole correction.

## Re-Audit Notes

- This is a sharpened architecture repair for #884, not a reversal of it.
- The added mathematics serves the physics question: which degrees of freedom
  must be retained before local hydrodynamics or SK hydrodynamics is a
  controlled long-wavelength theory.
- Process notes remain in planning files, not in monograph TeX.

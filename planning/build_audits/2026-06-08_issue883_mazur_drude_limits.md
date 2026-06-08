# Issue #883 Mazur/Drude Limit Audit

## Scope

- Volume X, Chapter 4 spectral functions, Kubo formulae, and transport.
- `calculation-checks/thermal_kubo_checks.py` and calculation-check inventory.
- Chapter 4 dossier and bibliography guide.

## Physics Repair

- Kept the finite-volume Mazur lemma at the level it proves: a Cesaro
  projection onto the zero-Liouvillian subspace.
- Removed the ordinary pointwise `t -> infinity` Drude definition from the
  finite-volume proof.
- Defined the Drude matrix as the coefficient of the zero-frequency atom in
  the thermodynamic conductivity measure.
- Added the spectral-convergence hypothesis needed to turn the finite-volume
  Mazur projection into a thermodynamic Drude lower bound.
- Added a proposition separating Cesaro, Abel, and pointwise time-domain
  limits.  Cesaro and Abel identify the zero atom for a finite thermodynamic
  spectral measure with no additional atom at zero; the pointwise limit
  requires an extra dephasing or mixing hypothesis.
- Distinguished a genuine Drude atom from singular-continuous response and
  from absolutely continuous low-frequency tails without a finite dc limit.

## Regression Guard

`thermal_kubo_checks.py` now includes the finite negative control

`C(t)=C0+cos(Omega t)`.

The check verifies that complete-period Cesaro averages and the Abel
regularization isolate `C0`, while two late-time subsequences remain separated
by order one.  This prevents the chapter from silently replacing the
finite-volume Mazur time average by an ordinary pointwise long-time limit.

## Re-Audit Notes

- The change is an order-of-limits and transport-architecture repair.
- The added finite algebra is only the minimal negative control needed to make
  the physics distinction executable.
- Process notes remain in planning files, not in monograph TeX.

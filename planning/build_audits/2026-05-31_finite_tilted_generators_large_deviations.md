# Finite Tilted-Generator Large-Deviation Pass

Date: 2026-05-31

Scope:
- Volume X, Chapter 10.
- GitHub issue context: #703, statmech-to-QFT absorption and finite-regulator
  nonequilibrium foundations.

Edits:
- Added the section `Tilted Generators and Dynamical Large Deviations`.
- Defined finite additive jump observables with separate state and jump
  weights.
- Derived the finite Feynman--Kac tilted backward generator by conditioning
  on the first short time interval.
- Identified the Perron--Frobenius spectral input for finite irreducible
  chains while explicitly separating it from the additional hypotheses needed
  for a full path large-deviation principle.
- Derived the stationary entropy-production tilted-generator similarity
  identity giving the finite Gallavotti--Cohen spectral symmetry.
- Updated the chapter dossier and public calculation-check inventory.

Quality Notes:
- The new proposition is finite-dimensional and exact; it is not a continuum
  stochastic-field theorem.
- No large-deviation principle is claimed without the separate analytic and
  tightness hypotheses that such a theorem requires.
- The entropy-production symmetry is presented as a matrix identity, so the
  proof burden is the explicit off-diagonal and diagonal entry check.

Checks:
- `calculation-checks/nonequilibrium_open_system_checks.py` now verifies the
  finite tilted Feynman--Kac generator and a three-state stationary
  Gallavotti--Cohen similarity identity.

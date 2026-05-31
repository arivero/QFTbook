# Finite Empirical-Flow Level-2.5 Pass

Date: 2026-05-31

Scope:
- Volume X, Chapter 10.
- GitHub issue context: #703, statmech-to-QFT absorption for
  nonequilibrium field theory and dynamical large deviations.

Edits:
- Added the section `Empirical Measures, Flows, and the Level-2.5 Cost`.
- Defined finite empirical occupations and empirical jump flows.
- Derived the finite boundary conservation law for empirical flows.
- Defined the level-2.5 relative-entropy cost with support and conservation
  constraints.
- Derived the cost from the Radon--Nikodym density between the original
  jump process and the auxiliary process whose rates are
  `R_ij = q_ij / rho_i`.
- Added the level-2 contraction and the explicit two-state occupation cost.
- Connected the level-2.5 variational formula back to the tilted-generator
  Perron eigenvalue.
- Updated the chapter dossier and calculation-check inventory.

Quality Notes:
- The construction is finite-dimensional and regulator-level.
- The text explicitly separates the finite empirical-pair construction from
  any continuum QFT hydrodynamic large-deviation claim.
- The proof uses the finite path-density Radon--Nikodym identity and finite
  covering argument rather than informal "typical trajectory" language.

Checks:
- `calculation-checks/nonequilibrium_open_system_checks.py` now verifies the
  empirical-flow conservation condition, the Radon--Nikodym sign of the
  level-2.5 cost, the zero cost of the typical flow, and the two-state
  level-2 contraction formula.

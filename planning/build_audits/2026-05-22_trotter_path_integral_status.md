# Trotter Path-Integral Status Pass

Date: 2026-05-22.

Development pass:

- Added a Trotter-limit section to the Hamiltonian time-sliced path-integral
  chapter.
- Distinguished finite-dimensional time-sliced integrals from strong operator
  limits, smeared distributional kernel limits, Euclidean semigroup
  constructions, and perturbative asymptotic expansions.
- Stated the operator-level status of Lorentzian and Euclidean product
  formulas before using continuum path-integral notation.

Verification:

- `tools/audit_monograph_text.sh`
- deferred-topic scan for AdS/CFT, supersymmetry, bootstrap, large \(N\),
  localization, and defect material in active volumes
- hard-coded chapter-number scan
- active-volume orphan chapter scan
- `tools/build_monograph.sh`

Result:

- All checks passed.
- The compiled manuscript is `/Users/xiyin/QFT/monograph/tex/main.pdf`.

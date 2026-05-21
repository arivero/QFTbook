# Landau Coleman-Norton Audit

Date: 2026-05-21.

Development pass:

- Added a spacetime interpretation of positive Landau solutions in the
  analytic-scattering chapter.
- Stated the Coleman--Norton criterion in terms of active internal lines,
  vertex positions, nonnegative propagation parameters, and on-shell momenta.
- Clarified that first-sheet physical singularities require the algebraic
  Landau solution, sheet selection, contour trapping, and nonzero local
  singular contribution.
- Replaced an unsupported numerical triangle criterion with the general
  positive-parameter first-sheet condition.

Verification:

- `tools/audit_monograph_text.sh`
- deferred-topic scan for AdS/CFT, supersymmetry, bootstrap, large \(N\),
  localization, and defect material in active volumes
- hard-coded chapter-number scan
- `tools/build_monograph.sh`

Result:

- All checks passed.
- The compiled manuscript is
  `/Users/xiyin/QFT/monograph/tex/main.pdf`.

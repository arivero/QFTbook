# Issue #314 Pauli--Villars Status Audit

## Issue

GitHub issue #314 reported that Pauli--Villars appeared in planning as an
available regulator class but had no path-integral status statement in the
monograph.

## Resolution

- Added a Pauli--Villars row to
  `tab:regulator-integration-status-catalog`.
- The row classifies Pauli--Villars as an auxiliary-field or
  determinant-ratio prescription, not as a measure on the original field
  space.
- The row requires the statistics, coefficients, masses, symmetry action,
  enlarged field variables, density or integration cycle, and sign or
  indefinite-metric structure whenever it is written as a path integral.
- The catalog now states that the monograph does not use Pauli--Villars as a
  default path-integral construction.
- The chiral-anomaly chapter now states explicitly that its Berezinian
  calculation uses a heat-kernel/spectral regulator of an operator trace, not
  a Pauli--Villars auxiliary-field or determinant-ratio regulator.

## Verification

- Working-tree verification before commit:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`

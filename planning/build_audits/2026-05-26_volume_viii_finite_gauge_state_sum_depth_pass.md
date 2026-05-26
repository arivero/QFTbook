# 2026-05-26 Volume VIII Chapter 11 Finite-Gauge State-Sum Depth Pass

Status: completed and pushed after verification.

## Scope

- Rewrote the finite gauge theory chapter from a brief outline into a
  theorem-led construction of finite topological gauge theory.
- Added finite groupoid cardinality, finite groupoid integration, and a proof
  of the action-groupoid cardinality formula.
- Proved the connected-manifold formula
  \(Z_G(M)=|\operatorname{Hom}(\pi_1(M),G)|/|G|\).
- Developed boundary state spaces and bordism maps as push-pull along spans
  of finite groupoids.
- Proved finite groupoid gluing through descent for principal bundles and
  Fubini over finite homotopy fibers.
- Added the triangulated flat-connection state sum and its equality with
  groupoid cardinality.
- Developed Dijkgraaf-Witten cocycle twists, including the simplex weight,
  Pachner-move proof from \(\delta\omega=1\), transgressed boundary line, and
  twisted state spaces.
- Added explicit closed-surface partition functions and the character formula
  \(Z_G(\Sigma_g)=|G|^{2g-2}\sum_R d_R^{2-2g}\), with the Schur-averaging
  derivation.
- Added the circle class-function state space, convolution pair-of-pants
  algebra, \(T^3\) commuting-triple formula, Drinfeld-center line-operator
  description, finite correspondence defects, and finite anomaly inflow.

## Calculation Check

- Added `calculation-checks/finite_gauge_state_sum_checks.py`.
- The script verifies action-groupoid cardinality, connected hom-count
  formulas, surface character formulas for cyclic groups and \(S_3\),
  class-function convolution, the standard \(\mathbb Z_n\)
  Dijkgraaf-Witten \(3\)-cocycle condition, spanning-tree gauge-fixing
  counts, and torus commuting-pair counts.

## Verification

- `python3 calculation-checks/finite_gauge_state_sum_checks.py` passed.
- `python3 -m py_compile calculation-checks/finite_gauge_state_sum_checks.py`
  passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed with clean log scan.
- `pdfinfo monograph/tex/main.pdf` reports 1800 pages.

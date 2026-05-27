# 2026-05-27 Lattice Gradient Flow Audit

## Scope

- Added a Wilson/gradient-flow section to Volume XI Chapter 5.
- Formulated the flow as a finite-dimensional negative-gradient ODE on the
  compact link manifold \(G^E\).
- Proved global existence, gauge covariance, and action monotonicity at finite
  cutoff.
- Added the continuum linearized heat-kernel smoothing argument, flowed
  energy-density scale coordinates \(t_0,w_0\), and the Chern--Weil proof that
  smooth flow preserves fixed-bundle topological charge.
- Separated admissible/geometric or index-theoretic topological-charge
  definitions from numerical flow plateaux.
- Added `calculation-checks/lattice_gradient_flow_checks.py`.

## Checks

- `python3 calculation-checks/lattice_gradient_flow_checks.py`: passed.
- `python3 -m py_compile calculation-checks/lattice_gradient_flow_checks.py`:
  passed.
- `git diff --check` on the touched files: passed.
- `tools/build_monograph.sh`: passed with clean strict text audit and clean
  final log scan after one overfull paragraph was tightened.
- `pdfinfo monograph/tex/main.pdf`: 2169 pages, created
  2026-05-27 11:20 EDT.

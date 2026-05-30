# 2026-05-30 Anomaly-Line Groupoid Descent Pass

Scope:
- Continued #696 and #691 in Volume XII, Chapter 7.
- Focused on the QFT descent criterion extracted from determinant/Pfaffian
  line holonomy, not on proving the external APS/Bismut--Freed/mod-two-index
  global-analysis theorems.

Edits:
- Added a quotient-background groupoid paragraph after finite gauge
  transformations as determinant-line transport.
- Made the anomaly line a groupoid line bundle: objects carry lines `L_A`,
  morphisms carry isomorphisms `Phi_g(A):L_A -> L_{A^g}`, and a quotient
  partition function requires an equivariant trivialization.
- Wrote the local-trivialization cocycle `alpha(A,g)`, its groupoid cocycle
  law, its coboundary shift under `e_A -> beta(A)e_A`, and the invariance of
  based-loop holonomy.
- Stated explicitly that tensoring independent fermion systems tensors
  anomaly lines, multiplying cocycles and adding logarithmic exponents.
- Extended `calculation-checks/eta_global_anomaly_checks.py` with exact finite
  action-groupoid cocycle/coboundary checks, based-loop holonomy invariance,
  tensor-product exponent addition, and stabilizer-character descent tests.

Checks run:
- `python3 calculation-checks/eta_global_anomaly_checks.py`
- `python3 -m py_compile calculation-checks/eta_global_anomaly_checks.py`

Status:
- #696 remains open.  This pass makes the determinant/Pfaffian-line descent
  criterion explicit; the APS, Bismut--Freed, and mod-two-index global-analysis
  infrastructure remains an external theorem-boundary cluster.
- #691 remains open for continued semantic proof-substance and anti-wrapper
  audit.

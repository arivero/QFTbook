# 2026-05-26 Symmetric-Product Primitive Joining Schwarzian Pass

## Scope

Issue #606 / 2D CFT stringbook-depth follow-up.  This pass connects the
primitive joining cover in Volume V, Chapter 11 to the stress-tensor
Schwarzian ledger and to the universal OPE power fixed by conformal
covariance.

## Substantive Edits

- Added a proposition deriving the local inverse-branch Schwarzian
  double-pole coefficient for a ramification point of index \(r\).
- Specialized the result to primitive symmetric-product joining branch data
  \(K,L,N=K+L-1\), deriving the OPE power \(h_N-h_K-h_L\).
- Stated explicitly that the monodromy, Riemann--Hurwitz, Schwarzian, and
  global-conformal ledgers fix the power but not the numerical OPE
  coefficient, which still depends on the seed correlator, local coordinate
  anomaly functional, and twist normalization.
- Extended `calculation-checks/symmetric_product_orbifold_checks.py` with
  exact rational checks for Schwarzian double-pole weights and primitive
  joining OPE powers.
- Updated the calculation-check inventory, Chapter 11 dossier, and stringbook
  crosswalk.

## Verification

Final verification for this pass:

- `python3 calculation-checks/symmetric_product_orbifold_checks.py`
- `python3 -m py_compile calculation-checks/symmetric_product_orbifold_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The post-rebase TeX build completed cleanly at 1804 pages.

# 2026-05-26 Symmetric-Product Twist Cover Ledger Pass

## Scope

Issue #606 / 2D CFT stringbook-depth follow-up.  This pass starts the
covering-space twist-correlator obligation in Volume V, Chapter 11 by adding
the finite monodromy and Riemann--Hurwitz genus ledger that must precede any
numerical covering-space OPE-coefficient calculation.

## Substantive Edits

- Added a Riemann--Hurwitz proposition for connected genus-zero
  symmetric-product twist correlators in
  `monograph/tex/volumes/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.tex`.
- Stated the required monodromy product, transitivity, and nonnegative
  integer genus tests for active branch-cycle data.
- Derived the local ramification contribution `N - c(gamma)` from cycle
  decomposition, including fixed points on active sheets.
- Added two explicit genus-zero examples: the length-\(K\) two-point cover and
  the primitive three-point joining cover with overlapping cycles.
- Extended `calculation-checks/symmetric_product_orbifold_checks.py` with
  exact permutation, transitivity, product-identity, cycle-count, and
  Riemann--Hurwitz checks.
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

The post-rebase TeX build completed cleanly at 1791 pages.

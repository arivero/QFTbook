# 2026-05-26 Symmetric-Product Hecke Cover Count Pass

## Scope

Issue #606 / 2D CFT stringbook-depth follow-up.  This pass strengthens the
symmetric-product orbifold discussion in Volume V, Chapter 11 by making the
finite covering-count normalization behind the Hecke transform explicit.

## Substantive Edits

- Added a connected-torus-cover lemma to
  `monograph/tex/volumes/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.tex`.
- Derived the Hermite-normal-form classification of degree-\(m\) connected
  unbranched covers of a torus, with modulus \((a\tau+b)/d\) and
  count \(\sigma_1(m)\).
- Explained the deck-automorphism factor \(1/m\) in the nonholomorphic Hecke
  transform from the finite gauge-volume normalization.
- Added the constant-seed consistency test
  \(\exp(\sum_m p^m\sigma_1(m)/m)=\prod_{r\ge1}(1-p^r)^{-1}\), whose
  coefficients count cycle types of \(S_N\).
- Extended `calculation-checks/symmetric_product_orbifold_checks.py` and
  updated the calculation-check inventory, Chapter 11 dossier, and stringbook
  crosswalk.

## Verification

Final verification for this pass:

- `python3 calculation-checks/symmetric_product_orbifold_checks.py`
- `python3 -m py_compile calculation-checks/symmetric_product_orbifold_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh` (clean after rebasing onto `origin/main`, 1784 pages)

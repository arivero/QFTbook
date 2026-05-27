# 2026-05-26 Symmetric-Product Class Joining Normalization Pass

## Scope

Issue #606 / 2D CFT stringbook-depth follow-up.  This pass adds the finite
group-theoretic normalization layer that turns labelled primitive twist
joining OPEs into conjugacy-class symmetric-product operators.

## Substantive Edits

- Added a proposition defining normalized single-cycle class operators
  \(\Sigma_r^{(M)}\) from labelled twists with diagonal two-point functions.
- Derived the class size \(|[r]|=M!/(r(M-r)!)\) and the unit two-point
  normalization of the class sum.
- Counted primitive factorizations of a fixed \(R=K+L-1\) cycle into a
  \(K\)-cycle and an \(L\)-cycle, obtaining exactly \(R\) labelled
  factorizations.
- Derived the class-normalized primitive joining group factor
  \[
    (\mathfrak g_{K,L}^{(M)})^2
    =
    KLR\,\frac{(M-K)!(M-L)!}{M!(M-R)!}.
  \]
- Extended `calculation-checks/symmetric_product_orbifold_checks.py` with
  finite class-size, factorization-count, and group-factor checks.
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

The post-rebase TeX build completed cleanly at 1813 pages.

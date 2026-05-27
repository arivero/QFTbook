# 2026-05-26 Symmetric-Product Primitive Joining Cover Pass

## Scope

Issue #606 / 2D CFT stringbook-depth follow-up.  This pass deepens the
covering-space twist-correlator development in Volume V, Chapter 11 beyond
the finite Riemann--Hurwitz ledger by adding the first explicit local
coordinate cover used for a primitive joining correlator.

## Substantive Edits

- Added a proposition giving the beta-normalized polynomial cover
  \(z_{K,L}(t)=B_{K,L}^{-1}\int_0^t u^{K-1}(u-1)^{L-1}\,du\) for the
  primitive joining branch data \(K,L,K+L-1\).
- Proved the normalization \(z(0)=0\), \(z(1)=1\), the derivative
  factorization, and the absence of extra branch points.
- Derived the local coefficients at \(0\), \(1\), and \(\infty\), separating
  these Jacobian data from the still-unfixed seed-correlator and
  twist-normalization inputs needed for a numerical OPE coefficient.
- Extended `calculation-checks/symmetric_product_orbifold_checks.py` with
  exact polynomial, derivative, endpoint, and local-coefficient checks.
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

The post-rebase TeX build completed cleanly at 1796 pages.

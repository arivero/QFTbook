# 2026-05-26 Symmetric-Product Transposition Join/Split Pass

## Scope

Issue #606 / 2D CFT stringbook-depth follow-up.  This pass expands the
symmetric-product twist-field algebra in Volume V, Chapter 11 from primitive
single-cycle joining to the normalized transposition perturbation's finite
join and split channels.

## Substantive Edits

- Added a proposition deriving the class-normalized factor for joining a
  fixed point to a \(K\)-cycle by a transposition.
- Added the corresponding split-channel derivation for a \(K\)-cycle
  splitting into two nontrivial cycles of lengths \(a\) and \(b\), including
  the equal-length orbit symmetry factor.
- Treated the endpoint split into a fixed point plus a \(b\)-cycle separately,
  because the fixed point can lie on any sheet outside the nontrivial output
  support.
- Extended `calculation-checks/symmetric_product_orbifold_checks.py` with
  exact finite \(S_M\) checks for the transposition join/split labelled
  factorization counts and class-normalized group factors.
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

The post-rebase TeX build completed cleanly at 1820 pages.

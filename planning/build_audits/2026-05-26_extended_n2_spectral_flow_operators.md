# 2026-05-26 Extended N=2 Spectral-Flow Operator Pass

## Scope

Issue #606 / 2D CFT stringbook-depth follow-up.  This pass expands the
stringbook Appendix J discussion of extended \(N=2\) spectral flow into a
self-contained CFT-volume derivation.

## Substantive Edits

- Added a new section
  `Extended N=2 Spectral-Flow Operators` to
  `monograph/tex/volumes/volume_v/chapter15_two_dimensional_superconformal_algebras.tex`.
- Separated the abstract \(N=2\) spectral-flow automorphism from the stronger
  assertion that spectral flow is implemented by a chiral operator in a
  given CFT.
- Stated the needed \(U(1)_R\) Heisenberg/lattice hypothesis, bosonized
  \(J=i\sqrt{c/3}\,\partial\varphi\), and defined spectral-flow vertices
  \(X_\eta\) with their locality/spin-sector monodromy condition.
- Derived the OPE of \(X_\eta\) with a charged field, recovering the
  spectral-flow shifts of \(h\) and \(q\) from the Heisenberg weight
  calculation.
- Derived the integer-flow generator weights and charges, the shortening of
  \(X^\pm\), the \(Y^\pm\) descendant weights and charges, and the first
  terms of the \(X_\eta X_{-\eta}\) OPE.
- Added a Calabi-Yau-type algebraic example for \(c=3n\), including the
  integer and half-integer spectral-flow field weights and charges without
  claiming a sigma-model construction.
- Extended `calculation-checks/superconformal_algebra_checks.py` and updated
  the calculation-check inventory, Chapter 15 dossier, and stringbook
  crosswalk.

## Verification

Final verification for this pass:

- `python3 calculation-checks/superconformal_algebra_checks.py`
- `python3 -m py_compile calculation-checks/superconformal_algebra_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh` (clean after rebasing onto `origin/main`, 1778 pages)

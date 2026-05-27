# 2026-05-26 Supersymmetric Rank-One Coset Pass

## Scope

Issue #606 / 2D CFT stringbook-depth follow-up.  This pass expands the
stringbook Appendix J material on the \(N=2\) \(SU(2)_k/U(1)\) and
\(SL(2,\mathbb R)_k/U(1)\) cosets into a self-contained CFT-volume
chiral-algebra interface.

## Substantive Edits

- Added
  `monograph/tex/volumes/volume_v/chapter15_two_dimensional_superconformal_algebras.tex`
  section `Supersymmetric Rank-One Coset Interfaces`.
- Stated the parent supersymmetric WZW hypotheses, decoupled Cartan
  `N=1` sector, compact and noncompact `N=2` generator conventions,
  central charges, primary weights, and `R`-charges.
- Derived compact minimal-coset chiral-primary values and matched them to
  the protected `A`-series Landau--Ginzburg algebraic data without claiming
  an RG-flow theorem.
- Added spectral-flowed compact and cigar formulas, compact
  simple-current/`Z_k` data, cigar continuous/discrete spectrum status
  boundary, momentum/winding bookkeeping, and the noncompact
  field-identification rule.
- Updated the Chapter 11 bosonic coset note to point to the Chapter 15
  exact supersymmetric coset interface while keeping GLSM/mirror dynamics
  assigned to Volume VII.
- Extended `calculation-checks/superconformal_algebra_checks.py` and its
  README entry, updated the Chapter 11 and Chapter 15 dossiers, and updated
  the stringbook crosswalk.

## Verification

Completed verification for this pass:

- `python3 calculation-checks/superconformal_algebra_checks.py`
- `python3 -m py_compile calculation-checks/superconformal_algebra_checks.py`
- `python3 calculation-checks/wzw_sugawara_coset_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh` (clean log scan, 1772 pages)

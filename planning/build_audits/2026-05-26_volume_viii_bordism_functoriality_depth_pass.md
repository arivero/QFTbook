# 2026-05-26 Volume VIII Chapter 2 Bordism-Functoriality Depth Pass

Status: completed and pushed after verification.

## Scope

- Rewrote the bordism-functoriality chapter from a mostly definitional
  overview into a precise target statement for ordinary and extended TQFT.
- Added the tangential-structure convention
  \(\theta_\xi:B_\xi\to BO(D)\), stabilized lower-stratum
  \(\xi\)-structures, collared bordisms, and collar gluing.
- Added an honest-vs-relative/anomalous TQFT distinction so anomaly lines are
  part of the functorial datum rather than an afterthought.
- Proved the finite-dimensional state-space duality proposition from the
  cap/cup zig-zag identities.
- Added a complete ordinary \(2D\) oriented TQFT theorem via commutative
  Frobenius algebras, including the inverse-pairing cylinder identity,
  Frobenius neck exchange, pair-of-pants gluing, and the semisimple genus
  formula.
- Added an extended Morita \(2\)-category example identifying the point
  value, interval bimodule, and circle Hochschild trace.
- Added a functorial extraction criterion for topological sectors of local
  QFTs.

## Calculation Check

- Added `calculation-checks/tqft_frobenius_gluing_checks.py`.
- The check verifies, with exact rational arithmetic, the semisimple
  Frobenius cylinder identity, neck-exchange relation,
  associativity/commutativity, and
  \(Z(\Sigma_g)=\sum_\alpha\lambda_\alpha^{1-g}\).

## Verification

- `python3 calculation-checks/tqft_frobenius_gluing_checks.py` passed.
- `python3 -m py_compile calculation-checks/tqft_frobenius_gluing_checks.py`
  passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed with clean log scan.
- `pdfinfo monograph/tex/main.pdf` reports 1793 pages.

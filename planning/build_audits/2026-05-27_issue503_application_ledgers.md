# 2026-05-27 Issue #503 Application-Ledger Pass

GitHub issue: #503, concerning Borel resummation, Lefschetz thimbles,
resurgence, and renormalons.

## Manuscript Changes

Volume II, Chapter 10 now contains an application-status layer after the
Borel--Leroy, thimble, and renormalon foundations.

- Definition `def:regulated-asymptotic-analysis-datum` specifies the minimum
  data required before Borel, transseries, or thimble language is used for a
  QFT observable: regulator, complex domain, coefficient extraction,
  Borel-plane analyticity/growth data, nonperturbative sector data, and the
  regulator-removal statement.
- Remark `rem:regulated-asymptotic-datum-status` states the scope of the
  regulated asymptotic datum: fixed-regulator Borel--Laplace reconstruction
  becomes a continuum QFT statement only after the regulator-removal limit has
  been established.
- Proposition `prop:zero-dimensional-quartic-positive-ray-borel-control`
  proves positive-ray Borel control for the stable zero-dimensional quartic
  integral from Euler's hypergeometric representation.
- Definition `def:instanton-sector-transseries-ledger` and Proposition
  `prop:instanton-ledger-algebra` record instanton-sector transseries
  bookkeeping: integer topological charge, theta periodicity, and conjugate
  sector pairing.  The surrounding remark explicitly separates this ledger
  from a derivation of instanton calculus.

## Calculation Checks

`calculation-checks/borel_laplace_checks.py` now additionally checks:

- rational samples of the positive-ray Euler-integrand bound used in the
  quartic Borel-control proof;
- integer winding and conjugate-pair arithmetic for the instanton-sector
  transseries ledger.

`calculation-checks/README.md` and the chapter dossier were updated.

## Verification

Completed before checkpoint:

- `python3 calculation-checks/borel_laplace_checks.py`
- `python3 -m py_compile calculation-checks/borel_laplace_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The first build surfaced two overfull boxes in the new text.  Both were fixed
before the final build.  The final build/log scan is clean and produces
`monograph/tex/main.pdf` with 2079 pages.

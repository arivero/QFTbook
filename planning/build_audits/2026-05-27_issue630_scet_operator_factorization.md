# 2026-05-27 Issue #630 SCET Operator Factorization

## Scope

- Upgraded Volume II, Chapter 19b around jet factorization and resummation.
- Replaced a scale-separation paragraph by an operator-level SCET
  datum for two-jet endpoint factorization.
- Defined the entries needed before \(H\), \(J\), and \(S\) have meaning:
  lightlike directions, mode coordinates, collinear Wilson-line building
  blocks, soft Wilson lines, matched currents, renormalized jet and soft
  matrix elements, zero-bin/overlap subtraction, rapidity-regulator data, and
  Glauber-sector status.
- Tied the SCET collinear building-block normalization to the monograph's
  coupling-absorbed Yang--Mills convention
  \(-\frac1{4g_{\rm YM}^2}\operatorname{tr}(F_{\mu\nu}F^{\mu\nu})\).
- Added a finite-regulator proof of the leading soft Wilson-line decoupling
  identity and stated explicitly what the identity does not prove.
- Strengthened the leading-power SCET factorization hypothesis by requiring a
  topology for any theorem-level power-remainder estimate.
- Added a finite calculation check for endpoint convolutions and the
  Wilson-line decoupling algebra.

## Checks

- `python3 calculation-checks/scet_factorization_checks.py`
- `python3 -m py_compile calculation-checks/scet_factorization_checks.py`
- `git diff --check -- ...` on the changed manuscript, calculation-check,
  README, dossier, and audit files.
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`: 2153 pages, 8716324 bytes, PDF 1.5.

## Status

This pass addresses the SCET/factorization part of #630 at the level of an
operator datum and finite algebraic decoupling lemma.  It does not claim a
nonperturbative proof of endpoint factorization in four-dimensional QCD, nor a
proof of Glauber cancellation; those remain named theorem-level targets.

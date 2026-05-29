# 2026-05-26 Issue #503 Borel--Leroy and OPE Ambiguity Pass

GitHub issue: #503, concerning Borel resummation, Lefschetz thimbles,
resurgence, and renormalons.

## Manuscript Changes

Volume II, Chapter 10 now includes a second #503 development layer beyond the
earlier Gevrey, Watson-lemma, lateral-summation, transseries, conformal-map,
thimble, and renormalon-model material.

- Definition `def:borel-leroy-conformal-approximants` defines the
  Borel--Leroy transform, Borel--Leroy sum, conformal-Borel--Leroy truncation,
  and the data \((A,b,N)\) that must be declared in numerical use.
- The conformal-Borel--Leroy truncation calculation records that the input
  perturbative coefficients are preserved through the stated order.  This was
  later demoted from proposition form to prose in the anti-wrapper pass because
  the content is local-coordinate Taylor truncation plus the exact
  \(\Gamma(n+b+1)\) normalization of the Borel--Leroy Laplace kernel.
- Remark `rem:critical-exponent-borel-practice-status` records the rigorous
  status of Wilson--Fisher and fixed-dimension critical-exponent resummations:
  loop coefficients alone are not enough; the chart, Borel--Leroy parameter,
  singularity location, Borel-plane analyticity domain, and error procedure are
  part of the theorem or approximation.
- Remark `rem:ope-renormalon-ambiguity-cancellation` records the algebraic
  cancellation condition for a two-term OPE lateral ambiguity:
  \(\Delta C_0+Q^{-p}C_p\Delta M_p=0\).  It is intentionally not a
  theorem-family wrapper: the algebra is immediate, while a QFT application
  still has to construct the factorization scheme, the operator matrix element,
  and the lateral sums.

## Calculation Checks

`calculation-checks/borel_laplace_checks.py` now additionally checks:

- Borel--Leroy coefficient recovery for integer \(b\), verifying the exact
  \(\Gamma(n+b+1)\) normalization algebra.
- The two-term OPE ambiguity cancellation identity in rational arithmetic.

`calculation-checks/README.md` was updated accordingly.

## Verification

Completed before commit:

- `python3 calculation-checks/borel_laplace_checks.py`
- `python3 -m py_compile calculation-checks/borel_laplace_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full monograph build completed cleanly and produced
`monograph/tex/main.pdf` with 1764 pages.

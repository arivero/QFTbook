# 2026-05-25 Borel--Laplace and Lefschetz-Thimble Pass

GitHub issue: #503, concerning Borel resummation, resurgence, and
Lefschetz thimbles.

## Manuscript Change

Volume II, Chapter 10 now expands the former compressed Borel paragraph into
a theorem-level treatment of the foundational analytic machinery:

- Definition `def:gevrey-one-directional-borel-sum` introduces Gevrey-one
  formal series, the Borel transform, admissible directions, exponential
  growth bounds, and directional Borel--Laplace sums.
- Theorem `thm:watson-borel-laplace` proves that the directional
  Borel--Laplace integral is holomorphic in the corresponding sector and has
  the prescribed formal series as its asymptotic expansion.
- Example `ex:zero-dimensional-quartic-large-order` computes the
  zero-dimensional stable quartic integral, its exact perturbative
  coefficients, the large-order ratio, and the hypergeometric Borel transform
  with first finite singularity at \(\xi=-3/2\).
- Definition `def:lefschetz-thimble-data` gives the finite-dimensional
  holomorphic oscillatory-integral setup with \(h_\theta\), constant-phase
  flow, and upward/downward thimbles.
- Theorem `thm:finite-dimensional-thimble-decomposition` states and proves
  the relative-homology thimble decomposition, saddle expansion, and Stokes
  basis-jump statement under finite-dimensional Morse/properness hypotheses.
- Remark `rem:resurgence-regulated-statement` records the regulator-level
  status of using these ideas in QFT path integrals.

The pass also adds `calculation-checks/borel_laplace_checks.py`, which checks
the Gaussian moment formula, perturbative quartic coefficients, the
large-order ratio, Borel-radius normalization, and the hypergeometric
coefficient identity.

## Boundary

This pass does not close all of #503.  It supplies the rigorous
Borel--Laplace and finite-dimensional thimble infrastructure.  Further passes
should still develop lateral/median summation in more detail, transseries
bookkeeping, Borel--Pade and conformal-Borel numerical practice, and additional
applications to anharmonic oscillators, Wilson-Fisher resummation, gauge
theory, instantons, and string-theoretic examples.

## Verification

- `python3 calculation-checks/borel_laplace_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed with a clean final log scan.
- `pdfinfo monograph/tex/main.pdf` reports 1248 pages.

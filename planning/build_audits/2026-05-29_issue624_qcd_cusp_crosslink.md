# 2026-05-29 — Issue #624 QCD Cusp Cross-Link Pass

## Scope

Developed the QCD side of the cusp/large-spin cross-link requested in issue
#624 and in `claude_review.md` standing directive 11.

## Manuscript Changes

- Replaced the thin endpoint paragraph in Vol II ch19 by
  `Cusped Wilson Lines, Large Spin, and the DIS Endpoint`.
- Defined the regulated Euclidean cusped Wilson-line operator with
  smooth-line subtraction.
- Derived the one-loop angular integral
  \(J(\phi)=\phi\cot\phi\) and the corner-specific logarithm
  \(K_R^{(1)}=(g^2C_R/4\pi^2)(\phi\cot\phi-1)\).
- Continued to Lorentzian timelike angle and extracted the lightlike cusp
  coefficient \(\Gamma_{\rm cusp}^R=g^2C_R/(4\pi^2)+O(g^4)\).
- Connected the same coefficient to the \(D_0\) endpoint singularity and the
  large-spin nonsinglet Mellin evolution
  \(P_{{\rm ns},N}=-\Gamma_{\rm cusp}^q\log N+O(N^0)\), with explicit sign
  separation between matrix-element evolution and local-operator anomalous
  dimensions.
- Added a Vol VII ch13 cross-reference explaining that the BES planar N=4
  scaling function and the QCD cusp coefficient share an operator mechanism
  but have different logical statuses.

## Calculation Check

- Added `calculation-checks/qcd_cusp_large_spin_checks.py` to verify the
  cusp angular integral, smooth-line subtraction, Lorentzian lightlike limit,
  \(D_0\) Mellin harmonic identity, large-spin sign, and trace-normalization
  invariance of \(g^2C_R\).

## Issue Status

This pass addresses the QCD/DIS cross-link portion of #624.  The issue remains
open because the deeper planar N=4 items remain: higher BES expansions,
Bremsstrahlung, BMN/free-magnon opening, classical curve/finite-gap,
Pohlmeyer, Konishi wrapping, and TBA/QSC comparison.

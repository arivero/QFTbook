# Issue #582 Dual-Norm Chaos Checkpoint

## Manuscript Change

- Added Proposition `prop:spde-dual-norm-finite-chaos-estimate` to Volume XI,
  Chapter 9.
- The proposition defines the projective tensor norm on
  \(H^{\odot q}\widehat\otimes_\pi E'\), constructs \(E'\)-valued chaos
  integrals by completion from finite tensors, and proves an explicit
  \(L^{2m}\) bound for the Banach-dual norm.
- The proof uses only the scalar finite-chaos moment estimate, the triangle
  inequality in \(E'\), and Minkowski's inequality.
- The text applies the proposition with \(E=E_r\), the \(C^r\) test-function
  Banach space supported in the unit parabolic ball, so that
  \(Q_{n,\tau}^{#}\) is a dual norm rather than a finite-dimensional
  parameter supremum.

## Calculation Check

- Extended `calculation-checks/constructive_scalar_spde_checks.py` with exact
  arithmetic for the dual-norm finite-chaos constants.
- The check verifies the integer overestimate constant used for fourth
  moments and the exponent transfer
  \(2^{-((d+\epsilon)/p)\ell}\mapsto 2^{-(d+\epsilon)\ell}\) after taking the
  \(p\)-th moment.

## Remaining Issue #582 Obligations

- Prove the concrete projective tensor bounds for the BPHZ kernels of
  \(\Xi,X,X^2,X^3,XY,X^2Y\).
- Prove the scalar kernel bounds for the \(c_n\) reexpansion coordinate on
  \(K\times A_{\mathfrak s}\).
- Extend the strict negative-sector estimates to the positive solution sector
  used by the modelled-distribution fixed-point theorem.
- Complete the invariant-law and OS-reconstruction comparison.

# Issue #582 Gaussian Coordinate Estimates Checkpoint

## Manuscript Change

- Added Proposition `prop:spde-gaussian-wick-coordinate-scale-estimates` to
  Volume XI, Chapter 9.
- The proposition proves the scale estimates for the primitive Gaussian
  strict negative-sector coordinates:
  \[
    \Xi,\quad X,\quad X^2,\quad X^3 .
  \]
- For white noise, the proof derives
  \[
    \|\delta^{5/2+\kappa}\xi(\psi_z^\delta)\|_{L^{2m}}
    \lesssim \delta^\kappa .
  \]
- For the stochastic convolution, the proof assumes the covariance
  singularity
  \[
    |C(u,v)|\lesssim \|u-v\|_{\mathfrak s}^{-1}
  \]
  and derives, using Wick covariance and parabolic scaling,
  \[
    \|\delta^{k/2+k\kappa}\langle :X^k:,\psi_z^\delta\rangle\|_{L^{2m}}
    \lesssim \delta^{k\kappa},
    \qquad k=1,2,3 .
  \]
- Same-scale edge estimates are proved with a Holder factor
  \(\eta^\theta\).

## Calculation Check

- Extended `calculation-checks/constructive_scalar_spde_checks.py` with exact
  arithmetic for:
  - the white-noise coordinate slack \(\kappa\);
  - the Wick-coordinate slacks \(k\kappa\), \(k=1,2,3\);
  - local integrability condition \(k<5\);
  - a sample Holder edge factor.

## Remaining Issue #582 Obligations

- Promote these scalar Gaussian estimates to the full \(E_r'\)-valued
  dual-norm estimates using the wavelet/projective machinery where needed.
- Prove the genuinely nonlinear BPHZ coordinate estimates for \(XY\) and
  \(X^2Y\).
- Prove the scalar \(c_n\) reexpansion coordinate estimates.
- Extend from the strict negative sector to the solution sector and complete
  the invariant-law/OS comparison.

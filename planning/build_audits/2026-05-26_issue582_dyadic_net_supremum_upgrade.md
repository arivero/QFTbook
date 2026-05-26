# 2026-05-26 Issue #582 Dyadic-Net Supremum Upgrade

## Scope

- Volume XI, Chapter 9 now includes a dyadic-net theorem converting
  pointwise \(L^p\) coordinate estimates and dyadic edge increment estimates
  into a compact supremum estimate.
- The theorem is placed after the deterministic parabolic
  Taylor-subtraction gain, because BPHZ model convergence needs both the
  local scale gain and the passage from fixed coordinates to model seminorms.

## Mathematical Content

- The proof constructs the telescoping expansion along finite nets
  \(\pi_\ell x\to x\), uses sample-path continuity to identify the limit,
  bounds the base net and each edge level by finite \(L^p\) sums, and sums the
  geometric series with ratio \(2^{-\epsilon/p}\).
- The displayed constant is
  \(C_0^{1/p}B_0+C_1^{1/p}B/(1-2^{-\epsilon/p})\).
- If base and increment estimates carry a cutoff factor \(2^{-\rho n}\), the
  same factor multiplies the final compact-supremum bound.

## Calculation Check

- `calculation-checks/constructive_scalar_spde_checks.py` now checks the
  finite-net entropy cancellation \(2^{d\ell}2^{-(d+\epsilon)\ell}\), the
  geometric-series constant, and the cutoff-factor propagation in an exact
  rational sample.

## Remaining Issue #582 Obligations

- Prove the actual BPHZ random-model increment estimates for the parameter
  spaces entering the model seminorm, not only the abstract net upgrade once
  those estimates are available.
- Combine the kernel convolution bound, Taylor-subtraction gain,
  finite-chaos moment lemma, and dyadic-net upgrade into a complete
  finite-sector BPHZ model-convergence theorem for dynamic \(\Phi^4_3\).
- Extend the finite-sector theorem to the full sector needed by the
  invariant-law and OS-reconstruction comparison, with all local coordinates
  and regulator charts specified.

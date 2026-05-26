# 2026-05-26 Issue #582 Multiscale Sector Summability

## Scope

- Volume XI, Chapter 9 now includes a multiscale sector summability theorem
  for deterministic coordinate kernels.
- The theorem is placed after the dyadic convolution and Taylor-subtraction
  estimates, because those estimates are the ingredients that must produce
  the positive sector-gap exponents.

## Mathematical Content

- Sector gap variables \(r_1,\ldots,r_R\in\mathbb N\) carry positive
  deficits \(\eta_1,\ldots,\eta_R\).
- If each sector kernel satisfies
  \[
    \|f_{\mathbf r,a,q}\|\leq
    B_q\sigma(a)\prod_h 2^{-\eta_h r_h},
  \]
  then the cutoff kernel \(f_{n,a,q}\) has a uniform bound with geometric
  factor \(G=\prod_h(1-2^{-\eta_h})^{-1}\).
- The cutoff increment \(f_{n+1,a,q}-f_{n,a,q}\) is bounded by a shell union
  over maximal gap variables, with shell factor
  \[
    \widetilde G=\sum_h\prod_{k\neq h}(1-2^{-\eta_k})^{-1}.
  \]
- The theorem therefore supplies the deterministic kernel hypotheses needed
  by the finite-chaos moment corollary, with \(\rho=\min_h\eta_h\).

## Calculation Check

- `calculation-checks/constructive_scalar_spde_checks.py` now verifies the
  exact sample \(\eta=(1,2,3)\), including
  \(G=64/21\), \(\widetilde G=136/21\), the uniform kernel bound, the
  cutoff-increment bounds at \(n=4\), and the exact shell union inequality.

## Remaining Issue #582 Obligations

- Prove the BPHZ sector-gap bound for each negative dynamic \(\Phi^4_3\)
  tree and each coordinate entering \(\Pi\) and \(\Gamma\).
- Specify the sector decomposition and the map from tree scale assignments
  to non-negative gap variables.
- Combine those tree estimates with the sector theorem, the finite-chaos
  moment corollary, the dyadic-net theorem, and the coordinate-to-model
  theorem to obtain finite-sector BPHZ model convergence.

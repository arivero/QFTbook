# 2026-05-26 Issue #582 Negative Ledger And C1 Growth

## Scope

- Volume XI, Chapter 9 now identifies the first nonlinear dynamic
  \(\Phi^4_3\) drift monomials whose homogeneity is negative.
- The same section now derives the sharp spatial Fourier-cutoff form and
  linear ultraviolet growth of the one-loop local coordinate \(C_1\).

## Mathematical Content

- With \(X=\mathcal I(\Xi)\) and \(Y=\mathcal I(X^3)\), the homogeneities are
  \(|X|=-1/2-\kappa\) and \(|Y|=1/2-3\kappa\).
- For \(0<\kappa<1/14\), the negative cubic drift monomials in the first
  nonlinear expansion are exactly \(X^3\) and \(X^2Y\).  The monomials
  \(XY^2\) and \(Y^3\) have positive homogeneity.
- In the sharp spatial cutoff chart on \(\mathbb T^3\), the stationary
  Ornstein--Uhlenbeck variance gives
  \[
    C_1(M)=(2\pi)^{-3}\sum_{|n|_\infty\leq M}
    (|n|^2+m^2)^{-1}.
  \]
- The shell identity
  \[
    |\{n\in\mathbb Z^3:|n|_\infty=r\}|=(2r+1)^3-(2r-1)^3=24r^2+2
  \]
  proves both linear growth of \(C_1(M)\) and the dyadic increment bound
  \(C_1(2^{N+1})-C_1(2^N)=O(2^N)\).

## Calculation Check

- `calculation-checks/constructive_scalar_spde_checks.py` now verifies the
  four cubic homogeneities at \(\kappa=1/20\), the \(\kappa<1/14\)
  ledger boundary, the \(\mathbb Z^3\) shell-count identity, the single-shell
  upper and lower bounds, and an exact dyadic shell count for
  \(9\leq |n|_\infty\leq16\).

## Remaining Issue #582 Obligations

- Extend the drift-level ledger into the complete negative regularity-sector
  coordinate list for the BPHZ model.
- Prove the two-loop nested and non-nested sector decompositions with
  overlapping subtractions.
- Verify the \(\Pi\)- and \(\Gamma\)-coordinate estimates that convert the
  tree estimates into the random-model Cauchy theorem.

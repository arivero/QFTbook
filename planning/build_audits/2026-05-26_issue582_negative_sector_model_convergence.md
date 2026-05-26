# 2026-05-26 Issue #582 Negative-Sector Model Convergence

## Manuscript Change

- Volume XI, Chapter 9 now proves a negative-sector model convergence theorem
  for dynamic \(\Phi^4_3\) at
  `thm:spde-phi-four-three-negative-sector-model-convergence`.
- The theorem fixes the strict sector
  \[
    \mathcal T_-=\{\mathbf1,\Xi,X,X^2,X^3,XY,X^2Y\},
  \]
  names the six \(\Pi\)-coordinate functions and the single \(c_n\)
  reexpansion coordinate, and states scale-by-scale compact-parameter entropy
  hypotheses for each coordinate.
- The proof applies the scale-summed dyadic-net theorem coordinate by
  coordinate, inserts the finite negative-sector coordinate domination
  proposition, and then invokes the dyadic random-model Cauchy theorem.

## Constants Checked

- For each coordinate \(i\), the theorem defines
  \[
    S_i^{\rm sc}
    =
    \frac{C_{i,0}^{1/p}B_{i,0}
    +C_{i,1}^{1/p}B_i(1-2^{-\varepsilon_i/p})^{-1}}
    {1-2^{-(\sigma_i-D_i/p)}}
  \]
  and the analogous \(\widetilde S_i^{\rm sc}\).
- The resulting model constants are
  \[
    C_N=A_-^p\left(1+\sum_i S_i^{\rm sc}\right)^p,
    \qquad
    C_D=A_-^p\left(\sum_i\widetilde S_i^{\rm sc}\right)^p .
  \]
- `calculation-checks/constructive_scalar_spde_checks.py` now verifies the
  seven-coordinate arithmetic in an exact rational sample.

## Remaining Issue #582 Obligations

- Prove the concrete BPHZ kernel bounds for every \(\Pi\)-coordinate
  \(P_{n,\tau}\) and for the \(c_n\) reexpansion coordinate in the dynamic
  \(\Phi^4_3\) model.
- Identify the compact parameter spaces and entropy constants used by the
  concrete coordinate estimates rather than leaving them as hypotheses of the
  convergence criterion.
- Extend the finite negative-sector convergence to the full positive sector
  needed by the nonlinear fixed-point theorem.

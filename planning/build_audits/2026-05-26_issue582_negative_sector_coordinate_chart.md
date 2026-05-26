# 2026-05-26 Issue #582 Negative-Sector Coordinate Chart

## Scope

- Volume XI, Chapter 9 now constructs the finite strict negative-sector
  coordinate chart for dynamic \(\Phi^4_3\) at
  \(\gamma_-=\frac12-7\kappa\).
- This pass connects the abstract coordinate-to-model convergence theorem to
  concrete \(\Pi\)- and \(\Gamma\)-coordinates for the first dynamic
  \(\Phi^4_3\) BPHZ sector.

## Mathematical Content

- With \(X=\mathcal I(\Xi)\), \(Y=\mathcal I(X^3)\), and
  \(0<\kappa<1/14\), the strict sector \(T_{<\gamma_-}\) contains
  \[
    \mathbf1,\Xi,X,X^2,X^3,XY,X^2Y .
  \]
- The boundary monomial \(XY^2\) has homogeneity exactly
  \(\gamma_-=\frac12-7\kappa\), so it is excluded by the strict inequality.
- Since \(|Y|=\frac12-3\kappa\in(0,1)\), the reexpansion of \(Y\) below
  \(\gamma_-\) has only a constant lower component:
  \[
    \Gamma_{zz'}Y=Y+c(z,z')\mathbf1 .
  \]
- Multiplicativity gives the two nontrivial strict lower stochastic
  reexpansion coordinates:
  \[
    \Gamma_{zz'}(XY)=XY+c(z,z')X,\qquad
    \Gamma_{zz'}(X^2Y)=X^2Y+c(z,z')X^2 .
  \]
- The gap in both cases is \(|Y|\), so the normalized
  \(\Gamma\)-coordinate is
  \[
    |c(z,z')|/\|z-z'\|_{\mathfrak s}^{|Y|}.
  \]
- The proposition proves domination of the finite-sector model seminorm and
  model distance by six normalized \(\Pi\)-coordinates and this single
  \(\Gamma\)-coordinate.

## Calculation Check

- `calculation-checks/constructive_scalar_spde_checks.py` now verifies:
  - \(|Y|=7/20\) and \(\gamma_-=3/20\) at \(\kappa=1/20\);
  - the strict below-\(\gamma_-\) symbol list;
  - the equality \(|XY^2|=\gamma_-\);
  - the two \(\Gamma\)-gap identities
    \(|XY|-|X|=|Y|\) and \(|X^2Y|-|X^2|=|Y|\);
  - the resulting count of eight nontrivial coordinates.

## Remaining Issue #582 Obligations

- Prove the parameter-increment moment estimates for these coordinate fields.
- Use the dyadic-net theorem and coordinate-to-model theorem to complete the
  finite-sector random-model Cauchy application.
- Extend from the strict negative sector to the solution sector needed by the
  modelled fixed-point theorem, then carry out the SPDE-to-OS passage.

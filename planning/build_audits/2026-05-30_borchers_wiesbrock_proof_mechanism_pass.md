# 2026-05-30 Borchers--Wiesbrock Proof-Mechanism Pass

## Scope

This pass addresses the half-sided modular inclusion component of the
foundational AQFT proof-debt cluster in Volume IV, Chapter 4.  The
Borchers--Wiesbrock statement remains a quoted theorem.  The manuscript now
distinguishes the deep theorem from the elementary differentiated commutator
that follows after the translation group has already been constructed.

## Manuscript Change

- Clarified that a standard half-sided modular inclusion means standardness
  for `M`, `N`, and the relative commutant `N' cap M`, together with the
  half-sided invariance condition.
- Added the standard-real-subspace formulation:
  `H_M = closure{A Omega : A=A^* in M}` and similarly for `H_N`.
- Explained that half-sidedness is a modular-dilation invariance statement for
  those standard subspaces.
- Stated the proof mechanism: Borchers--Wiesbrock theory constructs a
  positive-energy affine-group representation from the half-sided modular
  inclusion, with the translation group `T(a)=exp(i a P)`, `P >= 0`.
- Made explicit that the positivity of `P` is the analytic half-sidedness
  input, while the displayed Lie-algebra commutator is only the infinitesimal
  consequence of the already-constructed affine covariance relation.

## Issue Alignment

- #695: improves the Borchers--Wiesbrock component of the foundational
  quoted-theorem proof debt.
- #691: preserves a substantive theorem while preventing the elementary
  commutator differentiation from being mistaken for the proof of the theorem.

## Remaining Proof Debt

This pass does not close #695.  Remaining pieces include OS boundary-value
infrastructure and substantial interacting examples of AQFT objects.

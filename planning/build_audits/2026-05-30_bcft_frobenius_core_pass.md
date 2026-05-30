# 2026-05-30 BCFT Frobenius-Core Pass

## Scope

- Continued the Volume V CFT proof-debt work for issues #625 and #697.
- Targeted the boundary-CFT point where the chapter had quoted the
  Cardy-Lewellen rational sewing theorem but had only sketched the
  Frobenius-algebra mechanism behind the theorem.

## Edits

- Added the algebraic core of the rational boundary construction to
  `volume_v/chapter14_boundary_conformal_field_theory.tex`:
  symmetric special Frobenius algebra objects in the chiral tensor category,
  left-module boundary conditions, open-sector multiplicities
  \(\dim \operatorname{Hom}_A(M\otimes U_i,N)\), boundary OPE composition by
  \(A\)-linear morphisms, and the associator-pentagon origin of the
  Cardy-Lewellen boundary sewing equation.
- Explained the diagonal Cardy solution as the special case \(A=\mathbf 1\).
- Added the bimodule formula for closed bulk multiplicities and explained
  the classifying-algebra interpretation of disk one-point functions.
- Updated the Volume V BCFT dossier and the public calculation companion.

## Verification Added

- `calculation-checks/bcft_cardy_checks.py` now checks that the \(A=\mathbf 1\)
  module-morphism multiplicity formula reduces exactly to Ising/Cardy fusion
  multiplicities.

## Remaining Boundary

- The analytic all-surface rational sewing theorem remains a quoted theorem.
  This pass supplies the finite-categorical mechanism used by the theorem,
  while leaving analytic convergence and global sewing over moduli space at
  the theorem boundary.

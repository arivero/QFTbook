# Issue #624: Free Magnons and BMN Entry Point

## Scope

This pass strengthens Volume VII, Chapter 12 at the beginning of the planar
spin-chain development.  It does not use pp-wave string quantization as an
input.  The added material derives the finite-chain one-loop BMN normalization
directly from the cyclic single-trace Bethe equations.

## Manuscript Changes

- Added `Free Magnons and BMN Double Scaling` to
  `monograph/tex/volumes/volume_vii/chapter12_planar_n4_spectral_problem_spin_chains.tex`.
- Defined the unquotiented length-`L` spin-chain space, translation operator,
  cyclic projection, one-magnon Fourier vector, and the reason nonzero
  one-magnon states vanish after the single-trace projection.
- Defined the relative two-impurity BMN Fourier convention while explicitly
  separating this coordinate convention from diagonalization of the
  interacting dilatation operator.
- Proved the exact one-loop two-magnon quantization
  `exp(i p (L-1))=1`, hence `p=2 pi n/(L-1)`, and
  `gamma=(lambda/pi^2) sin^2(pi n/(L-1))`.
- Derived the double-scaling limit
  `J=L-2 -> infinity`, `lambda'=lambda/J^2` fixed, giving
  `gamma=lambda' n^2+O(J^{-1})`.
- Adjusted the Chapter 13 BMN scaling check so it references the gauge-theory
  one-loop normalization rather than presenting a string-theory derivation as
  input.

## Calculation Check

- Extended `calculation-checks/planar_n4_integrability_checks.py` with a
  two-magnon BMN quantization check:
  - verifies the exact cyclic Bethe phase;
  - verifies the rapidity and sine forms of the energy;
  - verifies the displayed anomalous-dimension normalization;
  - verifies `O(J^{-1})` relative convergence at fixed `lambda'`.

## Remaining Issue #624 Items

This pass resolves the free-magnon/BMN start item.  The issue remains open
for BES/cusp depth, classical finite-gap/Pohlmeyer material, four-loop Konishi
wrapping depth, and a rigorous TBA/QSC comparison.

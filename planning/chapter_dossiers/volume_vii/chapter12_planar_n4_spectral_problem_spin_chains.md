# Chapter 12: Planar N=4 Supersymmetric Yang-Mills as a Spectral Problem

## Source Position

This chapter begins the planar-integrability block after the core
supersymmetric QFT examples.  It rewrites the stringbook spin-chain material
as a local-operator spectral problem in four-dimensional gauge theory.

## Notation Inventory

- `lambda`: 't Hooft coupling `g_YM^2 N`.
- `g`: integrability coupling `sqrt(lambda)/(4 pi)`.
- `V`: one-letter space of elementary fields and covariant derivatives.
- `H_L^cyc`: cyclic single-trace spin-chain quotient.
- `S`: closed sector of one-letter space under planar mixing.
- `tau`: cyclic shift on spin-chain sites.
- `X,Z`: two complex scalars defining the `SU(2)` scalar sector.
- `P_{j,j+1}`: adjacent spin permutation.
- `I,P,K`: identity, permutation, and trace maps in the `SO(6)` scalar chain.
- `H_XXX`: one-loop Heisenberg Hamiltonian.
- `u_j,p_j`: Bethe rapidities and momenta.
- `D_+`: lightlike covariant derivative in the `SL(2)` sector.

## Claim Ledger

- Defines the planar single-trace operator space as a cyclic quotient before
  introducing spin-chain language.
- Adds the planar two-point inner product and quotient status of spin-chain
  representatives.
- Adds a two-site scalar mixing proposition with color-locality and BPS
  protection fixing the identity term.
- Adds the full one-loop `SO(6)` scalar density
  `K+2I-2P` and proves its holomorphic `SU(2)` reduction.
- States and derives the one-loop `SU(2)` Hamiltonian from nearest-neighbor
  planar mixing, BPS protection of the identity term, and the adjacent
  exchange coefficient.
- Derives the coordinate Bethe ansatz, cyclicity condition, and energy formula
  for the rational chain.
- Carries the one-loop Konishi descendant calculation to
  `gamma_K^(1)=3 lambda/(4 pi^2)`.
- Separates the asymptotic long-chain problem from finite-length wrapping.
- Records the `SL(2)`, `SU(2|3)`, and full oscillator-module sector hierarchy
  and the range growth of the long-range dilatation operator.

## Figure Ledger

No figure is included in this pass.  A future figure should show the cyclic
single-trace word and the adjacent exchange interaction.

## Calculation Checks

- `calculation-checks/planar_n4_integrability_checks.py` verifies the
  one-magnon finite-difference spectrum and the displayed cyclic Konishi
  Bethe roots.
- The same script checks that the `SO(6)` trace operator vanishes on the
  holomorphic `X,Z` subsector.
- Same script now also checks BMN scaling and bound-state dispersion
  normalizations that depend on the chapter's coupling convention.

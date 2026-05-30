# Chapter 11: Finite Gauge Theory and State-Sum TQFT

## Source Position

This chapter follows finite-dimensional BV localization by giving a genuinely
finite TQFT class where field groupoids, path sums, twists, gluing, boundary
state spaces, defects, and anomaly inflow can be stated without analytic
regularization.  It also serves as the main exact example for the
bordism-functoriality chapter.

## Notation Inventory

- `G`: finite gauge group.
- `mathfrak Z_{G,omega}^{(D)}`: finite gauge state-sum datum, including
  gauge group, Dijkgraaf-Witten cocycle class, bundle groupoids, boundary
  transgression line, state spaces, bordism operators, and triangulated flat
  connection representatives.
- `X`: finite groupoid when used in the groupoid-cardinality section.
- `Aut_X(x)`: automorphism group of an object `x` in `X`.
- `Bun_G(M)`: groupoid of principal `G`-bundles on `M`.
- `rho`: monodromy homomorphism `pi_1(M)->G`.
- `C_G(rho)`: centralizer of the image of `rho`.
- `B_Sigma`: boundary field groupoid `Bun_G(Sigma)`.
- `H_G(Sigma)`: untwisted boundary state space of functions on
  `pi_0 Bun_G(Sigma)`.
- `r_0,r_1`: boundary restriction maps from `Bun_G(M)` to incoming/outgoing
  boundary groupoids.
- `K`: triangulation of `M`; `K_0`, `K_D` are vertex and top-simplex sets.
- `g_ij`: flat lattice connection on oriented edges.
- `omega`: normalized degree-`D` group cocycle defining a
  Dijkgraaf-Witten twist.
- `L_omega(Sigma)`: transgressed boundary line for the twisted state space.
- `Irr(G)`: irreducible complex representations of `G`.
- `d_R`: dimension of an irreducible representation `R`.
- `alpha`: degree-`D+1` finite-symmetry anomaly cocycle.

## Claim Ledger

1. Defines the finite gauge state-sum datum before developing its pieces:
   finite group, cocycle twist, principal-bundle groupoids, transgressed
   boundary lines, state spaces, push-pull bordism maps, and triangulated
   representatives.
2. Defines finite groupoid cardinality and finite groupoid integration with
   the automorphism denominator.
3. Proves the action-groupoid formula `|X//H|=|X|/|H|`.
4. Defines untwisted finite gauge theory as `|Bun_G(M)|`.
5. Proves the connected-manifold formula
   `Z_G(M)=|Hom(pi_1(M),G)|/|G|`.
6. Defines boundary state spaces as functions on boundary bundle groupoids and
   bordism maps as push-pull along spans.
7. Proves finite groupoid Fubini with explicit image/kernel automorphism
   weights, then proves finite groupoid gluing by descent for principal
   bundles and Fubini over finite homotopy fibers.
8. Defines the triangulated flat-connection state sum and derives its equality
   with groupoid cardinality through the action groupoid
   `Flat_G(K)//G^{K_0}`.
9. Defines Dijkgraaf-Witten twists from normalized cocycles and proves
   Pachner-move invariance from the cocycle equation.
10. Defines twisted boundary state spaces as sections of the transgressed
   boundary line.
11. Computes explicit closed-surface partition functions:
    `Z_G(Sigma_g)=|G|^{2g-2} sum_R d_R^{2-2g}`.
12. Identifies the circle state space with class functions on `G` and the
    pair-of-pants product with convolution.
13. Records the three-dimensional `T^3` commuting-triple formula and the
    Drinfeld-center description of line operators.
14. States finite correspondence defects and degree-`D+1` anomaly inflow.

## Figure Ledger

- `fig:finite-gauge-gluing-span`: span/homotopy-fiber-product diagram for
  finite gauge gluing along an intermediate boundary.

## Calculation Checks

- `calculation-checks/finite_gauge_state_sum_checks.py` verifies with exact
  arithmetic: action-groupoid cardinality, surface partition formulas for
  cyclic groups and `S_3`, class-function convolution, the standard
  `Z_n` Dijkgraaf-Witten `3`-cocycle condition, tree gauge-fixing counts,
  one-object finite-groupoid Fubini with image/kernel automorphism factors,
  and torus commuting-pair counts.

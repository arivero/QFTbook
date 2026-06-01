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
- `A`, `Ahat`, `C_A=A op Ahat`: finite Abelian gauge group, Pontryagin dual,
  and Abelian Drinfeld-double line-label group.
- `B((a,chi),(b,psi))`, `theta(a,chi)`: Abelian line braiding pairing and
  topological spin.
- `L`, `L^perp`, `B_L`: bosonic Lagrangian line subgroup, its braiding
  orthogonal, and the corresponding finite line-condensation boundary datum.
- `H_cyl(L_0,L_1)`: finite cylinder sector vector space between two Abelian
  line-condensation boundaries.
- `H`, `H_0`, `H_1`: finite subgroup boundary data for a nonabelian finite
  group `G`.
- `B_H`: subgroup boundary with boundary fields given by `H`-reductions of
  the boundary `G`-bundle.
- `beta`: normalized boundary `2`-cochain satisfying
  `delta beta = i^* omega` for a relative Dijkgraaf-Witten boundary.
- `H_0\G/H_1`: double-coset set of interval sectors between subgroup
  boundaries.
- `V(H_i,H_j)`: bi-invariant function space
  `Fun(G,C)^{H_i x H_j}` assigned to a subgroup-boundary interval.
- `star_{H_1}`: normalized finite push-pull convolution composing two
  subgroup-boundary intervals across the intermediate boundary `H_1`.
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
14. Develops finite Abelian line-condensation boundaries: the line-label
    group `A op Ahat`, braiding, spin, bosonic Lagrangian subgroups, endpoint
    criterion, and cylinder sector count
    `dim H_cyl(L_0,L_1)=|C_A/(L_0+L_1)|=|L_0 cap L_1|`.
15. Develops finite subgroup boundaries for general finite `G`, works out the
    interval sector groupoid with double-coset labels `H_0\G/H_1`, records the
    stabilizer weights, and gives the relative Dijkgraaf-Witten boundary
    condition `delta beta=i^* omega` as an explicit state-sum cancellation
    identity.  Also derives the boundary-junction convolution
    `f star_{H_1} k = |H_1|^{-1} sum_{xy=g} f(x)k(y)`, proves
    associativity and unit sectors by finite Fubini, and computes the
    `S_3` transposition-boundary algebra `X^2=2*1+X`.
16. States finite correspondence defects and degree-`D+1` anomaly inflow.

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
- `calculation-checks/finite_gauge_boundary_checks.py` verifies the Abelian
  finite-gauge boundary algebra for `Z_N`: electric and magnetic bosonic
  Lagrangian subgroups, rejection of non-bosonic diagonal subgroups, endpoint
  absorption equivalence, and the cylinder-sector count for same and mixed
  rough/smooth boundary pairs.
- `calculation-checks/finite_gauge_subgroup_boundary_checks.py` verifies the
  nonabelian subgroup-boundary interval groupoid for `S_3` and `D_4`
  examples, including double-coset partitions, stabilizer weights, groupoid
  cardinality, normalized boundary-junction convolution, associativity, unit
  sectors, integral structure constants, the `S_3` two-sector algebra, and
  the finite relative cochain cancellation `delta beta=i^* omega`.

## Audit Notes

- 2026-05-31 finite-boundary pass: added an exact Abelian finite-gauge
  boundary laboratory.  The text now separates the bosonic Lagrangian
  boundary datum from a general continuum gapped-boundary theorem and proves
  the cylinder sector count by endpoint absorption of condensed lines.
- 2026-05-31 subgroup-boundary pass: added the exact nonabelian subgroup
  boundary construction and relative Dijkgraaf-Witten boundary cochain
  cancellation.  The chapter now distinguishes double-coset sector labels
  from stabilizer-weighted groupoid cardinalities and states the boundary
  anomaly cancellation condition as `delta beta=i^* omega`.
- 2026-05-31 subgroup-junction pass: added the finite span for composing two
  subgroup-boundary intervals, derived the normalized convolution from the
  intermediate `H_1` gauge volume, and checked associativity/unit/structure
  constants in exact finite examples.
- 2026-05-31 issue #691 continuation: demoted the relative
  Dijkgraaf-Witten boundary cocycle cancellation from proposition/proof form
  to paragraph-level finite state-sum verification.  The exact local ratios,
  the `delta beta=i^* omega` cancellation, and the obstruction class remain
  explicit; theorem-family rank is reserved for deeper state-sum/gluing
  machinery rather than this local cochain cancellation check.
- 2026-06-01 issue #691 continuation: demoted the subgroup-boundary interval
  sector double-coset classification from proposition/proof form to a worked
  groupoid paragraph.  The action groupoid, double-coset labels, stabilizer
  groups, and groupoid cardinality remain explicit, but the direct orbit
  calculation no longer carries theorem-family rank.

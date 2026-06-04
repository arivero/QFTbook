# Chapter 10: Perturbative Algebraic QFT On Curved Backgrounds

## Source Position

Volume XII follows the microlocal spectrum condition with perturbative
algebraic QFT, the local curved-background perturbation framework built from
Hadamard functions and causal factorization.

## Notation Inventory

- `E(M)`, `F^(n)`, `WF`: configuration space, functional derivatives, and
  wavefront sets.
- `F_loc(M)`, `F_muc(M)`: local and microcausal functionals.
- `H`, `star_H`, `Gamma_H`: Hadamard two-point function, star product, and
  contraction bidifferential.
- `w`, `alpha_w`: smooth Hadamard difference and induced algebra isomorphism.
- `H_F`: Feynman bidistribution used away from diagonals.
- `T_n`: time-ordered products.
- `sd(t)`: scaling degree of a distribution near a diagonal.
- `S(F)`, `S_V(F)`, `R_V(F)`: time-ordered exponential, relative S-matrix,
  and interacting Bogoliubov field.
- `Z`: local renormalization map between time-ordered-product choices.
- `V_{lambda,H}(g)`, `w_Delta`, `a_m`, `a_R`: compactly supported
  `lambda phi^4` interaction in a Hadamard Wick coordinate, smooth diagonal
  Hadamard-scheme change, and the local mass/curvature components of that
  change.
- `S_BV`, `Delta_BV`: BV action and renormalized BV second-order operator.

## Claim Ledger

- Defines Bastiani-smooth functionals, functional support, local
  jet-dependent functionals, and their diagonal functional derivatives.
- Defines microcausal functionals through wavefront-set avoidance with the
  future/past covector convention inherited from the microlocal chapter.
- Defines the Hadamard star product, proves associativity by commuting
  tensor-factor contractions, and derives the Peierls bracket commutator.
- Proves the smooth-Hadamard-change isomorphism by the second-order
  Laplacian product rule.
- Defines time-ordered products as extensions from configuration space with
  partial diagonals removed; states and proves the finite scaling-degree
  extension theorem and identifies the local contact-term ambiguity.
- Explains Epstein--Glaser induction by causal factorization away from the
  total diagonal.
- Defines interacting fields by the relative S-matrix and proves the causal
  support statement for Bogoliubov fields.
- Records the Stueckelberg--Petermann local renormalization map and the BV
  quantum master equation as the gauge-theory consistency condition.
- Adds a worked interacting scalar coordinate: a compactly supported
  `lambda phi^4` interaction is transported under a smooth Hadamard-scheme
  change, producing the exact quartic Wick-power shift, finite mass and
  curvature-coupling coordinate shifts, geometric source terms, and a
  state-independent Wick-square observable shift in any Hadamard state.
  This gives the Volume XII interacting-example lane a concrete
  renormalization/state/output calculation rather than only the formal
  relative-S-matrix definition.

## Calculation Checks

- `calculation-checks/paqft_algebra_checks.py`: verifies the finite
  polynomial model of star-product associativity, the smooth-Hadamard-change
  intertwiner, the combinatorics of scaling-degree extension ambiguity, and
  the `lambda phi^4` Hadamard-scheme transport coefficients: quartic tadpole,
  vacuum term, Wick-square observable shift, mass/curvature coordinate
  shifts, and geometric-source coordinates.

## Figure Ledger

No figure is included in this pass.  Future figures should include causal
factorization regions, diagonal extensions in configuration space, and
Hadamard star-product comparison maps.

## Anti-Wrapper Audit

- 2026-06-04: added a worked interacting scalar example for issue #729.  The
  passage follows a concrete `lambda phi^4` interaction through a
  Hadamard-scheme change to mass, curvature-coupling, geometric-source, and
  Wick-square observable outputs; it does not present the pAQFT machinery as
  a nonperturbative curved-spacetime construction.

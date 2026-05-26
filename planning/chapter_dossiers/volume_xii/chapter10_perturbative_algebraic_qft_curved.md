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

## Calculation Checks

- `calculation-checks/paqft_algebra_checks.py`: verifies the finite
  polynomial model of star-product associativity, the smooth-Hadamard-change
  intertwiner, and the combinatorics of scaling-degree extension ambiguity.

## Figure Ledger

No figure is included in this pass.  Future figures should include causal
factorization regions, diagonal extensions in configuration space, and
Hadamard star-product comparison maps.

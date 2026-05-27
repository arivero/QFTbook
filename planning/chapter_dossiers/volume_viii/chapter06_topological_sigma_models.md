# Chapter 06: Topological Sigma Models

## Source Position

This chapter follows the general cohomological-field-theory chapter and
develops the first sigma-model family of examples.  Its role is to separate
the continuum cohomological QFT datum from the finite-dimensional
Gromov--Witten and B-model outputs obtained after localization.

## Notation Inventory

- `Sigma`, `j_Sigma`: compact Riemann surface and its complex structure.
- `X`: compact target manifold; almost Kahler for the A-model, Calabi-Yau
  complex manifold for the closed B-model.
- `phi`: bosonic map from `Sigma` to `X`.
- `Q_A`, `Q_B`: A-model and B-model cohomological differentials.
- `psi`, `eta`, `theta`: fermionic local variables in the A- and B-model
  complexes.
- `bar partial_J phi`: Cauchy-Riemann section whose zero locus is the
  holomorphic-map space.
- `beta`: curve class in `H_2(X;Z)`.
- `Q^beta`: Novikov/Kahler weight
  `exp(2*pi*i int_beta(B+i omega))`.
- `Mbar_{g,n}(X,beta)`: compactified stable-map moduli space.
- `ev_a`: evaluation map at the `a`-th marked point.
- `[Mbar]^{vir}`: virtual fundamental class or equivalent virtual integration
  datum.
- `eta_ab`: Poincare pairing on `H^*(X)`.
- `star`: genus-zero small quantum product.
- `PV^{p,q}(X)`: Dolbeault polyvector complex for the B-model.

## Claim Ledger

- Defines the mapping field space as a Frechet manifold together with
  locally super-ringed fermionic directions.
- Defines the A-model local scalar complex and proves
  `Q_A O_alpha = O_{d alpha}`.
- Proves the pointwise A-model energy identity
  `1/2 |d phi|^2 = phi^* omega + |bar partial_J phi|^2`
  with the chapter's normalization of `bar partial_J`.
- Derives the fixed-domain Fredholm index by Riemann-Roch and the
  stable-map virtual dimension by adding the curve-moduli dimension.
- Defines stable maps, evaluation maps, primary GW functionals, and the
  degree-selection rule while explicitly separating virtual integration
  input from continuum QFT construction.
- Defines the small quantum product and proves associativity from the
  splitting axiom on `Mbar_{0,4}`.
- Works out the projective-space relation
  `QH^*(P^m)=C[H,Q]/(H^{m+1}-Q)`.
- Defines descendants through cotangent-line classes on the universal curve
  and separates them from fixed-worldsheet descent observables.
- Defines the B-model Dolbeault polyvector complex, trace pairing through
  the holomorphic volume form, and the complex-structure Maurer-Cartan
  equation.
- States the continuum construction problem for topological sigma models as
  an explicit open problem rather than treating finite-dimensional
  enumerative formulas as a complete QFT definition.

## Calculation Ledger

- `calculation-checks/topological_sigma_model_checks.py`
  verifies the A-model pointwise energy identity, projective-space quantum
  cohomology relation and associativity, the projective-space degree
  selection rule, the virtual-dimension formula, and the B-model top-form
  degree condition.

## Figure Ledger

No figure is included.  A later visual pass should add a diagram of the
universal curve, marked sections, evaluation maps, and the boundary
factorization of `Mbar_{0,4}(X,beta)`.

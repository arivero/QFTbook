# Chapter 06: Topological Sigma Models

## Source Position

This chapter follows the general cohomological-field-theory chapter and
develops the first sigma-model family of examples.  Its role is to separate
the continuum cohomological QFT datum from the finite-dimensional
Gromov--Witten and B-model outputs obtained after localization.

## Notation Inventory

- `mathfrak A_X`: A-model cohomological sigma-model datum, including
  source surface, almost Kahler target, locally super-ringed field space,
  `Q_A`, localization section, virtual integration package, Novikov
  completion, and contact-term prescription.
- `mathfrak B_X`: closed B-model cohomological sigma-model datum, including
  Kahler parent target, closed `B`-field, axial-anomaly trivialization,
  holomorphic canonical trivialization, chosen holomorphic volume form,
  polyvector complex, trace pairing, regulated integration cycle, and
  contact-term prescription.
- `Sigma`, `j_Sigma`: compact Riemann surface and its complex structure.
- `X`: compact target manifold; almost Kahler for the A-model, Kahler as the
  ordinary parent target for the closed B-model.
- `phi`: bosonic map from `Sigma` to `X`.
- `Q_A`, `Q_B`: A-model and B-model cohomological differentials.
- `psi`, `eta`, `theta`: fermionic local variables in the A- and B-model
  complexes.
- `bar partial_J phi`: Cauchy-Riemann section whose zero locus is the
  holomorphic-map space.
- `beta`: curve class in `H_2(X;Z)`.
- `Q^beta`: Novikov/Kahler weight
  `exp(2*pi*i int_beta(B+i omega))`.
- `v_{g,n,beta}`: real virtual dimension of the stable-map sector and the
  number of real zero-mode degrees that primary or descendant insertions must
  saturate.
- `Mbar_{g,n}(X,beta)`: compactified stable-map moduli space.
- `ev_a`: evaluation map at the `a`-th marked point.
- `[Mbar]^{vir}`: virtual fundamental class or equivalent virtual integration
  datum.
- `eta_ab`: Poincare pairing on `H^*(X)`.
- `star`: genus-zero small quantum product.
- `PV^{p,q}(X)`: Dolbeault polyvector complex for the B-model.
- `a_B`: axial/global anomaly-line trivialization for the B-twist.
- `tau_K`, `Omega_X`: holomorphic canonical trivialization and chosen volume
  form used by the closed B-model trace.
- `c_A`, `c_B`: A- and B-model source/collision/contact-term prescriptions.

## Claim Ledger

- States upfront hypotheses for the closed A-model and B-model data, making
  explicit which pieces belong to the cohomological QFT layer and which
  finite-dimensional packages enter after localization.
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
- Adds an A-model worldsheet-instanton amplitude datum: the fixed-`beta`
  contribution is the Novikov weight times the virtual integral only after
  determinant-line, orientation, compactification, gluing, and contact-term
  data have been specified.
- Adds the A-model zero-mode saturation rule behind the degree selection:
  after nonzero modes have been paired and the determinant line has been
  oriented, primary insertions must supply total real degree
  `v_{g,n,beta}`, while descendants contribute `2 k_a` from psi-classes.
  This records the instanton-sector amplitude gate rather than treating
  holomorphic maps alone as a scalar contribution.
- Specifies the finite-dimensional virtual integration package used by the
  A-model formulas, including the diagonal refined-pullback identity on
  genus-zero boundary strata.
- Defines the small quantum product and derives associativity as a
  conditional consequence of the splitting identity on `Mbar_{0,4}`, without
  treating virtual geometry as a formal corollary of the path integral.
- Works out the projective-space relation
  `QH^*(P^m)=C[H,Q]/(H^{m+1}-Q)` from the degree-one
  line-plus-three-marked-points instanton sector and its incidence
  normalization, with the scalar `Q` coefficient recovered by pairing with
  the Poincare-dual detector `H^m`.
- Defines descendants through cotangent-line classes on the universal curve
  and separates them from fixed-worldsheet descent observables.
- Defines the B-model Dolbeault polyvector complex, trace pairing through
  the holomorphic volume form, and the complex-structure Maurer-Cartan
  equation.
- Separates the B-model target/anomaly layers: Kahler parent sigma-model
  data, local Dolbeault-polyvector complex, perturbative axial anomaly
  cancellation, holomorphic triviality of `K_X`, chosen `Omega_X`, and
  all-genus/global determinant-line data.  Includes examples separating
  topological or de Rham `c1` tests from holomorphic volume-form existence.
- States the continuum construction problem for topological sigma models as
  an explicit open problem rather than treating finite-dimensional
  enumerative formulas as a complete QFT definition.

## Calculation Ledger

- `calculation-checks/topological_sigma_model_checks.py`
  verifies the A-model pointwise energy identity, projective-space quantum
  cohomology relation and associativity, the projective-space degree
  selection rule, the degree-one projective worldsheet-instanton dimension
  and product ledger, reconstruction of projective-space product
  coefficients from Poincare-dual Gromov-Witten pairings, primary and
  descendant zero-mode saturation against the
  virtual top degree, the virtual-dimension formula, and the B-model top-form
  degree condition plus the B-model condition lattice separating the parent,
  local complex, perturbative anomaly, trace, and all-genus gates.

## Audit Notes

- 2026-06-05 issue #809 B-model foundations pass: split the closed B-model
  datum into Kahler parent, closed `B`-field, axial-anomaly trivialization,
  holomorphic canonical trivialization, chosen volume form, trace, and global
  anomaly-line data; removed the false equivalence between `c1(TX)=0` and
  holomorphic triviality of `K_X`; added finite examples distinguishing
  topological/de Rham Chern-class tests from volume-form existence.
- 2026-06-05 issue #807 projective quantum-product proof pass: corrected the
  `P^m` relation proof so the scalar `Q` term is detected by pairing with
  `H^m`, showed the other basis coefficients vanish by the degree rule, and
  added a finite Poincare-pairing reconstruction check.

## Figure Ledger

No figure is included.  A later visual pass should add a diagram of the
universal curve, marked sections, evaluation maps, and the boundary
factorization of `Mbar_{0,4}(X,beta)`.

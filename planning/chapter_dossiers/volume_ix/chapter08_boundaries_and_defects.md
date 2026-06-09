# Chapter 08: Boundaries And Defects
Source-File: monograph/tex/volumes/volume_ix/chapter08_boundaries_and_defects.tex

## Source Position

Volume IX moves from bulk phase data to submanifold-supported QFT data.
Boundaries and defects refine global symmetry, anomaly, and phase information
and prepare later categorical treatments.

## Notation Inventory

- `Reg_partial(M)`: admissible regions in a spacetime with boundary,
  including interior, boundary, and mixed collar regions.
- `A_bulk(U)`, `A_partial(O)`, `B(V)`: interior bulk net, boundary-condition
  extension net on admissible regions, and boundary observable net.
- `C(W)`: mixed collar-region algebra used as the ordinary local target for
  both interior and boundary inclusion maps.
- `iota_{O_1 O_2}`, `jmath_{V,O}`: isotony maps for admissible regions and
  boundary-region embeddings into mixed regions.
- `omega_partial`: optional state or functional on the already-defined
  boundary-bulk local system.
- `O(x_perp,y)`, `Ohat_alpha(y)`: bulk local operator and boundary operators
  in the boundary expansion.
- `R_N`, `p_j`, `epsilon_{j,N}`: BOE remainder, seminorms on smeared
  separated correlators, and explicit asymptotic remainder functions.
- `phi`, `G_D`: free half-space scalar field and Euclidean Green function in
  the method-of-images boundary example.
- `T_-`, `T_+`: QFTs separated by an interface.
- `J(z)`: chiral WZW boundary current for Chern-Simons theory.
- `D_1`, `D_2`, `D_2 star D_1`: defects and their renormalized fusion.
- `1`, `eta`, `N`: critical Ising invisible, spin-flip, and Kramers-Wannier
  defects.
- `A`, `B`, `W_{e,m}`: compact one-form fields and line labels in the
  three-dimensional `Z_N` BF example.
- `L_D`: anomaly line of a boundary or defect.
- `U_gamma(A)`: open Wilson line parallel transport and its endpoint gauge
  variation.

## Claim Ledger

- Defines boundary QFT data as an AQFT-style boundary-preserving local net on
  admissible regions of a manifold with boundary.  Interior regions recover
  the bulk net, boundary regions carry a boundary net, mixed collar regions
  receive ordinary inclusion maps from both strata, and locality/covariance or
  Euclidean factorization is part of the structure.  States and amplitudes are
  additional data on this local system.
- Defines the boundary operator expansion as a renormalized approach datum
  with explicit seminorm/remainder control, while reserving stronger
  convergence for controlled BCFT-specific hypotheses or theorems.
- Displays the free half-space scalar Neumann versus Dirichlet leading
  boundary operators and now identifies the method-of-images two-point
  function as a state on the local boundary datum, not as part of the boundary
  condition itself.
- Defines interfaces, domain walls, and topological interfaces.
- Gives the Chern-Simons boundary WZW current as a concrete boundary operator
  algebra, cross-referenced to Volume VIII.
- Formulates defect fusion as a renormalized codimension-one limit.
- Displays the critical Ising defect fusion rules and proves that the
  Kramers-Wannier defect is noninvertible with Frobenius-Perron dimension
  `sqrt(2)`.
- Gives a three-dimensional `Z_N` BF electric-magnetic duality surface and its
  action on line labels.
- Relates boundary/defect anomaly lines to inflow-line trivialization, with
  proof.
- Shows the endpoint gauge variation of an open Wilson line and the resulting
  boundary-charge condition.
- Relates boundary/defect data to phase invariants.

## Calculation Checks

- `calculation-checks/extended_defect_ward_checks.py` verifies the finite
  higher-form Ward and junction-charge algebra used for extended operators
  and topological defects.
- `calculation-checks/categorical_defect_structure_checks.py` verifies finite
  defect-fusion, reflection-pairing, and junction-basis identities for the
  categorical defect language used later in the chapter.
- `calculation-checks/ising_defect_fusion_checks.py` verifies the
  \(\mathbb Q(\sqrt2)\) Ising/Kramers-Wannier defect fusion example,
  including Frobenius-Perron dimensions and the diagonal action on local
  primary sectors.
- `calculation-checks/finite_gauge_boundary_checks.py` verifies the finite
  Abelian gauge-theory line-condensation and boundary endpoint algebra that
  models the compact \(BF\) boundary examples.
- `calculation-checks/boundary_qft_datum_checks.py` verifies the finite
  stratified-net bookkeeping for the chapter opening: interior and boundary
  algebras map into collar algebras by ordinary inclusions, a direct
  interior-to-boundary map is rejected, states are separate from the boundary
  condition, and finite BOE jets carry nonzero controlled remainders.

## Audit Notes

- 2026-06-02 issue #561 dossier-link pass: recorded the existing
  boundary/defect companion checks explicitly in the chapter dossier.  The
  checks cover the finite algebraic examples used in the chapter; analytic
  boundary-QFT convergence statements remain manuscript proof obligations
  rather than finite calculation checks.
- 2026-06-09 issue #879 local-boundary-QFT pass: replaced the opening
  untyped `A(U) -> B(V)` datum with a boundary-preserving local net on
  interior, boundary, and mixed collar regions.  Re-audit note: the chapter now
  separates local algebraic structure, BOE/asymptotic approach maps, and
  states/amplitudes, so later endpoint, fusion, and anomaly statements have a
  typed local target instead of relying on a singular bulk-to-boundary
  restriction.  The BOE paragraph now points to Volume V Chapter 14 for the
  stronger positive-energy BCFT sewing package.

## Figure Ledger

No figure is included in this pass.  Later figures should show a half-space
boundary expansion, interface fusion by collision, and line endpoints on a
gauge-theory boundary.

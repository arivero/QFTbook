# Chapter 11: Higher-Group Symmetry And Symmetry TQFT

## Source Position

This chapter follows gauging and duality defects by defining higher-group
background fields and the one-higher-dimensional symmetry-TQFT organization
of backgrounds, anomalies, gauging, and condensation.

## Notation Inventory

- `mathfrak S_{Q,mathbb G}`: higher-group symmetry and symmetry-TQFT datum for the
  chapter: QFT, finite two-group, background higher groupoid, anomaly-line
  functor, symmetry TQFT, QFT boundary condition, topological defect system,
  and anomaly-trivialization/counterterm choice.
- `mathbb G=(G_0,A,rho,beta)`: finite two-group datum.
- `G_0`: ordinary finite internal symmetry.
- `A`: abelian one-form symmetry.
- `rho`: action of `G_0` on `A`.
- `beta`: Postnikov class in `H^3(BG_0,A_rho)`.
- `g`, `B`: ordinary and two-form background cochains.
- `B_mathbbG(M)`: finite higher groupoid of two-group backgrounds on `M`.
- `L_anom`: anomaly-line functor over the higher-group background groupoid.
- `T_sym`: one-higher-dimensional symmetry TQFT.
- `S_anom`: anomaly functional in one higher dimension.
- `B_Q`: boundary condition representing a QFT in the symmetry TQFT
  (manuscript notation `mathfrak B_{Q}` / `mathfrak B_{mathcal Q}`).
- `D_top`: topological defect system in the QFT, including symmetry surfaces,
  walls, junctions, endpoint operators, and isotopy/Pachner identifications.
- `tau`: anomaly trivialization or discrete counterterm used for gauging or
  condensation.
- `A_cond`: condensable algebra object in a defect category.
- `b`, `c`: `Z_N`-valued two-cochains in the finite five-dimensional
  one-form symmetry TQFT model.
- `lambda`, `kappa`: one-cochain gauge parameters for `b` and `c`.
- `Z_H(X;b,c)`: finite Heisenberg/BF symmetry-TQFT phase
  `exp(2 pi i/N int_X b cup delta c)`.
- `U_n(Sigma)`: topological symmetry surface labelled by `n in Z_N`.
- `mathsf U_b(Y)`: wall network determined by the Poincare-dual one-cycle of
  a closed two-cochain `b` on `Y`.
- `Y`: oriented three-manifold supporting a codimension-one condensation
  defect in a four-dimensional QFT.
- `C(Y)`: groupoid-normalized higher-gauging condensation insertion obtained
  by summing closed two-cochains on `Y` with normalization `|C^0|/|C^1|`.
- `Z^{(2)}_{Z_N}(Y)`: finite three-dimensional two-form gauge-theory factor
  `|C^0| |Z^2| / |C^1| = |H^0| |H^2| / |H^1|`.
- `(e,m)`: finite electric/magnetic one-form line charge label in
  `Z_N plus Z_N`.
- `j_5`: axial current normalized as in Chapter 50.
- `j_m`: magnetic one-form symmetry current in compact QED.
- `A_{N,p}`: minimal abelian three-dimensional TQFT with `Z_N` one-form
  symmetry anomaly `p`; spin refinement included when required.
- `B_A`: reduction of `[F/2 pi]` modulo `N` on the defect worldvolume.
- `D_{N,p}(M)`: dressed rational chiral defect on a closed oriented
  three-manifold `M`.
- `a`: compact `U(1)` gauge field living only on the `U(1)_N` defect for
  `p=1`.
- `b`, `c` in the QED half-space construction: compact two-form and one-form
  gauge fields on `X_+` used to gauge the `Z_N` subgroup of the magnetic
  one-form symmetry.
- `H(gamma)`: minimal renormalized `U(1)` 't Hooft line, as defined in
  Volume IX Chapter 3.

## Claim Ledger

- States the chapter's central higher-group symmetry and symmetry-TQFT datum
  upfront: QFT, finite two-group, background higher groupoids, anomaly-line
  functor, symmetry TQFT, QFT boundary condition, topological defect system,
  and trivialization/counterterm data.
- Defines two-group background fields through a twisted cocycle equation as
  the triangulated chart for the background higher groupoid in the datum.
- States the linked ordinary and one-form gauge transformations.
- Describes anomaly functionals for combined backgrounds as representatives of
  the anomaly-line functor in the datum.
- Defines the symmetry TQFT as the bulk organizer of QFT boundary conditions.
- Formulates gauging as condensation of an algebra object and records the
  anomaly obstruction.
- Constructs the finite five-dimensional `Z_N` one-form symmetry TQFT by the
  cochain action `b cup delta c` and proves its gauge invariance on closed
  manifolds.
- Explains fixed/summed boundary conditions for the finite one-form SymTFT and
  connects the exchange of boundary conditions with finite electric-magnetic
  line-charge duality.
- Defines a triangulated finite higher-gauging defect from a closed
  two-cochain sum over topological symmetry surfaces with the full finite
  groupoid normalization including gauge-for-gauge data.
- Makes the finite two-form gauge `2`-groupoid explicit: objects are closed
  two-cochains, one-morphisms are one-cochain gauge transformations, and
  two-morphisms are zero-cochain gauge-for-gauge transformations.  The
  homotopy cardinality
  `|H^0(Y,Z_N)| |H^2(Y,Z_N)| / |H^1(Y,Z_N)|` is shown to equal the
  unquotiented cochain measure `|C^0| |Z^2| / |C^1|`.
- Proves the finite cochain fusion theorem: two condensation defects fuse to
  the original condensation defect tensored with the three-dimensional finite
  `Z_N` two-form gauge-theory state sum
  `Z^{(2)}_{Z_N}(Y)=|C^0||Z^2|/|C^1|=|H^0||H^2|/|H^1|`.
- Defines the relative state space of the finite two-form factor on a cut
  surface as `C[H^2(Sigma,Z_N)]`, with automorphism weights entering gluing,
  so the phrase "three-dimensional topological factor" is an actual finite
  state-sum functor rather than a scalar slogan.
- Separates the locally proved finite cochain theorem from the remaining
  continuum QFT burden: constructing the required surface networks,
  junctions, correlation topology, and anomaly trivialization in the
  particular interacting theory.
- Defines the compact-QED noninvertible chiral defect `D_{N,p}` by dressing a
  rational axial wall with the minimal abelian TQFT `A_{N,p}` coupled to the
  magnetic background `B_A`.
- Proves the local topological cancellation for `D_{N,1}`: the axial anomaly
  phase is cancelled by the fractional Hall response of the compact defect
  Chern-Simons theory.
- Gives the half-space gauging construction of `D_{N,p}` by gauging the
  `Z_N` subgroup of the magnetic one-form symmetry with compact fields `b,c`,
  including the discrete-torsion choice and the compensating rational axial
  change of variables.
- Defines the compact path-integral construction of QED noninvertible chiral
  defects, including their action on local fermions, Wilson lines, and
  minimal 't Hooft lines, while separating this from a future fully axiomatic
  reconstruction of compact QED and its defect Hilbert spaces.
- Clarifies that four-dimensional generalized symmetry generally requires a
  higher-categorical defect object, while fusion two-categories arise from
  controlled truncations or wall theories.

## Figure Ledger

No figure is included in this pass.  Future figures should show the
two-group background cochain complex and the symmetry-TQFT slab with
background and summing boundaries.  A later diagram should also show the
finite one-form SymTFT slab with fixed `b` and summed `b` boundary conditions,
and the collision of two condensation defects producing a three-dimensional
topological factor.

## Calculation Checks

- `calculation-checks/finite_higher_gauging_checks.py` verifies the finite
  groupoid normalization in the condensation defect, the exact algebra
  \(\mathfrak C^2=Z^{(2)}\mathfrak C\), and the cell-dependence that would
  remain if the degree-zero gauge-for-gauge factor were omitted.  It now also
  enumerates explicit finite cochain complexes over `Z_N` and checks directly
  that the cochain measure equals the finite `2`-groupoid homotopy
  cardinality, that the condensation convolution has fiber size `|Z^2|`, and
  that boundary flux sectors are the `H^2(Sigma,Z_N)` cosets.

## Anti-Wrapper Audit

- 2026-05-30 pass: replaced the finite higher-gauging `quotedtheorem` by a
  local theorem with proof.  The theorem proves the finite cochain and
  defect-network mechanism under explicit anomaly-free topological-surface
  hypotheses; it does not claim that those symmetry surfaces have been
  constructed in every continuum Yang--Mills theory.
- 2026-06-08 issue #844 semantic-status pass: reclassified the QED
  noninvertible chiral defect block from `controlledapproximation` to
  `construction`.  The block is a compact path-integral defect construction
  under stated magnetic one-form-symmetry assumptions, not an approximation
  estimate or a completed axiomatic reconstruction theorem.

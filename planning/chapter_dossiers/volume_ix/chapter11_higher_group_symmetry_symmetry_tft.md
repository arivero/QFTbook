# Chapter 11: Higher-Group Symmetry And Symmetry TQFT

## Source Position

This chapter follows gauging and duality defects by defining higher-group
background fields and the one-higher-dimensional symmetry-TQFT organization
of backgrounds, anomalies, gauging, and condensation.

## Notation Inventory

- `G_0`: ordinary finite internal symmetry.
- `A`: abelian one-form symmetry.
- `beta`: Postnikov class in `H^3(BG_0,A)`.
- `g`, `B`: ordinary and two-form background cochains.
- `S_anom`: anomaly functional in one higher dimension.
- `B_Q`: boundary condition representing a QFT in the symmetry TQFT.
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
- `C(Y)`: higher-gauging condensation insertion obtained by summing closed
  two-cochains on `Y`.
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

- Defines two-group background fields through a twisted cocycle equation.
- States the linked ordinary and one-form gauge transformations.
- Describes anomaly functionals for combined backgrounds.
- Defines the symmetry TQFT as a bulk organizer of QFT boundary conditions.
- Formulates gauging as condensation of an algebra object and records the
  anomaly obstruction.
- Constructs the finite five-dimensional `Z_N` one-form symmetry TQFT by the
  cochain action `b cup delta c` and proves its gauge invariance on closed
  manifolds.
- Explains fixed/summed boundary conditions for the finite one-form SymTFT and
  connects the exchange of boundary conditions with finite electric-magnetic
  line-charge duality.
- Defines a triangulated finite higher-gauging defect from a closed
  two-cochain sum over topological symmetry surfaces.
- Proves the finite cochain fusion mechanism: two condensation defects fuse to
  the original condensation defect tensored with a three-dimensional finite
  `Z_N` two-form gauge-theory state sum.
- Records the source-lineage theorem boundary for higher-gauging
  noninvertible condensation defects in four-dimensional QFT: the finite
  cochain mechanism is proved here, while the continuum surface-operator
  construction remains a separate QFT input.
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
- States the compact path-integral theorem for QED noninvertible chiral
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

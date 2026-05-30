# Chapter 11: Six-Dimensional Superconformal Theories

## Source Position

This chapter follows three-dimensional supersymmetric gauge theories by
introducing supersymmetric QFTs whose fixed points are often specified
through representation data, tensor branches, anomalies, strings, and
compactification tests rather than microscopic Lagrangians.  The current pass
addresses the six-dimensional part of issue #588.

Reviewed source spine:

- `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`,
  lines 14506 onward: six-dimensional `(2,0)` theory, absence of ordinary
  Lagrangian, tensor branch, BPS strings, and compactification to 5D maximally
  supersymmetric Yang-Mills.
- `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`,
  lines 13955-14019: external motivation only.  The monograph definition and
  all logical uses in this chapter are QFT data, not string-theoretic
  constructions.
- GitHub issue #588: request for six-dimensional `(2,0)` theory data and
  compactification/normalization boundaries.

## Notation Inventory

- `Spin(1,5)`: six-dimensional Lorentz spin group.
- `G_R`: R-symmetry group, either `SU(2)_R` or `USp(4)_R` in the chapter.
- `OSp(8^*|2)`, `OSp(8^*|4)`: six-dimensional superconformal algebras for
  `(1,0)` and `(2,0)`.
- `phi^I`, `phi`: tensor-branch scalar coordinates.
- `B^I`, `H^I`: two-form gauge potentials and self-dual field strengths.
- `mathfrak g`, `mathfrak t_g`, `W_g`: simply laced Lie algebra, Cartan
  algebra, and Weyl group of a `(2,0)` theory.
- `I_8`, `I_8(1)`: interacting and free-tensor anomaly polynomials.
- `N_R`: rank-five `SO(5)_R` background bundle for `(2,0)` anomalies.
- `Omega^{IJ}`, `X_I^{(4)}`: tensor pairing and Green-Schwarz four-forms.
- `Lambda_str`: integral lattice of string charges.
- `Z_q^A`: tensor-branch central-charge vector of a string of charge `q`.
- `q`, `alpha`: BPS string charge vector and root-lattice charge.
- `Q_g`, `P_g`, `A_g`: root lattice, weight lattice, and finite
  discriminant/defect group `P_g/Q_g` for a simply laced `(2,0)` type.
- `b_g`: finite pairing \(A_g\times A_g\to \mathbb Q/\mathbb Z\) induced by
  the lattice pairing.
- `K_Y(g)`, `L`: finite flux group \(H^3(Y;A_g)\) and a maximal isotropic
  polarization subgroup.
- `g_5`, `R`: five-dimensional trace-delta Yang-Mills coupling and circle
  radius.

## Claim Ledger

- Separates six-dimensional superconformal representation data from
  branch-EFT field variables.
- Proves that a six-dimensional Yang-Mills coupling has negative mass
  dimension and therefore is not a marginal conformal coordinate.
- Defines `(1,0)` and `(2,0)` tensor multiplet variables while marking
  self-dual field actions as formulation-dependent.
- Defines the abelian self-dual tensor datum using a local two-form gauge
  field, differential-cohomology/global-period caveat, integral string-charge
  lattice, and Dirac pairing.
- Records the little-group degree-of-freedom calculation showing that a
  six-dimensional chiral two-form has three physical polarizations and that a
  free `(2,0)` tensor multiplet has eight bosonic on-shell polarizations.
- Defines tensor-branch coordinates, the chamber structure, and
  Green-Schwarz couplings as effective data rather than a fixed-point
  construction.
- Gives the `(2,0)` tensor-branch quotient
  `(R^5 tensor t_g)/W_g`, with the type `A_{N-1}` chart as an example.
- States anomaly matching as an equality involving `I_8` and quadratic
  Green-Schwarz terms.
- Proves the quadratic Green-Schwarz descent factor
  `1/2 Omega^{IJ} X_I X_J`, including why the `1/2` disappears in the
  six-form descent representative.
- Records the `(2,0)` anomaly polynomial as a quoted theorem, with all
  coefficients and characteristic classes named.
- Displays and derives the ADE arithmetic of the `(2,0)` anomaly coefficient,
  including the `A_{N-1}` cubic scaling.
- Defines BPS string charges, tensions, and inflow data, including
  root-lattice strings for `(2,0)` theories.
- Derives the BPS string tension from the tensor-branch central charge using
  positivity of the string-sector supercharge anticommutator and its
  \(\pm|Z_q|\) eigenvalues, and states explicitly that this does not
  construct the tensionless limit.
- Defines the `(2,0)` finite defect group \(A_g=P_g/Q_g\), its nondegenerate
  \(\mathbb Q/\mathbb Z\)-valued pairing, the ADE group table, the finite
  flux group \(H^3(Y;A_g)\), and the need for a polarization before a
  self-dual finite flux sector gives numerical partition data.
- Works out the cyclic \(A_{N-1}\) finite-flux model \(K=\mathbb Z_N\oplus
  \mathbb Z_N\), including its alternating pairing and maximal isotropic
  subgroup.
- Proves the trace-delta compactification normalization
  `g_5^2 = 4 pi^2 R` from the BPST instanton mass and KK momentum.
- Derives the wrapped-string/W-boson mass matching and the scalar
  normalization `phi_5d = 2 pi R phi_6d`.
- Records compactification on Riemann surfaces as a test requiring twist,
  defect, anomaly, and descendant data.

## Calculation Checks

- `calculation-checks/susy_abjm_6d_checks.py` verifies the six-dimensional
  Yang-Mills coupling dimension, chiral two-form physical degrees of freedom,
  type `A_{N-1}`, `D_N`, and exceptional `(2,0)` rank/dimension/anomaly
  coefficient arithmetic, tensor-branch dimensions, the quadratic
  Green-Schwarz descent factor, the trace-delta five-dimensional
  instanton/Kaluza-Klein normalization, wrapped-string/W-boson scalar
  normalization, ADE defect-group orders from Cartan determinants, and the
  cyclic finite-flux polarization model.

## Proof Obligations And Boundaries

- The interacting `(2,0)` theory remains a non-Lagrangian object; the chapter
  gives protected and effective data, not a construction.
- The `(2,0)` anomaly polynomial is quoted theorem status because a
  first-principles construction of the interacting six-dimensional local QFT
  and its anomaly functional is not reproduced here.  External geometric or
  string-theoretic arguments can motivate the formula but are not used as
  foundations.
- Compactification to 5D maximally supersymmetric Yang-Mills is treated as a
  protected test/effective description, not as a definition of the parent
  six-dimensional local QFT.
- Future passes should add line/surface defect categories, anomaly descent
  calculations for string worldsheets, global forms/discrete quotients of the
  `(2,0)` theories, and class-`S` anomaly reductions.

## Development Log

- 2026-05-28 issue #633 reading audit pass: expanded the chapter with an
  abelian self-dual tensor datum, chiral two-form degree-of-freedom
  calculation, tensor-branch effective datum, Green-Schwarz descent proof,
  ADE anomaly-coefficient arithmetic, BPS tension derivation, and
  wrapped-string/W-boson compactification matching.  Extended
  `calculation-checks/susy_abjm_6d_checks.py` accordingly.
- 2026-05-29 anti-wrapper pass: strengthened the BPS string tension proof by
  writing the positive supercharge anticommutator matrix and showing how the
  BPS inequality and saturation condition follow from its eigenvalues.
- 2026-05-30 depth-pass-B follow-up: added the finite defect-group and
  polarization layer for `(2,0)` theories, including root/weight lattice data,
  ADE discriminant groups, the finite \(H^3(Y;A_g)\) Heisenberg pairing, and
  a cyclic \(A_{N-1}\) polarization model with exact calculation checks.

## Figure Ledger

No figure is included in this pass.  Future figures should show a tensor
branch cone, root-lattice BPS string walls, and compactification maps to
lower-dimensional protected data.

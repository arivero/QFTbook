# Chapter 11: Six-Dimensional Superconformal Theories

## Source Position

This chapter follows three-dimensional supersymmetric gauge theories by
introducing supersymmetric QFTs whose fixed points are often specified
through representation data, tensor branches, anomalies, strings, and
compactification tests rather than microscopic Lagrangians.  The current pass
addresses the six-dimensional part of issue #588.  A chapter-opening
construction/test architecture now separates the assumed fixed-point local
QFT, tensor-branch effective description, finite defect/global-form datum,
protected compactification tests, and the remaining construction frontier.

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
- `mathfrak T_{6d}[g]`: conditional six-dimensional `(2,0)` local QFT object
  satisfying the chapter's ADE defining-property hypothesis.
- `mathcal C_S=(C,{(p_a,D_a)},eta)`: class-`S` compactification datum:
  Riemann surface, marked points with codimension-two defect data, and twist
  sign.
- `mathfrak T_g[C,{(p_a,D_a)};eta]`: conditional four-dimensional
  class-`S` local QFT associated with the compactification datum.
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
- Adds Hypothesis `hyp:six-d-two-zero-ade-qft`, aggregating the defining
  properties of the assumed ADE `(2,0)` QFT: positive-energy
  `OSp(8^*|4)` representation, tensor-branch quotient, anomaly polynomial,
  BPS root-lattice strings, finite defect group, circle compactification, and
  conditional class-`S` compactification functoriality.
- Adds a construction/test architecture for the six-dimensional object:
  fixed-point local QFT data, tensor-branch EFT, finite defect/global-form
  polarization, protected circle and class-`S` compactification tests, and
  the final construction frontier are treated as distinct dependency layers.
- Records that a six-dimensional Yang-Mills coupling has negative mass
  dimension and therefore is not a marginal conformal coordinate; this is
  dimensional bookkeeping, not theorem-family content.
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
- Expands the quoted-theorem boundary by isolating the interacting excess
  `I_8[g]-r_g I_8(1)`, explaining that the branch free tensors supply only
  the `r_g I_8(1)` part, and deriving the simply laced positive-root
  second-moment identity and `d_g=r_g(h_g^vee+1)` arithmetic that make the
  Green-Schwarz tensor-index structure rigid once the long-root
  normalization is fixed.
- Displays and derives the ADE arithmetic of the `(2,0)` anomaly coefficient,
  including the `A_{N-1}` cubic scaling.
- Defines BPS string charges, tensions, and local inflow data, including
  root-lattice strings for `(2,0)` theories and the bulk inflow polynomial
  `I_4 = q_I i^* X_I^(4) + (1/2) q_I Omega^{IJ} q_J e(N_Sigma)`.
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
- Decomposes the finite flux system on \(S^1\times X_5\) as
  \(H^3(X_5;A_{\mathfrak g})\oplus\eta H^2(X_5;A_{\mathfrak g})\), derives
  the cross-pairing
  \(\int_{X_5}(b(v\smile u')-b(u\smile v'))\), and explains the resulting
  wrapped-line/unwrapped-surface polarization as the finite global-form datum
  of the five-dimensional compactification.
- Defines the finite absolute-polarization criterion after circle reduction:
  a maximal isotropic subgroup \(L_{X_5}=L_{X_5}^{\perp_\omega}\) selects the
  genuine finite-charge defects of that absolute theory, while charges outside
  \(L_{X_5}\) are relative/non-genuine because they fail to commute with some
  chosen genuine charge; polarization-changing interfaces are represented by
  Lagrangian relations in \(K\oplus\bar K\).
- Defines the five-dimensional instanton current
  \(j_{\rm inst}=*_5(8\pi^2)^{-1}\operatorname{tr}_{\rm top}F\wedge F\),
  its integral charge on spatial four-cycles, the trace-delta instanton
  particle energy bound, and the protected compactification normalization
  `g_5^2 = 4 pi^2 R` from BPST instanton mass and KK momentum.
- Derives the wrapped-string/W-boson mass matching and the scalar
  normalization `phi_5d = 2 pi R phi_6d`.
- Records compactification on Riemann surfaces as a test requiring twist,
  defect, anomaly, and descendant data.
- Adds Hypothesis `hyp:class-s-compactification-datum`, defining the
  conditional class-`S` object by the tuple
  `(C,{(p_a,D_a)},eta)` and the required four-dimensional QFT data, rather
  than using the phrase "class-S theory" as an undefined shorthand.
- Defines the smooth unpunctured class-\(S\) twist datum by decomposing
  \(SO(5)_R\) as \(SO(2)_r\oplus SO(3)_R\), setting
  \(e(N_2)=x+\eta t\), and pushing forward the six-dimensional anomaly
  polynomial to the four-dimensional six-form
  `I_6 = eta chi(C) x [ r_g (x^2-p+3u)/48 + d_g h_g^vee u/12 ]`.

## Calculation Checks

- `calculation-checks/susy_abjm_6d_checks.py` verifies the six-dimensional
  Yang-Mills coupling dimension, chiral two-form physical degrees of freedom,
  type `A_{N-1}`, `D_N`, and exceptional `(2,0)` rank/dimension/anomaly
  coefficient arithmetic, tensor-branch dimensions, the quadratic
  Green-Schwarz descent factor, the trace-delta five-dimensional
  instanton/Kaluza-Klein normalization, wrapped-string/W-boson scalar
  normalization, ADE defect-group orders from Cartan determinants, and the
  cyclic finite-flux polarization model.  It also checks the
  \(S^1\times X_5\) finite-flux cross-pairing signs, the finite commutant
  criterion for genuine versus relative defects in a chosen polarization,
  symplectic-graph interface relations, the simply laced
  root-system second-moment identities for the \(A\) and \(D\) series and the
  ADE relation \(d_{\mathfrak g}=r_{\mathfrak g}(h^\vee_{\mathfrak g}+1)\),
  as well as the class-\(S\) twist anomaly-pushforward coefficients.

## Proof Obligations And Boundaries

- The interacting `(2,0)` theory remains a non-Lagrangian object; the chapter
  now states a defining-property hypothesis for the assumed QFT and gives
  protected/effective consequences from that hypothesis, not a construction.
- Class-`S` theories are conditional four-dimensional local QFTs in this
  chapter.  The compactification datum and the resulting QFT assumptions are
  aggregated in `hyp:class-s-compactification-datum`; the Hitchin base,
  anomaly pushforward, and Seiberg-Witten curve data are protected
  consequences or tests, not standalone definitions of the QFT.
- The `(2,0)` anomaly polynomial is quoted theorem status because a
  first-principles construction of the interacting six-dimensional local QFT
  and its anomaly functional is not reproduced here.  External geometric or
  string-theoretic arguments can motivate the formula but are not used as
  foundations.
- Compactification to 5D maximally supersymmetric Yang-Mills is treated as a
  protected test/effective description, not as a definition of the parent
  six-dimensional local QFT.
- The construction/test architecture is now the governing map for the
  chapter: each derivation should be read as local representation theory,
  branch EFT, anomaly inflow, finite defect polarization, compactification
  comparison, or the still-open local-QFT construction problem.
- Future passes should add the full line/surface defect categories beyond the
  finite topological charge algebra, intrinsic anomaly computations for the
  two-dimensional theories supported on BPS strings, and punctured or
  irregular class-`S` anomaly reductions.

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
- 2026-05-30 anomaly-theorem boundary pass: expanded the local content around
  the `(2,0)` anomaly polynomial quoted theorem by identifying the interacting
  anomaly excess, deriving the root-system second-moment and dimension-count
  arithmetic used by tensor-branch Green-Schwarz matching, and extending the
  finite convention checks accordingly.
- 2026-05-30 class-\(S\) anomaly-pushforward pass: replaced the abstract
  compactification checklist by an explicit smooth unpunctured twist datum and
  anomaly-integration calculation, with the twist sign \(\eta\), surface Euler
  class \(t\), \(SO(2)_r\) Euler class \(x\), \(SO(3)_R\) Pontryagin class
  \(u\), and exact finite coefficient checks.
- 2026-05-30 BPS-string inflow pass: replaced placeholder support-theory
  anomaly language by a local derivation from the charged surface insertion,
  Green-Schwarz descent, global-angular-form regularization of the tubular
  neighborhood, and the normal-bundle Euler inflow coefficient.
- 2026-05-30 issue #700 defining-property pass: added explicit hypotheses for
  the ADE `(2,0)` QFT object and for class-`S` compactification data, rewrote
  the class-`S` Hitchin-base discussion to depend on those hypotheses, and
  changed the status ledger from a retrospective definition into a reference
  to the named conditional objects.
- 2026-06-01 instanton-current compactification pass: kept the old
  six-dimensional Yang-Mills coupling dimension check in remark form, added
  the five-dimensional instanton current and charge normalization, derived
  the trace-delta instanton-particle energy bound as the branch-EFT mechanism
  behind the \(g_5^2=4\pi^2R\) compactification test, and recorded that this
  still does not define the parent six-dimensional local QFT.
- 2026-06-01 circle finite-flux decomposition pass: expanded the finite
  defect-group section with the \(S^1\times X_5\) Kunneth splitting of
  \(H^3(-;A_{\mathfrak g})\), the sign derivation of the cross-pairing
  between \(H^3(X_5;A_{\mathfrak g})\) and \(H^2(X_5;A_{\mathfrak g})\), and
  the interpretation of the two isotropic halves as unwrapped surface defects
  and circle-wrapped line defects in the five-dimensional compactification.
- 2026-06-01 genuine-defect polarization pass: added the finite absolute
  polarization criterion \(L=L^\perp\), the Heisenberg commutator test for
  genuine versus relative/non-genuine finite defects, and the Lagrangian
  relation description of polarization-changing interfaces; extended the
  cyclic finite-algebra calculation check accordingly.
- 2026-06-03 issue #626/#701 architecture pass: added a front-loaded
  construction/test ladder so the six-dimensional chapter reads as a
  dependency chain rather than as separate protected-data cells.

## Figure Ledger

No figure is included in this pass.  Future figures should show a tensor
branch cone, root-lattice BPS string walls, and compactification maps to
lower-dimensional protected data.

# Volume II, Gauge Fixing, Ghosts, and BRST Cohomology Dossier

## Source Position

- Manuscript file:
  `monograph/tex/volumes/volume_ii/chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex`.
- Follows the construction of classical Yang--Mills theory and matter
  representations.
- Precedes QCD renormalization, chiral anomalies, global anomalies, and
  infrared gauge-theory structure.
- Role in the monograph: formulate gauge fixing as a local coordinate choice on
  gauge orbits, introduce the Faddeev--Popov determinant and ghosts, define the
  BRST differential, and identify the cohomological objects that control
  physical states, local operators, counterterms, and anomalies.

## Source And Reference Controls

- `SRC-QFT-PDF`: second-sequence handwritten material after the classical
  Yang--Mills construction; used for the local order of gauge fixing, ghost
  fields, and BRST.  The block pp. 169--181 was checked directly on
  2026-05-22 against rendered source images
  `/tmp/253b_169_181-169.png`--`/tmp/253b_169_181-181.png`.
- `SRC-EXTERNAL`:
  `references/sound_references/barnich_brandt_henneaux_local_brst_cohomology_hep-th_0002245.pdf`
  and text sidecar, especially Sections 2.3, 2.6, and 2.7.
- `SRC-EXTERNAL-GRIBOV`: Singer's 1978 theorem on the Gribov ambiguity and
  Gribov's original 1978 analysis, used to state the global obstruction to a
  smooth gauge slice and to define the first Gribov region/fundamental modular
  domain.
- `SRC-EXTERNAL-KUGO-OJIMA`: Kugo--Ojima's 1979 covariant operator formalism,
  lattice Landau-gauge tests by Nakajima--Furui, Kondo's Gribov--Zwanziger
  infrared analysis, and the 2023 lattice computation of the Kugo--Ojima
  correlation function.  These sources control the quartet terminology, the
  \(u(0)=-1\) condition, and the current status caveat.
- `SRC-EXTERNAL-KREIN`: Bognar's Krein-space monograph, Dollard--Friedman
  product-integration reference for operator evolutions, and
  Strocchi--Wightman/Strocchi indefinite-metric gauge-QFT references.  These
  sources control the fundamental decomposition, fundamental symmetry,
  Hilbert-majorant topology, Krein adjoint, and domain language used for the
  BRST charge.
- `SRC-EXTERNAL-DIMREG`: 't Hooft--Veltman's gauge-field dimensional
  regularization paper, the Breitenlohner--Maison treatment of
  \(\gamma_5\), Siegel's dimensional-reduction paper, and Stockinger's
  consistency/QAP analysis for DRED.  These sources control only the
  perturbative regularization machinery; the manuscript does not treat
  dimensional regularization as a nonperturbative field-space measure.
- The external source is used for the distinction between \(H(s)\) and
  \(H(s\mid d)\), for the contractible-pair/nonminimal-sector statement, and for
  the roles of ghost-number-zero and ghost-number-one local cohomology.
- The chapter does not reproduce the full antifield/BV computation of local
  BRST cohomology.  The following BV chapter develops the field-antifield
  framework for gauge-theory 1PI and Wilsonian effective actions, with
  Weinberg Volume II, the stringbook appendices, and standard BV literature
  treated as convention checks and source leads rather than as exposition to
  import.

## Framework

- Perturbative Yang--Mills theory on a fixed spacetime \(M\), in a local
  trivialization of the gauge bundle.
- Compact gauge group \(G\) with structure constants fixed by the preceding
  Yang--Mills chapter.
- Gauge potentials, infinitesimal gauge parameters, and ghosts are written in
  the Hermitian coordinate space
  \(\mathfrak g=i\,\mathfrak g_{\mathrm{ah}}\), with
  \([X,Y]_{\mathrm H}=-i[X,Y]\).
- Local gauge fixing around a field-space region where the Faddeev--Popov
  operator is transverse after separating residual zero modes.
- The Faddeev--Popov construction is formulated on the regular part of
  field space as a local principal-bundle quotient
  \(q:U\to U/\mathcal G_\Lambda\), with orbit measure induced from right Haar
  density and quotient density represented by
  \(\delta(F)|\det\mathcal M_F|\dd\mu_\Lambda\) on a section.
- The Faddeev--Popov path-integral formulae are local coordinate formulae on
  orbit space; they are not asserted to be a single global nonperturbative
  gauge fixing for nonabelian gauge theory.
- Off-shell nilpotent BRST differential using the Nakanishi--Lautrup field.
  The nilpotency proof assumes the Yang--Mills gauge generators close as vector
  fields on field space before imposing the Euler--Lagrange equations.
- Local cohomology is formulated in the algebra of finite jets of fields and
  ghosts.
- The canonical state space before BRST quotient is a Krein space
  \((\mathcal K,[\cdot,\cdot],J)\), not merely an algebraic indefinite
  inner-product space.  The fundamental symmetry \(J\) supplies the Hilbert
  majorant topology in which operator domains, closures, and adjoints are
  interpreted.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\mathcal A\) | affine space of local gauge potentials |
| \(\mathcal A_k(P)\) | Sobolev \(L^2_k\)-completed affine space of connections on \(P\) |
| \(\mathcal G\) | local gauge group |
| \(\mathcal G_{k+1}(P)\) | Sobolev-completed gauge group acting on \(\mathcal A_k(P)\) |
| \(\xi^\alpha\) | local coordinates on \(\mathcal G\), with \(\alpha=(a,x)\) in Yang--Mills theory |
| \(S_\alpha\) | vector field on field space generated by the infinitesimal gauge transformation \(\xi^\alpha\) |
| \(q:U\to B_U\) | local quotient map from a regular field-space chart to orbit space |
| \(\dd\mu_{\mathcal O_\phi}\) | orbit measure obtained by pushing right Haar density forward along \(\xi\mapsto\phi^\xi\) |
| \(\dd\nu_F\) | quotient density represented in the gauge section \(F=0\) |
| \(d_A,d_A^*\) | infinitesimal gauge action at a connection \(A\) and its \(L^2\)-adjoint |
| \(\mathcal S_A(\epsilon)\) | Coulomb local slice \(d_A^*(B-A)=0\) through an irreducible connection |
| \(F(A)\) | gauge-condition map |
| \(\mathcal M_F(A)\) | Faddeev--Popov operator |
| \(\Delta_F(A)\) | Faddeev--Popov determinant |
| \(\Omega_{\rm G}\) | first Gribov region in Landau gauge, \(\partial^\mu A_\mu=0\) and \(\mathcal M_L(A)\ge0\) after zero modes are removed |
| \(\Omega_{\rm G}^{\circ}\) | interior of the first Gribov region, where \(\mathcal M_L(A)\) is strictly positive on nonzero gauge directions |
| \(\mathfrak F\) | fundamental modular domain of absolute minima of \(\|A^g\|^2\) along gauge orbits |
| \(b_A\) | condensed-index antighost paired with \(F^A\), related to the conventional \(\bar c_A\) by \(b_A=\bar c_A\) in this chapter |
| \(c,\bar c\) | odd adjoint-valued ghost and independent antighost fields |
| \(B\) | Nakanishi--Lautrup auxiliary integration variable; Gaussian elimination removes it from the remaining gauge-fixed path integral |
| \(s\) | BRST differential |
| \(Q_B\) | BRST charge convention defined by \(\delta_B X=i\epsilon Q_B\cdot X\), so \(Q_B=-is\) classically |
| \(\Psi\) | gauge-fixing fermion |
| \(\mathcal F_{\mathrm{loc}}\) | algebra of local functions in finite jets |
| \(\Omega^p_{\mathrm{loc}}\) | local \(p\)-forms |
| \(d\) | spacetime exterior derivative |
| \(H^g(s)\) | local BRST cohomology at ghost number \(g\) |
| \(H^{g,D}(s\mid d)\) | BRST cohomology of local \(D\)-forms modulo \(d\) |
| \(Q\) | canonical BRST charge |
| \(\mathcal K\) | gauge-fixed Krein state space before BRST quotient |
| \([\cdot,\cdot]\) | indefinite Hermitian form on \(\mathcal K\) |
| \(J\) | fundamental symmetry determined by a decomposition \(\mathcal K=\mathcal K_+\oplus\mathcal K_-\) |
| \((\cdot,\cdot)_J\) | positive Hilbert majorant inner product \((\psi,\chi)_J=[\psi,J\chi]\) |
| \(T^\times\) | Krein adjoint of a densely defined operator \(T\) |
| \(\mathcal D\) | common dense invariant domain used for \(Q^2=0\), Krein symmetry, and field operations |
| \(\mathcal H_{\mathrm{phys}}\) | ghost-number-zero BRST cohomology of states |
| \(u(p^2)\) | transverse Kugo--Ojima function defined by the \((D_\mu c,g_{\mathrm{YM}}A_\nu\times\bar c)\) two-point function in Landau gauge |
| \(F_{\mathrm{KO}}(p^2)\) | convention \(F_{\mathrm{KO}}=-u\), so the original infrared criterion is \(F_{\mathrm{KO}}(0)=1\) |
| \(G_{\rm gh}(p^2)\) | Landau-gauge ghost dressing function in \(\langle c\bar c\rangle=G_{\rm gh}(p^2)/p^2\) |
| \(K^{a\mu},L^a\) | sources for nonlinear BRST variations, precursor to antifields |
| \(W[J,K,L]\) | connected generating functional with ordinary field sources \(J\) and BRST-variation sources \(K,L\) |
| \(J_{\Phi^A}\) | ordinary source conjugate to the field \(\Phi^A\), eliminated in the 1PI Legendre transform |
| \(\mathcal W_\alpha\) | Abelian Ward--Takahashi first-order operator used for comparison with the quadratic nonabelian Slavnov--Taylor identity |
| \(\mathcal B_X\) | linearized Slavnov operator at a functional \(X\) |
| \(\Delta_N=\int a_N\) | order-\(N\) local Slavnov--Taylor breaking in the all-order restoration proof |
| \(\Phi^*_A\) | BV antifield paired with a field \(\Phi^A\), deferred to the BV chapter |
| \(D=d-\epsilon\) | complex dimension parameter used in dimensional analytic regularization |
| \(I_G(D,\nu,p,m)\) | meromorphically continued scalar graph integral for graph \(G\) |
| \(\hat\eta,\hat\delta\) | continued metric and identity used for \(D\)-dimensional loop contractions, with \(\hat\delta^\mu{}_\mu=D\) |
| \(\eta_4,\tilde\eta\) | four-dimensional metric and evanescent complementary projector in DRED, \(\eta_4=\hat\eta+\tilde\eta\) |
| CDR | conventional dimensional regularization: loop momenta, unobserved momenta, polarizations, and gamma algebra continued to \(D\) |
| HV | 't Hooft--Veltman prescription: observed external states physical, unresolved/internal sectors continued |
| DRED | dimensional reduction: four-dimensional spin/gauge algebra with \(D\)-dimensional momentum contractions and evanescent scalar coordinates |
| FDH | four-dimensional helicity prescription for scattering amplitudes with scheme-dependent evanescent couplings |
| \(\gamma_5\) | chirality matrix whose dimensional-regulator algebra must be specified before chiral traces are manipulated |
| \(\epsilon^{\mu\nu\rho\sigma}\) | physical four-dimensional Levi-Civita tensor used in chiral and anomaly computations |

## Claims Established

- Gauge fixing is a local coordinate construction on gauge orbits.  The chapter
  now gives the formal normalization by
  \((\int_{\mathcal G}[D\xi]_{\rm H})^{-1}\), the right-Haar property, and the
  local Faddeev--Popov determinant identity before introducing ghosts.
- The chapter now displays the orbit-measure construction behind the identity:
  on a regular local quotient chart, the orbit measure is the Haar pushforward,
  \(\int_{\mathcal O_\phi}\delta(F)|\det\mathcal M_F|=1\) for a
  one-intersection transverse section, and
  \(\delta(F)|\det\mathcal M_F|\dd\mu_\Lambda\) represents the quotient measure
  when tested on gauge-invariant functions.  The oriented determinant used by
  ghosts is distinguished from the positive Euclidean density.
- The local meaning of a gauge slice is now made precise by a Sobolev
  Coulomb-slice theorem on irreducible connections: after stabilizer removal,
  \(d_A^*d_A\) is an elliptic invertible Faddeev--Popov operator on the gauge
  directions, and the inverse function theorem gives a Hilbert-manifold chart
  \(\mathcal S_A(\epsilon)\times\mathcal U_{\id}\to\mathcal A_k(P)\).
- Singer's theorem is stated in structural form: the irreducible-connection
  bundle over nonabelian gauge-orbit space is not globally trivial in the
  standard continuum setting, so no single smooth gauge condition supplies an
  everywhere transverse one-representative slice.  The chapter defines the
  first Gribov region, the Gribov horizon, and the fundamental modular domain,
  and states that perturbative Faddeev--Popov/BRST formulae are local near a
  chosen background.
- The chapter now derives the Landau-gauge Gribov-free regime from the orbit
  norm functional \(N_A(g)=\|A^g\|^2\): Landau gauge is the stationarity
  condition, the Hessian is \(2\mathcal M_L(A)\), the interior
  \(\Omega_{\rm G}^{\circ}\) is the infinitesimally transverse region, and the
  Gribov horizon is the failure locus of the local Faddeev--Popov chart.
- Ghosts represent the Faddeev--Popov determinant and carry fermionic statistics
  although they are Lorentz scalars; the determinant sign is fixed to match the
  \(s\Psi\) convention in the Minkowski weight, up to field-independent
  Grassmann-Gaussian normalization.  The \(b_A=-\bar c_A\) sign convention is
  explicit.
- The nonabelian covariant Faddeev--Popov operator
  \(\partial^\mu D_\mu^{ab}(A)\) depends on the gauge field.  This is the
  structural difference from the abelian Maxwell linear-gauge case, where the
  determinant is field-independent and ghosts decouple.  In Yang--Mills theory
  the \(A\)-dependent determinant is represented by dynamical ghost fields with
  local ghost-gluon interactions.
- The BRST differential is an odd ghost-number-one derivation with \(s^2=0\)
  for the off-shell closed Yang--Mills algebra; the chapter now derives
  nilpotency on general fields in condensed notation, on \(c\), on \(A_\mu\),
  and on matter fields from the Jacobi identity, the graded derivation rule,
  and the representation identity.
- The chapter explicitly separates this elementary Faddeev--Popov/BRST
  construction from gauge systems whose commutator closes only modulo the
  equations of motion; those require the BV field-antifield framework for an
  off-shell nilpotent differential.
- The gauge-fixing and ghost action is \(s\)-exact after introducing the
  Nakanishi--Lautrup field, equivalently
  \(S_{\rm GF}=-iQ_B\cdot(b_AF^A)\) in the \(Q_B\) convention.
- The Nakanishi--Lautrup field is now declared to be an integrated auxiliary
  variable, not an external source.  The manuscript writes the fixed-regulator
  Gaussian \(B\)-integral explicitly and shows that it produces the usual
  \(-(\partial A)^2/(2g_{\rm YM}^2\xi)\) covariant-gauge term, up to the
  field-independent normalization.
- Transition amplitudes between BRST-closed boundary states are independent of
  infinitesimal deformations of the gauge-fixing functional, assuming BRST
  invariance of the measure and no field-space boundary contribution.
- \(H^0(s;\mathcal F_{\mathrm{loc}})\) describes local gauge-invariant
  composite operators modulo BRST-exact representatives.
- \(H^{0,D}(s\mid d)\) controls local counterterm densities and
  \(H^{1,D}(s\mid d)\) controls candidate local anomalies.
- The nonminimal pair \((\bar c,B)\) is contractible and can be removed from
  cohomology under the standard perturbative regularity assumptions.
- Physical states are represented by ghost-number-zero cohomology of the
  canonical BRST charge when positivity of the quotient is established, with
  the exact-state equivalence \(|\Psi\rangle\sim|\Psi\rangle+Q|\chi\rangle\)
  included explicitly.
- The chapter now names the gauge-fixed state space as a Krein space and states
  the functional-analytic data needed before the BRST quotient: fundamental
  decomposition, fundamental symmetry \(J\), Hilbert majorant topology, Krein
  adjoint \(T^\times\), and a dense invariant BRST domain on which \(Q^2=0\)
  and \(Q\subset Q^\times\).
- The manuscript distinguishes Krein symmetry/self-adjointness of \(Q\) from
  Hilbert self-adjointness in a positive inner product, so the statement that
  \(Q\) is Hermitian in covariant gauge has a precise operator-theoretic
  meaning.
- The perturbative doublet argument is now separated from the Kugo--Ojima
  quartet mechanism.  A BRST quartet is defined as two conjugate doublets in
  the Krein space, and the manuscript states that perturbative
  longitudinal/timelike gauge modes and ghost/antighost modes form quartets
  mode by mode after the BRST charge and positive quotient are constructed.
- The nonperturbative Kugo--Ojima confinement criterion is stated as a
  conjectural Landau-gauge BRST scenario with explicit hypotheses: existence of
  the nonperturbative BRST charge and global color charges, unbroken BRST,
  absence of a massless boundary contribution from
  \(\partial^\nu F_{\mu\nu}^a\), and \(u(0)=-1\) without a compensating singular
  longitudinal remainder.
- The manuscript gives the conditional ghost-dressing relation
  \(G_{\rm gh}^{-1}=1+u+p^2v\) and records that lattice minimal-Landau-gauge
  and Gribov--Zwanziger infrared studies generally find finite ghost dressing
  and do not realize the original Kugo--Ojima condition.
- The Slavnov--Taylor sources \(K,L\) are identified as the elementary
  precursor of BV antifields; the dedicated BV chapter now develops the
  field-antifield framework for gauge-theory 1PI and Wilsonian effective
  actions.
- The manuscript now distinguishes Abelian Ward--Takahashi identities from
  nonabelian Slavnov--Taylor identities at the point where the latter are
  introduced.  An Abelian Ward identity is linear in the unknown 1PI
  functional because a fixed first-order field-space operator
  \(\mathcal W_\alpha\) annihilates \(\Gamma_{\rm inv}\).  The
  Slavnov--Taylor identity is quadratic in \(\Gamma\) after Legendre
  transformation because the composite BRST variations are represented by
  \(K,L\) derivatives while ordinary sources become field derivatives of
  \(\Gamma\).
- Dimensional regularization is defined as a perturbative meromorphic
  graph-distribution assignment, not as a literal noninteger-dimensional
  path-integral measure.  The manuscript separates scalar analytic
  continuation from the additional contraction algebra needed for tensors,
  spinors, gauge polarizations, and external-state kinematics.
- The chapter distinguishes CDR, HV, DRED, and FDH by their algebraic data.
  DRED is formulated with the projectors
  \(\eta_4=\hat\eta+\tilde\eta\), \(\hat\eta^\mu{}_\mu=D\), and
  \(\tilde\eta^\mu{}_\mu=4-D\), so evanescent scalar components and their
  couplings are part of the local coordinate system rather than optional
  decorations.
- The \(\gamma_5\) and Levi-Civita prescriptions are made explicit.  The
  manuscript states the obstruction to a universal cyclic, fully anticommuting
  \(D\)-dimensional \(\gamma_5\) prescription and directs the anomaly
  computation to the four-dimensional chiral data retained in the anomaly
  chapter.
- Proposition `prop:dimreg-st-control` states the order-by-order
  algebraic-renormalization control theorem needed here: pole parts of
  superficially divergent subgraphs are local functionals of fields, sources,
  and evanescent coordinates; the Slavnov--Taylor breaking is a local
  ghost-number-one cocycle; exact cocycles are removed by local counterterms,
  while nonzero cohomology classes are gauge anomalies.
- Theorem `thm:all-order-slavnov-taylor-restoration` states the all-order
  perturbative BRST renormalizability result with explicit hypotheses:
  compact semisimple gauge group, off-shell nilpotent classical BRST
  differential, power-counting renormalizable local coordinate set including
  evanescent variables, a subtraction scheme satisfying the quantum action
  principle, and vanishing local gauge-anomaly class in \(H^{1,D}(s_0\mid d)\).
  The proof is an induction on loop order: the order-\(N\) breaking
  \(\Delta_N\) is local, the Slavnov consistency identity makes it a
  \(\mathcal B_{S_0}\)-cocycle, the anomaly hypothesis writes it as
  \(s_0 b_N+d r_N\), and the local counterterm \(-\int b_N\) cancels it.
- The chapter explicitly separates regularization, renormalization, and
  operator-insertion regularization/source-coordinate choices for composite
  operators.

## Figure Requirements

- Figure 44.1 is a TikZ reconstruction of the handwritten gauge-slice figure:
  blue gauge orbits, a red slice \(F^A[\phi]=0\), representatives \(\phi\) and
  \(\phi^\xi\), and an arrow denoting motion along the gauge orbit.
- Render check: `/tmp/qft_brst_cert3-356.png` shows the figure in place between
  the gauge-condition paragraph and the Faddeev--Popov matrix definition.
- Figure `fig:gribov-region-fundamental-domain` displays the Landau surface,
  the first Gribov region, the Gribov horizon, the fundamental modular domain,
  and boundary gauge identifications.  It supports the distinction between a
  local Faddeev--Popov chart and a global gauge-fixed measure.

## Open Boundaries

- Full BV/antifield formalism is developed in the following compiled chapter.
  This BRST chapter remains the elementary gauge-fixed precursor.
- The chapter states the Gribov/Singer obstruction and its effect on the scope
  of Faddeev--Popov gauge fixing, but it does not construct a full
  nonperturbative gauge-fixed continuum measure on the fundamental modular
  domain.
- Positivity of the BRST quotient is stated as a required condition rather than
  proved in full generality.
- The existence of a nonperturbative Krein-space operator domain for
  interacting covariant-gauge Yang--Mills is stated as a construction problem;
  Slavnov--Taylor identities from a regularized path integral are separate
  formal consequences of the BRST symmetry.
- The Kugo--Ojima criterion is treated as a conditional covariant-gauge
  confinement scenario, not as a proved nonperturbative theorem for
  four-dimensional Yang--Mills theory.
- Dimensional regularization is used only as an order-by-order perturbative
  regulator of graph distributions.  The chapter does not claim a positive
  nonperturbative Hilbert space, a probability measure, or a continuum
  gauge-field measure at \(D\neq d\).
- 2026-05-24 issue #243 pass: added a dedicated Gribov/Singer block to the
  manuscript.  The chapter now labels the global obstruction, defines local
  slice versus global section, gives the first Gribov region and fundamental
  modular domain, and explicitly states that the path-integral formulae in the
  chapter are locally valid perturbative Faddeev--Popov coordinates.
- 2026-05-24 issue #244 pass: added the explicit abelian/nonabelian
  Faddeev--Popov contrast.  The manuscript now points back to the Maxwell
  linear-gauge determinant and states that nonabelian \(A\)-dependence is why
  ghosts are dynamical rather than a field-independent normalization.
- 2026-05-24 issue #245 pass: flagged the off-shell closure hypothesis in the
  BRST nilpotency proof and linked open/on-shell closure to the BV chapter.
- 2026-05-24 issue #246 pass: added the Kugo--Ojima quartet mechanism, the
  Landau-gauge Kugo--Ojima two-point function, the \(F_{\mathrm{KO}}(0)=1\)
  / \(u(0)=-1\) infrared condition, the conditional relation to ghost dressing,
  and the lattice/Gribov status statement.
- 2026-05-24 issue #247 pass: inserted a Krein-space foundations section for
  covariant gauge quantization and added the required functional-analytic
  symbols and domain assumptions to this dossier.
- 2026-05-24 issue #248 pass: added the linear Ward--Takahashi versus
  quadratic Slavnov--Taylor distinction to both the QED renormalization chapter
  and the BRST chapter, including the connected-to-1PI Legendre-transform
  mechanism that produces the product of \(\Gamma\)-derivatives.
- 2026-05-24 issue #502 pass: inserted a dimensional-regularization section
  before Slavnov--Taylor counterterms.  The pass defines dimensional
  regularization as meromorphic analytic regularization of graph
  distributions, distinguishes CDR/HV/DRED/FDH, records the \(\gamma_5\) and
  Levi-Civita scheme data, proves the locality/Slavnov--Taylor cohomology
  control statement, and separates regularization from renormalization and
  composite-operator source regularization.
- 2026-05-24 issue #263 pass: inserted the opening regulator-status remark.
  The chapter now states before the gauge-orbit construction that covariant
  BRST gauge fixing is perturbative/cohomological machinery whose
  nonperturbative comparison target is the lattice Yang--Mills continuum-limit
  hypothesis.
- 2026-05-24 issue #267 pass: added the all-order Slavnov--Taylor restoration
  theorem and induction proof, and recorded that global gauge anomalies remain
  outside the local \(H^{1,D}(s_0\mid d)\) obstruction.
- 2026-05-24 issue #312 pass: strengthened the Gribov/Singer discussion by
  adding a Sobolev Coulomb-slice local-chart theorem, deriving the Landau
  first Gribov region from the norm-functional Hessian, adding the
  Gribov/FMD figure, and making the abelian Maxwell contrast explicit.
- 2026-05-24 issue #320 pass: declared \(B\) to be an integrated
  Nakanishi--Lautrup auxiliary variable and added the explicit Gaussian
  elimination formula in the covariant-gauge path integral.

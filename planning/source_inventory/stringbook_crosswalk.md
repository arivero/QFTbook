# String Book Crosswalk

Source:

- `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`
- `/Users/xiyin/ED3-orbifold/references/stringbook-main/texsource/string notes.tex`

The string book is an adjacent high-value source. It may supply mature
appendix material, examples, convention checks, and source leads for any
QFT-relevant topic. It is not an import source in the ordinary textbook sense:
the QFT monograph must give an independent development, with its own order,
definitions, hypotheses, proofs, examples, and external reference boundaries.

The stringbook may inspire what to include and may help detect convention
conflicts. It must not determine the monograph's exposition, chapter sequence,
or theorem status.

Coverage directive: essentially all purely QFT content in the stringbook is
source-coverage material for the QFT monograph.  The material is not to be
copied or treated as authoritative prose; it must be rebuilt in the monograph
with independent definitions, hypotheses, derivations, convention checks, and
examples, and in most cases expanded far beyond its stringbook form.  When a
stringbook calculation is convention-sensitive, the monograph should either
include the calculation in full or supply a public calculation-check script
that verifies the finite algebra used in the derivation.

Current high-priority QFT blocks to absorb are:

- bosonic and fermionic path-integral constructions, including coherent-state
  Berezin integrals and the distinction between supergeometric field variables
  and Hilbert-space fermion operators;
- gauge fixing, BRST/BV, anomalies, and dimensional-reduction anomaly
  calculations, with all trace and gamma-matrix conventions checked against
  the monograph conventions;
- two-dimensional CFT: chiral stress-tensor Ward identities, Virasoro
  symmetry, BPZ/radial pairing, OPE convergence, modular/Riemann-surface
  structure, free fields, nonlinear sigma models, defects, orbifolds,
  twist-field deformations, boundary CFT, and superconformal symmetry;
- supersymmetry: spinor conventions, super-Poincare representation theory,
  the distinction between particle multiplets and off-shell field-variable
  multiplets, superspace, nonrenormalization arguments, and Wilsonian/BV
  scheme issues;
- planar integrability and large-\(N\) gauge-theory spectral problems,
  including the precise separation from relativistic factorized scattering;
- QFT aspects of strings, Wilson lines, flux tubes, confinement, branes as
  defects, and gauge/string large-\(N\) limits, only after their QFT
  assumptions have been stated without relying on a string-theory framework.

## Import Rules

For any string-book import, record:

- source section;
- object consulted;
- role: inspiration, convention check, source lead, example, or calculation to
  rederive;
- framework;
- definitions needed before use;
- theorem or formal status;
- notation changes;
- whether figures or diagrams are reused or redrawn;
- monograph chapter placement.

Do not reuse prose or rely on the string-theory context as the logical
setting. Rebuild the material as QFT: state the local quantum framework,
operator or path-integral status, symmetry algebra, representation category,
regularization, and analytic assumptions before using any
stringbook-motivated formula.

## Relevant Sections

### The Path Integral

Consulted source:

- `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`,
  section "The path integral", especially the subsections "Path integral
  formulation of quantum mechanics" and "Path integral with Grassmann-odd
  field variables".

Potential use:

- finite-dimensional time slicing;
- phase-space and configuration-space forms;
- measure dependence;
- Grassmann path integrals;
- bosonic trace as periodic Euclidean boundary condition;
- fermionic thermal trace as anti-periodic Euclidean boundary condition and
  supertrace as periodic fermionic boundary condition;
- semiclassical analysis;
- instantons, Borel summation, and Lefschetz thimbles.

Required checks:

- classify every integral by mathematical status;
- state regulators and contours;
- identify formal expansions.

Likely placement:

- Volume I path-integral chapters;
- Volume II perturbation and renormalization;
- advanced semiclassical appendices.

Current absorption:

- Volume I, Chapter 4 now includes the bosonic Euclidean trace and periodic
  boundary condition derivation.
- Volume I, Chapter 16 now includes the coherent-state completeness
  derivation, ordered finite-dimensional Berezin measure, fermionic thermal
  trace, anti-periodic boundary condition, and supertrace/periodic boundary
  condition.

### Path Integral Quantization Of Gauge Theories

Potential use:

- quotient by gauge redundancy;
- Faddeev--Popov procedure;
- BRST and BV;
- Wilsonian effective action with master-equation structure.

Required checks:

- define field space, gauge group, ghosts, antifields, and grading;
- distinguish redundancy from physical symmetry;
- state perturbative or finite-dimensional status.

Likely placement:

- Volume IV gauge fixing, Yang--Mills, QCD, and anomalies;
- a dedicated BV block in the gauge-theory volume, where antifields,
  antibrackets, master equations, and the BV forms of the 1PI and Wilsonian
  effective actions are developed systematically.

Current absorption:

- The issue #583 BV deepening pass expands the gauge-theory BV chapter with
  a finite-regulator infinitesimal exact-RG theorem, a local BV--BRST
  comparison theorem for Yang--Mills with matter, ghost-number-zero
  counterterm representatives, the ghost-number-one anomaly ledger, and the
  regulated local-observable/factorization-algebra boundary.
- The finite-dimensional BV/localization chapter now includes the compact
  \(S^2\) Atiyah--Bott fixed-point model in addition to BV Stokes,
  pushforward, normal Gaussian factors, and the Mathai--Quillen rank-one
  calculation.
- Companion checks now cover BV master-algebra signs, Yang--Mills ghost
  nilpotency, doublet contraction, BV localization algebra, and the
  \(S^2\) fixed-point coefficient identity.

### Local Quantum Field Theories

Potential use:

- local fields and microcausality;
- stress tensor;
- Wightman functions;
- Euclidean continuation;
- conformal symmetry;
- OPE intuition;
- Kontsevich--Segal-type comments.

Required checks:

- separate Hilbert-space, Euclidean, and categorical frameworks;
- treat point fields distributionally;
- state reconstruction or analytic-continuation hypotheses.

Likely placement:

- Volume I opening and correlation chapters;
- Volume IV framework comparison;
- Volume III/V CFT material.

Current absorption:

- Issue #599 added a dedicated Kontsevich--Segal functorial QFT chapter in
  `monograph/tex/volumes/volume_iv/chapter06_kontsevich_segal_functorial_qft.tex`,
  included in the Volume I foundations sequence after OS reconstruction.
- The chapter states Segal sewing, proves the K-S allowability angle
  criterion, defines the functorial bordism datum, relates K-S data to OS,
  Wightman, and local-net frameworks under explicit hypotheses, derives OPE
  from sewing under annular spectral/nuclear assumptions, and records the
  construction-status ledger.
- The finite algebra is checked by
  `calculation-checks/ks_allowability_checks.py`.

### Two-Dimensional CFT

Potential use:

- two-dimensional conventions;
- Virasoro algebra;
- state-operator correspondence;
- OPE and conformal blocks;
- modular considerations.
- bosonic and supersymmetric nonlinear sigma-model CFTs;
- finite orbifolds, discrete torsion, twist sectors, and twist-field
  deformations.

Required checks:

- define chiral versus full CFT data;
- state convergence and sewing assumptions when needed;
- separate local operator statements from categorical structures.

Likely placement:

- Volume III CFT chapters;
- Volume V vertex algebra and modular tensor category chapters.

Special boundary:

- two-dimensional CFT material must be developed from local QFT, radial
  quantization, chiral algebras, stress-tensor Ward identities, and sewing or
  modular hypotheses as needed;
- string worldsheet uses of CFT may suggest examples but cannot replace the
  QFT-side construction of chiral and full CFT data.
- all relevant two-dimensional CFT content in the stringbook appendices is a
  required source-coverage item for the QFT monograph; it must be rewritten
  with the monograph's definitions, hypotheses, and proof boundaries, not
  imported as string-theory background.

Current absorption:

- Volume III/Volume V, Chapter 5 now includes the chiral stress-tensor mode
  construction, Virasoro algebra proof, Schwarzian transformation, and
  plane-cylinder \(c/24\) shift.
- Volume V, Chapter 11 now starts the QFT-side development of bosonic and
  supersymmetric sigma-model CFTs, Narain lattice CFTs and toroidal sigma
  models, WZW/current-algebra/coset CFTs, finite orbifolds, twist sectors,
  cyclic and rotation twist weights, and twist-field deformations.  The
  NLSM renormalization pass now gives the covariant exponential background
  split, the source-coupled mean-zero 1PI effective-action convention, the
  pure-metric second variation and curvature vertex, the background-field
  one-loop Ricci divergence with the local heat-kernel pole and
  Ricci-counterterm normalization derived explicitly, the \(G,B,\Phi\)
  Weyl-anomaly package with full string-frame metric/dilaton variation and
  trace representative, scheme-redefinition geometry, torsionful one-loop
  packaging, the
  pure-metric two-loop representative, the precise RG-time conversion to
  Hamilton Ricci flow, and constant-curvature sphere/hyperbolic radius-flow
  checks.  The Narain pass
  rebuilds the stringbook lattice vertex-operator material with explicit
  locality, spin, cocycle, modular-anomaly, and \(O(d,d;\mathbb Z)\) moduli
  statements, together with a public calculation check for the cocycle and
  pairing algebra.  The WZW pass adds integral level quantization, affine
  current algebra, Sugawara stress tensors, integrable highest weights, coset
  stress tensors, the diagonal \(SU(2)\) minimal-model example, and the
  rank-one solvable cosets \(SU(2)_k/U(1)\) and
  \(SL(2,\mathbb R)_k/U(1)\), with the parafermion branching/field
  identification, fusion/modular data, and cigar momentum/winding and
  spectrum-status conventions stated before the gauged sigma-model
  geometries.  The monograph now also checks the bell and cigar
  one-loop Weyl-anomaly equations directly from the rotational curvature
  formulas.  The orbifold twist-field pass now derives the complex-boson
  rotation twist weight from the fractional oscillator normal-ordering
  constant.  The symmetric-product orbifold pass now includes the
  connected-torus-cover Hermite-normal-form count behind the Hecke transform
  and the constant-seed partition-number normalization test, together with a
  Riemann--Hurwitz monodromy ledger for the first twist-correlator covering
  checks and the beta-normalized local coordinate map for the primitive
  joining cover, plus the Schwarzian/OPE-power ledger and class-normalized
  group factor for the primitive joining channel, together with the normalized
  transposition join/split class-algebra factors.  The twist-deformation layer
  now derives the annular conformal-perturbation beta function and the
  contact-term scheme law instead of leaving exact marginality as a slogan.
  The public arithmetic check covers the central-charge,
  conformal-weight, field-identification, compact fusion, reflection-weight,
  integer-spin, and bell/cigar geometry formulas.
- Volume V, Chapter 12 now adds the algebraic chiral-CFT layer: vertex
  operator algebras, ordinary modules, characters, Zhu algebras and top-level
  module classification, unitary Virasoro minimal-model representation data,
  conformal blocks as Ward identity functionals, higher-genus sewing, modular
  tensor category data, the Verlinde formula, rational full-CFT modular
  invariants, torus one-point trace blocks, Verlinde topological defect lines,
  a leading Cardy high-temperature derivation, and logarithmic CFT
  boundaries.  The torus/defect layer states Zhu modular covariance with
  explicit hypotheses, proves the diagonal Verlinde defect fusion and
  temporal/spatial modular \(S\)-move, and works the Ising spin-flip and
  Kramers--Wannier defect examples.  The unitary minimal-model layer now
  includes the full A-series \(S,T\) modular data, the
  Kac-field-identification quotient normalization, and the finite
  \(SU(2)\)-quotient fusion rule.  The Ising minimal-model
  discussion now includes the level-two Virasoro Gram/null-vector calculation,
  the BPZ equation for the spin four-point function, and the crossing
  calculation fixing
  \(C_{\sigma\sigma\varepsilon}=1/2\), expanding the stringbook appendix
  discussion into a self-contained monograph derivation.  The Ising modular,
  defect-line, Zhu, logarithmic-cell, and unitary-minimal-model data are
  checked by `calculation-checks/cft_voa_modular_checks.py` and
  `calculation-checks/cft_virasoro_minimal_checks.py`.
- Volume V, Chapter 13 develops Liouville CFT from the QFT side: classical
  action and stress tensor, background charge and central charge, Seiberg
  domain, probabilistic construction boundary, reflection relation,
  continuous conformal-block decomposition, DOZZ theorem boundary, BPZ
  equations for both \(V_{-b/2}\) and \(V_{-1/(2b)}\), ordinary and dual
  one-screening coefficients, hypergeometric connection formulas,
  Virasoro block Gram-projector coefficients through level three, the
  elliptic nome interface to Zamolodchikov recursion, and boundary Liouville
  states with FZZT one-point functions and ZZ finite differences.  The finite
  convention algebra is checked by
  `calculation-checks/liouville_bpz_checks.py` and the Liouville boundary
  hyperbolic identities are checked by
  `calculation-checks/bcft_cardy_checks.py`.
- Volume V, Chapter 14 develops the 2D BCFT appendix material as a
  self-contained boundary-state theory: conformal boundary data, Ishibashi
  states, Cardy consistency, Cardy--Lewellen sewing hypotheses,
  compact-boson Neumann/Dirichlet states, Majorana/Ising boundary states,
  boundary-condition-changing OPE constants, direct-sum/Chan--Paton
  boundaries, and the nonrational Liouville FZZT/ZZ bridge.  The finite
  Cardy, Ising, compact-boson, Chan--Paton, and Liouville-boundary algebra is
  checked by `calculation-checks/bcft_cardy_checks.py`.
- Volume V, Chapter 15 now absorbs the chiral-algebra part of Appendix J:
  spin-sector data, NS/R mode conventions, \(\mathcal N=1\) and
  \(\mathcal N=2\) superconformal OPEs and mode algebras, the Ramond
  zero-mode shift, \(\mathcal N=2\) spectral flow, chiral-primary bounds,
  the extended \(\mathcal N=2\) spectral-flow operator layer with the
  charge-lattice/locality hypothesis, \(U(1)_R\) bosonization, integer and
  half-integer flow fields, and \(X^\pm/Y^\pm\) charge bookkeeping,
  elliptic-genus Ramond trace hypotheses, right-moving ground-state
  localization, spectral-flow/Jacobi covariance, protected
  Landau--Ginzburg central-charge and \(\chi_y\) charge-polynomial tests,
  and the supersymmetric rank-one coset interfaces for
  \(SU(2)_k/U(1)\) minimal models and the
  \(SL(2,\mathbb R)_k/U(1)\) cigar, including central charges, weights,
  \(R\)-charges, the compact \(A\)-series chiral ring, spectral-flowed
  labels, field identifications, compact \(\mathbb Z_k\) action, and cigar
  momentum/winding bookkeeping.
  It explicitly coordinates with the Volume VII supersymmetric-QFT lane for
  the actual LG/GLSM RG-flow, elliptic-genus realization theorem, and
  cigar/Liouville mirror-duality
  constructions.  The finite algebra is checked by
  `calculation-checks/superconformal_algebra_checks.py`.

### Two-Dimensional Supersymmetric Models

Current Appendix K absorption:

- Volume VI, Chapter 06 now absorbs the ordinary scalar Landau-Ginzburg part
  of Appendix K as a perturbed two-dimensional QFT interface: it defines the
  normal-ordered polynomial source chart, proves the local logarithmic
  collision integrability used by the perturbative expansion, derives the
  normal-ordered equation-of-motion relation, and records the finite
  order-field quotient for the even multicritical family.  The expected
  \(M(m,m+1)\) minimal-model endpoint is stated as an RG construction
  problem, not imported as a theorem from the polynomial algebra.
- Volume VII, Chapter 09 develops the Landau--Ginzburg, sigma-model, GLSM,
  and abelian mirror material as intrinsic two-dimensional QFT.  The current
  GLSM/mirror pass expands the stringbook Appendix K charged-chiral duality
  and cigar/Liouville material with a first-order `B_i` derivation, the
  twisted-linear constraint, Legendre elimination, the
  `-Q_i^a Sigma_a Y_i` integration-by-parts term, the vortex-exponential
  proof boundary, a proper-time derivation of the local Coulomb one-loop
  logarithm and its anomaly-completed holomorphic branch, exact elimination
  of the `Y_i` to recover the Coulomb one-loop twisted superpotential, the
  finite FI-coordinate shift, the logarithmic-torus mirror presentation,
  `P^{N-1}` critical-point simplicity, and the classical cigar quotient
  metric.
- The Appendix K Landau--Ginzburg nonrenormalization footnote is now
  rewritten as an explicit two-dimensional Wilsonian-coordinate argument:
  with chiral Wilsonian regularity, flavor spurion symmetries, and
  `R(W)=1`, regular holomorphic corrections to Fermat superpotentials are
  restricted to the original `g_i (Phi^i)^{d_i}` monomials.  The text states
  the regulator and infrared-existence boundaries rather than treating the
  selection rule as a standalone theorem about the continuum fixed point.
- The hypersurface chamber material from Appendix K is now expanded with
  the adjunction calculation `c1(TY_G)=(N-d)H|_{Y_G}`, the `d=N`
  Calabi-Yau condition, the sigma/LG central-charge matching condition, the
  residual `mu_d` finite-gauge action and untwisted invariant Jacobi-basis
  condition, and the anomaly-free Coulomb-coordinate singular signal.
- The monograph deliberately treats Hori--Vafa/Hori--Kapustin-style formulas
  as mechanisms to reconstruct rather than proof sources.  The remaining
  proof obligations are regulator-level construction of the vortex sectors,
  determinant normalizations, local operator maps, topological sectors, and
  equality of continuum Hilbert spaces/local algebras.
- Companion checks in `calculation-checks/susy_2d_lg_glsm_checks.py` now
  cover the finite algebra in the charged-dual elimination, FI shift,
  `P^{N-1}` critical ledger, cigar metric elimination, hypersurface
  adjunction/central-charge matching, residual finite-gauge invariant
  monomials, the Coulomb-coordinate signal, and the Fermat Wilsonian
  superpotential spurion-selection arithmetic.

### Planar Integrability

Current relativistic-integrability absorption:

- Volume VI now contains the algebraic/nested Bethe-ansatz infrastructure that
  the stringbook mostly used in the planar gauge-theory setting:
  RTT relations, transfer-matrix commutativity, the \(XXX_{1/2}\) algebraic
  Bethe ansatz, matrix Bethe--Yang quantization, \(SU(N)\) nested equations,
  an explicit \(SU(3)\) nested-root example, nested TBA, Baxter \(TQ\)
  relations, \(T\)-systems, \(Q\)-operators, and separation variables.  The
  finite algebra is checked by
  `calculation-checks/nested_bethe_ansatz_checks.py`.  The planar
  \(\mathcal N=4\) SYM development remains separate because its dispersion,
  cyclic-trace finite-size effects, and quantum spectral curve are different
  physical structures.

Current planar-integrability absorption:

- Volume VII now contains a dedicated planar \(\mathcal N=4\) SYM
  integrability spine: single-trace operators as cyclic spin chains, the
  one-loop `SU(2)` Heisenberg Hamiltonian and Konishi calculation, the
  centrally extended magnon dispersion relation, the all-loop asymptotic
  Bethe ansatz with scalar dressing phase and proof-boundary statement,
  mirror TBA and the T-hook Y-system, the QSC Pmu system and its
  weak-coupling Baxter limit, and the hexagon form-factor framework for
  three-point functions.  The finite algebra is checked by
  `calculation-checks/planar_n4_integrability_checks.py`.

Potential use:

- planar single-trace spectral problem in \(\mathcal N=4\) SYM;
- spin-chain realization of one-loop and asymptotic dilatation operators;
- centrally extended \(su(2|2)\) magnon representation theory;
- asymptotic Bethe ansatz, dressing phase, BES equation, cusp anomalous
  dimension;
- mirror TBA, wrapping corrections, Konishi, \(Y\)-system, and quantum spectral
  curve.

Required checks:

- define the large-\(N\) limit, operator sector, coupling scheme, and spectral
  problem before introducing spin-chain or worldsheet variables;
- distinguish planar gauge-theory integrability from relativistic
  two-dimensional factorized scattering in Volume VI;
- state which integrability inputs are theorem-level, perturbatively checked,
  symmetry-derived, or conjectural;
- reproduce convention-sensitive calculations with public calculation-check
  scripts, using the stringbook notebooks as source leads.

Likely placement:

- a later large-\(N\), gauge/string, or special-structure volume after the
  gauge-theory, supersymmetric, and CFT foundations are mature.

Special boundary:

- the two planar-integrability chapters in the stringbook are the internal
  source spine for the monograph's eventual planar-integrability treatment;
  the QFT monograph must deepen and expand them into a self-contained
  mathematical-physics development.

### Supersymmetry And Supergravity Appendices

Potential use:

- spinor and gamma-matrix convention checks;
- supersymmetry algebra and representation examples;
- superspace notation;
- component-field transformations;
- nonrenormalization and protected-quantity examples;
- supergravity only as a later comparison point, not as an early foundation for
  supersymmetric QFT.

Required checks:

- define the spacetime dimension, signature, spin group, reality condition, and
  R-symmetry before writing a supersymmetry algebra;
- distinguish algebraic representation theory from field-theoretic existence
  statements;
- derive component and superspace formulas in the QFT monograph's own
  conventions;
- state whether the discussion is off-shell, on-shell, perturbative, or
  nonperturbative;
- distinguish particle supermultiplets as Hilbert-space representations from
  off-shell field-variable multiplets as superfield or component-coordinate
  packages;
- for \(4D\) \(\mathcal N=1\) and \(\mathcal N=2\) gauge dynamics, define the
  supersymmetric Wilsonian scheme before importing holomorphy, exact
  superpotential, quantum-moduli-space, Seiberg-Witten, or duality arguments;
- separate supersymmetric QFT from string compactification or worldsheet
  motivation.

Likely placement:

- Volume VII supersymmetric QFT;
- later topological/cohomological volume for twists;
- advanced special-topic volumes for superconformal theories and protected
  sectors.

### Symmetries, Defects, And Orbifolds

Potential use:

- topological defect lines;
- non-invertible symmetries;
- orbifolds;
- anomaly and discrete torsion data.

Required checks:

- define defects as operators, interfaces, or categorical objects depending on
  framework;
- state codimension and locality properties;
- identify topological versus dynamical assumptions.

Likely placement:

- Volume V generalized symmetries and defects.

### Anomalies

Potential use:

- axial anomalies;
- gauge anomalies;
- contact-term viewpoint;
- anomaly polynomials and descent;
- inflow.

Required checks:

- define background fields and gauging problem;
- distinguish current nonconservation, obstruction to gauging, and anomaly
  inflow;
- state perturbative, topological, or cohomological framework.

Likely placement:

- Volume II anomalies;
- Volume V advanced anomaly structures.

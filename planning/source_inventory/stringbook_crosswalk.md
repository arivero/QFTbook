# String Book Crosswalk

Source:

- `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`

The string book is an adjacent high-value source. It may supply mature
appendix material, examples, convention checks, and source leads for any
QFT-relevant topic. It is not an import source in the ordinary textbook sense:
the QFT monograph must give an independent development, with its own order,
definitions, hypotheses, proofs, examples, and external reference boundaries.

The stringbook may inspire what to include and may help detect convention
conflicts. It must not determine the monograph's exposition, chapter sequence,
or theorem status.

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

### Two-Dimensional CFT

Potential use:

- two-dimensional conventions;
- Virasoro algebra;
- state-operator correspondence;
- OPE and conformal blocks;
- modular considerations.

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

### Planar Integrability

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

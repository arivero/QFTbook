# Master Architecture

## Governing Constraint

The architecture follows the logical construction of local quantum field
theory.  The source lecture-note order controls the core sequence, but the
monograph is organized by subject matter rather than by semester or course
division.  Volume boundaries mark conceptual domains of QFT.

The spine is:

1. nonperturbative local quantum data, states, observables, spectrum, and
   fields as distributional coordinates;
2. Euclidean, Wightman, and algebraic comparison frameworks introduced from
   the beginning with their hypotheses stated locally;
3. path-integral constructions for Green functions;
4. Kallen--Lehmann spectral representation and particle content;
5. perturbative Green functions as a calculus for correlators;
6. nonperturbative asymptotic states and the S-matrix;
7. LSZ reduction;
8. perturbative scattering amplitudes only after LSZ;
9. renormalization, effective field theory, and critical phenomena;
10. gauge theory, infrared structure, anomalies, and symmetry breaking;
11. detailed studies of QFTs with special structures;
12. thermal, constructive, lattice, curved-background, and global-structure
    extensions.

## Global Rules

- QFT is presented nonperturbatively from the beginning.
- Existing frameworks such as Wightman, Osterwalder--Schrader, AQFT,
  constructive, perturbative algebraic, factorization, and functorial
  approaches are used as framework-specific theorem sources and comparison
  structures.  No single one is treated as the final foundation of the whole
  subject.
- Kallen--Lehmann spectral representation appears early in the foundational
  construction.
- Feynman diagrams for Green functions may appear before scattering.
- The S-matrix is first defined nonperturbatively.
- LSZ follows the nonperturbative S-matrix.
- Feynman diagrams for S-matrix elements appear only after LSZ.
- Every volume may include mathematical interludes, but an interlude must
  serve the local construction in that volume.
- Advanced subjects are compiled only when their foundations have been
  developed, not as topical surveys.

## Volume I: Foundations Of Local Quantum Field Theory

Purpose: establish QFT as local quantum data before perturbation theory.
This volume introduces the principal nonperturbative frameworks, fields as
operator-valued distributions, local algebras, Euclidean reconstruction,
regulated path integrals, spectral representations, and perturbative Green
functions as a controlled expansion of correlators.

Current compiled material:

1. Starting Data For Local Quantum Field Theory
2. Wightman Fields And Reconstruction
3. Algebraic QFT: Local Nets And States
4. Superselection Sectors And Locality Properties
5. Relativistic Quantum Mechanics And Local Operator Structure
6. Local Fields, Covariance, And Microcausality
7. Lagrangian Formalism And Quantum-Mechanical Path Integrals
8. Correlation Functions, Wick Rotation, And Gaussian Integrals
9. Relativistic Scalar Fields And Canonical Quantization
10. Symmetries, Noether Theorem, And Stress Tensors
11. Scalar Path Integrals And Euclidean Green Functions
12. Osterwalder--Schrader Reconstruction
13. Kontsevich--Segal Functorial Quantum Field Theory
14. Kallen--Lehmann Spectral Representation And Particle Content
15. Perturbative Green Functions And Feynman Graphs
16. Lorentzian Green Functions And Analytic Continuation

Further development targets:

- sharpen the relation between local nets and field coordinatizations;
- expand reconstruction hypotheses with clear domains of validity;
- deepen spectral theory before scattering;
- add rigorous examples where the full set of hypotheses is known.
- keep entanglement in QFT, if developed, in the AQFT/local-algebraic
  framework: von Neumann algebras, modular theory, split property,
  relative entropy, and type-III issues must precede any use of entropy or
  replica language.

## Volume II: Particles, Scattering, And Analyticity

Purpose: define particles and scattering nonperturbatively before
perturbative amplitudes.  This volume treats isolated mass shells,
Haag--Ruelle wave operators, LSZ, cross sections, spin and helicity,
bound states, resonances, and analyticity.

Current compiled material:

1. Haag--Ruelle Scattering Theory
2. LSZ Reduction And The S-Matrix
3. Cross Sections, Partial Waves, And Unitarity
4. Massive Particles With Spin
5. Massless Particles, Helicity, And Gauge Redundancy
6. Haag--Ruelle Theory And Mathematical Scattering
7. Local QFT, Spectral Data, And Path Integrals Revisited
8. The S-Matrix And LSZ Revisited
9. Bound States From Exchange Amplitudes
10. Unstable Particles, Self-Energies, And Resonances
11. Composite Bound States And Bethe--Salpeter Amplitudes
12. Analyticity, Crossing, And Landau Singularities
13. Partial Waves, Dispersion Relations, And High-Energy Bounds

Further development targets:

- align the two Haag--Ruelle chapters into one layered treatment;
- deepen the precise hypotheses behind LSZ;
- expand massless scattering and infrared limits without moving QED material
  out of its gauge-theory volume;
- separate analytic theorems from perturbative illustrations.

## Volume III: Renormalization, Effective Field Theory, And Critical Phenomena

Purpose: develop renormalization as local continuum structure and scale
dependence, rather than as a bookkeeping device.  This volume includes 1PI
generating functionals, local counterterms, BPHZ forests, renormalized
operators, RG, Wilsonian EFT, and critical scaling.

Current compiled material:

1. Generating Functionals And The One-Particle-Irreducible Effective Action
2. Renormalizability And Local Counterterms
3. Subdivergences And BPHZ Subtractions
4. The 1PI Renormalization Group
5. Renormalized Operators And Minimal Subtraction
6. Stress Tensor Trace, Scale Invariance, And Conformal Currents
7. Wilsonian Effective Field Theory
8. The Wilson--Fisher Fixed Point And Scaling Operators
9. The Statistical Ising Model And Universality
10. Effective Field Theories Without Poincare-Invariant UV Completion

Further development targets:

- deepen the new BPHZ--Wilsonian--1PI bridge with worked examples;
- use the source-dependent Wilsonian/operator insertion bridge, now including
  multi-insertion contact-term coordinates, to tighten the transition from
  universality correlators to fixed-point and CFT data;
- propagate the explicit one-loop BPHZ--Wilsonian--1PI matching calculation
  into later operator and observable examples where it clarifies coordinate
  changes;
- mark where these constructions are ordinary-field constructions and where
  gauge-theory 1PI/Wilsonian effective actions require the BV master
  framework developed in the gauge-theory volume or a finite lattice
  gauge-theory construction with gauge-invariant blocking maps;
- deepen operator mixing and anomalous dimensions;
- deepen the worked connection between finite-cutoff universality,
  renormalized composite operators, and observable correlation functions;
- prepare the logical bridge to the CFT volume.

## Volume IV: Gauge Theory, Infrared Structure, And Anomalies

Purpose: develop gauge theory as local quantum physics with constraints,
redundant representatives, BRST organization, infrared sectors, anomalies,
and physical observables.  The BV formalism belongs to this volume as the
homological framework for gauge-theory 1PI effective actions, Wilsonian
effective actions, gauge fixing, and renormalization identities; the lattice
gauge construction is the companion finite-cutoff framework with exact gauge
invariance and compact group integrals.

Current compiled material:

1. Spinor Fields, Fermionic Statistics, And Grassmann Path Integrals
2. Maxwell Theory, Constraints, And Gauge Fixing
3. Quantum Electrodynamics And External States
4. QED Renormalization And Electromagnetic Form Factors
5. Infrared Divergences And Inclusive QED
6. Yang--Mills Theory And Matter Fields
7. Lattice Yang--Mills As A Nonperturbative Definition
8. Gauge Fixing, Ghosts, And BRST Cohomology
9. The BV Master Formalism For Gauge Effective Actions
10. QCD Renormalization, Asymptotic Freedom, And Deep Inelastic Scattering
11. Jets, Infrared-Safe Observables, And Hadronization
12. Chiral And Axial Anomalies
13. Schwinger Model And Two-Dimensional QED
14. Large-\(N\) Two-Dimensional QCD And The Light-Front Bound-State Equation
15. The Standard Model As A Hybrid Quantum Field Theory
16. Global Anomalies, Spontaneous Symmetry Breaking, And Pions

Further development targets:

- place all gauge-representative statements in relation to observable data;
- develop detector observables, especially energy correlators, as
  stress-tensor-defined color-singlet observables before discussing partonic
  approximations, jet algorithms, or hadronization models;
- treat jet definitions through IRC-safe measurement functions, controlled
  fixed-order/resummed approximations, and explicitly stated nonperturbative
  inputs for fragmentation and hadronization;
- expand nonabelian BRST and gauge-invariant operator construction;
- deepen the BV development for reducible gauge symmetries, open algebras,
  exact RG implementations, and global BV integration-cycle issues;
- deepen confinement, global form, theta-angle, and anomaly-inflow material;
- prepare the later global-structure and TQFT volumes.

## Volume V: Conformal Field Theory

Purpose: develop core CFT as a special class of local QFTs governed by
fixed-point, operator, representation-theoretic, and OPE data.

Current compiled material:

1. Fixed Points And Conformal Data
2. Conformal Killing Vectors And The Conformal Group
3. Stress Tensor Weyl Structure And Improvement
4. Radial Quantization And State-Operator Correspondence
5. Conformal Charges And Ward Identities
6. Primary Operators And Finite Transformations
7. Unitarity Bounds And Short Multiplets
8. Correlation Functions And Conformal Frames
9. Operator Product Expansion
10. Light-Ray Operators And Energy Correlators
11. Two-Dimensional Sigma Models, Orbifolds, And Twist Fields
12. Vertex Operator Algebras, Modular Sewing, And Logarithmic CFT
13. Liouville Conformal Field Theory
14. Boundary Conformal Field Theory
15. Two-Dimensional Superconformal Algebras

Further development targets:

- keep the core CFT volume focused on local operator structure;
- develop modern two-dimensional CFT inside Volume V, not as an afterthought:
  chiral and full CFT data, Virasoro and affine current algebras,
  highest-weight and non-highest-weight representations, BPZ and null-vector
  technology, OPE convergence and sewing, modular covariance and invariance,
  rational and non-rational examples, and the relevant stringbook appendix
  material rewritten as self-contained QFT;
- keep entanglement-entropy and replica material out of the compiled core CFT
  spine.  If such material is later developed, its natural home is an
  AQFT/local-algebraic treatment where algebraic factorization, type-III
  behavior, modular theory, relative entropy, regulator dependence, and any
  replica analytic continuation are all part of the stated object;
- treat light-ray and energy-detector observables as the first nonlocal CFT
  observables in the compiled CFT volume, with the null-integral hypotheses,
  contact terms, and conformal-collider positivity conditions stated at the
  point of use;
- use the source-functional Ward-identity conventions from the opening
  chapter when deriving conformal currents, charges, and primary
  transformation laws; the charge chapter now uses these conventions for
  local current Ward identities, and the primary chapter now uses them for
  spin-source contact terms and finite transformation laws;
- use radial reflection positivity and \(P_\mu^\dagger=K_\mu\) as the source
  of unitarity bounds; the short-multiplet chapter now derives the
  symmetric-traceless spin bounds from first-level Casimir eigenvalues;
- develop crossing equations only through convergent OPE and Hilbert-space
  radial quantization;
- reserve supersymmetric, non-conformal integrable, topological, holographic,
  and planar-integrable special structures for their own volumes or later
  subject-specific parts.

Source protocol:

- Xi's QFT lecture notes set the logical CFT spine.
- Stringbook appendices may be consulted for two-dimensional CFT conventions,
  examples, and source leads, but the CFT volume must be written as a new
  comprehensive QFT treatment.
- All two-dimensional CFT material in the stringbook appendices is a required
  coverage source for Volume V: it must be absorbed, corrected where needed,
  and deepened in the monograph with explicit representation-theoretic and
  analytic hypotheses.
- Every theorem-level CFT claim needs either a derivation in the monograph or an
  external reference with hypotheses recorded in the chapter dossier.

## Volume VI: Integrable Quantum Field Theory

Purpose: relativistic two-dimensional QFTs whose exact dynamics are controlled
by infinitely many conserved quantities, factorized scattering, form-factor
bootstrap, thermodynamic Bethe ansatz, and exact finite-volume or RG-flow
data.  The volume treats integrability as a structure of local two-dimensional
QFT, not as a generic synonym for solvability.

Current compiled material:

1. Factorized Scattering And Integrability
2. Two-Dimensional Scattering Analyticity And Bootstrap Data
3. Yang--Baxter Consistency And Internal Symmetry
4. Algebraic Bethe Ansatz And Transfer Matrices
5. Nested Bethe Ansatz And Matrix Bethe--Yang Equations
6. Form-Factor Bootstrap And Local Operators
7. Thermodynamic Bethe Ansatz
8. Nested TBA, Baxter Relations, And Separation Variables
9. Integrable RG Flows And Perturbed Two-Dimensional CFT
10. Mirror-Channel TBA And Finite-Size Effects
11. Sine-Gordon, Massive Thirring, And Affine Toda Theories
12. \(O(N)\), Gross--Neveu, And Integrable Sigma-Model Families
13. Bridges To Nonintegrable Two-Dimensional QFT And CFT
14. Finite-Volume Form Factors And Spectral Expansions

Further development targets:

1. Conservation Laws And Factorization
2. Two-Dimensional Scattering Analyticity And Bootstrap Data
3. Yang--Baxter Equation And Internal-Symmetry Representation Theory
4. Form-Factor Bootstrap And Local Operators
5. Thermodynamic Bethe Ansatz And Exact Ground-State Energies
6. Integrable RG Flows And Perturbed Two-Dimensional CFT
7. Mirror-Channel TBA, Finite-Size Effects, And Wrapping Corrections
8. Sine-Gordon, Massive Thirring, And Affine Toda Theories
9. \(O(N)\), Gross--Neveu, And Integrable Sigma-Model Families
10. Bridges To Nonintegrable Two-Dimensional QFT And To Two-Dimensional CFT
11. Finite-Volume Form Factors And Spectral Expansions

Planar integrability is not a main topic of this volume.  It should be
introduced here only to compare objects and conventions: relativistic
two-dimensional factorized scattering data are not the same mathematical
object as the spin-chain/worldsheet spectral problem of a large-\(N\) gauge
theory.  A substantial treatment of planar \(N=4\) SYM, spin chains,
worldsheet integrability, and gauge/string spectral problems belongs in a
later large-\(N\), gauge-string, or special-structure volume after the relevant
gauge-theory and supersymmetric foundations have been developed.

## Volume VII: Supersymmetric Quantum Field Theory

Purpose: QFTs with supersymmetry developed after gauge theory and CFT
foundations.

Current compiled material:

1. Supersymmetry Algebras And Representations
2. Superspace, Superfields, And Local Actions
3. Supersymmetric Gauge Theory
4. Supersymmetric Wilsonian Schemes And Exact Dynamics
5. Nonrenormalization And Holomorphy
6. Four-Dimensional \(\mathcal N=1\) Gauge Dynamics
7. Four-Dimensional \(\mathcal N=2\) Gauge Dynamics And Seiberg-Witten Theory
8. Spectral Bridges Among Supersymmetric Yang--Mills Cousins
9. Moduli Spaces In Supersymmetric Quantum Field Theory
10. Two-Dimensional Landau--Ginzburg, Sigma-Model, And Calabi--Yau Theories
11. Three-Dimensional Chern--Simons--Matter Theories
12. Six-Dimensional Superconformal Theories
13. Planar \(\mathcal N=4\) Supersymmetric Yang--Mills As A Spectral Problem
14. All-Loop Asymptotic Bethe Ansatz
15. Mirror TBA And The Y-System
16. Quantum Spectral Curve And Hexagon Form Factors
17. Supersymmetric Localization On Compact Manifolds

Further development targets:

1. Supersymmetry Algebras And Representations
2. Multiplets And Superspace
3. Supersymmetric Gauge Theory
4. Supersymmetric Wilsonian Schemes And Exact Dynamics
5. Nonrenormalization And Holomorphy
6. Four-Dimensional \(\mathcal N=1\) Gauge Dynamics
7. Four-Dimensional \(\mathcal N=2\) Gauge Dynamics And Seiberg-Witten Theory
8. Moduli Spaces
9. Two-Dimensional Landau-Ginzburg, Sigma-Model, And Calabi-Yau Theories
10. Three-Dimensional Chern-Simons-Matter Theories
11. Six-Dimensional Superconformal Theories
12. Superconformal Field Theories
13. Protected Sectors
14. Supersymmetric Localization With Regulated Localization Data
15. Supersymmetric Regularization And Anomalies

Source protocol:

- The volume must begin from supersymmetry algebras, spin representation
  theory, state spaces, fields, multiplets, and local dynamics as QFT objects.
- It must keep particle supermultiplets separate from off-shell field-variable
  multiplets.  Particle multiplets are Hilbert-space representations
  constrained by positivity, mass, spin/helicity, and central charges.
  Off-shell superfields are local coordinate packages with auxiliary fields
  and possible gauge redundancy.  Any map between the two is derived only
  after dynamics, constraints, quotienting, and quantization or reconstruction.
- Four-dimensional \(\mathcal N=1\) and \(\mathcal N=2\) gauge dynamics are
  central targets.  Holomorphy, exact superpotentials, quantum moduli spaces,
  anomaly matching, Seiberg-Witten curves, and duality claims must be
  formulated in explicitly defined supersymmetric Wilsonian schemes before
  they are used as physics.  Existing Seiberg-style arguments are source
  leads, not substitutes for scheme definitions and derivations.
- The volume must separate supersymmetric Wilsonian integration from
  supersymmetric regularization.  BV with off-shell superfields is the natural
  framework for the symmetry and coarse-graining problem once a regulator is
  given, but the existence of a fully satisfactory manifestly supersymmetric
  regulator for four-dimensional gauge theories is not assumed.  Dimensional
  reduction, higher-covariant-derivative heat-kernel schemes, and
  Pauli--Villars-type completions must be treated as schemes whose precise
  regulated Ward identities, algebraic consistency, decoupling, and anomaly
  classes require verification.
- Supersymmetric examples in other dimensions must be developed as QFTs in
  their own ambient categories, not as informal analogues of four-dimensional
  theories.  Two-dimensional Landau--Ginzburg, Calabi--Yau sigma-model, and
  GLSM examples require explicit UV data, RG assumptions, chiral-ring and
  infrared-CFT statements, and sigma-model control.  Three-dimensional
  Chern--Simons--matter examples require level quantization, parity-anomaly
  and framing data, monopole-operator definitions, and boundary/global-form
  choices.  Six-dimensional superconformal examples require a non-Lagrangian
  status ledger, tensor-branch effective theory, anomaly polynomial, BPS
  strings, compactification tests, and extended-operator data.
- Localization belongs later in the supersymmetry volume after the Wilsonian,
  gauge, and cohomological foundations.  A localization chapter must begin
  from a regulated localization datum: integration space or cycle, odd
  symmetry \(Q\), \(Q^2\), \(Q\)-exact deformation, convergence and boundary
  behavior, fixed-locus normal complex, zero modes, singular strata, and
  contour or residue prescription.  Jeffrey--Kirwan residues, noncompact
  Coulomb directions, and zero-size instantons must be derived from or
  explicitly built into this datum.
- Stringbook appendices and verification codes may be used for convention
  checks and examples, but the development must be independent rather than an
  adaptation of string-theory support material.
- Supergravity, compactification, branes, holography, and localization may
  enter only after the necessary supersymmetric QFT foundations have been
  built.

## Volume VIII: Topological And Cohomological Quantum Field Theory

Purpose: metric-independent and cohomological QFTs, developed from local QFT,
gauge theory, anomalies, and later supersymmetric twists.

Current compiled material:

1. Metric Independence And Cohomological Observables
2. Bordism Functoriality And Extended Topological Field Theory
3. BF Theory
4. Chern--Simons Theory
5. Cohomological Field Theories
6. Topological Sigma Models
7. Twists Of Supersymmetric Theories
8. Witten--Donaldson Theory And The Seiberg-Witten Comparison
9. Boundaries, Defects, And Categories
10. BV Integration And Finite-Dimensional Localization
11. Finite Gauge Theory And State-Sum TQFT

Further development targets:

1. Topological Invariance In Local QFT
2. Atiyah--Segal And Extended TQFT Frameworks
3. BF Theory
4. Chern--Simons Theory
5. Cohomological Field Theories
6. Topological Sigma Models
7. Twists Of Supersymmetric Theories
8. Witten--Donaldson Theory And The Donaldson/Seiberg-Witten Comparison
9. Boundaries, Defects, And Categories
10. BV Integration And Finite-Dimensional Localization
11. Finite Gauge Theory And State-Sum TQFT

Source protocol:

- Witten--Donaldson theory is a central four-dimensional cohomological gauge
  theory target.  The volume must define the Donaldson side through the
  twisted \(\mathcal N=2\) Yang--Mills/cohomological gauge-theory path
  integral, instanton moduli-space compactification, orientation data,
  observables, and metric-dependence boundary terms.
- The relation to the Seiberg--Witten monopole equations must be treated as an
  RG comparison problem, not as an unexplained equality of invariants.  The
  argument must state the ultraviolet \(\mathcal N=2\) gauge theory, the
  topological twist, the Coulomb-branch Wilsonian effective action, singular
  loci, monopole/dyon light fields, Abelian low-energy EFT, contact terms,
  \(u\)-plane or wall-crossing contributions when relevant, and the precise
  observable map.
- The mathematical gap ledger must identify which parts are rigorous
  differential geometry of moduli spaces, which parts are finite-dimensional
  localization or gluing, which parts rely on physical RG assumptions, and what
  remains to be proved to turn the Seiberg--Witten explanation of Donaldson
  invariants into a theorem-level QFT derivation.

## Volume IX: Global Structure, Phases, And Extended Operators

Purpose: symmetry and phase structure beyond local order parameters.

Current compiled material:

1. Global Forms And Higher-Form Symmetry
2. Extended Operators And Topological Defects
3. Line, Surface, And Domain-Wall Operators
4. Confinement, Screening, And Oblique Confinement
5. Discrete Theta Terms
6. Anomaly Inflow And Invertible Field Theories
7. Phases Of Gauge Theories
8. Boundaries And Defects
9. Categorical Symmetry And Defect Fusion
10. Duality Defects, Gauging, And Orbifold Data
11. Higher-Group Symmetry And Symmetry TQFT

Further development targets:

1. Global Forms Of Symmetry Groups
2. Higher-Form And Categorical Symmetries
3. Line, Surface, And Domain-Wall Operators
4. Confinement, Screening, And Oblique Confinement
5. Discrete Theta Terms
6. Anomaly Inflow And Invertible Field Theories
7. Phases Of Gauge Theories
8. Boundaries And Defects
9. Categorical Symmetry And Defect Fusion
10. Duality Defects, Gauging, And Orbifold Data
11. Higher-Group Symmetry And Symmetry TQFT

## Volume X: Thermal Quantum Field Theory, Hydrodynamics, And Nonequilibrium Dynamics

Purpose: QFT at nonzero temperature, real-time response, transport, and
hydrodynamics as the long-distance effective theory of conserved densities.
This volume develops equilibrium from the KMS condition, then derives the
correlator input for transport before introducing hydrodynamic effective
actions and nonequilibrium limits.

Current compiled material:

1. KMS States And Thermal Correlators
2. Finite-Temperature Path Integrals
3. Real-Time Schwinger--Keldysh Formalism
4. Spectral Functions, Kubo Formulae, And Transport
5. Hydrodynamics From Ward Identities
6. Schwinger--Keldysh Hydrodynamic Effective Actions
7. Thermal Gauge Theory And Screening
8. Kinetic Theory As A Controlled Limit
9. Anomalous And Topological Transport
10. Nonequilibrium Steady States And Open-System Limits
11. Hydrodynamic Fluctuations And Long-Time Tails
12. QCD Phase Structure, Plasma, And Dense Matter

Further development targets:

1. KMS States And Thermal Correlators
2. Finite-Temperature Path Integrals
3. Real-Time Schwinger--Keldysh Formalism
4. Spectral Functions, Kubo Formulae, And Transport
5. Hydrodynamics From Ward Identities And Local Equilibrium
6. Schwinger--Keldysh Hydrodynamic Effective Actions
7. Thermal Gauge Theory And Screening
8. Kinetic Theory As A Controlled Limit
9. Anomalous And Topological Transport
10. Nonequilibrium Steady States And Open-System Limits
11. Hydrodynamic Fluctuations And Long-Time Tails

## Volume XI: Constructive, Lattice, And Numerical QFT

Purpose: nonperturbative constructions and computable regulator frameworks.

Current compiled material:

1. Constructive Status And Routes To Continuum QFT
2. Constructive Scalar Models And OS Data
3. Lattice Reflection Positivity
4. Continuum Limits And Scaling Windows
5. Wilson Lattice Gauge Theory
6. Monte Carlo Methods And Sign Problems
7. Rigorous Renormalization Group
8. Relation Between Lattice And Continuum Local QFT
9. Stochastic Quantization And Singular SPDE
10. Hamiltonian Truncation, DLCQ, And Benchmark Protocols
11. Lattice Fermions And Chiral Symmetry

Further development targets:

1. Constructive Examples
2. Lattice Regularization
3. Reflection Positivity On The Lattice, Including Fermionic Mid-Link
   Reflection Positivity
4. Continuum Limits
5. Wilson Lattice Gauge Theory
6. Monte Carlo And Sign Problems
7. Rigorous Renormalization Group
8. Relation Between Lattice And Continuum Local QFT
9. Stochastic Quantization And Singular SPDE
10. Numerical Hamiltonian Truncation, DLCQ, And Benchmark Scripts
11. Lattice Fermions And Chiral Symmetry

Code policy:

- Calculation checks live in `calculation-checks/` and certify finite algebra
  or convention-sensitive formulae used by the text.
- Reader-facing numerical demonstrations live in `qft_scripts/`; they must
  state their regulator, cutoff parameters, dependencies, and theorem status.
  The smoke harness is `tools/run_qft_scripts_smoke.sh`, and the policy is
  recorded in `planning/14_code_policy.md`.

## Volume XII: QFT In Curved Spacetime And Background Fields

Purpose: QFT on fixed geometric backgrounds without treating quantum gravity
as part of the core construction.

Current compiled material:

1. Locally Covariant QFT And Hadamard States
2. Point Splitting And Stress Tensor Renormalization
3. Trace Anomalies And Background Variations
4. The Unruh Effect And Wedge Modular Theory
5. The Hawking Effect
6. Background Gauge Fields And Index Theory
7. Eta Invariants And Global Anomalies
8. Cosmological Spacetimes And Particle Creation
9. Microlocal Spectrum Condition And Hadamard Geometry
10. Perturbative Algebraic QFT On Curved Backgrounds
11. Semiclassical Backreaction And Stress-Tensor Fluctuations

Further development targets:

1. Locally Covariant QFT
2. Hadamard States
3. Stress Tensor Renormalization
4. Trace Anomalies In Curved Backgrounds
5. Unruh Effect
6. Hawking Effect
7. Background Gauge Fields And Index Theory
8. Eta Invariants And Global Anomalies
9. Cosmological Spacetimes And Particle Creation
10. Microlocal Spectrum Condition And Hadamard Geometry
11. Perturbative Algebraic QFT On Curved Backgrounds
12. Semiclassical Backreaction And Stress-Tensor Fluctuations

## Roadmap Volumes XIII--XX

The following volumes are part of the public subject architecture but are not
yet active compiled assemblies.  Their material may already be partially
developed in Volumes I--XII; a roadmap volume becomes compiled only after its
source assembly, chapter dossiers, verification pass, and reader-facing
frontmatter are in place.

| Volume | Roadmap title | Intended subject domain |
| --- | --- | --- |
| XIII | Large-\(N\) Gauge Theory, QCD Strings, Flux Tubes, Baryons, And Gauge-String Expansions | Nonperturbative large-\(N\) limits, QCD string observables, baryons, flux tubes, planar limits, and controlled bridges to gauge/string spectral problems. |
| XIV | Advanced Local-Algebraic QFT And Modular Structure | Local von Neumann algebras, split property, modular inclusions, relative entropy, entanglement as an AQFT topic, superselection sectors in examples, and concrete interacting nets. |
| XV | Advanced Scattering, Amplitudes, Resonances, And Infrared-Safe Observables | Analytic connected S-matrix elements, resonance poles and external unstable states, charged scattering beyond ordinary Haag--Ruelle, detector-defined inclusive observables, and nonperturbative amplitude constraints. |
| XVI | Advanced Supersymmetric Theories And Protected Sectors | Supersymmetric Wilsonian schemes, GLSM and mirror symmetry, four-dimensional \(\mathcal N=1\) and \(\mathcal N=2\) exact dynamics, localization with regulated data, six-dimensional theories, and protected sectors. |
| XVII | Advanced Two-Dimensional CFT And Exact Two-Dimensional QFT | Full and chiral CFT on Riemann surfaces, rational and non-rational examples, Liouville and Coulomb-gas residue logic, orbifolds, twist fields, sigma models, form factors, TCSA, TFFSA, and bridges to integrable and nonintegrable two-dimensional QFT. |
| XVIII | Advanced Constructive, Stochastic, And Rigorous Wilsonian QFT | Constructive existence theorems, stochastic quantization, singular SPDEs, nonperturbative Wilsonian RG, scaling limits, and proofs connecting regulator data to local QFT frameworks. |
| XIX | Advanced Phases, Defects, Categorical Symmetry, And Extended-Operator Theory | Line, surface, and domain-wall operators; generalized global symmetry; categorical symmetry; noninvertible defects; phase diagnostics; anomaly inflow; and substantial examples. |
| XX | Advanced Curved-Background, Locally Covariant, And Semiclassical QFT | Locally covariant QFT, microlocal methods, Hadamard renormalization, index-theoretic anomaly structure, semiclassical backreaction, and controlled curved-background examples. |

## Inclusion Rule

Only chapters that have passed the dossier, definition, source, and audit gates
may be included in the compiled manuscript. Draft files may exist on disk; the
compiled TeX is the mature subset.

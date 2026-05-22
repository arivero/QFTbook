# Development Dependency Map

This file is a non-reader-facing control document.  It records the dependency
order for comprehensive development of the monograph, including volumes that
are not yet compiled.  Its purpose is to prevent premature topical expansion:
future chapters may be planned in dossiers, but they enter the compiled
manuscript only after their prerequisites and audit gates are satisfied.

## Global Dependency Ladder

The core development proceeds through the following dependency objects.
Each item supplies data, constructions, or theorems used by later items.

1. Local quantum data on Minkowski spacetime: state space, observables,
   spacetime symmetry, spectrum condition, vacuum sector, locality, and
   comparison frameworks.
2. Fields as distributional coordinates and Wightman functions, with domains,
   covariance, positivity, spectral support, and reconstruction hypotheses.
3. Euclidean and algebraic presentations, including reflection positivity,
   GNS reconstruction, local nets, and precise comparison maps.
4. Regulated and continuum path-integral constructions of Green functions,
   with regulator, measure or oscillatory prescription, topology of limits,
   and positivity status declared.
5. Kallen--Lehmann spectral representation and the extraction of stable
   one-particle spectral subspaces from positive two-point data.
6. Perturbative Green functions and Feynman graphs as a calculus for
   correlation distributions.
7. Nonperturbative asymptotic states, Haag--Ruelle wave operators, and the
   S-matrix as a Hilbert-space scattering construction.
8. LSZ reduction as a theorem relating scattering matrix elements to poles
   or residues of time-ordered Green functions under stated hypotheses.
9. Perturbative scattering amplitudes, unitarity, analyticity, partial waves,
   bound states, resonances, and massless limits.
10. Renormalization, local counterterms, effective actions, Wilsonian flows,
    renormalized operators, critical phenomena, and continuum limits.
11. Gauge theory as constrained local quantum theory: gauge representatives,
    BRST organization, BV master formalism, physical observables, infrared
    sectors, anomalies, symmetry breaking, and global form.
12. Fixed-point local QFT and CFT operator data, built after the local,
    spectral, path-integral, and renormalization foundations are stable.
13. Special QFT structures: integrability, supersymmetry, topology,
    cohomological sectors, and extended operators, each promoted only after
    its ordinary local-QFT prerequisites are in place.
14. Thermal, nonequilibrium, constructive, lattice, numerical, and curved
    background extensions.

## Volume Dependencies

### Volume I: Foundations of Local Quantum Field Theory

Status: compiled mature subset.

Depends on: the source-note logical spine, basic Hilbert-space spectral
theory, distribution theory, and local algebra language.

Supplies: local quantum data, framework comparison language, fields as
operator-valued distributions, Euclidean and Wightman reconstruction targets,
regulated path-integral correlators, Kallen--Lehmann spectral data, and
perturbative Green functions.

Do not promote further material before: each definition states its ambient
category, all field expressions are distributional or smeared, path-integral
symbols have declared status, and spectral claims are certified.

Immediate target: re-audit the opening framework, then align the Wightman,
AQFT, OS, path-integral, and Kallen--Lehmann chapters so their comparison
maps use one consistent vocabulary.

### Volume II: Particles, Scattering, and Analyticity

Status: compiled mature subset with known duplication around Haag--Ruelle and
LSZ.

Depends on: Volume I spectral theory, local fields, time-ordered Green
functions, analytic continuation, and perturbative Green-function calculus.

Supplies: nonperturbative particle subspaces, wave operators, S-matrix,
LSZ reduction, cross sections, spin and helicity, bound states, resonances,
analyticity, dispersion theory, and high-energy bounds.

Do not promote further material before: S-matrix language is always downstream
of wave operators, perturbative amplitudes are downstream of LSZ, and massless
or infrared claims state their limiting observable.

Immediate target: merge the duplicated Haag--Ruelle and LSZ treatments into a
layered treatment that separates theorem, examples, and perturbative
applications.

### Volume III: Renormalization, Effective Field Theory, and Critical Phenomena

Status: compiled mature subset.

Depends on: Volume I perturbative Green functions and Volume II scattering
only for later physical applications; its intrinsic objects are local
functionals, distributions, scales, counterterms, and continuum limits.

Supplies: generating functionals, 1PI effective actions, local counterterm
criteria, BPHZ forests, renormalized operators, RG equations, Wilsonian
effective actions, critical fixed points, and universality statements with
specified convergence objects.  For ordinary scalar and matter systems these
objects are developed directly; for gauge theories, the gauge-compatible 1PI
and Wilsonian effective actions depend on the BV master formalism developed in
Volume IV.

Do not promote further material before: every renormalization claim identifies
the regulator, subtraction or flow scheme, locality statement, and equivalence
relation.

Immediate target: use the explicit BPHZ--Wilsonian--1PI matching,
mass-insertion example, and multi-insertion contact-coordinate construction
to tighten observable correlation-function statements in the universality and
CFT transition chapters.  Keep the gauge-theory extension routed through BV.

### Volume IV: Gauge Theory, Infrared Structure, and Anomalies

Status: compiled mature subset.

Depends on: Volumes I--III, especially local observables, path-integral
Green functions, renormalization, and nonperturbative scattering.

Supplies: spinor and gauge-field foundations, constraints, gauge fixing,
BRST complexes, BV master formalism, QED and QCD renormalization, inclusive
infrared observables, local and global anomalies, spontaneous symmetry
breaking, pion effective theory, and anomaly matching.

Do not promote further material before: gauge-representative statements are
related to gauge-invariant observables or cohomology classes, and anomaly
claims identify the compared cocycle class modulo local counterterms.

Immediate target: deepen gauge-invariant operator construction and extend the
new BV block toward reducible/open gauge algebras, explicit exact-RG
realizations, and global BV integration-cycle issues.  Continue confinement
diagnostics, global form, theta-angle, and anomaly inflow without importing
premature TQFT or supersymmetric machinery.

### Volume V: Conformal Field Theory

Status: compiled mature subset, intentionally limited to core CFT.

Depends on: Volumes I and III, with Volume IV needed for gauge-theory
examples and anomalies.

Supplies: conformal fixed-point data, conformal group actions, stress-tensor
structure, radial quantization, state-operator correspondence, Ward
identities, unitarity bounds, correlation functions, and OPE.

Do not promote further material before: fixed-point assumptions and Hilbert
space or Euclidean reconstruction assumptions are stated, and crossing/OPE
claims are formulated as convergence or distributional statements.

Immediate target: keep the core volume focused on local operator structure;
move two-dimensional, supersymmetric, integrable, topological, defect, and
bootstrap-specialized material into later volumes or deprecated drafts until
their prerequisites are complete.

### Volume VI: Integrable Quantum Field Theory

Status: planning only.

Depends on: Volumes I--II for local QFT, scattering, LSZ, analyticity, and
massive particles; Volume V for integrable perturbations of CFT.

Supplies: conserved charges, elastic and factorized scattering, Yang--Baxter
relations, exact S-matrices, form factors, local-operator reconstruction
problems, and thermodynamic Bethe ansatz.

Do not promote before: the Volume II scattering and analyticity treatment is
uniform, and the relation between exact S-matrix data and local fields is
stated as a reconstruction problem with hypotheses.

Immediate target: create chapter dossiers only.

### Volume VII: Supersymmetric Quantum Field Theory

Status: planning only.

Depends on: Volumes I--V, especially spin representations, gauge theory,
renormalized operators, anomalies, moduli, and CFT.

Supplies: supersymmetry algebras, multiplets, superspace, supersymmetric
actions, gauge theories, nonrenormalization, holomorphy, moduli spaces,
superconformal theories, and protected sectors.

Do not promote before: ordinary spinor, gauge, renormalization, anomaly, and
CFT foundations are stable.  Localization, branes, holography, and
supergravity remain out of scope until the supersymmetric QFT foundations are
developed.

Immediate target: collect source leads from the stringbook appendices and
external references into dossiers without adapting their prose.

### Volume VIII: Topological and Cohomological Quantum Field Theory

Status: planning only.

Depends on: Volumes I, IV, V, VII, and IX, depending on the chapter.

Supplies: metric-independent sectors, cohomological field theories, BF and
Chern--Simons theory, Atiyah--Segal and extended frameworks, twists,
boundaries, defects, and categorical structures.

Do not promote before: gauge-theory observables, anomalies, global symmetries,
and supersymmetric twists are formulated in QFT terms.

Immediate target: keep TQFT separate from integrable QFT; use overlap only
when a theorem or construction explicitly relates the two.

### Volume IX: Global Structure, Phases, and Extended Operators

Status: planning only.

Depends on: Volumes I--IV, with later use of Volumes V, VII, and VIII.

Supplies: global forms of symmetry groups, higher-form symmetries,
categorical symmetries, line and surface operators, domain walls,
confinement and screening diagnostics, discrete theta terms, anomaly inflow,
and phases of gauge theories.

Do not promote before: the core gauge and anomaly chapters provide stable
objects for local operators, extended operators, and background fields.

Immediate target: prepare dossiers for global form, line operators, and
confinement after the Volume IV gauge-observable pass.

### Volume X: Thermal, Statistical, and Nonequilibrium QFT

Status: planning only.

Depends on: Volumes I, III, IV, and XI.

Supplies: KMS states, finite-temperature path integrals, real-time
Schwinger--Keldysh theory, spectral functions, transport, hydrodynamic
effective theory, thermal gauge theory, and nonequilibrium effective actions.

Do not promote before: states, algebras, spectral functions, and path-integral
status have been standardized in earlier volumes.

Immediate target: no compiled material; record source dossiers only when
needed.

### Volume XI: Constructive, Lattice, and Numerical QFT

Status: planning only.

Depends on: Volumes I, III, IV, and X.

Supplies: rigorous constructions, lattice regularization, lattice reflection
positivity, continuum limits, Wilson lattice gauge theory, Monte Carlo
frameworks, sign problems, rigorous RG, and links between lattice and
continuum local QFT.

Do not promote before: regulator and continuum-limit vocabulary is made
uniform with Volumes I and III.

Immediate target: use as a reference framework for claims about existence,
regulators, and controlled continuum limits.

### Volume XII: QFT in Curved Spacetime and Background Fields

Status: planning only.

Depends on: Volumes I, III, IV, IX, and X.

Supplies: locally covariant QFT, Hadamard states, stress-tensor
renormalization, trace anomalies, Unruh and Hawking effects, background gauge
fields, and index-theoretic anomaly computations.

Do not promote before: flat-spacetime stress tensors, anomalies, states, and
renormalization are stable.

Immediate target: keep background-field technology available for anomaly and
index-theory checks without converting the core monograph into curved
spacetime QFT prematurely.

## Compiled-Core Uniformization Queue

1. Volume I, Chapter 1: re-audit starting data, symbol typing, local algebra
   convention, and comparison-framework definitions.
2. Volume I, Chapters 2--4: make Wightman, AQFT, OS, and superselection
   vocabulary mutually consistent.
3. Volume I, Chapters 7--13: align regulated path integrals, Green functions,
   Kallen--Lehmann spectral measures, and early perturbation theory.
4. Volume II, Chapters 1--2 and 6--8: remove duplication in Haag--Ruelle,
   S-matrix, and LSZ material by making theorem/example/application layers.
5. Volume III, Chapters 1--8: connect 1PI, BPHZ, Wilsonian, operator-mixing,
   and critical phenomena treatments.
6. Volume IV, Chapters 2--10: deepen gauge observables, BRST cohomology, add
   the BV master formalism as the framework for gauge-theory 1PI/Wilsonian
   effective actions, and then refine infrared sectors, anomalies, and global
   form.
7. Volume V: audit every CFT chapter for fixed-point assumptions, convergence
   statements, and the boundary between core CFT and later special volumes.

## Promotion Gate For Future Volumes

A planning-only chapter may become compiled manuscript only after:

- a chapter dossier exists with source anchors, external references,
  notation inventory, claim ledger, and figure ledger;
- prerequisites in this dependency map are either already compiled or
  explicitly imported with hypotheses;
- no topic is included merely because it is fashionable or adjacent;
- examples verify definitions, test hypotheses, compute invariants, or mark a
  theorem boundary;
- the strict writing harness, deferred-topic audit, TeX build, and visual
  figure checks pass.

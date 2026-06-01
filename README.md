# Notes on Quantum Field Theory

This repository contains the working manuscript and project infrastructure for
a comprehensive multi-volume monograph on quantum field theory.

Author line for the monograph:

> GPT 5.5 under the supervision of Xi Yin

The manuscript is an active draft.  The reader-facing text is in
`monograph/tex/`; planning notes, source transcriptions, and local reference
material are kept separate from the compiled monograph.

## Quick Full Volume Index

The full current volume program has twenty numbered volumes.  Volumes I-XII
are active compiled volumes in `monograph/tex/main.pdf`; Volumes XIII-XX are
public roadmap volumes whose subject matter is planned but not yet assembled
as compiled TeX volumes.

1. Volume I: Foundations of Local Quantum Field Theory
2. Volume II: Particles, Scattering, and Analyticity
3. Volume III: Renormalization, Effective Field Theory, and Critical Phenomena
4. Volume IV: Gauge Theory, Infrared Structure, and Anomalies
5. Volume V: Conformal Field Theory
6. Volume VI: Integrable Quantum Field Theory
7. Volume VII: Supersymmetric Quantum Field Theory
8. Volume VIII: Topological and Cohomological Quantum Field Theory
9. Volume IX: Global Structure, Phases, and Extended Operators
10. Volume X: Thermal Quantum Field Theory, Hydrodynamics, and Nonequilibrium Dynamics
11. Volume XI: Constructive, Lattice, and Numerical Quantum Field Theory
12. Volume XII: Quantum Field Theory in Curved Spacetime and Background Fields
13. Volume XIII: Large-N Gauge Theory, QCD Strings, Flux Tubes, Baryons, and Gauge-String Expansions
14. Volume XIV: Advanced Local-Algebraic QFT and Modular Structure
15. Volume XV: Advanced Scattering, Amplitudes, Resonances, and Infrared-Safe Observables
16. Volume XVI: Advanced Supersymmetric Theories and Protected Sectors
17. Volume XVII: Advanced Two-Dimensional CFT and Exact Two-Dimensional QFT
18. Volume XVIII: Advanced Constructive, Stochastic, and Rigorous Wilsonian QFT
19. Volume XIX: Advanced Phases, Defects, Categorical Symmetry, and Extended-Operator Theory
20. Volume XX: Advanced Curved-Background, Locally Covariant, and Semiclassical QFT

## Complete Volume Program

### Complete Volume List I-XX

The table below is the complete public-facing volume program at the present
stage of the project.  Volumes I-XII are active compiled volumes and are
included in `monograph/tex/main.pdf`.  Volumes XIII-XX are prospective roadmap
volumes: their subject matter is part of the intended monograph architecture,
but they are not yet compiled public volumes and do not yet have chapter maps.
A prospective volume becomes active only after it has a TeX assembly file,
chapter dossiers, verification pass, frontmatter entry, and README entry in
the same commit.

| Volume | Status | Title |
| --- | --- | --- |
| I | Active compiled volume | Foundations of Local Quantum Field Theory |
| II | Active compiled volume | Particles, Scattering, and Analyticity |
| III | Active compiled volume | Renormalization, Effective Field Theory, and Critical Phenomena |
| IV | Active compiled volume | Gauge Theory, Infrared Structure, and Anomalies |
| V | Active compiled volume | Conformal Field Theory |
| VI | Active compiled volume | Integrable Quantum Field Theory |
| VII | Active compiled volume | Supersymmetric Quantum Field Theory |
| VIII | Active compiled volume | Topological and Cohomological Quantum Field Theory |
| IX | Active compiled volume | Global Structure, Phases, and Extended Operators |
| X | Active compiled volume | Thermal Quantum Field Theory, Hydrodynamics, and Nonequilibrium Dynamics |
| XI | Active compiled volume | Constructive, Lattice, and Numerical Quantum Field Theory |
| XII | Active compiled volume | Quantum Field Theory in Curved Spacetime and Background Fields |
| XIII | Prospective roadmap volume | Large-N Gauge Theory, QCD Strings, Flux Tubes, Baryons, and Gauge-String Expansions |
| XIV | Prospective roadmap volume | Advanced Local-Algebraic QFT and Modular Structure |
| XV | Prospective roadmap volume | Advanced Scattering, Amplitudes, Resonances, and Infrared-Safe Observables |
| XVI | Prospective roadmap volume | Advanced Supersymmetric Theories and Protected Sectors |
| XVII | Prospective roadmap volume | Advanced Two-Dimensional CFT and Exact Two-Dimensional QFT |
| XVIII | Prospective roadmap volume | Advanced Constructive, Stochastic, and Rigorous Wilsonian QFT |
| XIX | Prospective roadmap volume | Advanced Phases, Defects, Categorical Symmetry, and Extended-Operator Theory |
| XX | Prospective roadmap volume | Advanced Curved-Background, Locally Covariant, and Semiclassical QFT |

This table is the authoritative full list of volumes currently recognized by
the public project.  There are twelve active compiled volumes and eight
prospective roadmap volumes.  The detailed chapter map later in this README
lists only Volumes I-XII because only those volumes presently have compiled
chapter assemblies.

### Active Compiled Volumes I-XII

The active public manuscript currently consists of exactly twelve compiled
volumes:

1. Volume I: Foundations of Local Quantum Field Theory
2. Volume II: Particles, Scattering, and Analyticity
3. Volume III: Renormalization, Effective Field Theory, and Critical Phenomena
4. Volume IV: Gauge Theory, Infrared Structure, and Anomalies
5. Volume V: Conformal Field Theory
6. Volume VI: Integrable Quantum Field Theory
7. Volume VII: Supersymmetric Quantum Field Theory
8. Volume VIII: Topological and Cohomological Quantum Field Theory
9. Volume IX: Global Structure, Phases, and Extended Operators
10. Volume X: Thermal Quantum Field Theory, Hydrodynamics, and Nonequilibrium Dynamics
11. Volume XI: Constructive, Lattice, and Numerical Quantum Field Theory
12. Volume XII: Quantum Field Theory in Curved Spacetime and Background Fields

The public volume program has two layers.  The first layer is the launched
compiled manuscript: twelve reader-facing volumes, numbered I--XII, whose
assembly files are included by `monograph/tex/main.tex` and therefore by
`monograph/tex/main.pdf`.  The second layer is the prospective future volume
program: Volumes XIII-XX record the intended subject architecture, but remain
roadmap entries until their assembly files and verification infrastructure are
created.

Chapter ranges are continuous printed chapter numbers, and counts are counts
of printed `\chapter` entries, not raw `\input` lines.  Volume IV also inputs
the spinor-convention source as a section inside Chapter 40.

| Volume | Chapters | Count | Title | Scope | Assembly file |
| --- | ---: | ---: | --- | --- | --- |
| I | 1-16 | 16 | Foundations of Local Quantum Field Theory | Local quantum data, Wightman/AQFT/OS/KS frameworks, path integrals, spectral representations, and Green functions. | `monograph/tex/volumes/volume_i/volume_i_current.tex` |
| II | 17-29 | 13 | Particles, Scattering, and Analyticity | Haag--Ruelle scattering, LSZ, particles, spin, helicity, bound states, resonances, crossing, and dispersion theory. | `monograph/tex/volumes/volume_ii/volume_ii_current.tex` |
| III | 30-39 | 10 | Renormalization, Effective Field Theory, and Critical Phenomena | 1PI actions, counterterms, BPHZ forests, renormalized operators, RG, Wilsonian flow, scaling limits, and EFT. | `monograph/tex/volumes/volume_iii/volume_iii_current.tex` |
| IV | 40-55 | 16 | Gauge Theory, Infrared Structure, and Anomalies | Spinors, gauge fixing, BV, QED, Yang--Mills, QCD, jets, anomalies, and the Standard Model as a hybrid QFT. | `monograph/tex/volumes/volume_iv/volume_iv_current.tex` |
| V | 56-70 | 15 | Conformal Field Theory | Conformal representation theory, radial quantization, OPE, light-ray observables, 2D CFT, Liouville theory, and boundary CFT. | `monograph/tex/volumes/volume_v/volume_v_current.tex` |
| VI | 71-84 | 14 | Integrable Quantum Field Theory | Factorized scattering, Bethe ansatz, form factors, TBA, integrable RG flows, and exact two-dimensional examples. | `monograph/tex/volumes/volume_vi/volume_vi_current.tex` |
| VII | 85-101 | 17 | Supersymmetric Quantum Field Theory | Supersymmetry algebras, superfields, gauge dynamics, Seiberg--Witten theory, lower-dimensional examples, planar N=4 SYM, and localization. | `monograph/tex/volumes/volume_vii/volume_vii_current.tex` |
| VIII | 102-112 | 11 | Topological and Cohomological Quantum Field Theory | Metric independence, bordism functoriality, BF and Chern--Simons theory, cohomological theories, twists, and state-sum models. | `monograph/tex/volumes/volume_viii/volume_viii_current.tex` |
| IX | 113-123 | 11 | Global Structure, Phases, and Extended Operators | Global forms, higher-form symmetry, extended operators, confinement diagnostics, anomaly inflow, defects, and categorical symmetry. | `monograph/tex/volumes/volume_ix/volume_ix_current.tex` |
| X | 124-135 | 12 | Thermal Quantum Field Theory, Hydrodynamics, and Nonequilibrium Dynamics | KMS states, finite-temperature path integrals, Schwinger--Keldysh theory, transport, hydrodynamics, kinetic theory, and thermal gauge theory. | `monograph/tex/volumes/volume_x/volume_x_current.tex` |
| XI | 136-146 | 11 | Constructive, Lattice, and Numerical Quantum Field Theory | Constructive models, reflection positivity, continuum limits, lattice gauge theory, rigorous RG, stochastic quantization, and numerical regulators. | `monograph/tex/volumes/volume_xi/volume_xi_current.tex` |
| XII | 147-157 | 11 | Quantum Field Theory in Curved Spacetime and Background Fields | Locally covariant QFT, Hadamard states, stress tensors, Unruh and Hawking effects, index theory, microlocal methods, and semiclassical backreaction. | `monograph/tex/volumes/volume_xii/volume_xii_current.tex` |

These twelve rows are the complete list of launched public volumes.  There are
no hidden active volumes outside this roster.  Draft files, deprecated files,
source transcriptions, local reference files, and planning notes are not
additional public volumes.

### Prospective Roadmap Volumes XIII-XX

The table below gives the complete current roadmap for the prospective
volumes after the twelve compiled volumes.  These entries are numbered so that
the README contains the full volume program, but their status remains
prospective until the corresponding source assemblies exist and pass the same
verification standards as Volumes I-XII.

| Volume | Current status | Intended scope | Current compiled home |
| --- | --- | --- | --- |
| XIII | Prospective roadmap volume | Nonperturbative large-N limits, QCD string observables, baryons and solitons, planar versus confining string limits, and controlled bridges to gauge/string spectral problems. | Mainly Volumes IV, VI, VII, and IX |
| XIV | Prospective roadmap volume | Local von Neumann algebras, split property, modular inclusions, relative entropy, entanglement as an AQFT topic, superselection sectors in examples, and concrete interacting nets. | Volumes I, X, XI, and XII |
| XV | Prospective roadmap volume | Analytic connected S-matrix elements, resonance poles and external unstable states, charged scattering beyond ordinary Haag--Ruelle, energy correlators, light-ray observables, and detector-defined inclusive observables. | Volumes II, IV, and V |
| XVI | Prospective roadmap volume | GLSM and mirror symmetry, two-dimensional supersymmetric models, four-dimensional N=1 and N=2 dynamics, localization with regulated data, six-dimensional theories, and protected sectors. | Volume VII |
| XVII | Prospective roadmap volume | Full and chiral CFT on Riemann surfaces, rational and non-rational examples, Liouville and Coulomb-gas residue logic, orbifolds, twist fields, sigma models, form factors, TCSA, TFFSA, and bridges to integrable and nonintegrable two-dimensional QFT. | Volumes V, VI, VII, and XI |
| XVIII | Prospective roadmap volume | Constructive existence theorems, stochastic quantization, singular SPDEs, nonperturbative Wilsonian RG, scaling limits, and proofs connecting regulator data to local QFT frameworks. | Volume XI |
| XIX | Prospective roadmap volume | Line, surface, and domain-wall operators; generalized global symmetry; categorical symmetry; noninvertible defects; phase diagnostics; anomaly inflow; and substantial examples. | Volumes VIII and IX |
| XX | Prospective roadmap volume | Locally covariant QFT, microlocal methods, Hadamard renormalization, index-theoretic anomaly structure, semiclassical backreaction, and controlled curved-background examples. | Volume XII |

Contributors should treat the twelve active volumes as the authoritative
compiled manuscript and the roadmap table as the authoritative list of
prospective subject expansions.  A prospective volume becomes an active public
compiled volume only after it has its own assembly file, chapter dossiers,
verification pass, and frontmatter/README entry.

### Permanent Cross-Cutting Layer

Mathematical machinery and verification infrastructure are distributed through
the active volumes rather than being a separate numbered volume.  This layer
includes spinors, supergeometry, distribution theory, functional analysis,
rigged Hilbert spaces, calculation-check scripts, finite-regulator examples,
and proof dossiers.

## Repository Layout

- `monograph/tex/`: reader-facing LaTeX manuscript.
- `planning/`: project constitution, rigor standards, source hierarchy,
  and chapter dossiers.
- `transcription/`: TeX reconstruction of source lecture notes used as local
  source material, not as reader-facing monograph prose.
- `references/`: local source and reference shelf.  PDFs, extracted text, and
  private source files are intentionally excluded from git by `.gitignore`.
- `tools/`: build, audit, OCR, and skeleton-generation utilities.
- `calculation-checks/`: public-facing Python and Wolfram Language scripts
  that verify convention-sensitive algebra used in the manuscript.
- `qft_scripts/`: reader-facing finite-regulator numerical demonstrations
  such as Monte Carlo, Hamiltonian truncation, and DLCQ smoke examples.

## Volume Architecture And Chapter Map

The full volume program is the twenty-volume list at the top of this README.
The compiled manuscript currently contains the first twelve subject volumes
and uses continuous chapter numbering across those active volumes.
The chapter order below records the current contents of every launched volume,
I--XII, and then continues with the planned subject blocks for roadmap
Volumes XIII--XX.  The roadmap entries are not compiled chapters yet; they
are included here so the README contains the full volume program in one
continuous list.  The source directory names for Volumes I--XII are historical
assembly locations, while the reader-facing part titles and chapter order
below are the authoritative compiled-volume structure.  The frontmatter Source
Assembly Map records how source files are assembled into the printed order.

### Detailed Chapter Map

1. Volume I: Foundations of Local Quantum Field Theory
   - Starting Data for Local Quantum Field Theory
   - Wightman Fields and Reconstruction
   - Algebraic QFT: Local Nets and States
   - Superselection Sectors and Locality Properties
   - Relativistic Quantum Mechanics and Local Operator Structure
   - Local Fields, Covariance, and Microcausality
   - Hamiltonian Evolution and Time-Sliced Path Integrals
   - Euclidean Correlation Functions and Gaussian Perturbation Theory
   - Relativistic Scalar Fields and Canonical Quantization
   - Symmetries, Noether Currents, and Stress Tensors
   - Scalar Path Integrals and Green Functions
   - Osterwalder--Schrader Reconstruction
   - Kontsevich--Segal Functorial Quantum Field Theory
   - Kallen--Lehmann Spectral Representation
   - Perturbative Green Functions and Feynman Graphs
   - Lorentzian Green Functions and Analytic Continuation
2. Volume II: Particles, Scattering, and Analyticity
   - Haag--Ruelle Scattering Theory
   - LSZ Reduction
   - Cross Sections, Phase Space, and Unitarity
   - Massive Particles and Spin
   - Massless Particles, Helicity, and Gauge Redundancy
   - Haag--Ruelle Theory and Mathematical Scattering
   - Local Data and Kernel Conventions
   - Scattering Kernels, LSZ, and Cluster Decomposition
   - Bound States from Exchange Amplitudes
   - Resonances and Dressed Propagators
   - Composite Bound States and Bethe--Salpeter Amplitudes
   - Analyticity, Crossing, and Landau Singularities
   - Partial Waves, Dispersion Relations, and High-Energy Bounds
3. Volume III: Renormalization, Effective Field Theory, and Critical Phenomena
   - Generating Functionals and the One-Particle-Irreducible Effective Action
   - Renormalizability and Local Counterterms
   - Subdivergences and Forest Formulas
   - The 1PI Renormalization Group
   - Renormalized Operators and Minimal Subtraction
   - Stress Tensor Trace and Conformal Currents
   - Wilsonian Effective Actions and Exact Cutoff Flow
   - The Wilson-Fisher Fixed Point and Scaling Operators
   - The Statistical Ising Model and Universality
   - Effective Field Theories Without Poincare-Invariant UV Completion
4. Volume IV: Gauge Theory, Infrared Structure, and Anomalies
   - Spinor Fields, Fermionic Statistics, and Grassmann Path Integrals,
     including Spinor and Gamma-Matrix Conventions
   - Maxwell Theory, Constraints, and Gauge Fixing
   - Quantum Electrodynamics and External States
   - QED Renormalization and Electromagnetic Form Factors
   - Infrared Divergences and Inclusive QED
   - Classical Yang-Mills Theory and Matter Fields
   - Lattice Yang--Mills as a Nonperturbative Formulation
   - Gauge Fixing, Ghosts, and BRST Cohomology
   - The BV Master Formalism for Gauge Effective Actions
   - QCD Renormalization, Asymptotic Freedom, and Deep Inelastic Scattering
   - Jets, Infrared-Safe Observables, and Hadronization
   - Chiral Axial Anomalies
   - The Schwinger Model: Two-Dimensional Quantum Electrodynamics
   - Large-N Two-Dimensional QCD and the Light-Front Bound-State Equation
   - The Standard Model as a Hybrid Quantum Field Theory
   - Global Anomalies, Spontaneous Symmetry Breaking, and Pions
5. Volume V: Conformal Field Theory
   - Fixed Points and Conformal Data
   - Conformal Killing Vectors and the Conformal Group
   - Stress Tensor, Weyl Structure, and Improvement
   - Radial Quantization and the State-Operator Correspondence
   - Conformal Charges and Ward Identities
   - Primary Operators and Finite Conformal Transformations
   - Unitarity Bounds and Short Multiplets
   - Correlation Functions and Conformal Frames
   - The Operator Product Expansion
   - Light-Ray Operators and Energy Correlators
   - Two-Dimensional Sigma Models, Orbifolds, and Twist Fields
   - Vertex Operator Algebras, Modular Sewing, and Logarithmic CFT
   - Liouville Conformal Field Theory
   - Boundary Conformal Field Theory
   - Two-Dimensional Superconformal Algebras
6. Volume VI: Integrable Quantum Field Theory
   - Factorized Scattering and Integrability
   - Two-Dimensional Scattering Analyticity and Bootstrap Data
   - Yang--Baxter Consistency and Internal Symmetry
   - Algebraic Bethe Ansatz and Transfer Matrices
   - Nested Bethe Ansatz and Matrix Bethe--Yang Equations
   - Form-Factor Bootstrap and Local Operators
   - Thermodynamic Bethe Ansatz
   - Nested TBA, Baxter Relations, and Separation Variables
   - Integrable RG Flows and Perturbed Two-Dimensional CFT
   - Mirror-Channel TBA and Finite-Size Effects
   - Sine-Gordon, Massive Thirring, and Affine Toda Theories
   - O(N), Gross--Neveu, and Sigma-Model Families
   - Bridges to Nonintegrable Two-Dimensional QFT and CFT
   - Finite-Volume Form Factors and Spectral Expansions
7. Volume VII: Supersymmetric Quantum Field Theory
   - Supersymmetry Algebras and Representation Data
   - Superspace, Superfields, and Local Actions
   - Supersymmetric Gauge Theory
   - Supersymmetric Wilsonian Schemes and Exact Dynamics
   - Nonrenormalization and Holomorphy
   - Four-Dimensional N=1 Gauge Dynamics
   - Four-Dimensional N=2 Gauge Dynamics and Seiberg-Witten Theory
   - Spectral Bridges among Supersymmetric Yang--Mills Cousins
   - Moduli Spaces in Supersymmetric Quantum Field Theory
   - Two-Dimensional Supersymmetric Models
   - Three-Dimensional Chern--Simons--Matter Theories
   - Six-Dimensional Superconformal Theories
   - Planar N=4 Supersymmetric Yang-Mills as a Spectral Problem
   - All-Loop Asymptotic Bethe Ansatz
   - Mirror TBA and the Y-System
   - Quantum Spectral Curve and Hexagon Form Factors
   - Supersymmetric Localization on Compact Manifolds
8. Volume VIII: Topological and Cohomological Quantum Field Theory
   - Metric Independence and Cohomological Observables
   - Bordism Functoriality and Extended Topological Field Theory
   - BF Theory
   - Chern--Simons Theory
   - Cohomological Field Theories
   - Topological Sigma Models
   - Twists of Supersymmetric Theories
   - Witten-Donaldson Theory and the Seiberg-Witten Comparison
   - Boundaries, Defects, and Categories in Topological QFT
   - BV Integration and Finite-Dimensional Localization
   - Finite Gauge Theory and State-Sum TQFT
9. Volume IX: Global Structure, Phases, and Extended Operators
   - Global Forms and Higher-Form Symmetry
   - Extended Operators and Topological Defects
   - Line, Surface, and Domain-Wall Operators
   - Confinement, Screening, and Oblique Confinement
   - Discrete Theta Terms
   - Anomaly Inflow and Invertible Field Theories
   - Phases of Gauge Theories
   - Boundaries and Defects
   - Categorical Symmetry and Defect Fusion
   - Duality Defects, Gauging, and Orbifold Data
   - Higher-Group Symmetry and Symmetry TQFT
10. Volume X: Thermal Quantum Field Theory, Hydrodynamics, and Nonequilibrium Dynamics
    - KMS States and Thermal Correlators
    - Finite-Temperature Path Integrals
    - Real-Time Schwinger--Keldysh Formalism
    - Spectral Functions, Kubo Formulae, and Transport
    - Hydrodynamics from Ward Identities
    - Schwinger--Keldysh Hydrodynamic Effective Actions
    - Thermal Gauge Theory and Screening
    - Kinetic Theory as a Controlled Limit
    - Anomalous and Topological Transport
    - Nonequilibrium Steady States and Open-System Limits
    - Hydrodynamic Fluctuations and Long-Time Tails
    - QCD Phase Structure, Plasma, and Dense Matter
11. Volume XI: Constructive, Lattice, and Numerical Quantum Field Theory
    - Constructive Status and Routes to Continuum QFT
    - Constructive Scalar Models and OS Data
    - Lattice Reflection Positivity
    - Continuum Limits and Scaling Windows
    - Wilson Lattice Gauge Theory
    - Monte Carlo Methods and Sign Problems
    - Rigorous Renormalization Group
    - Relation between Lattice and Continuum Local QFT
    - Stochastic Quantization and Singular SPDE
    - Hamiltonian Truncation, DLCQ, and Benchmark Protocols
    - Lattice Fermions and Chiral Symmetry
12. Volume XII: Quantum Field Theory in Curved Spacetime and Background Fields
    - Locally Covariant QFT and Hadamard States
    - Point Splitting and Stress Tensor Renormalization
    - Trace Anomalies and Background Variations
    - The Unruh Effect and Wedge Modular Theory
    - The Hawking Effect
    - Background Gauge Fields and Index Theory
    - Eta Invariants and Global Anomalies
    - Cosmological Spacetimes and Particle Creation
    - Microlocal Spectrum Condition and Hadamard Geometry
    - Perturbative Algebraic QFT on Curved Backgrounds
    - Semiclassical Backreaction and Stress-Tensor Fluctuations
13. Volume XIII: Large-N Gauge Theory, QCD Strings, Flux Tubes, Baryons, and Gauge-String Expansions
    - Nonperturbative large-N limits and order-of-limits questions
    - Wilson loops, flux tubes, and QCD string observables
    - Baryons, solitons, and large-N scaling of multiparticle sectors
    - Planar versus confining string limits
    - Bridges to gauge/string spectral problems
14. Volume XIV: Advanced Local-Algebraic QFT and Modular Structure
    - Local von Neumann algebras and concrete interacting nets
    - Split property, nuclearity, and phase-space conditions
    - Modular inclusions, relative entropy, and structural reconstruction
    - Entanglement as an AQFT topic rather than a formal path-integral slogan
    - Superselection sectors in substantial examples
15. Volume XV: Advanced Scattering, Amplitudes, Resonances, and Infrared-Safe Observables
    - Analytic connected S-matrix elements and sheet structure
    - Resonance poles and the problem of external unstable particles
    - Charged scattering beyond ordinary Haag--Ruelle theory
    - Energy correlators, light-ray observables, and detector-defined inclusive data
    - Polynomial bounds, dispersion theory, and nonperturbative amplitude constraints
16. Volume XVI: Advanced Supersymmetric Theories and Protected Sectors
    - Supersymmetric Wilsonian schemes and BV-compatible regulators
    - GLSM, mirror symmetry, and two-dimensional supersymmetric models
    - Four-dimensional N=1 and N=2 exact dynamics
    - Localization with explicitly stated analytic and regulator hypotheses
    - Protected sectors and higher-dimensional supersymmetric examples
17. Volume XVII: Advanced Two-Dimensional CFT and Exact Two-Dimensional QFT
    - Full and chiral CFT on Riemann surfaces
    - Rational, logarithmic, and non-rational examples
    - Liouville theory and Coulomb-gas residue logic
    - Orbifolds, twist fields, sigma models, and conformal perturbation theory
    - Bridges to form factors, TCSA, TFFSA, and integrable/nonintegrable 2D QFT
18. Volume XVIII: Advanced Constructive, Stochastic, and Rigorous Wilsonian QFT
    - Constructive existence theorems and OS/Wightman output maps
    - Stochastic quantization and singular SPDE reconstruction
    - Nonperturbative Wilsonian RG and scaling limits
    - Proofs connecting regulator data to local QFT frameworks
    - Examples that test the relationship among constructive, lattice, and RG routes
19. Volume XIX: Advanced Phases, Defects, Categorical Symmetry, and Extended-Operator Theory
    - Line, surface, and domain-wall operators
    - Generalized global symmetry and categorical symmetry
    - Noninvertible defects and phase diagnostics
    - Anomaly inflow and extended-operator anomaly matching
    - Substantial examples across gauge theory, TQFT, and CFT
20. Volume XX: Advanced Curved-Background, Locally Covariant, and Semiclassical QFT
    - Locally covariant QFT beyond the introductory framework
    - Microlocal methods and Hadamard renormalization
    - Index-theoretic anomaly structure on backgrounds
    - Semiclassical backreaction and stress-tensor fluctuations
    - Controlled curved-background examples and open structural problems

## Build

The monograph build expects a TeX installation with `xelatex`, `latexmk`, TikZ,
and standard AMS packages.  The strict text audit additionally requires
`ripgrep`.

From the repository root:

```bash
tools/build_monograph.sh
```

The script runs the reader-facing text audit, builds
`monograph/tex/main.tex`, scans the final LaTeX logs for serious issues, and
writes the compiled PDF to `monograph/tex/main.pdf`.

Convention-sensitive calculation checks can be run with:

```bash
tools/run_calculation_checks.sh
```

The runner first executes the Python checks.  If `.wl` checks exist, it then
requires a working Wolfram backend, preferring
`/Applications/Wolfram.app/Contents/MacOS/WolframKernel -script` on the
author's macOS installation and falling back to `wolframscript -file` only
when the kernel entrypoint is unavailable.  The runner probes the selected
backend, runs every `.wl` file, rejects known Wolfram line-continuation parse
hazards, and fails unless each Wolfram script prints its success marker.
Computationally heavy or numerical checks should be implemented in Python.
Wolfram Language checks are reserved for lightweight, reader-readable symbolic
convention checks.  Set `QFT_SKIP_WOLFRAM=1` only for an explicitly
Python-only pass, and set `WOLFRAMKERNEL=/absolute/path/to/WolframKernel` or
`WOLFRAMSCRIPT=/absolute/path/to/wolframscript` to override executable paths.

Reader-facing companion scripts can be smoke-tested with:

```bash
tools/run_qft_scripts_smoke.sh
```

These scripts illustrate finite regulators.  Their smoke tests do not certify
continuum extrapolations or physical spectra unless the accompanying chapter
states and proves the finite claim being checked.

## Quality Gates

Before a manuscript change is considered ready:

1. Run `tools/build_monograph.sh`.
2. Check that the strict monograph text audit is clean.
3. Check that the LaTeX log scan is clean.
4. For figure-heavy edits, render and inspect the affected PDF pages.
5. For edits involving sign, spinor, group-theory, anomaly, conformal-block,
   or Feynman-integral conventions, run `tools/run_calculation_checks.sh` or
   the relevant script in `calculation-checks/`.
6. For edits to public numerical companion scripts, run
   `tools/run_qft_scripts_smoke.sh` or the edited script's smoke mode.

The planning layer records additional writing standards and audit procedures.

## GitHub Policy

Generated files, local build products, OCR outputs, source PDFs, and extracted
reference text are ignored.  Compiled PDFs should be distributed through
release artifacts rather than committed directly unless the author explicitly
decides otherwise.

The repository does not use a GitHub CI gate.  Manuscript verification is run
locally with the tools listed above, and `.github/workflows/` should not be
introduced unless the author explicitly requests GitHub Actions.

## Contributing

This is an open-source project.  Contributions should be made by pull request,
and every pull request must be reviewed and approved by Xi Yin or by a
maintainer explicitly designated by Xi Yin before it is merged.  See
`CONTRIBUTING.md` for the manuscript-quality, verification, and licensing
expectations.

## License

See `LICENSE` for the mixed licensing terms: manuscript and scholarly content
under CC BY 4.0, executable code under MIT.

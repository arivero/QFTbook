# Notes on Quantum Field Theory

This repository contains the working manuscript and project infrastructure for
a comprehensive multi-volume monograph on quantum field theory.

Author line for the monograph:

> GPT 5.5 under the supervision of Xi Yin

The manuscript is an active draft.  The reader-facing text is in
`monograph/tex/`; planning notes, source transcriptions, and local reference
material are kept separate from the compiled monograph.

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

The compiled manuscript currently contains twelve subject volumes and uses
continuous chapter numbering across the whole monograph.  The source directory
names are historical assembly locations; the reader-facing part titles and
chapter order below are the authoritative compiled-volume structure.  The
frontmatter Source Assembly Map records how source files are assembled into
the printed order.

### Complete Volume List

The compiled monograph currently contains the following twelve volumes.  This
table is the public volume roadmap; the chapter map below gives the current
compiled contents of each volume.

| Volume | Chapters | Source assembly | Compiled part title |
| --- | ---: | --- | --- |
| I | 16 | `monograph/tex/volumes/volume_i/volume_i_current.tex` | Foundations of Local Quantum Field Theory |
| II | 13 | `monograph/tex/volumes/volume_ii/volume_ii_current.tex` | Particles, Scattering, and Analyticity |
| III | 10 | `monograph/tex/volumes/volume_iii/volume_iii_current.tex` | Renormalization, Effective Field Theory, and Critical Phenomena |
| IV | 17 | `monograph/tex/volumes/volume_iv/volume_iv_current.tex` | Gauge Theory, Infrared Structure, and Anomalies |
| V | 15 | `monograph/tex/volumes/volume_v/volume_v_current.tex` | Conformal Field Theory |
| VI | 14 | `monograph/tex/volumes/volume_vi/volume_vi_current.tex` | Integrable Quantum Field Theory |
| VII | 17 | `monograph/tex/volumes/volume_vii/volume_vii_current.tex` | Supersymmetric Quantum Field Theory |
| VIII | 11 | `monograph/tex/volumes/volume_viii/volume_viii_current.tex` | Topological and Cohomological Quantum Field Theory |
| IX | 11 | `monograph/tex/volumes/volume_ix/volume_ix_current.tex` | Global Structure, Phases, and Extended Operators |
| X | 12 | `monograph/tex/volumes/volume_x/volume_x_current.tex` | Thermal Quantum Field Theory, Hydrodynamics, and Nonequilibrium Dynamics |
| XI | 11 | `monograph/tex/volumes/volume_xi/volume_xi_current.tex` | Constructive, Lattice, and Numerical Quantum Field Theory |
| XII | 11 | `monograph/tex/volumes/volume_xii/volume_xii_current.tex` | Quantum Field Theory in Curved Spacetime and Background Fields |

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

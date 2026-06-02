# QFT Monograph Manuscript

This directory contains the developing QFT monograph. It is separate from
`../transcription/`, which remains the faithful TeX reconstruction of the
source notes.

The compiled manuscript contains only rewritten prose intended to stand as a
monograph draft. Planning files and source transcriptions are kept outside the
reader-facing TeX build.

## Full Public Volume Program

The public monograph program currently has twenty numbered volumes.  The first
twelve are active compiled volumes included by `tex/main.tex`; Volumes XIII-XX
are roadmap volumes that record the intended subject architecture and become
compiled volumes only after their TeX assemblies, chapter dossiers,
verification passes, and frontmatter entries are created.

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

| Volume | Status | Title |
| --- | --- | --- |
| I | Compiled | Foundations of Local Quantum Field Theory |
| II | Compiled | Particles, Scattering, and Analyticity |
| III | Compiled | Renormalization, Effective Field Theory, and Critical Phenomena |
| IV | Compiled | Gauge Theory, Infrared Structure, and Anomalies |
| V | Compiled | Conformal Field Theory |
| VI | Compiled | Integrable Quantum Field Theory |
| VII | Compiled | Supersymmetric Quantum Field Theory |
| VIII | Compiled | Topological and Cohomological Quantum Field Theory |
| IX | Compiled | Global Structure, Phases, and Extended Operators |
| X | Compiled | Thermal Quantum Field Theory, Hydrodynamics, and Nonequilibrium Dynamics |
| XI | Compiled | Constructive, Lattice, and Numerical Quantum Field Theory |
| XII | Compiled | Quantum Field Theory in Curved Spacetime and Background Fields |
| XIII | Roadmap | Large-N Gauge Theory, QCD Strings, Flux Tubes, Baryons, and Gauge-String Expansions |
| XIV | Roadmap | Advanced Local-Algebraic QFT and Modular Structure |
| XV | Roadmap | Advanced Scattering, Amplitudes, Resonances, and Infrared-Safe Observables |
| XVI | Roadmap | Advanced Supersymmetric Theories and Protected Sectors |
| XVII | Roadmap | Advanced Two-Dimensional CFT and Exact Two-Dimensional QFT |
| XVIII | Roadmap | Advanced Constructive, Stochastic, and Rigorous Wilsonian QFT |
| XIX | Roadmap | Advanced Phases, Defects, Categorical Symmetry, and Extended-Operator Theory |
| XX | Roadmap | Advanced Curved-Background, Locally Covariant, and Semiclassical QFT |

## Build

From `monograph/tex/`:

```bash
latexmk -xelatex main.tex
```

Or from the repository root:

```bash
tools/build_monograph.sh
```

The current build is a twelve-volume active draft.  The table below gives the
complete compiled-volume list with printed chapter ranges; no additional
public compiled volume is active outside this list.

| Volume | Printed chapters | Title | Role in the monograph | Assembly file |
| --- | ---: | --- | --- | --- |
| I | 1-16 | Foundations of Local Quantum Field Theory | Local fields, Wightman and algebraic data, Euclidean reconstruction, path integrals, and spectral representations. | `tex/volumes/volume_i/volume_i_current.tex` |
| II | 17-29 | Particles, Scattering, and Analyticity | Haag--Ruelle scattering, LSZ, particles, bound states, resonances, analyticity, crossing, and dispersion theory. | `tex/volumes/volume_ii/volume_ii_current.tex` |
| III | 30-39 | Renormalization, Effective Field Theory, and Critical Phenomena | 1PI actions, BPHZ, renormalized operators, Wilsonian flow, scaling limits, and effective theories. | `tex/volumes/volume_iii/volume_iii_current.tex` |
| IV | 40-55 | Gauge Theory, Infrared Structure, and Anomalies | Spinors, gauge fixing, BV, QED, Yang--Mills, QCD, jets, anomalies, and the Standard Model as a hybrid QFT. | `tex/volumes/volume_iv/volume_iv_current.tex` |
| V | 56-70 | Conformal Field Theory | Conformal representation theory, radial quantization, OPE, light-ray observables, 2D CFT, Liouville theory, and boundary CFT. | `tex/volumes/volume_v/volume_v_current.tex` |
| VI | 71-84 | Integrable Quantum Field Theory | Factorized scattering, Bethe ansatz, form factors, TBA, integrable RG flows, and exact two-dimensional examples. | `tex/volumes/volume_vi/volume_vi_current.tex` |
| VII | 85-101 | Supersymmetric Quantum Field Theory | Supersymmetry algebras, superfields, supersymmetric gauge dynamics, Seiberg--Witten theory, 2D/3D/6D examples, planar N=4 SYM, and localization. | `tex/volumes/volume_vii/volume_vii_current.tex` |
| VIII | 102-112 | Topological and Cohomological Quantum Field Theory | Metric independence, bordism functoriality, BF and Chern--Simons theory, cohomological theories, twists, and state-sum models. | `tex/volumes/volume_viii/volume_viii_current.tex` |
| IX | 113-123 | Global Structure, Phases, and Extended Operators | Global forms, higher-form symmetry, extended operators, confinement diagnostics, anomaly inflow, defects, and categorical symmetry. | `tex/volumes/volume_ix/volume_ix_current.tex` |
| X | 124-135 | Thermal Quantum Field Theory, Hydrodynamics, and Nonequilibrium Dynamics | KMS states, real-time formalisms, transport, hydrodynamics, kinetic theory, anomalous transport, and thermal gauge theory. | `tex/volumes/volume_x/volume_x_current.tex` |
| XI | 136-146 | Constructive, Lattice, and Numerical Quantum Field Theory | Constructive models, reflection positivity, continuum limits, lattice gauge theory, rigorous RG, stochastic quantization, and numerical regulators. | `tex/volumes/volume_xi/volume_xi_current.tex` |
| XII | 147-157 | Quantum Field Theory in Curved Spacetime and Background Fields | Locally covariant QFT, Hadamard states, stress tensors, Unruh and Hawking effects, index theory, microlocal methods, and semiclassical backreaction. | `tex/volumes/volume_xii/volume_xii_current.tex` |

The draft remains under systematic development.  Compiled volume titles and
chapter order are determined by the manifest files under
`tex/volumes/volume_*/*_current.tex`.  The repository root README gives the
same twenty-volume public program, the compiled-volume chapter map, and the
roadmap-volume subject map.

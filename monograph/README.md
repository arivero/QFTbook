# QFT Monograph Manuscript

This directory contains the developing QFT monograph. It is separate from
`../transcription/`, which remains the faithful TeX reconstruction of the
source notes.

The compiled manuscript contains only rewritten prose intended to stand as a
monograph draft. Planning files and source transcriptions are kept outside the
reader-facing TeX build.

## Build

From `monograph/tex/`:

```bash
latexmk -xelatex main.tex
```

Or from the repository root:

```bash
tools/build_monograph.sh
```

The current build is a twelve-volume active draft:

1. Foundations of Local Quantum Field Theory
2. Particles, Scattering, and Analyticity
3. Renormalization, Effective Field Theory, and Critical Phenomena
4. Gauge Theory, Infrared Structure, and Anomalies
5. Conformal Field Theory
6. Integrable Quantum Field Theory
7. Supersymmetric Quantum Field Theory
8. Topological and Cohomological Quantum Field Theory
9. Global Structure, Phases, and Extended Operators
10. Thermal Quantum Field Theory, Hydrodynamics, and Nonequilibrium Dynamics
11. Constructive, Lattice, and Numerical Quantum Field Theory
12. Quantum Field Theory in Curved Spacetime and Background Fields

The draft remains under systematic development.  Compiled volume titles and
chapter order are determined by the manifest files under
`tex/volumes/volume_*/*_current.tex`.

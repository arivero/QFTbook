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

The manuscript is in an early rewrite stage. The current build includes the
foundations and scattering sequence, the renormalization and Wilsonian sequence,
and the first nonabelian gauge-dynamics sequence through BRST, QCD running,
axial anomalies, global anomalies, and pion effective actions.

# Quantum Field Theory

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
  chapter dossiers, and audit records.
- `transcription/`: TeX reconstruction of source lecture notes used as local
  source material, not as reader-facing monograph prose.
- `references/`: local source and reference shelf.  PDFs, extracted text, and
  private source files are intentionally excluded from git by `.gitignore`.
- `tools/`: build, audit, OCR, and skeleton-generation utilities.

## Active Volume Architecture

The compiled manuscript uses continuous chapter numbering across subject
volumes.

1. Foundations of Local Quantum Field Theory
2. Particles, Scattering, and Analyticity
3. Renormalization, Effective Field Theory, and Critical Phenomena
4. Gauge Theory, Infrared Structure, and Anomalies
5. Conformal Field Theory

Future special-topic volumes are planned for integrable QFT, supersymmetric
QFT, topological and cohomological QFT, global structure and extended
operators, thermal and nonequilibrium QFT, constructive/lattice/numerical QFT,
and QFT in curved spacetime.

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

## Quality Gates

Before a manuscript change is considered ready:

1. Run `tools/build_monograph.sh`.
2. Check that the strict monograph text audit is clean.
3. Check that the LaTeX log scan is clean.
4. For figure-heavy edits, render and inspect the affected PDF pages.

The planning layer records additional writing standards and audit procedures.

## GitHub Policy

Generated files, local build products, OCR outputs, source PDFs, and extracted
reference text are ignored.  Compiled PDFs should be distributed through
release artifacts rather than committed directly unless the author explicitly
decides otherwise.

No open-source license has been selected yet.  Until a license is added, all
rights are reserved by default.

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

# Code Policy For Calculation Checks And Companion Scripts

The monograph uses code in two different roles.  The distinction is part of
the rigor standard, because a script can certify a finite calculation without
certifying the continuum QFT claim that motivated the calculation.

## Calculation Checks

Files in `calculation-checks/` are regression tests for finite algebra,
normalizations, signs, tensor contractions, short numerical identities, and
other convention-sensitive calculations that are used directly in the
manuscript.  A calculation check should be deterministic, fast, and small
enough to run during an ordinary manuscript pass.  When a calculation check is
edited, run the edited check before committing.  When no calculation-check
file is edited, do not rerun the entire suite merely as a commit ritual.

Wolfram Language checks are allowed only for lightweight symbolic identities.
Heavy computation belongs in Python.  In `.wl` files, continued arithmetic
must keep the binary operator at the end of the previous line, or the full
right-hand side must be parenthesized; `wolframscript -file` can parse a
newline followed by a leading `+` or `-` as a new statement.

## Companion Scripts

Files in `qft_scripts/` are reader-facing finite-regulator demonstrations:
small Monte Carlo runs, Hamiltonian truncation matrices, DLCQ toy matrices,
TBA iterations, period integrals, and similar numerical examples.  They are
not proof substitutes.  Each script must state:

- the finite object being computed;
- the regulator and cutoff parameters;
- the mathematical status of the limiting claim;
- the default command needed for a quick smoke run;
- the expected dependencies.

The preferred dependency stack is Python plus NumPy/SciPy when needed.
Scripts intended for heavy computation must provide a small smoke mode that
finishes quickly on a laptop.  Long production runs belong in separate
examples or documented command lines, not in the smoke harness.

## Verification

The smoke harness is `tools/run_qft_scripts_smoke.sh`.  It checks that each
companion script executes and that built-in finite-regulator consistency
tests pass.  The smoke harness does not certify continuum extrapolation,
critical exponents, or exact spectra unless the script explicitly proves a
finite identity that implies the displayed number.

Before a script is cited in reader-facing TeX, the corresponding chapter must
explain what the code computes and what it does not compute.  In particular:

- a Monte Carlo estimate at finite lattice spacing is a statement about a
  finite probability measure;
- a Hamiltonian truncation eigenvalue is an eigenvalue of a finite matrix
  after declared counterterms and cutoffs;
- a DLCQ spectrum at harmonic resolution \(K\) is a finite light-front
  regulator output, with zero modes and continuum restoration listed among
  the proof obligations;
- a numerical extrapolation requires a model for the cutoff error and an
  independent stability check.

## Repository Boundary

The `references/` directory is a local study cache and is not pushed.  Public
scripts in `qft_scripts/`, calculation checks, and manuscript text may record
which references guided a computation, but they must be self-contained enough
for a reader to understand the finite calculation without access to private
reference files.

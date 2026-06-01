# Issue 494 scalar lattice Metropolis pass

Date: 2026-06-01

Issue context: GitHub #494, numerical methods with reader-facing finite
regulator scripts.

## Scope

This pass adds the two-dimensional scalar \(\phi^4\) lattice Metropolis
warmup requested in the numerical-methods issue.  The construction is kept at
finite regulator.  It defines the periodic finite-dimensional action,
states the stability condition for \(\lambda>0\), derives the local
single-site action difference, and proves detailed balance for a symmetric
single-site proposal.

The manuscript explicitly does not promote the finite run to a continuum
\(\phi^4_2\) construction, critical exponent estimate, or scaling theorem.

## Files

- `monograph/tex/volumes/volume_xi/chapter06_monte_carlo_and_sign_problems.tex`
- `qft_scripts/phi4_2d_metropolis.py`
- `qft_scripts/README.md`
- `tools/run_qft_scripts_smoke.sh`
- `calculation-checks/phi4_lattice_metropolis_checks.py`
- `calculation-checks/README.md`
- `calculation-checks/INDEX.md`
- `planning/chapter_dossiers/volume_xi/chapter06_monte_carlo_and_sign_problems.md`

## Verification

- `python3 qft_scripts/phi4_2d_metropolis.py --smoke`
- `python3 calculation-checks/phi4_lattice_metropolis_checks.py`
- `python3 -m py_compile qft_scripts/phi4_2d_metropolis.py calculation-checks/phi4_lattice_metropolis_checks.py`
- `tools/run_qft_scripts_smoke.sh`
- `tools/run_calculation_checks.sh --list --only phi4_lattice`
- `tools/run_calculation_checks.sh --python-only --only phi4_lattice`
- `git diff --check`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/build_monograph.sh`

All checks passed.  The full monograph build completed cleanly at 2833 pages.

## Closure status

Issue #494 remains open.  This pass closes the toy scalar lattice MCMC slice,
but the broader numerical-methods program still includes deeper production
examples, continuum-control studies, and larger Hamiltonian/DLCQ benchmarks.

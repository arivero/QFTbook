# Issue 494 correlated extrapolation script pass

Date: 2026-06-01

Issue context: GitHub #494, numerical methods with actual reader-facing
scripts and finite-regulator evidence standards.

## Scope

This pass adds a reusable finite-regulator extrapolation diagnostic rather
than another model-specific spectrum script.  The new script implements the
correlated-fit coordinate system already developed in Volume XI Chapter 10:
regulator labels, finite observable values, a covariance source, declared
remainder envelopes, and fit windows are explicit input data.

The manuscript now points to
`qft_scripts/finite_regulator_extrapolation.py` at the point where correlated
fit windows are defined.  The script reports fitted intercepts, propagated
statistical errors, deterministic systematic coordinates, correlated
residuals, condition numbers, and the spread of intercepts across declared
windows.  It also prints that the result is a finite diagnostic, not a proof
of the cutoff ansatz or continuum limit.

## Files

- `monograph/tex/volumes/volume_xi/chapter10_hamiltonian_truncation_dlcq_benchmarks.tex`
- `qft_scripts/finite_regulator_extrapolation.py`
- `qft_scripts/README.md`
- `tools/run_qft_scripts_smoke.sh`
- `calculation-checks/numerical_extrapolation_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_xi/chapter10_hamiltonian_truncation_dlcq_benchmarks.md`

## Verification

- `python3 qft_scripts/finite_regulator_extrapolation.py --smoke`
- `python3 calculation-checks/numerical_extrapolation_checks.py`
- `python3 -m py_compile qft_scripts/finite_regulator_extrapolation.py calculation-checks/numerical_extrapolation_checks.py`
- `tools/run_qft_scripts_smoke.sh`
- `git diff --check`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/build_monograph.sh`

All checks passed.  The full monograph build completed cleanly at 2832 pages.

## Closure status

Issue #494 remains open.  This pass adds reusable extrapolation infrastructure
for the numerical-methods program, but #494 still includes broader lattice,
Hamiltonian-truncation, DLCQ, and continuum-control development.

# 2026-05-30 Issue #700 Hamiltonian Truncation Datum Pass

## Target

- GitHub issue: #700.
- Local target:
  `monograph/tex/volumes/volume_xi/chapter10_hamiltonian_truncation_dlcq_benchmarks.tex`.
- Problem: the chapter used Rayleigh-Ritz, residual certificates, TCSA/TFFSA,
  DLCQ, and extrapolation machinery before aggregating the Hamiltonian
  regulator framework as a named datum.

## Edit

- Added `Definition~\ref{def:hamiltonian-truncation-regulator-datum}` at the
  chapter opening.
- The datum now states the target Hilbert space and closed quadratic form,
  directed cutoff trial spaces, computational bases, counterterm scheme,
  finite-regulator observables, and systematic-error model.
- Rewrote the projected-Hamiltonian opening as the elementary fixed-Hamiltonian
  specialization of the named datum.
- Added `Definition~\ref{def:dlcq-regulator-datum}` in the DLCQ section,
  including light-front compactification, harmonic resolution, parton
  partitions, zero-mode treatment, finite \(P^-\)/\(M^2\) operator, and
  continuum diagnostic.
- Updated the Volume XI Chapter 10 dossier.

## Verification

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`: 2686 pages.

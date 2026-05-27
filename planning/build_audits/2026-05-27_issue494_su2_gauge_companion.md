# Issue 494 SU(2) Gauge Companion Pass

## Scope

- GitHub issue: #494, numerical methods with reader-facing scripts.
- Branch: `main`.
- Files edited:
  - `monograph/tex/volumes/volume_xi/chapter06_monte_carlo_and_sign_problems.tex`
  - `qft_scripts/su2_gauge_4d_metropolis.py`
  - `calculation-checks/su2_gauge_metropolis_checks.py`
  - `qft_scripts/README.md`
  - `tools/run_qft_scripts_smoke.sh`
  - `calculation-checks/README.md`
  - `planning/chapter_dossiers/volume_xi/chapter06_monte_carlo_and_sign_problems.md`

## Substantive Changes

- Added a finite compact \(SU(2)\) lattice gauge section to the Monte Carlo
  chapter, using product Haar measure and the Wilson plaquette score
  \(Q(U)=\sum_p\frac12\operatorname{Re}\operatorname{tr}U_p\).
- Proved pairwise detailed balance for a compact local-link Metropolis update
  with inversion-symmetric proposal law.
- Defined finite rectangular Wilson-loop measurements and their gauge
  invariance at the finite-regulator level.
- Added a reader-facing four-dimensional \(SU(2)\) lattice-gauge companion
  script using unit-quaternion links, local compact proposals, plaquette
  measurements, and rectangular Wilson loops.
- Added a deterministic calculation check for quaternion group operations,
  local plaquette-score changes, detailed balance, gauge invariance, and the
  \(1\times1\) Wilson-loop/plaquette identity.

## Verification Plan

- `python3 qft_scripts/su2_gauge_4d_metropolis.py --smoke`
- `python3 calculation-checks/su2_gauge_metropolis_checks.py`
- `python3 -m py_compile qft_scripts/su2_gauge_4d_metropolis.py calculation-checks/su2_gauge_metropolis_checks.py`
- `tools/run_qft_scripts_smoke.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

## Verification Results

- `python3 qft_scripts/su2_gauge_4d_metropolis.py --smoke`: passed; the
  finite \(L=2\) run produced nontrivial acceptance and plaquette/Wilson-loop
  means in the \(SU(2)\) trace range.
- `python3 calculation-checks/su2_gauge_metropolis_checks.py`: passed;
  printed `All finite SU(2) gauge Metropolis checks passed.`
- `python3 -m py_compile qft_scripts/su2_gauge_4d_metropolis.py
  calculation-checks/su2_gauge_metropolis_checks.py`: passed.
- `tools/run_qft_scripts_smoke.sh`: passed, including the new compact
  \(SU(2)\) smoke run.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed; `latexmk` reported all targets
  up-to-date and the monograph build/log scan clean.
- `pdfinfo monograph/tex/main.pdf`: `Pages: 1949`, `File size: 7795590
  bytes`, `CreationDate: Tue May 26 22:50:00 2026 EDT`.

## Closure Status

This pass advances #494 but does not close it.  It supplies the missing
compact nonabelian pure-gauge finite-regulator layer.  Remaining production
items include heat-bath/overrelaxation, HMC/RHMC, richer TCSA spectra,
large-\(K\) DLCQ extrapolation, and systematic continuum-extrapolation
examples.

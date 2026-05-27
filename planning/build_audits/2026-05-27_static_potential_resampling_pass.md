# 2026-05-27 Static-Potential Resampling Pass

## Scope

This pass continues issue #631 by closing the immediate gap between
Wilson-loop central-value extraction and correlated Monte Carlo error
propagation for static-potential observables.

## Substantive Additions

- Added a finite Taylor-bound proposition for correlated delete-one-block
  jackknife errors of smooth nonlinear observables.
- Applied the proposition to Wilson-loop effective masses and Creutz ratios,
  emphasizing that these logarithmic ratios must be recomputed on the same
  deleted or resampled blocks.
- Extended `qft_scripts/static_potential_from_wilson_loops.py` with a
  sample-level CSV mode using columns `sample,R,T,W`.
- The sample-level mode forms complete consecutive blocks, computes central
  Wilson-loop means, recomputes effective-mass and Creutz-ratio observables
  on delete-one-block samples, and optionally performs block bootstrap.
- Extended `calculation-checks/static_potential_analysis_checks.py` to verify
  the correlated delete-one jackknife value on deterministic synthetic
  Wilson-loop samples.

## Verification

- Passed: `python3 qft_scripts/static_potential_from_wilson_loops.py --smoke`
- Passed: `python3 calculation-checks/static_potential_analysis_checks.py`
- Passed: `python3 -m py_compile qft_scripts/static_potential_from_wilson_loops.py calculation-checks/static_potential_analysis_checks.py`
- Passed: `tools/run_qft_scripts_smoke.sh`
- Passed: primitive-fraction scan on touched files.
- Passed: `git diff --check` on touched files.
- Passed: `tools/build_monograph.sh`
- Built PDF: `monograph/tex/main.pdf`, 2239 pages.

## Remaining Work

- The production sampler side still needs HDF5/checkpointed SU(3)
  Wilson-flow/static-potential ensemble generation and a small cluster
  workflow.  This pass supplies the correlated ratio-analysis layer that such
  sampler output should feed.

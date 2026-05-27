# 2026-05-27 Autocorrelation Resampling Pass

## Scope

This pass continues issue #631 by adding autocorrelation-aware blocking,
jackknife, and bootstrap diagnostics to Volume XI, Chapter 6 and to the
reader-facing script suite.

## Substantive Additions

- Added a Chapter 6 section on blocking, delete-one-block jackknife, and
  block-bootstrap error coordinates.
- Defined block means \(Y_j\), block sample variance \(s_Y^2\), blocked
  standard error, and delete-one-block jackknife variance.
- Proved the exact identity
  \(\operatorname{Var}_{\rm jack}(\overline Y)=s_Y^2/B\) for the sample mean.
- Stated the asymptotic hypotheses needed for block-bootstrap use in Markov
  chains.
- Added `qft_scripts/autocorrelation_resampling.py` for one-column CSV time
  series: biased autocovariances, windowed \(\tau_{\rm int}\), block means,
  blocked standard errors, delete-one-block jackknife, and block bootstrap.
- Added `calculation-checks/autocorrelation_resampling_checks.py`.
- Wired the script into `tools/run_qft_scripts_smoke.sh` and documented it.

## Verification

- Passed: `python3 qft_scripts/autocorrelation_resampling.py --smoke`
- Passed: `python3 calculation-checks/autocorrelation_resampling_checks.py`
- Passed: `python3 -m py_compile qft_scripts/autocorrelation_resampling.py calculation-checks/autocorrelation_resampling_checks.py`
- Passed: `tools/run_qft_scripts_smoke.sh`
- Passed: primitive-fraction scan on touched files.
- Passed: `git diff --check` on touched files.
- Passed: `tools/build_monograph.sh`
- Built PDF: `monograph/tex/main.pdf`, 2237 pages.

## Remaining Work

- The sampler side of #631 still needs HDF5/checkpointed SU(3) Wilson-flow
  and static-potential ensemble generation, plus production-quality
  autocorrelation treatment of correlated Wilson-loop ratios.

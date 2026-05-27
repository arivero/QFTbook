# 2026-05-27 Static-Potential Analysis Script Pass

## Scope

This pass continues issue #631 by adding a theorem-anchored finite-regulator
analysis script for rectangular Wilson-loop data.

## Substantive Additions

- Added `qft_scripts/static_potential_from_wilson_loops.py`.
- The script reads CSV data with columns `R,T,W[,dW]`.
- It computes transfer-matrix effective masses
  \(-a^{-1}\log[W(R,T+1)/W(R,T)]\).
- It computes Creutz ratios
  \(-\log[W(R,T)W(R-1,T-1)/(W(R,T-1)W(R-1,T))]\).
- It includes a smoke test on synthetic area-plus-perimeter Wilson-loop data,
  verifying \(V_{\rm eff}(R)=\sigma R+\mu\) and \(\chi(R,T)=\sigma\).
- Updated the qft-scripts smoke runner and README.
- Added `calculation-checks/static_potential_analysis_checks.py` to verify
  the script functions independently.
- Added a short manuscript pointer in Volume XI, Chapter 5 linking the script
  to the static-potential and Creutz-ratio formulas.

## Verification

- Passed: `python3 qft_scripts/static_potential_from_wilson_loops.py --smoke`
- Passed: `python3 calculation-checks/static_potential_analysis_checks.py`
- Passed: `python3 -m py_compile qft_scripts/static_potential_from_wilson_loops.py calculation-checks/static_potential_analysis_checks.py`
- Passed: `tools/run_qft_scripts_smoke.sh`
- Passed: primitive-fraction scan on touched files.
- Passed: `git diff --check` on touched files.
- Passed: `tools/build_monograph.sh`
- Built PDF: `/Users/xiyin/QFT/monograph/tex/main.pdf`, 2236 pages.

## Remaining Work

- The script is an analysis vertical slice.  The cluster-runnable sampler
  producing Wilson-loop ensembles, HDF5 output, autocorrelation-aware
  jackknife/bootstrap blocks, and SU(3) Wilson-flow measurements remain open
  parts of #631.

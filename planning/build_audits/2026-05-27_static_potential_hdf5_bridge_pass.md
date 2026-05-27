# 2026-05-27 Static-Potential HDF5 Bridge Pass

## Scope

This pass continues issue #631 by connecting the finite \(SU(3)\)
subgroup-Metropolis HDF5 measurement format directly to the static-potential
analysis script.

## Substantive Additions

- Extended `qft_scripts/static_potential_from_wilson_loops.py` with
  `--samples-hdf5`, reading
  `measurements/wilson_loops[sample,R-1,T-1]`.
- Kept the finite-regulator logic unchanged: effective masses and Creutz
  ratios are recomputed on deleted or resampled Monte Carlo blocks, so the
  covariance among rectangular Wilson loops is retained.
- Updated Volume XI, Chapter 5 to state the HDF5 data coordinate used by the
  finite \(SU(3)\) sampler.
- Updated README and dossier entries so the sampler-to-analysis interface is
  explicit.

## Verification

- Passed: `python3 -m py_compile qft_scripts/static_potential_from_wilson_loops.py calculation-checks/static_potential_analysis_checks.py`.
- Passed: `python3 qft_scripts/static_potential_from_wilson_loops.py --smoke`.
- Passed: `python3 calculation-checks/static_potential_analysis_checks.py`,
  including the HDF5 bridge check with bundled Python and `h5py`.
- Passed: primitive-fraction scan on touched files.
- Passed: `git diff --check` on touched files.
- Passed: `tools/build_monograph.sh`; produced
  `monograph/tex/main.pdf` with 2243 pages.

## Remaining Work

- This pass is an analysis-interface improvement.  It does not supply the
  production-scale SU(3) HMC code, glueball GEVP pipeline, static-potential
  excited-state variational analysis, or SLURM/MPI orchestration still scoped
  under issue #631.

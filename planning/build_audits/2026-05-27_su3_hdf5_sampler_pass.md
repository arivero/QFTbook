# 2026-05-27 SU(3) HDF5 Sampler Pass

## Scope

This pass continues issue #631 by adding the first checkpointed finite
\(SU(3)\) Wilson-gauge data generator in `qft_scripts/`.

## Substantive Additions

- Added `qft_scripts/su3_gauge_4d_metropolis_hdf5.py`, a finite periodic
  four-dimensional pure \(SU(3)\) Wilson-lattice subgroup-Metropolis sampler.
- The Markov proposal uses small left multiplications in the three embedded
  \(SU(2)\) color-pair subgroups, matching the finite subgroup-invariance
  theorem in Volume XI, Chapter 6.
- The script measures normalized plaquettes and rectangular Wilson loops,
  writes `sample,R,T,W` CSV files for the static-potential resampling script,
  and writes HDF5 files with measurements, metadata, final link checkpoint,
  and pseudorandom-generator state when `h5py` is available.
- Added `calculation-checks/su3_hdf5_sampler_checks.py`, which verifies
  embedded subgroup proposals, local score changes, gauge invariance, the
  \(1\times1\) Wilson-loop/plaquette identity, and HDF5
  measurement/checkpoint layout.
- Wired the new sampler into `tools/run_qft_scripts_smoke.sh` and documented
  it in `qft_scripts/README.md`.

## Verification

- Passed: `python3 qft_scripts/su3_gauge_4d_metropolis_hdf5.py --smoke`.
- Passed: HDF5 run with bundled Python and `h5py`, including sample CSV
  export.
- Passed: `python3 calculation-checks/su3_hdf5_sampler_checks.py`.
- Passed: `python3 -m py_compile qft_scripts/su3_gauge_4d_metropolis_hdf5.py calculation-checks/su3_hdf5_sampler_checks.py`.
- Passed: `tools/run_qft_scripts_smoke.sh`.
- Passed: primitive-fraction scan on touched files.
- Passed: `git diff --check` on touched files.
- Passed: `tools/build_monograph.sh`; the rebuilt PDF has 2240 pages.

## Remaining Work

- This is still a local finite-regulator generator, not a full cluster
  workflow.  The next steps for #631 are SLURM/MPI orchestration, Wilson-flow
  evolution of saved configurations, and stronger continuum-control examples.

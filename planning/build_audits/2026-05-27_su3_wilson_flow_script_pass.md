# 2026-05-27 SU(3) Wilson-Flow Script Pass

## Scope

This pass continues issue #631 by adding the first finite \(SU(3)\)
Wilson-flow evolution tool for checkpointed lattice gauge configurations.

## Substantive Additions

- Added `qft_scripts/su3_wilson_flow_hdf5.py`, a finite periodic \(SU(3)\)
  Wilson-score gradient-flow script.
- Added the explicit normalized \(SU(3)\) Wilson-flow force to Volume XI,
  Chapter 5:
  \(Z_\mu(x;U)=-\frac13[U_\mu(x)C_\mu(x;U)]_{\mathfrak{su}(3)}\).
- The manuscript now derives the force by a left directional derivative of
  the normalized plaquette score and proves finite score monotonicity.
- The script reads the sampler's `checkpoint/links` HDF5 dataset, or creates
  hot/cold finite links, and writes flow-time, plaquette, action-density, and
  final-link datasets.
- Added `calculation-checks/su3_wilson_flow_checks.py`, which verifies the
  force by directional derivatives, one-step gauge covariance, monotonicity,
  group preservation, and the sampler-to-flow HDF5 pipeline.

## Verification

- Passed: `python3 qft_scripts/su3_wilson_flow_hdf5.py --smoke`.
- Passed: HDF5 sampler-to-flow pipeline with bundled Python and `h5py`.
- Passed: `python3 calculation-checks/su3_wilson_flow_checks.py`.
- Passed: `python3 -m py_compile qft_scripts/su3_wilson_flow_hdf5.py calculation-checks/su3_wilson_flow_checks.py`.
- Passed: `tools/run_qft_scripts_smoke.sh`.
- Passed: primitive-fraction scan on touched files.
- Passed: `git diff --check` on touched files.
- Passed: `tools/build_monograph.sh`; the rebuilt PDF has 2242 pages.

## Remaining Work

- This pass supplies flow evolution of saved configurations but does not yet
  define a geometric or index-theoretic topological charge pipeline.  The
  next #631 numerical steps are topological-charge diagnostics, SLURM/MPI
  orchestration, and stronger continuum-control examples.

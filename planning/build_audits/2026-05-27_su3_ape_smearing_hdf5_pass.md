# 2026-05-27 SU(3) APE-Smearing HDF5 Pass

## Scope

This pass continues issue #631 by adding a finite \(SU(3)\) APE-smearing
post-processing layer for HDF5 lattice configurations.

## Substantive Additions

- Added `qft_scripts/su3_ape_smearing_hdf5.py`, implementing finite APE
  smearing for raw, flowed, or already-smeared checkpoints.
- The script supports spatial mode, leaving temporal links unchanged for
  static-line operator construction, and all-direction mode for fully
  Euclidean smearing.
- The output HDF5 file records the plaquette trajectory and
  `checkpoint/smeared_links`.
- Added `calculation-checks/su3_ape_smearing_checks.py`, verifying the cold
  fixed point, spatial-mode temporal-link preservation, gauge covariance, and
  sampler-to-smearing plus smearing-to-smearing HDF5 layout.
- Updated Volume XI, Chapter 5 and dossier/README entries so the smearing map
  is tied to a checked finite-data companion.

## Verification

- Passed: `python3 -m py_compile qft_scripts/su3_ape_smearing_hdf5.py calculation-checks/su3_ape_smearing_checks.py`.
- Passed: `python3 qft_scripts/su3_ape_smearing_hdf5.py --smoke`.
- Passed: `python3 calculation-checks/su3_ape_smearing_checks.py`.
- Passed: `tools/run_qft_scripts_smoke.sh`.
- Passed: primitive-fraction scan on touched files.
- Passed: `git diff --check` on touched files.
- Passed: `tools/build_monograph.sh`; produced
  `monograph/tex/main.pdf` with 2244 pages.

## Remaining Work

- This pass supplies the smearing layer only.  Static-potential excited-state
  variational analysis, glueball GEVP operators, production-scale HMC, and
  SLURM/MPI orchestration remain open under issue #631.

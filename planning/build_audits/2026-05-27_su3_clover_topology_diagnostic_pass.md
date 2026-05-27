# 2026-05-27 SU(3) Clover Topology Diagnostic Pass

## Scope

This pass continues issue #631 by adding a finite-regulator \(SU(3)\) clover
topological-charge diagnostic for raw and flowed lattice configurations.

## Substantive Additions

- Added `qft_scripts/su3_topological_charge_diagnostics_hdf5.py`, a finite
  \(SU(3)\) clover diagnostic script.
- Added the oriented-link and oriented-plaquette conventions to Volume XI,
  Chapter 5, including the clover curvature
  \(F_{\mu\nu}^{\rm cl}=\frac14[C_{\mu\nu}^{\rm cl}]_{\mathfrak{su}(3)}\).
- Added the finite diagnostic
  \(Q_{\rm clover}=(32\pi^2)^{-1}\sum_x\epsilon_{\mu\nu\rho\sigma}
  \operatorname{Re}\operatorname{Tr}(F_{\mu\nu}^{\rm cl}F_{\rho\sigma}^{\rm cl})\),
  with a proof of gauge invariance.
- The manuscript explicitly distinguishes \(Q_{\rm clover}\) from the
  admissible geometric or index-theoretic topological charge.
- Added `calculation-checks/su3_topological_charge_diagnostics_checks.py`,
  which verifies orientation conventions, cold-configuration vanishing,
  clover anti-Hermiticity/tracelessness/antisymmetry, gauge invariance, and
  the sampler-to-flow-to-topology HDF5 pipeline.

## Verification

- Passed: `python3 qft_scripts/su3_topological_charge_diagnostics_hdf5.py --smoke`.
- Passed: HDF5 sampler-to-flow-to-topology pipeline with bundled Python and
  `h5py`, including flowed-checkpoint auto-detection and optional local-density
  output.
- Passed: `python3 calculation-checks/su3_topological_charge_diagnostics_checks.py`.
- Passed: `python3 -m py_compile qft_scripts/su3_topological_charge_diagnostics_hdf5.py calculation-checks/su3_topological_charge_diagnostics_checks.py`.
- Passed: `tools/run_qft_scripts_smoke.sh`.
- Passed: primitive-fraction scan on touched files.
- Passed: `git diff --check` on touched files.
- Passed: `tools/build_monograph.sh`; produced
  `monograph/tex/main.pdf` with 2243 pages.

## Remaining Work

- This pass supplies the finite clover diagnostic.  It does not construct an
  admissible geometric charge, a chiral-Dirac index charge, or a continuum
  theta-sector pipeline.  Those remain natural next steps for #631.

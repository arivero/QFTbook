# QFT Companion Scripts

This directory contains small reader-facing finite-regulator demonstrations
for the monograph.  They are distinct from `calculation-checks/`: calculation
checks certify signs and formulae used directly in the text, while companion
scripts illustrate numerical regulator frameworks.

Quick smoke run:

```bash
tools/run_qft_scripts_smoke.sh
```

Individual examples:

```bash
python3 qft_scripts/ising2d_metropolis.py --smoke
python3 qft_scripts/z2_gauge_3d_metropolis.py --smoke
python3 qft_scripts/su2_gauge_4d_metropolis.py --smoke
python3 qft_scripts/su2_gauge_4d_heatbath_overrelaxation.py --smoke
python3 qft_scripts/su3_gauge_4d_metropolis_hdf5.py --smoke
python3 qft_scripts/su3_wilson_flow_hdf5.py --smoke
python3 qft_scripts/su3_topological_charge_diagnostics_hdf5.py --smoke
python3 qft_scripts/autocorrelation_resampling.py --smoke
python3 qft_scripts/static_potential_from_wilson_loops.py --smoke
python3 qft_scripts/glueball_gevp_from_correlators.py --smoke
python3 qft_scripts/tcsa_ising_energy_benchmark.py --smoke
python3 qft_scripts/tffsa_ising_spin_connected.py --smoke
python3 qft_scripts/tffsa_ising_spectral_flow.py --smoke
python3 qft_scripts/thooft_dlcq.py --smoke
python3 qft_scripts/thooft_dlcq_extrapolation.py --smoke
```

The scripts use Python 3 and NumPy.  Their output is JSON so that future
notebooks or CI checks can consume the results without scraping prose.

## Cluster Templates

`qft_scripts/cluster/` contains SLURM and SSH-control templates for running
the finite-regulator scripts on a cluster without storing authentication
secrets.  The first vertical slice,
`qft_scripts/cluster/slurm/su3_small_pipeline.sbatch`, runs the SU(3) HDF5
sampler, Wilson flow, and static-potential extraction into one results
directory.  It is a reproducibility wrapper for a small cluster smoke run, not
a production lattice-QCD workflow or a continuum extrapolation.

## Scripts

- `ising2d_metropolis.py`: finite two-dimensional Ising Metropolis sampler
  with periodic boundary conditions.  It demonstrates detailed balance and
  autocorrelation diagnostics at finite volume.
- `z2_gauge_3d_metropolis.py`: finite three-dimensional \(\mathbb Z_2\)
  lattice gauge sampler with plaquette and rectangular Wilson-loop
  measurements.  It demonstrates compact gauge variables, gauge-invariant
  observables, and a small phase-scan benchmark at finite cutoff.
- `su2_gauge_4d_metropolis.py`: finite four-dimensional \(SU(2)\) lattice
  gauge sampler with unit-quaternion links, Haar-symmetric local proposals,
  plaquette measurements, and rectangular Wilson loops.  It demonstrates the
  compact nonabelian link structure at finite cutoff; it is not a production
  heat-bath, HMC, or continuum-extrapolation code.
- `su2_gauge_4d_heatbath_overrelaxation.py`: finite four-dimensional
  \(SU(2)\) Wilson-lattice sampler using exact single-link heat-bath
  conditionals for the staple density, optionally interleaved with
  deterministic overrelaxation sweeps.  It illustrates the finite conditional
  measure and microcanonical reflection described in the monograph; it is not
  a continuum extrapolation or a production error-analysis framework.
- `su3_gauge_4d_metropolis_hdf5.py`: finite four-dimensional \(SU(3)\)
  Wilson-gauge subgroup-Metropolis sampler using the embedded \(SU(2)\)
  color-pair updates described in the monograph.  It writes HDF5 measurement
  and checkpoint files when `h5py` is available, and can also export
  `sample,R,T,W` CSV data for the static-potential analysis script.  It is a
  small finite-regulator data generator, not a production lattice-QCD code.
- `su3_wilson_flow_hdf5.py`: finite \(SU(3)\) Wilson-score gradient-flow
  evolution for saved link checkpoints.  It reads the HDF5 checkpoint format
  written by the subgroup-Metropolis script, records plaquette/action-density
  flow trajectories and final flowed links, and exposes a smoke test that
  checks monotonicity and group preservation at finite cutoff.  It is not an
  integer topological-charge definition or a continuum extrapolation.
- `su3_ape_smearing_hdf5.py`: finite \(SU(3)\) APE-smearing utility for raw,
  flowed, or already-smeared HDF5 checkpoints.  Spatial mode leaves temporal
  links unchanged and is intended for static-line operator construction; all
  mode smears every Euclidean direction.  The script records the plaquette
  trajectory and final smeared links, and its calculation check verifies
  gauge covariance and HDF5 auto-dataset behavior.
- `su3_topological_charge_diagnostics_hdf5.py`: finite \(SU(3)\) clover
  curvature and topological-charge diagnostic for raw or flowed HDF5
  checkpoints.  It reports \(Q_{\rm clover}\), clover action density, and an
  admissibility-style plaquette-deviation diagnostic, and can optionally write
  local density arrays.  It is explicitly not a geometric or index-theoretic
  definition of a lattice topological sector.
- `autocorrelation_resampling.py`: one-column Markov-chain time-series
  diagnostics.  It computes biased autocorrelations, a windowed integrated
  autocorrelation time, block means, blocked standard errors,
  delete-one-block jackknife errors, and block-bootstrap errors.
- `static_potential_from_wilson_loops.py`: finite-regulator analysis tool for
  positive rectangular Wilson-loop data.  It computes transfer-matrix
  effective-mass ratios and Creutz ratios from aggregate CSV input, and it
  has sample-level CSV and HDF5 modes that recompute those nonlinear ratios
  on deleted or resampled Monte Carlo blocks for correlated
  jackknife/bootstrap errors.  The HDF5 mode reads the subgroup-Metropolis
  dataset `measurements/wilson_loops` with index convention
  `wilson_loops[sample,R-1,T-1]`.  The smoke test uses synthetic
  area-plus-perimeter data.
- `glueball_gevp_from_correlators.py`: finite-regulator GEVP analysis tool
  for Hermitian correlator matrices with CSV columns `t,i,j,C` or
  `t,i,j,real,imag`.  It solves `C(t) v = lambda C(t0) v` by positive
  whitening of `C(t0)` and reports effective energies
  `-log(lambda)/(a(t-t0))`.  The smoke test uses an exact two-state
  spectral matrix, so any deviation is a finite linear-algebra error.
- `tcsa_ising_energy_benchmark.py`: exactly solvable Hamiltonian truncation
  benchmark for the Ising thermal deformation, written as finite Majorana
  Bogoliubov blocks.
- `tffsa_ising_spin_connected.py`: finite zero-momentum TFFSA-style
  connected-block benchmark for the massive Ising spin perturbation.  It
  assembles off-diagonal form-factor matrix elements in a free-fermion basis
  and declares its diagonal convention explicitly; it is not a production
  magnetic-Ising spectrum calculation.
- `tffsa_ising_spectral_flow.py`: finite spectral-flow diagnostic for the
  connected Ising TFFSA block.  It diagonalizes the finite matrix on a grid of
  magnetic couplings and checks Hellmann-Feynman slopes against centered
  finite differences; it is a finite-matrix benchmark, not a continuum
  magnetic-Ising or \(E_8\) spectrum claim.
- `thooft_dlcq.py`: finite harmonic-resolution matrix for the large-\(N\)
  two-dimensional QCD meson equation.  It is a DLCQ-style principal-value
  regulator, not a proof of the continuum spectrum.
- `thooft_dlcq_extrapolation.py`: large-\(K\) diagnostic for fixed eigenvalue
  labels of the finite 't Hooft DLCQ matrices.  It reports polynomial fits in
  \(K^{-\omega}\), residuals, conditioning, and the finite linear-algebra
  amplification factor for a possible remainder bound; it does not assert a
  continuum meson spectrum without the missing analytic large-\(K\) estimate.

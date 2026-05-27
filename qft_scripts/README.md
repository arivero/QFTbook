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
python3 qft_scripts/autocorrelation_resampling.py --smoke
python3 qft_scripts/static_potential_from_wilson_loops.py --smoke
python3 qft_scripts/tcsa_ising_energy_benchmark.py --smoke
python3 qft_scripts/tffsa_ising_spin_connected.py --smoke
python3 qft_scripts/thooft_dlcq.py --smoke
```

The scripts use Python 3 and NumPy.  Their output is JSON so that future
notebooks or CI checks can consume the results without scraping prose.

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
- `autocorrelation_resampling.py`: one-column Markov-chain time-series
  diagnostics.  It computes biased autocorrelations, a windowed integrated
  autocorrelation time, block means, blocked standard errors,
  delete-one-block jackknife errors, and block-bootstrap errors.
- `static_potential_from_wilson_loops.py`: finite-regulator analysis tool for
  positive rectangular Wilson-loop data.  It computes transfer-matrix
  effective-mass ratios and Creutz ratios from aggregate CSV input, and it
  has a sample-level CSV mode that recomputes those nonlinear ratios on
  deleted or resampled Monte Carlo blocks for correlated jackknife/bootstrap
  errors.  The smoke test uses synthetic area-plus-perimeter data.
- `tcsa_ising_energy_benchmark.py`: exactly solvable Hamiltonian truncation
  benchmark for the Ising thermal deformation, written as finite Majorana
  Bogoliubov blocks.
- `tffsa_ising_spin_connected.py`: finite zero-momentum TFFSA-style
  connected-block benchmark for the massive Ising spin perturbation.  It
  assembles off-diagonal form-factor matrix elements in a free-fermion basis
  and declares its diagonal convention explicitly; it is not a production
  magnetic-Ising spectrum calculation.
- `thooft_dlcq.py`: finite harmonic-resolution matrix for the large-\(N\)
  two-dimensional QCD meson equation.  It is a DLCQ-style principal-value
  regulator, not a proof of the continuum spectrum.

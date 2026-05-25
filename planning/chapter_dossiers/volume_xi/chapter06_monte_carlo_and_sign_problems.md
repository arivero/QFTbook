# Chapter 06: Monte Carlo Methods And Sign Problems

## Source Position

This chapter follows Wilson lattice gauge theory by describing how
finite-regulator Euclidean integrals are estimated and where positivity
breaks down.  It prepares later numerical and lattice-continuum comparison
chapters.

## Notation Inventory

- `Omega_Lambda`: finite-dimensional regulator space.
- `nu_Lambda`: positive sampling probability measure.
- `P(Phi,dPhi')`: Markov transition kernel.
- `O_bar_N`: sample average estimator.
- `tau_int(O)`: integrated autocorrelation time.
- `Theta`: phase of a complex Euclidean weight.
- `D[U]`: lattice fermion operator in a background gauge field.
- `Lambda_L`, `s`, `H_L`, `pi_beta`: finite periodic Ising lattice,
  spin configuration, finite Hamiltonian, and Boltzmann probability.
- `P(s,s')`, `a(s,x)`: single-spin Metropolis transition probability and
  acceptance probability.

## Claim Ledger

- Defines finite-regulator expectation values as finite-dimensional
  probability integrals.
- States the detailed-balance condition and convergence role of Markov-chain
  hypotheses.
- Proves detailed balance, irreducibility, and aperiodicity for the finite
  single-spin Metropolis chain in the two-dimensional periodic Ising model.
- Derives the variance formula with integrated autocorrelation time.
- Derives exponential degradation of phase reweighting from the average
  phase.
- Separates finite-lattice numerical estimates from continuum QFT claims.
- Adds the companion script `qft_scripts/ising2d_metropolis.py` as a
  finite-regulator demonstration with a smoke-mode algorithm check.

## Figure Ledger

No figure is included.  Future figures should show the reweighting ratio and
the exponential decay of average phase with volume.

## Companion Scripts

- `qft_scripts/ising2d_metropolis.py --smoke`: finite periodic Ising
  Metropolis sampler.  Certifies the implemented finite chain and reports
  acceptance, energy, magnetization, and a windowed autocorrelation estimate.
  It does not certify a continuum limit.

## Calculation Checks

- `calculation-checks/ising_metropolis_finite_checks.py` enumerates the
  \(2\times2\) periodic Ising chain and verifies the companion script's local
  energy difference and detailed-balance identity exactly at finite volume.

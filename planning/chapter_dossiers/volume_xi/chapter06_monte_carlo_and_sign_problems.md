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
- `pi`: stationary finite-chain probability vector.
- `C_O(t)`: connected stationary autocorrelation function.
- `tau_int(O)`: integrated autocorrelation time.
- `Theta`: phase of a complex Euclidean weight.
- `Z`, `Z_R`, `Delta f`: target partition function,
  phase-quenched partition function, and average-phase free-energy
  difference.
- `D[U]`: lattice fermion operator in a background gauge field.
- `Gamma`: finite lattice chirality involution in the determinant-positivity
  discussion.
- `Lambda_L`, `s`, `H_L`, `pi_beta`: finite periodic Ising lattice,
  spin configuration, finite Hamiltonian, and Boltzmann probability.
- `P(s,s')`, `a(s,x)`: single-spin Metropolis transition probability and
  acceptance probability.
- `Q(U)`: total plaquette score in the finite \(\mathbb Z_2\) gauge model.
- `B_e(U)`: sum of plaquettes containing a link \(e\).
- `U^e`: gauge configuration obtained by flipping the link \(e\).

## Claim Ledger

- Defines finite-regulator expectation values as finite-dimensional
  probability integrals.
- States the detailed-balance condition and convergence role of Markov-chain
  hypotheses.
- Proves the finite-state ergodic theorem by a primitive-power/minorization
  contraction argument, separating finite-regulator convergence from
  continuum limits.
- Proves detailed balance, irreducibility, and aperiodicity for the finite
  single-spin Metropolis chain in the two-dimensional periodic Ising model.
- Proves detailed balance and irreducibility for the finite single-link
  Metropolis chain in the periodic \(\mathbb Z_2\) lattice gauge model, and
  separates full link-space sampling from gauge-orbit interpretation.
- Proves the exact finite-\(N\) autocorrelation variance identity and derives
  the integrated-autocorrelation asymptotic under absolute summability.
- Defines the average phase as \(Z/Z_R\), defines the finite-volume
  free-energy difference \(\Delta f\), and proves the relative-variance lower
  bound behind exponential phase-reweighting degradation.
- Separates \(\gamma_5\)-Hermiticity, determinant reality, and positivity
  after even-degenerate or conjugate flavor pairing.
- Separates finite-lattice numerical estimates from continuum QFT claims.
- Adds the companion script `qft_scripts/ising2d_metropolis.py` as a
  finite-regulator demonstration with a smoke-mode algorithm check.
- Adds the companion script `qft_scripts/z2_gauge_3d_metropolis.py` as a
  compact-gauge finite-regulator demonstration measuring plaquettes and
  Wilson loops.

## Figure Ledger

No figure is included.  Future figures should show the reweighting ratio and
the exponential decay of average phase with volume.

## Companion Scripts

- `qft_scripts/ising2d_metropolis.py --smoke`: finite periodic Ising
  Metropolis sampler.  Certifies the implemented finite chain and reports
  acceptance, energy, magnetization, and a windowed autocorrelation estimate.
  It does not certify a continuum limit.
- `qft_scripts/z2_gauge_3d_metropolis.py --smoke`: finite periodic
  \(\mathbb Z_2\) gauge Metropolis sampler.  Certifies a compact gauge
  single-link update and reports plaquette and Wilson-loop measurements for a
  small beta scan.  It does not certify an infinite-volume transition or a
  continuum limit.

## Calculation Checks

- `calculation-checks/ising_metropolis_finite_checks.py` enumerates the
  \(2\times2\) periodic Ising chain and verifies the companion script's local
  energy difference and detailed-balance identity exactly at finite volume.
- `calculation-checks/z2_gauge_metropolis_checks.py` verifies the companion
  script's local score change, detailed-balance identity, gauge invariance,
  and the \(1\times1\) Wilson-loop/plaquette identity.
- `calculation-checks/monte_carlo_sign_problem_checks.py` verifies the
  finite-\(N\) autocorrelation variance identity, phase-reweighting identity,
  average-phase relative-variance bound, and the determinant
  reality/positivity distinction in finite examples.

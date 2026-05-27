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
- `U_{x,mu}`: compact \(SU(2)\) link variable on a four-dimensional
  periodic hypercubic lattice.
- `U_{x;mu nu}`: oriented \(SU(2)\) plaquette variable.
- `Q(U)=sum_p 1/2 Re tr U_p`: finite Wilson plaquette score for the
  \(SU(2)\) companion chain.
- `kappa(dR)`: inversion-symmetric local \(SU(2)\) proposal law.
- `W_{R,T}`: rectangular Wilson-loop observable, averaged over translations
  and coordinate planes.
- `Q_Lambda`: finite-dimensional HMC configuration manifold.
- `Gamma_Lambda`, `lambda`: finite-dimensional HMC phase space and
  reference measure.
- `H(q,p)`: extended HMC Hamiltonian
  \(S(q)+\frac12 p^T M^{-1}p\) in Euclidean coordinates.
- `R(q,p)=(q,-p)`: momentum-flip involution.
- `Phi`, `G=R Phi`: reversible trajectory map and involutive Metropolis
  proposal.
- `K_a`, `D_epsilon`, `L_epsilon`: leapfrog kick, drift, and one-step
  leapfrog map.
- `A=D^\dagger D`: positive Hermitian fermion matrix after flavor pairing.
- `phi`: complex pseudofermion vector.
- `r_m(A)`: positive rational approximation to \(A^{-\alpha}\) in RHMC.

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
- Defines finite compact \(SU(2)\) lattice gauge sampling with product Haar
  measure and Wilson plaquette score \(Q(U)=\sum_p\frac12\operatorname{Re}
  \operatorname{tr}U_p\).
- Proves pairwise detailed balance for a compact \(SU(2)\) local-link
  Metropolis chain with inversion-symmetric proposal law, and states the
  Haar-irreducibility condition without claiming continuum convergence.
- Defines gauge transformations and rectangular Wilson-loop measurements for
  the finite \(SU(2)\) script.
- Proves the finite-regulator HMC Metropolis-correction theorem from
  volume preservation, reversibility, and the momentum-flip involution.
- Proves leapfrog volume preservation and reversibility in finite Euclidean
  phase space by block-triangular Jacobian and kick/drift conjugation.
- Explains the compact-gauge HMC analogue on a finite cotangent bundle with
  Haar/Liouville measure, while leaving force construction and ergodicity as
  separate regulator-dependent data.
- Proves the pseudofermion determinant identity
  \(\int e^{-\phi^\dagger A^{-1}\phi}=\pi^N\det A\) for positive Hermitian
  finite matrices by unitary diagonalization.
- States RHMC as exact sampling of a rationalized finite determinant
  \(1/\det r_m(A)\), and separates that theorem from any approximation or
  reweighting claim for \(\det A^\alpha\).
- Proves the pointwise spectral action-error bound
  \(|\phi^\dagger(r_m(A)-A^{-\alpha})\phi|\le\delta\|\phi\|^2\).
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
- Adds the companion script `qft_scripts/su2_gauge_4d_metropolis.py` as a
  compact nonabelian finite-regulator demonstration with unit-quaternion
  \(SU(2)\) links and Wilson loops.

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
- `qft_scripts/su2_gauge_4d_metropolis.py --smoke`: finite periodic
  four-dimensional \(SU(2)\) gauge Metropolis sampler with unit-quaternion
  links.  Certifies a Haar-symmetric local compact-link proposal and reports
  plaquette and Wilson-loop measurements.  It does not certify a heat-bath
  algorithm, HMC/RHMC implementation, or a continuum limit.

## Calculation Checks

- `calculation-checks/ising_metropolis_finite_checks.py` enumerates the
  \(2\times2\) periodic Ising chain and verifies the companion script's local
  energy difference and detailed-balance identity exactly at finite volume.
- `calculation-checks/z2_gauge_metropolis_checks.py` verifies the companion
  script's local score change, detailed-balance identity, gauge invariance,
  and the \(1\times1\) Wilson-loop/plaquette identity.
- `calculation-checks/su2_gauge_metropolis_checks.py` verifies the companion
  script's quaternion group operations, local score change,
  detailed-balance identity, gauge invariance, and the \(1\times1\)
  Wilson-loop/plaquette identity.
- `calculation-checks/hmc_pseudofermion_checks.py` verifies the finite HMC
  and pseudofermion algebra: one-dimensional leapfrog determinant one,
  leapfrog reversibility, pairwise Metropolis balance, the diagonalized
  pseudofermion determinant identity, and the RHMC spectral action-error
  bound.
- `calculation-checks/monte_carlo_sign_problem_checks.py` verifies the
  finite-\(N\) autocorrelation variance identity, phase-reweighting identity,
  average-phase relative-variance bound, and the determinant
  reality/positivity distinction in finite examples.

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
- `b`, `B`, `Y_j`: block length, number of complete blocks, and block means
  in finite Markov-chain error analysis.
- `se_block`, `Var_jack`: blocked standard-error and delete-one-block
  jackknife variance coordinates.
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
- `nu(x|y)`: regular conditional probability used in the heat-bath theorem.
- `K_HB`: coordinate heat-bath kernel.
- `V_e=c_e W_e`: \(SU(2)\) staple polar form for a selected link.
- `x_0`: scalar quaternion coordinate in the \(SU(2)\) heat-bath density
  \(\sqrt{1-x_0^2}e^{\beta c_e x_0}\).
- `O_{W_e}(U_e)=W_e^{-1}U_e^{-1}W_e^{-1}`: single-link
  overrelaxation involution.
- `H_{12},H_{13},H_{23}`: embedded \(SU(2)\) subgroups of \(SU(3)\) acting
  on color-pair planes.
- `V_e`: \(SU(3)\) local staple matrix in
  \(Q_e(U_e)=\frac13\operatorname{Re}\operatorname{Tr}_3(U_eV_e)+Q_{\widehat e}\).
- `nu_{alpha,e}(h|U)`: conditional subgroup density for an \(SU(3)\)
  Cabibbo-Marinari type link update.
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
- Proves exact coordinate heat-bath detailed balance from regular
  conditional probabilities.
- Derives the local \(SU(2)\) Wilson-link conditional density in terms of the
  staple polar form \(V_e=c_eW_e\) and the scalar quaternion density
  \(\sqrt{1-x_0^2}e^{\beta c_ex_0}\).
- Defines the \(SU(2)\) overrelaxation map
  \(U_e\mapsto W_e^{-1}U_e^{-1}W_e^{-1}\), proves it is an involution,
  proves local-score preservation, and proves finite Wilson-measure
  invariance.
- Defines the three embedded \(SU(2)\) color-pair subgroups of \(SU(3)\),
  proves that their Lie algebras span \(\mathfrak{su}(3)\), and explains why
  the \(SU(3)\) staple matrix does not reduce to the special
  \(SU(2)\) polar form.
- Defines exact finite subgroup heat-bath and Metropolis kernels for an
  \(SU(3)\) link, proves detailed balance on the subgroup orbit, and records
  the precise boundary between invariant-measure preservation and claims about
  mixing, topological freezing, or continuum extrapolation.
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
- Defines block means and proves the delete-one-block jackknife identity for
  the sample mean, \(\operatorname{Var}_{\rm jack}=s_Y^2/B\), while stating
  the Markov-chain hypotheses needed for blocked bootstrap use.
- Proves a finite Taylor bound for correlated delete-one-block jackknife
  errors of smooth nonlinear observables, with Wilson-loop effective masses
  and Creutz ratios as the principal example.
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
- Adds the companion script
  `qft_scripts/su2_gauge_4d_heatbath_overrelaxation.py` as an exact
  single-link heat-bath and deterministic-overrelaxation finite-regulator
  demonstration for the \(SU(2)\) Wilson lattice action.
- Adds the companion script `qft_scripts/autocorrelation_resampling.py` for
  autocorrelation, blocking, delete-one-block jackknife, and block-bootstrap
  diagnostics on one-column time series.
- Connects the static-potential analysis script's sample-level mode to the
  correlated jackknife construction for nonlinear Wilson-loop ratios.

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
- `qft_scripts/su2_gauge_4d_heatbath_overrelaxation.py --smoke`: finite
  periodic four-dimensional \(SU(2)\) Wilson sampler using exact single-link
  heat-bath conditionals for the staple density, interleaved with optional
  overrelaxation sweeps.  It reports plaquette and Wilson-loop measurements.
  It does not certify autocorrelation error estimates, thermodynamic limits,
  or continuum extrapolation.
- `qft_scripts/autocorrelation_resampling.py --smoke`: finite time-series
  diagnostic script.  It reports a windowed integrated autocorrelation
  coordinate, block means, blocked standard errors, delete-one-block
  jackknife errors, and block-bootstrap errors.
- `qft_scripts/static_potential_from_wilson_loops.py --smoke`: also certifies
  the sample-level mode that recomputes static-potential logarithmic ratios
  on deleted or resampled Monte Carlo blocks.

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
- `calculation-checks/heatbath_overrelaxation_checks.py` verifies finite
  conditional heat-bath balance, \(SU(2)\) staple reduction, overrelaxation
  involution, local score preservation, and orthogonality of the
  overrelaxation map on \(S^3\), plus the local-staple and unit-link
  identities in `qft_scripts/su2_gauge_4d_heatbath_overrelaxation.py`.
- `calculation-checks/su3_lattice_update_checks.py` verifies embedded
  \(SU(2)\) unitarity and determinant one, the
  \(\mathfrak{su}(3)\) span from the three color-pair subgroups, subgroup
  commutators, local staple-score gauge covariance, and Metropolis pairwise
  balance.
- `calculation-checks/hmc_pseudofermion_checks.py` verifies the finite HMC
  and pseudofermion algebra: one-dimensional leapfrog determinant one,
  leapfrog reversibility, pairwise Metropolis balance, the diagonalized
  pseudofermion determinant identity, and the RHMC spectral action-error
  bound.
- `calculation-checks/monte_carlo_sign_problem_checks.py` verifies the
  finite-\(N\) autocorrelation variance identity, phase-reweighting identity,
  average-phase relative-variance bound, and the determinant
  reality/positivity distinction in finite examples.
- `calculation-checks/autocorrelation_resampling_checks.py` verifies the
  finite block means, blocked standard error, delete-one-block jackknife
  identity, biased autocovariances, and windowed \(\tau_{\rm int}\) used by
  the companion script.
- `calculation-checks/static_potential_analysis_checks.py` includes the
  correlated delete-one jackknife check for static-potential nonlinear
  Wilson-loop ratios.

## Audit Notes

- 2026-05-27 issue #631 pass: added explicit \(SU(3)\) lattice subgroup
  update material.  This fills the previous gap where the chapter had only
  \(SU(2)\) compact-gauge algorithms, and it states the finite-regulator
  invariant-measure theorem without promoting subgroup reachability to a
  continuum or rapid-mixing theorem.
- 2026-05-27 issue #631 pass: added blocking/jackknife/bootstrap error
  coordinates and a theorem-anchored time-series diagnostic script, providing
  the upstream error layer needed for Wilson-loop and flowed-observable
  analysis.
- 2026-05-27 issue #631 pass: added the correlated nonlinear jackknife Taylor
  estimate and tied it to the static-potential script's sample-level
  resampling mode.

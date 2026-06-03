# Chapter 06: Monte Carlo Methods And Sign Problems

## Source Position

This chapter follows Wilson lattice gauge theory by describing how
finite-regulator Euclidean integrals are estimated and where positivity
breaks down.  It prepares later numerical and lattice-continuum comparison
chapters.  The front of the chapter now fixes a production-evidence
architecture that separates finite target measure, invariant kernel theorem,
implementation-defect record, estimator/error record, observable-analysis map,
and scaling-window inference.

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
- `phi_x`, `S_L(phi)`, `m^2`, `lambda`: finite scalar lattice field,
  Euclidean action, mass coordinate, and quartic coupling in the
  two-dimensional \(\phi^4\) Metropolis warmup.
- `Delta S_x`: local single-site scalar action difference for the symmetric
  Metropolis proposal.
- `r(eta)`, `delta`: symmetric single-site proposal density and uniform
  proposal half-width in the scalar \(\phi^4\) companion script.
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
- `Q(U)=sum_p 1/3 Re Tr_3 U_p`: normalized finite \(SU(3)\) Wilson
  plaquette score used by the HDF5 companion sampler.
- `sample,R,T,W`: sample-level Wilson-loop table coordinates exported by
  the finite \(SU(3)\) generator and consumed by the static-potential script.
- `measurements/wilson_loops[sample,R-1,T-1]`: HDF5 Wilson-loop coordinate
  written by the \(SU(3)\) sampler and read by the static-potential script.
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
- `Delta H`, `Delta_rev`, `rho_lin`: finite HMC Hamiltonian change,
  reversibility defect, and linear-solver residual diagnostics.
- `lambda_-`, `W_rat`: spectral lower bound for the positive fermion matrix
  and RHMC determinant reweighting factor.
- `O_hat_a`, `s_a`, `N_a^eff`, `w_a`: chain-level estimate, declared
  standard error, optional effective sample size, and inverse-variance weight
  in the cluster independent-chain aggregation record.
- `chi^2_chain`, `nu_chain`: between-chain disagreement coordinate and
  formal residual degree count for a finite job-array estimator record.

## Claim Ledger

- Defines a production evidence architecture for lattice Monte Carlo outputs:
  target finite measure, invariant Markov kernel, implementation-defect
  record, estimator and covariance analysis, nonlinear observable map, and
  scaling-window evidence package in the sense of Volume XI Chapter 4.
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
- Adds the companion script `qft_scripts/su3_gauge_4d_metropolis_hdf5.py` as
  a finite \(SU(3)\) Wilson-gauge subgroup-Metropolis data generator with
  HDF5 measurement/checkpoint output and sample-level Wilson-loop CSV export.
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
- Defines production HMC/RHMC finite check records: integrator step data,
  reversibility defect, Hamiltonian-change logs, linear-solver residuals,
  spectral interval, rational approximation ledger, and determinant
  reweighting convention.
- Proves the independent-chain aggregation variance identity for cluster
  job-array summaries and separates the between-chain chi-square/error
  inflation diagnostic from any claim of Markov-chain mixing.
- Derives residual bounds for pseudofermion action and force errors:
  \(|\phi^\dagger A^{-1}\phi-\phi^\dagger x|\le
  \lambda_-^{-1}\|\phi\|\,\|r\|\) and the corresponding force bound from
  \(\|\dot A\|_{\rm op}\).
- Derives the RHMC determinant reweighting coordinate
  \(W_{\rm rat}=\det(A)^\alpha\det r_m(A)\) and the finite bound
  \(|\log W_{\rm rat}|\le N\eta_*\) when
  \(r_m(\lambda)=\lambda^{-\alpha}e^{\eta(\lambda)}\).
- Adds `qft_scripts/hmc_rhmc_finite_demo.py`, a finite HMC/RHMC smoke module
  reporting acceptance, Hamiltonian-change, reversibility, positive-matrix
  spectral edge, rational pseudofermion action, and solver-residual
  coordinates.
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
- Defines the finite two-dimensional scalar \(\phi^4\) Euclidean lattice
  measure, proves the pointwise stability bound for \(\lambda>0\), derives
  the local single-site action difference, and proves symmetric-proposal
  Metropolis detailed balance at finite regulator.
- Adds the companion script `qft_scripts/phi4_2d_metropolis.py` as a finite
  scalar-field Metropolis warmup reporting action density, field moments,
  susceptibility-like zero-momentum moment, and \(\phi^2\) autocorrelation
  coordinates.
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
  correlated jackknife construction for nonlinear Wilson-loop ratios,
  including the HDF5 sampler data coordinate.

## Figure Ledger

No figure is included.  Future figures should show the reweighting ratio and
the exponential decay of average phase with volume.

## Companion Scripts

- `qft_scripts/ising2d_metropolis.py --smoke`: finite periodic Ising
  Metropolis sampler.  Verifies the implemented finite chain and reports
  acceptance, energy, magnetization, and a windowed autocorrelation estimate.
  It does not prove a continuum limit.
- `qft_scripts/phi4_2d_metropolis.py --smoke`: finite two-dimensional scalar
  \(\phi^4\) Metropolis sampler.  Verifies the local action difference and
  symmetric-proposal finite-measure setup by running the public companion
  implementation.  It does not prove a continuum \(\phi^4_2\) construction
  or a critical scaling law.
- `qft_scripts/z2_gauge_3d_metropolis.py --smoke`: finite periodic
  \(\mathbb Z_2\) gauge Metropolis sampler.  Verifies a compact gauge
  single-link update and reports plaquette and Wilson-loop measurements for a
  small beta scan.  It does not prove an infinite-volume transition or a
  continuum limit.
- `qft_scripts/su2_gauge_4d_metropolis.py --smoke`: finite periodic
  four-dimensional \(SU(2)\) gauge Metropolis sampler with unit-quaternion
  links.  Verifies a Haar-symmetric local compact-link proposal and reports
  plaquette and Wilson-loop measurements.  It does not prove a heat-bath
  algorithm, HMC/RHMC implementation, or a continuum limit.
- `qft_scripts/su2_gauge_4d_heatbath_overrelaxation.py --smoke`: finite
  periodic four-dimensional \(SU(2)\) Wilson sampler using exact single-link
  heat-bath conditionals for the staple density, interleaved with optional
  overrelaxation sweeps.  It reports plaquette and Wilson-loop measurements.
  It does not prove autocorrelation error estimates, thermodynamic limits,
  or continuum extrapolation.
- `qft_scripts/su3_gauge_4d_metropolis_hdf5.py --smoke`: finite periodic
  four-dimensional \(SU(3)\) Wilson-gauge subgroup-Metropolis sampler.  It
  reports plaquette and Wilson-loop measurements and can write HDF5
  measurement/checkpoint files when `h5py` is available.
- `qft_scripts/su3_ape_smearing_hdf5.py --smoke`: downstream HDF5
  post-processing utility for constructing smeared links before static-line
  or glueball-operator measurements.
- `qft_scripts/autocorrelation_resampling.py --smoke`: finite time-series
  diagnostic script.  It reports a windowed integrated autocorrelation
  coordinate, block means, blocked standard errors, delete-one-block
  jackknife errors, and block-bootstrap errors.
- `qft_scripts/hmc_rhmc_finite_demo.py --smoke`: finite scalar HMC and
  rational pseudofermion diagnostic.  It reports acceptance, maximum
  Hamiltonian change, reversibility defect, positive-matrix spectral edge,
  rational pseudofermion action, and conjugate-gradient residuals.
- `qft_scripts/static_potential_from_wilson_loops.py --smoke`: also verifies
  the sample-level mode that recomputes static-potential logarithmic ratios
  on deleted or resampled Monte Carlo blocks; its HDF5 mode reads
  `measurements/wilson_loops[sample,R-1,T-1]`.
- `qft_scripts/cluster/chain_ensemble_summary.py --smoke`: finite
  independent-chain aggregation utility for job-array outputs.  It reports an
  inverse-variance weighted estimate, internal standard error, between-chain
  chi-square, error-inflation factor, and effective-sample-size sum when
  supplied.

## Calculation Checks

- `calculation-checks/ising_metropolis_finite_checks.py` enumerates the
  \(2\times2\) periodic Ising chain and verifies the companion script's local
  energy difference and detailed-balance identity exactly at finite volume.
- `calculation-checks/phi4_lattice_metropolis_checks.py` verifies the scalar
  companion script's local action difference against the total finite action,
  checks pairwise detailed balance for symmetric proposals, and checks the
  pointwise quartic lower bound for the finite measure.
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
- `calculation-checks/su3_hdf5_sampler_checks.py` verifies the companion
  \(SU(3)\) sampler's embedded subgroup proposals, local score-change
  computation, gauge invariance, \(1\times1\) Wilson-loop/plaquette identity,
  and HDF5 measurement/checkpoint layout.
- `calculation-checks/hmc_pseudofermion_checks.py` verifies the finite HMC
  and pseudofermion algebra: one-dimensional leapfrog determinant one,
  leapfrog reversibility, pairwise Metropolis balance, the diagonalized
  pseudofermion determinant identity, and the RHMC spectral action-error
  bound.  It also checks linear-solver action/force residual bounds, the RHMC
  determinant reweighting log bound, and imports the finite HMC/RHMC smoke
  module as a companion-script regression.
- `calculation-checks/monte_carlo_sign_problem_checks.py` verifies the
  finite-\(N\) autocorrelation variance identity, phase-reweighting identity,
  average-phase relative-variance bound, and the determinant
  reality/positivity distinction in finite examples.
- `calculation-checks/autocorrelation_resampling_checks.py` verifies the
  finite block means, blocked standard error, delete-one-block jackknife
  identity, biased autocovariances, and windowed \(\tau_{\rm int}\) used by
  the companion script.
- `calculation-checks/cluster_chain_ensemble_checks.py` verifies the exact
  inverse-variance weighted mean, internal standard error, between-chain
  chi-square, inflated error, effective-sample-size aggregation, and CSV
  round trip for the job-array chain summary tool.
- `calculation-checks/static_potential_analysis_checks.py` includes the
  correlated delete-one jackknife check for static-potential nonlinear
  Wilson-loop ratios and the HDF5 bridge from sampler data to static-potential
  analysis.
- `calculation-checks/su3_ape_smearing_checks.py` verifies the gauge-covariant
  HDF5 smearing layer used between raw link generation and smeared-observable
  measurements.

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
- 2026-05-27 issue #631 pass: added a finite \(SU(3)\)
  subgroup-Metropolis HDF5/checkpointed data generator, with explicit
  Wilson-loop sample export feeding the static-potential/error-analysis
  scripts.
- 2026-05-27 issue #631 pass: connected the static-potential script directly
  to the sampler HDF5 coordinate
  `measurements/wilson_loops[sample,R-1,T-1]`.
- 2026-05-27 issue #631 pass: added a checked \(SU(3)\) APE-smearing HDF5
  post-processing layer for smeared static-line and glueball-operator
  construction.
- 2026-05-31 issue #631/#703 pass: added production HMC/RHMC finite
  check records, solver-residual and determinant-reweighting bounds, plus a
  public-facing HMC/RHMC smoke module with calculation-check coverage.
- 2026-06-01 issue #494 pass: added the finite scalar \(\phi^4_2\)
  Metropolis warmup requested by the numerical-methods issue, with manuscript
  stability/detailed-balance derivation, public script, and paired
  calculation-check coverage.
- 2026-06-03 issue #631 architecture pass: added a front-loaded production
  evidence ladder for lattice Monte Carlo outputs and tied the public script
  README to the same layer structure.
- 2026-06-03 issue #631 cluster estimator pass: added the independent-chain
  aggregation proposition and the public chain-ensemble summary tool.  This
  supplies the missing finite job-array estimator record after SLURM tasks have
  produced per-chain summaries, while explicitly leaving chain independence,
  equilibration, target-measure equality, and scaling-window interpretation as
  separate evidence layers.

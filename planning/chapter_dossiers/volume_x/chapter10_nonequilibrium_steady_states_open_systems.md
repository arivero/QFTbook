# Chapter 10: Nonequilibrium Steady States And Open-System Limits

## Source Position

Volume X follows anomalous transport with nonequilibrium steady-state and
open-system definitions needed for later thermal, hydrodynamic, and curved
real-time topics.  The chapter now treats steady states as invariant
positive functionals, reservoir steady states as local weak limits, finite
fluctuation relations as path-measure Radon--Nikodym identities, and
  finite-step Langevin/MSRJD variables as exact Fourier rewritings of finite
  Gaussian transition kernels.  It now also derives Doi--Peliti variables from
  finite reaction-network master equations and extracts the finite
  large-deviation Hamiltonian from exponential test functions, with the
  Doi--Peliti map explicitly framed as the finite-regulator bridge from
  classical stochastic occupation dynamics to local non-Hermitian QFT.
  Open-system dynamics is then treated as a weak-coupling limit of larger
  closed systems.
The finite tilted-generator construction for additive jump observables now
separates the exact microscopic Feynman--Kac identity from the additional
analytic hypotheses needed for path large deviations, and records the finite
matrix origin of the Gallavotti--Cohen symmetry for stationary entropy
production.  The chapter now also defines empirical occupations and flows,
derives the finite level-\(2.5\) relative-entropy cost by change of measure,
and contracts it to the level-\(2\) occupation cost in a two-state example.

## Notation Inventory

- `A`, `tau_t`, `omega_ss`: observable algebra, time evolution, and steady
  state.
- `beta_L`, `beta_R`, `mu_L`, `mu_R`: reservoir thermodynamic parameters.
- `J_E`, `J_Q`, `dot S_res`: energy current, charge current, and reservoir
  entropy production.
- `X`, `L`: thermodynamic-force vector and Onsager matrix in linear
  response.
- `gamma`, `Theta gamma`, `P_F`, `P_R`, `Sigma`: finite labelled trajectory,
  time-reversed trajectory, forward/reversed path measures, and trajectory
  entropy production.
- `W_ext`, `Delta F`: protocol work and finite free-energy difference in the
  Jarzynski specialization.
- `x_n`, `Delta x_n`, `F_n`, `eta_n`, `D`, `hat x_n`: finite-regulator
  Langevin variables, increments, drift, Gaussian noise covariance, and
  MSRJD Fourier-dual variables.
- `n`, `nu_r`, `nu'_r`, `v_r`, `kappa_r`, `a_s`, `a_s^dagger`,
  `L_DP`, `H_DP`: occupation vectors, reaction input/output/stoichiometry,
  rate constants, creation/annihilation operators, Doi-Peliti generator,
  and its normal symbol.
- `H_LD`, `p`, `Omega`: finite-regulator dynamical large-deviation
  Hamiltonian, exponential-test covector, and density-scaling parameter.
- `A_T`, `h_i`, `g_ij`, `mathsf L_lambda`, `psi(lambda)`: finite additive
  jump observable, state weight, jump weight, tilted backward generator, and
  scaled cumulant generating function.
- `sigma_ij`, `mathsf L_q^Sigma`, `Pi`: stationary entropy-production jump
  increment, entropy-production tilted generator, and diagonal stationary
  distribution matrix in the finite Gallavotti--Cohen similarity identity.
- `rho_i^T`, `q_ij^T`, `I_2.5`, `I_2`: empirical occupation, empirical
  jump flow, finite level-\(2.5\) empirical-flow cost, and contracted
  occupation cost.
- `H_S`, `H_E`, `S_a`, `E_a`: system/environment Hamiltonians and couplings.
- `gamma_ab(omega)`: bath spectral matrix.
- `S_a(omega)`: Bohr-frequency component of a system coupling operator.
- `L`, `L_alpha`: Markov generator and Lindblad jump operators; context
  distinguishes this from the Onsager matrix.
- `Gamma`, `H_eff`, `K_t`, `J`: total jump rate operator,
  non-Hermitian effective Hamiltonian, no-jump map, and jump map in the
  finite-dimensional GKSL proof.
- `S_IF`, `phi_r`, `phi_a`, `D_R`, `N`: influence functional, Keldysh
  variables, retarded kernel, and noise kernel.
- `gamma`, `chi`, `D_n`: relaxation rate, susceptibility, and homogeneous
  Ornstein-Uhlenbeck noise strength.

## Claim Ledger

1. A steady state is a positive normalized functional invariant under the
   real-time automorphism group.
2. Reservoir nonequilibrium steady states are local weak limits of
   long-time evolved observables near the junction.
3. With currents positive from left to right, reservoir entropy production is
   \[
     \dot S_{\rm res}
     =(\beta_R-\beta_L)J_E
     -(\beta_R\mu_R-\beta_L\mu_L)J_Q.
   \]
4. In linear response, \(\dot S_{\rm res}=X^TLX\), so positivity is
   equivalent to positive semidefiniteness of the symmetric Onsager matrix.
5. Finite fluctuation relations are path-measure statements: after specifying
   the labelled trajectory space, reversed protocol, and absolute-continuity
   condition, the trajectory entropy production is a Radon--Nikodym logarithm.
6. The finite path-measure identity gives
   \(\langle e^{-\Sigma}\rangle=1\); with thermal local detailed balance and
   Gibbs endpoint distributions it becomes the Jarzynski identity
   \(\langle e^{-\beta W_{\rm ext}}\rangle=e^{-\beta\Delta F}\).
7. A finite-step Ito Langevin process with covariance
   \(2\Delta t\,D\) has an exactly normalized Gaussian transition density.
   Its MSRJD response-field representation is the Fourier transform of that
   transition density at each time step, with \(\hat x_n\) the Fourier-dual
   variable to \(\Delta x_n-\Delta t F_n\).
8. The generator \(L_t=F^a\partial_a+D^{ab}\partial_a\partial_b\) and the
   Fokker-Planck adjoint equation follow from the finite-step moments before
   a continuum stochastic-field limit is taken.
9. For a finite reaction network with mass-action rates
   \(w_r(n)=\kappa_r(n)_{\nu_r}\), the normally ordered Doi-Peliti generator
   \(\sum_r\kappa_r[(a^\dagger)^{\nu'_r}-(a^\dagger)^{\nu_r}]a^{\nu_r}\)
   is exactly the master-equation generator on the algebraic occupation
   domain.
10. The coherent-state normal symbol
    \(H_{\rm DP}(\bar z,z)=\sum_r\kappa_r(\bar z^{\nu'_r}-\bar z^{\nu_r})z^{\nu_r}\)
    satisfies \(H_{\rm DP}(1,z)=0\) and yields the deterministic
    mass-action rate equation by differentiating at \(\bar z=1\).  The
    identity \(H_{\rm DP}(1,z)=0\) is recorded as the projection-state
    conservation law replacing unitary norm conservation in the non-Hermitian
    Markov representation.
11. Exponential test functions give the finite-regulator dynamical
    large-deviation Hamiltonian
    \(\mathcal H_{\rm LD}(x,p)=\sum_r\lambda_r(x)(e^{p\cdot v_r}-1)\)
    once a density scaling with rates
    \(\kappa_r(n)_{\nu_r}=\Omega\lambda_r(x)+o(\Omega)\) is specified.
12. For a finite jump process and additive observable
    \(A_T=\int h_{i(t)}dt+\sum g_{i_{m-1}i_m}\), conditioning on the first
    short interval gives the exact Feynman--Kac semigroup generated by
    \((\mathsf L_\lambda f)_i=\lambda h_if_i+
    \sum_{j\ne i}W_{ij}(e^{\lambda g_{ij}}f_j-f_i)\).
13. For an irreducible finite chain and real tilting parameter, the
    long-time scaled cumulant generating function is the Perron eigenvalue
    of \(\mathsf L_\lambda\); a path large-deviation principle still
    requires separate analytic and tightness hypotheses.
14. For stationary entropy production with
    \(\sigma_{ij}=\log(\pi_iW_{ij}/\pi_jW_{ji})\), the finite matrix
    identity
    \(\mathsf L_q^\Sigma=\Pi^{-1}(\mathsf L_{1-q}^\Sigma)^T\Pi\)
    implies the Gallavotti--Cohen spectral symmetry
    \(\psi_\Sigma(q)=\psi_\Sigma(1-q)\).
15. Empirical occupations and flows satisfy finite boundary conservation,
    and their finite level-\(2.5\) cost is
    \[
      I_{2.5}(\rho,q)=\sum_{i,j\ne i}
      \left[q_{ij}\log(q_{ij}/\rho_iW_{ij})-q_{ij}+\rho_iW_{ij}\right],
    \]
    with conservation and support constraints.
16. The level-\(2.5\) cost follows from the Radon--Nikodym density between
    the original jump process and the auxiliary process
    \(R_{ij}=q_{ij}/\rho_i\); contracting over conserved flows gives the
    level-\(2\) occupation cost, including
    \(I_2(p)=(\sqrt{pa}-\sqrt{(1-p)b})^2\) for a two-state chain.
17. In the weak-coupling Markovian limit, the bath spectral matrix
   \(\gamma_{ab}(\omega)\) is positive by the positive-type/Bochner
   argument and yields the Davies/GKSL generator after the van Hove and
   secular limits.
18. The GKSL form preserves trace, preserves Hermiticity, and generates a
   completely positive semigroup; the proof diagonalizes the positive bath
   spectral matrices and constructs the finite-time map by the
   Dyson-Phillips jump expansion.
19. KMS bath spectral functions obey detailed balance; the chapter verifies
   the sign and index order by spectral resolution and applies the result to
   the Gibbs stationary ratio for a two-level system.
20. The quadratic Schwinger-Keldysh influence action has explicitly defined
   retarded and noise kernels; KMS relates them by fluctuation-dissipation.
21. For a Markovian relaxing hydrodynamic density, the Fokker-Planck
   stationary-current computation with the stationary Gaussian
   equilibrium weight fixes \(D_n=\gamma\chi T\) and hence
   \(\langle\xi\xi\rangle=2\gamma\chi T\,\delta\).
22. Continuum QFT constructions must specify the order of long-time,
    thermodynamic, weak-coupling, Markovian, hydrodynamic, and continuum
    limits.
23. The Doi--Peliti/MSRJD synthesis distinguishes continuous Gaussian
    stochastic fields from integer-occupation jump systems, and defines
    nonequilibrium scaling classes operationally by common continuum
    fixed-point data, relevant perturbations, and scaling correlation/response
    functions rather than by naming a universality class.

## Calculation Checks

- `calculation-checks/nonequilibrium_open_system_checks.py` verifies the
  reservoir entropy formula, GKSL trace preservation, KMS detailed balance
  for a two-level system, Ornstein-Uhlenbeck noise normalization, and
  positive noise-kernel algebra.  It also verifies the cancellation of
  waiting-time factors in the finite path-measure entropy-production ratio
  and the driven two-state Jarzynski identity, together with the determinant
  normalization in the finite-step MSRJD Fourier kernel and the Langevin
  generator expansion on a cubic test function.  It also verifies the
  Doi-Peliti generator matrix on a fixed-total-number two-species reaction
  network, the projection-state symbol \(H_{\rm DP}(1,z)=0\), the
  mass-action drift extracted from the normal symbol, the exponential
  test-function large-deviation Hamiltonian, the finite Feynman--Kac tilted
  generator for jump additives, and the finite-ring Gallavotti--Cohen
  similarity identity for entropy production.  It also verifies the
  empirical-flow level-\(2.5\) cost, its Radon--Nikodym sign, and the
  two-state level-\(2\) contraction formula.

## Figure Ledger

No figure is included in this pass.  Future figures should include reservoir
joining, Keldysh influence contours, and relaxation/noise flow diagrams.

## Audit Notes

- 2026-05-31 statmech crosswalk/#703 pass: added finite trajectory
  probability measures and fluctuation relations as regulator-level
  Radon--Nikodym identities, before any continuum QFT or Schwinger--Keldysh
  formal path-integral language is invoked.
- 2026-05-31 finite-step MSRJD pass: added the exact finite-dimensional
  Gaussian/Fourier derivation of response-field variables and the
  finite-step generator calculation before continuum stochastic-field
  language is used.
- 2026-05-31 finite Doi-Peliti pass: added the exact occupation-basis
  reaction-network generator identity, coherent-state normal-symbol
  derivation, and finite exponential-test Hamiltonian underlying dynamical
  large deviations.
- 2026-05-31 Doi-Peliti synthesis/#704 pass: added the finite-regulator
  bridge from classical stochastic occupation dynamics to local
  non-Hermitian QFT, identified the projection-state Ward identity
  `H_DP(1,z)=0` as the Markov replacement for unitarity, and stated the
  operational meaning of nonequilibrium scaling-class claims.
- 2026-05-31 finite tilted-generator pass: added the exact Feynman--Kac
  derivation of tilted generators for finite jump additives, separated the
  finite Perron-Frobenius spectral input from large-deviation proof
  hypotheses, and recorded the finite stationary entropy-production
  Gallavotti--Cohen similarity identity.
- 2026-05-31 finite empirical-flow pass: added empirical occupation/flow
  variables, finite boundary conservation, the level-\(2.5\) relative
  entropy cost from an auxiliary-rate change of measure, its contraction to
  the two-state occupation cost, and paired calculation checks.

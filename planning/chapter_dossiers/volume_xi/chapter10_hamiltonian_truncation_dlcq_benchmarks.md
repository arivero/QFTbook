# Chapter 10: Hamiltonian Truncation, DLCQ, And Benchmark Protocols

## Source Position

Volume XI adds Hamiltonian regulator methods after stochastic and lattice
constructions, emphasizing controlled finite approximation rather than informal
numerics.

## Notation Inventory

- `mathfrak H_trunc`: Hamiltonian truncation regulator datum.
- `Q_H`: lower-bounded closed quadratic form underlying the target
  Hamiltonian when a limiting operator is known.
- `H`, `Hilb`, `Hilb_Lambda`, `P_Lambda`: Hamiltonian, Hilbert space,
  truncated subspace, and projection.
- `B_Lambda`: ordered computational basis, including inner-product and
  sector conventions.
- `H_Lambda^ren`, `c_a`: renormalized projected Hamiltonian and local
  counterterm coordinates.
- `O_obs`, `E_sys`: finite-regulator observables and systematic-error model.
- `E_n(Lambda)`: variational finite-subspace eigenvalue.
- `N_H(c)`: exact spectral-counting function below the energy `c` for a
  fixed lower-bounded self-adjoint Hamiltonian below its essential spectrum.
- `E_cut`: truncated conformal-space cutoff.
- `tau`, `h`: thermal and magnetic Ising deformation couplings.
- `r`, `p_r`, `H_r`, `H_N`: Neveu-Schwarz Majorana mode label, finite-circle
  momentum, two-dimensional Bogoliubov block, and finite direct-sum
  Hamiltonian for the Ising energy-deformation benchmark.
- `n`, `w`, `R`, `M`, `L_osc`, `m_r`, `bar m_r`, `alpha`,
  `V_SG^fin`: compact-boson momentum, winding, radius, oscillator-mode
  cutoff, total oscillator-level cutoff, left/right oscillator occupations,
  finite vertex charge, and assembled finite sine-Gordon TCSA vertex matrix.
- `N`, `P_max`, `P_tot`, `n_r`, `k_r`, `omega_r`, `phi_N`, `V_N`:
  Fourier-mode, particle-number, total-momentum, occupation-number,
  momentum, frequency, finite free-field, and normal-ordered quartic
  interaction coordinates in the scalar \(\phi^4\) truncation benchmark.
- `Q_s`, `theta_n`, `rho_I`: finite-volume fermion momentum set, rapidity,
  and free Bethe-state density used in the TFFSA spin matrix element.
- `H(h)`, `W`, `lambda_*(h)`, `g`: finite affine Hermitian spectral-flow
  family, perturbing matrix, simple eigenvalue branch, and finite spectral gap
  used in the Hellmann-Feynman derivative check.
- `rho_a`, `A_E8`, `v`: magnetic-Ising \(E_8\) target mass ratios, the
  \(E_8\) Dynkin adjacency matrix, and its Perron-Frobenius eigenvector used
  as a finite convention check for the target table.
- `x^pm`, `p^+`, `K`: light-front coordinates, longitudinal momentum, and
  harmonic resolution.
- `M^2`, `P^-`: invariant mass operator and light-front Hamiltonian.
- `N_n`, `K`, `Q_K`, `g`: DLCQ positive-longitudinal occupation numbers,
  harmonic resolution, normal-ordered scalar quartic operator, and finite
  scalar \(\phi^4\) DLCQ coupling coordinate.
- `M_K^2`, `x_n`, `gamma`: finite harmonic-resolution matrix for the
  large-N two-dimensional QCD meson principal-value operator, grid point, and
  coupling normalization.
- `I`, `X_i`, `A_i`, `sigma_i`, `E_i`: directed finite-regulator labels,
  finite regulator object, finite observable, statistical standard error, and
  declared systematic error model.
- `A_K`, `A_infty`, `omega`, `r_K`, `R_K`, `R_K^(m)`: cutoff sequence,
  continuum candidate, leading cutoff exponent, remainder, two-cutoff
  Richardson extrapolate, and multi-cutoff extrapolate.
- `s_j`, `w_j`: positive scale factors and exact extrapolation weights.
- `lambda_ell(K)`, `q_r`, `X_{ra}`, `B`: ordered finite DLCQ eigenvalue,
  large-`K` fit coordinate, Vandermonde design matrix, and least-squares
  left inverse used in the finite intercept-remainder amplifier.
- `W`, `Sigma_W`, `f_a`, `G`, `S_W`, `chi_W^2`: correlated fit window,
  finite covariance matrix, declared fit functions, Gram matrix,
  deterministic systematic coordinate, and correlated residual coordinate.
- `R_r`, `B_{0r}`, `A_hat_{infty,W}`: declared remainder envelopes,
  intercept-weight row of the correlated-fit left inverse, and the fitted
  window intercept reported by the public finite-regulator extrapolation
  script.
- `K_m(A,v)`, `V_m`, `T_m`, `beta_m`, `q_m`: finite Krylov subspace,
  orthonormal Krylov/Lanczos basis, tridiagonal compression, tail residual
  coordinate, and next Lanczos vector.
- `mu_v`, `theta_r`, `w_r`: finite seed spectral measure, Ritz values, and
  Krylov quadrature weights.
- `Theta`, `Psi`, `S`, `E_samp`: variational parameter space, trial-vector
  map, exact ansatz constraints, and sampling/error datum.
- `E_psi`, `r_psi`, `Delta_psi`: Rayleigh quotient, residual vector, and
  finite energy variance for a trial state.
- `E_loc(x)`, `p_psi(x)`: finite-basis local energy and sampling
  probability used by neural-state and variational Monte Carlo estimates.
- `gamma_t`, `rho_t`, `I_N`, `N_eff`: finite local-energy Markov-chain
  autocovariance, normalized autocorrelation, variance-inflation coordinate,
  and effective sample size for sampled VMC energy estimates.
- `mathsf s_a(x;theta)`: finite score coordinate
  `partial_a log psi_x(theta)` entering the neural/VMC force identity.
- `mathbb E`, `mathbb E_O`, `lambda_alpha`, `C_O(n)`, `m_eff(a,n)`:
  finite MPS transfer operator, local-operator insertion map, transfer
  eigenvalues, connected lattice correlator, and finite effective mass.
- `x^pm`, `p^pm`, `p_perp`, `Z_Lambda`, `C_{Lambda,alpha}`:
  light-front coordinates and momenta, transverse momentum, zero-mode sector,
  and finite-regulator constraints in the light-front Hamiltonian datum.
- `Hilb_Lambda^phys`, `P_Lambda^-`, `M_Lambda^2`: finite physical
  light-front Hilbert space, light-front Hamiltonian, and fixed-sector
  invariant-mass operator.
- `Q`, `m`, `X_m`, `N_m`, `s_m`, `R_m`, `b_m`: cross-method benchmark target
  observable, method label, finite regulator object, normalization map,
  statistical error coordinate, deterministic finite-regulator envelope, and
  scheme-matching coordinate.
- `x_m`, `sigma_m`, `rho_m`, `beta_m`, `e_m`: benchmark-manifest normalized
  coordinate vector, statistical error, finite-regulator envelope,
  matching-error coordinate, and total declared componentwise error.
- `C_num`, `D_fin`, `F_fin`, `I_check`, `S_scope`: companion-script finite
  check record, finite regulator datum, finite output map, checked finite
  identities, and scope boundary separating finite statements from continuum
  claims.

## Claim Ledger

- Defines the Hamiltonian truncation regulator datum before finite-matrix
  estimates are used, including the target quadratic form, cutoff net,
  computational bases, counterterms, finite observables, and systematic-error
  model.
- Defines projected Hamiltonian regulator data with counterterms as the
  elementary fixed-Hamiltonian specialization of the full datum.
- Derives the Rayleigh-Ritz upper bound for discrete eigenvalues at fixed
  regulated Hamiltonian.
- Proves gap-stable Ritz counting for a fixed lower-bounded self-adjoint
  Hamiltonian: in an isolated spectral window below the essential spectrum,
  form-norm dense finite trial spaces eventually produce exactly the correct
  number of Ritz eigenvalues in that window.
- Defines TCSA matrix elements from CFT data and identifies cutoff
  counterterm dependence.
- Proves the finite-mode Majorana Bogoliubov spectrum used as a
  Hamiltonian-truncation smoke benchmark.
- Constructs the finite compact-boson oscillator vertex matrix for a
  sine-Gordon TCSA calculation, including compact momentum, winding,
  oscillator descendants, the normal-ordered one-oscillator matrix element,
  spatial-integral spin projection, and the separation from any continuum
  sine-Gordon spectrum claim.
- Constructs a nonintegrable normal-ordered \(1+1\)-dimensional scalar
  \(\phi^4\) finite Hamiltonian truncation in a free massive Fock basis,
  with explicit Fourier-mode, particle-number, free-energy, and
  total-momentum cutoffs, and separates its finite Hermiticity from any
  continuum/counterterm claim.
- Derives the zero-mode two-particle normalization check
  \(\bra2\int:\phi_0^4:\ket2=3/(Lm^2)\), fixing the field normalization and
  \(4!\) convention used by the companion script.
- Develops the two-coupling Ising TCSA datum
  \(H_{\rm CFT}+\tau\int\varepsilon+h\int\sigma\), distinguishing cylinder
  operator normalizations and coupling dimensions.
- Defines the TFFSA reorganization in which the thermal deformation is
  treated exactly as a massive Majorana Hamiltonian and the spin perturbation
  is represented by finite-volume spin-field form factors.
- States the connected TFFSA spin matrix element with momentum conservation,
  free Bethe-state density \(\rho_I=\prod_i mL\cosh\theta_i\), disconnected
  contraction caveats, and finite-size correction status.
- Defines a zero-momentum connected TFFSA block with vacuum and
  two-particle-pair states, declares the diagonal vacuum-expectation
  convention, and proves Hermiticity plus the zero-coupling free spectrum.
- Proves the finite Hellmann-Feynman spectral-flow derivative formula for a
  simple eigenvalue of an affine finite Hermitian matrix family, including the
  resolvent-gap hypothesis and the trace identity for the sum of slopes.
- Records the exact \(E_8\) magnetic-Ising continuum target mass ratios for
  numerical comparison and gives a finite Perron--Frobenius check from
  the \(E_8\) adjacency matrix, while keeping the continuum integrable-QFT
  derivation separate from any finite TCSA/TFFSA diagonalization claim.
- Proves the Feshbach-Schur complement identity that underlies Hamiltonian
  truncation counterterms and high-energy tail corrections.
- Defines finite residual bounds for Hermitian truncation matrices and
  proves the residual-to-spectrum and spectral-projector leakage bounds used
  to bound numerical eigenpairs before any continuum interpretation.
- Records the exact finite Schur self-energy
  `Sigma_P(E)=PHQ(QHQ-E)^{-1}QHP` and isolates the separate norm-bound
  obligation for replacing it by a local counterterm.
- Defines finite Krylov spectral data for large truncation matrices,
  derives the exact Lanczos Ritz-residual identity
  `||(A-theta)V_m y||=beta_m |y_m|`, and explains why this is finite-matrix
  evidence rather than a continuum spectral theorem.
- Derives the finite Krylov spectral-measure moment identity through degree
  `2m-1`, using the orthogonality of the Lanczos residual polynomial, and
  states the seed-overlap and symmetry-sector coverage obligations needed
  before interpreting missing or present states.
- Defines finite variational ansatz data for tensor-network, DMRG/MERA, and
  neural-state calculations, including ansatz constraints and sampling-error
  data.
- Derives the finite energy-variance bound: variance equals residual
  norm, bounds distance from the finite spectrum, and bounds leakage from a
  separated finite spectral cluster.
- Derives the ground-projector leakage estimate when the finite ground
  energy and gap are known by an independent bound.
- Derives the tangent-gradient formula for a smooth normalized ansatz, so a
  variational stationary point is identified as tangent-space residual
  orthogonality rather than an eigenvector error bound.
- Derives the finite local-energy mean and variance identities used by
  sampled neural-state and variational Monte Carlo calculations.
- Derives the finite local-energy Markov-chain variance identity
  `Var(Fbar_N)=gamma_0 I_N/N` and the corresponding effective sample size
  coordinate, separating sampled VMC error bars from thermalization,
  slow-mode, autocorrelation-window, and optimizer-bias assumptions.
- Derives the finite score-covariance force identity for smooth
  neural-state/VMC ansatz families, and separates the exact finite gradient
  from optimizer convergence, Markov-chain autocorrelation, residual norm, and
  continuum regulator extrapolation.
- Adds the finite transfer-operator spectral expansion for
  translation-invariant MPS correlators, identifies the finite effective mass
  \(-a^{-1}\log\lambda_\alpha\), and states the scaling, operator
  normalization, and multipoint-convergence inputs needed before such a
  finite correlation length becomes a continuum QFT mass.
- Defines a general light-front Hamiltonian regulator datum before DLCQ is
  specialized: null-coordinate convention, positive-longitudinal nonzero
  modes, zero-mode/constraint sector, finite physical Hilbert space,
  self-adjoint \(P^-_\Lambda\), fixed-sector \(M_\Lambda^2\), and continuum
  diagnostic.
- Derives the free massive one-particle light-front measure
  \(\dd p^+\,\dd^{D-2}p_\perp/(2p^+)\) from
  \(\theta(p^0)\delta(p^2+m^2)\), making the \(p^+=0\) boundary a separate
  zero-mode/constraint datum rather than a silent omission.
- Defines DLCQ kinematics and the role of harmonic resolution, then packages
  the light-front compactification, parton partitions, zero-mode treatment,
  finite \(P^-\) or \(M^2\) operator, and finite-\(K\) continuum diagnostic
  into a DLCQ regulator datum.
- Constructs a scalar \(\phi^4\) DLCQ warmup at fixed harmonic resolution:
  positive-longitudinal bosonic partitions, free invariant mass
  \(Km^2\sum_nN_n/n\), normal-ordered quartic operator \(Q_K\), and finite
  matrix \(M_K^2=M_{0,K}^2+gK P_KQ_KP_K\), with the omitted zero mode stated
  as a regulator choice rather than hidden.
- Derives the finite \(K=3\) convention checks
  \(\bra3Q_3\ket{1,1,1}=4\sqrt2\) and
  \(\bra{1,1,1}Q_3\ket{1,1,1}=36\).
- Constructs a finite DLCQ-style matrix for the large-N two-dimensional QCD
  meson equation and records the finite quadratic-form identity that gives
  regulator-level positivity.
- Defines finite-regulator observable data, separating finite observables,
  statistical errors, and systematic cutoff-error models.
- Proves by Lagrange interpolation that finitely many cutoff values do not
  determine a continuum value without an analytic error model.
- Defines a power-law cutoff expansion with an explicit remainder bound.
- Proves two-cutoff Richardson cancellation with a displayed error bound.
- Records integer-power multi-cutoff extrapolation by exact Vandermonde
  weights and a displayed remainder estimate, with theorem status reserved for
  the separate cutoff-expansion hypothesis.
- Defines a fixed-label large-`K` diagnostic for the finite large-N QCD DLCQ
  matrix sequence, explicitly separating the numerical label convention from
  any continuum-state claim.
- Proves a finite least-squares intercept bound: if the finite data equal a
  polynomial in `K^{-omega}` plus a remainder, the fitted intercept differs
  from the continuum coefficient by at most the row-`l1` amplification factor
  times the maximum remainder.
- Adds the correlated-fit coordinate system for production extrapolations:
  the window, covariance matrix, model functions, and remainder envelopes are
  part of the finite datum; the text derives the exact intercept error
  decomposition, covariance propagation, deterministic systematic coordinate,
  and correlated residual diagnostic without treating fit stability as a
  continuum theorem.
- Adds a generic public finite-regulator extrapolation implementation that
  uses the chapter's correlated-fit coordinates: regulator labels, finite
  values, covariance source, remainder envelopes, and half-open fit windows
  are explicit data, and the reported intercepts remain finite diagnostics
  rather than continuum QFT claims.
- Defines cross-method benchmark data for comparing lattice Monte Carlo,
  Hamiltonian truncation/TCSA/TFFSA, and DLCQ outputs: common target
  observable, method-specific finite objects, normalization maps, statistical
  and deterministic error coordinates, scheme-matching coordinates, and the
  finite consistency bound
  \(|N_m(X_m)-N_n(X_n)|\le s_m+s_n+R_m+R_n+b_m+b_n\).
- Defines a machine-readable benchmark manifest as a finite representative
  of the cross-method benchmark datum, including target observable,
  coordinate dimension, method-specific normalized coordinates, statistical
  errors, regulator envelopes, matching errors, optional covariance data, and
  provenance; the finite pairwise check is
  \(|x_m-x_n|_{\rm comp}\le e_m+e_n\).
- Defines the public companion-script finite check
  \(C_{\rm num}=(D_{\rm fin},F_{\rm fin},I_{\rm check},S_{\rm scope})\):
  finite regulator datum, finite output map, checked identities, and explicit
  boundary against continuum or production-ensemble claims.
- Adds a public finite-regulator check index for all current
  `qft_scripts` families: spin/scalar Metropolis, compact-gauge samplers,
  lattice analysis functionals, HMC/RHMC and Markov-chain diagnostics,
  Hamiltonian truncation/TCSA/TFFSA matrices, DLCQ finite matrices,
  extrapolation/manifest tools, and cluster sweep wrappers.
- Records the current magnetic-Ising benchmark status: finite TFFSA block,
  spectral-flow, and exact \(E_8\) target scripts are finite checks, not
  yet a full continuum comparison without cutoff counterterms and
  extrapolation envelopes.
- Records benchmark requirements for truncation methods.
- Connects the chapter to `planning/14_code_policy.md`,
  `qft_scripts/tcsa_ising_energy_benchmark.py`,
  `qft_scripts/phi4_hamiltonian_truncation.py`,
  `qft_scripts/phi4_dlcq.py`,
  `qft_scripts/thooft_dlcq.py`, `qft_scripts/thooft_dlcq_extrapolation.py`,
  and `tools/run_qft_scripts_smoke.sh`.

## Figure Ledger

No figure is included in this pass.  Future figures should include Hilbert
space cutoff towers, DLCQ momentum partitions, and benchmark extrapolation
plots.

## Companion Scripts

- `qft_scripts/tcsa_ising_energy_benchmark.py --smoke`: diagonalizes finite
  Ising thermal-deformation Bogoliubov blocks and checks their exact
  eigenvalues.
- `qft_scripts/sine_gordon_zero_mode_truncation.py --smoke`: builds the
  finite compact-boson zero-mode matrix for the sine-Gordon vertex
  perturbation, checks finite Hermiticity and reflection symmetry, and reports
  the second-order ground-state shift.  It is a vertex-selection benchmark,
  not the full sine-Gordon finite-volume TCSA spectrum.
- `qft_scripts/sine_gordon_tcsa_vertex.py --smoke`: assembles the finite
  compact-boson oscillator vertex matrix for a sine-Gordon TCSA calculation,
  checks finite Hermiticity, spin projection of the spatial integral, and
  winding conservation, and reports the lowest finite eigenvalues without
  asserting a continuum sine-Gordon spectrum.
- `qft_scripts/phi4_hamiltonian_truncation.py --smoke`: builds a finite
  normal-ordered scalar \(\phi^4\) Hamiltonian truncation in a declared
  total-momentum, particle-number, free-energy, and Fourier-mode cutoff, then
  checks finite Hermiticity and reports the lowest finite eigenvalues.
- `qft_scripts/phi4_dlcq.py --smoke`: builds a finite positive-\(p^+\)
  scalar \(\phi^4\) DLCQ invariant-mass matrix at fixed harmonic resolution,
  checks finite Hermiticity, and reports the lowest finite invariant masses
  without asserting a continuum spectrum.
- `qft_scripts/tffsa_ising_spin_connected.py --smoke`: builds the finite
  zero-momentum connected Ising spin-field TFFSA block, checks Hermiticity,
  and reports the finite eigenvalues and free energies.
- `qft_scripts/tffsa_ising_spectral_flow.py --smoke`: diagonalizes the finite
  connected Ising TFFSA block across a small magnetic-coupling grid and checks
  Hellmann-Feynman slopes against centered finite differences at a separated
  finite spectral point.
- `qft_scripts/e8_ising_mass_ratios.py --smoke`: prints the exact \(E_8\)
  magnetic-Ising mass-ratio target table and checks that it equals the
  normalized Perron-Frobenius component ratios of the \(E_8\) Dynkin adjacency
  matrix.
- `qft_scripts/thooft_dlcq.py --smoke`: builds and diagonalizes the finite
  principal-value matrix for the large-N two-dimensional QCD meson equation
  at a small harmonic resolution, with a positivity smoke check.
- `qft_scripts/thooft_dlcq_extrapolation.py --smoke`: fits fixed finite
  DLCQ eigenvalue labels to a chosen polynomial in `K^{-omega}`, reporting
  residuals, conditioning, and the finite intercept-remainder amplification
  factor without asserting a continuum spectrum.
- `qft_scripts/finite_regulator_extrapolation.py --smoke`: builds a
  correlated synthetic finite-regulator data set, fits several declared
  windows, and reports finite intercepts, propagated statistical errors,
  deterministic systematic coordinates, residuals, condition numbers, and
  window spread.
- `qft_scripts/benchmark_manifest_consistency.py --smoke`: builds a
  synthetic cross-method benchmark manifest, validates coordinates,
  covariance/provenance data, total error envelopes, and reports the pairwise
  finite consistency matrix; it is a manifest-level compatibility check, not
  a continuum-agreement theorem.
- Public finite-regulator check index in the chapter groups every
  current `qft_scripts` entry by its mathematical check type and states
  the corresponding unproved continuum or production claim.
- `calculation-checks/numerical_extrapolation_checks.py`: exact rational and
  finite-matrix regression check for the Lagrange-interpolation obstruction,
  Richardson cancellation, integer-power extrapolation weights, and
  correlated-fit covariance/error propagation used in the chapter; it also
  imports the public finite-regulator extrapolation script and verifies its
  public smoke coordinates against the displayed formulas.
- `calculation-checks/hamiltonian_truncation_dlcq_checks.py`: finite
  regression check for the Ising-energy benchmark spectrum, the large-\(N\)
  two-dimensional QCD DLCQ quadratic-form identity, the sine-Gordon
  zero-mode vertex selection rule and second-order shift, the compact-boson
  sine-Gordon oscillator vertex assembly, the scalar
  \(\phi^4\) normal-ordered truncation basis and zero-mode matrix element,
  the scalar \(\phi^4\) DLCQ harmonic-resolution basis and quartic matrix
  elements, connected Ising TFFSA block normalization, finite Ising TFFSA
  spectral-flow derivative identities, the \(E_8\) target-ratio
  Perron--Frobenius check, finite large-`K` fit algebra, finite residual
  bounds, spectral-projector leakage, the Feshbach determinant
  identity, and the
  Krylov/Lanczos Ritz-residual plus finite spectral-moment identities.  It
  also checks variational energy variance, ground-projector leakage,
  tangent-gradient, local-energy mean/variance, Markov-chain variance
  inflation, and score-force identities, and
  the benchmark manifest's passing and failing finite pairwise checks.

## Anti-Wrapper Audit

- 2026-05-29: strengthened the Schur-complement proposition into a
  Feshbach-Schur reduction with an explicit resolvent-distance
  bound on the eliminated \(Q\)-component, so the statement now records the
  estimate relevant to truncation control rather than only a block-matrix
  rearrangement.
- 2026-05-29 eighth pass: demoted the finite residual spectral bound
  from proposition form to linear-algebra prose.  The residual-to-spectrum
  and leakage bounds remain as numbered equations because they are useful
  diagnostics, but their derivation is an elementary eigenbasis calculation.
- 2026-05-31 statmech numerical-evidence pass: added Krylov/Lanczos
  finite-spectral evidence machinery as derivational prose rather than a
  theorem wrapper, with exact residual and moment identities tied to
  seed-overlap and symmetry-sector coverage.
- 2026-05-31 second statmech numerical-evidence pass: added finite
  variational ansatz bounds for tensor-network/neural-state methods as
  derivational prose, with finite residual, variance, tangent-gradient, and
  local-energy identities rather than theorem wrappers.
- 2026-05-31 third statmech numerical-evidence pass: added correlated-fit
  and fit-window stability coordinates as finite data-analysis algebra, not
  as a theorem that finite extrapolation plots prove continuum QFT claims.
- 2026-06-03 issue #703 neural/VMC sampling pass: added the finite
  local-energy Markov-chain variance identity and exact effective-sample-size
  coordinate, with rational path enumeration checking the sampled-error
  formula rather than merely citing autocorrelation diagnostics.
- 2026-06-01 issue #494 scalar-truncation pass: added a nonintegrable
  \(1+1\)-dimensional normal-ordered \(\phi^4\) finite-matrix construction
  and script as a regulator benchmark, with finite Hermiticity and the
  zero-mode two-particle matrix element treated as checks rather than a
  continuum theorem.
- 2026-06-01 issue #494 scalar-DLCQ pass: added the requested
  \(1+1\)-dimensional \(\phi^4\) DLCQ warmup, keeping the omitted zero mode
  and \(K\to\infty\) counterterm problem explicit, and paired it with a
  smoke script plus finite matrix-element checks.
- 2026-06-01 issue #494 check-index pass: added the
  `C_num=(D_fin,F_fin,I_check,S_scope)` finite-check index so the
  public script layer is integrated into the manuscript without pretending
  that smoke tests prove continuum QFT claims.
- 2026-06-01 issue #494 correlated-extrapolation pass: added a reusable
  finite-regulator extrapolation script for correlated data and window
  diagnostics, with the manuscript text emphasizing that covariance choices,
  remainders, and fit windows are declared data rather than hidden proof of a
  continuum limit.
- 2026-06-01 issue #494 sine-Gordon benchmark pass: added a finite
  compact-boson zero-mode truncation section and public script checking the
  sine-Gordon vertex selection rule, finite Hermiticity, reflection symmetry,
  and the second-order ground-state shift, while explicitly leaving the full
  oscillator/winding/counterterm TCSA construction outside the benchmark.
- 2026-06-01 issue #494 sine-Gordon oscillator pass: added a finite
  compact-boson oscillator vertex-assembly section and public script checking
  normal-ordered vertex coefficients, spatial-integral spin projection,
  winding conservation, and finite Hermiticity without promoting the finite
  matrix to a continuum sine-Gordon spectrum.
- 2026-06-01 issue #494 E8 target-data pass: added the exact magnetic-Ising
  \(E_8\) mass-ratio table and a finite Perron-Frobenius adjacency
  check as benchmark target data, keeping the continuum factorized
  scattering derivation and finite TCSA/TFFSA diagonalization claims
  logically separate.
- 2026-06-01 issue #494 benchmark-manifest pass: added a machine-readable
  finite cross-method benchmark-manifest protocol and script.  The text
  explicitly identifies the pairwise consistency inequality as finite
  arithmetic on declared coordinates and error envelopes, not as evidence
  that any continuum QFT limit or common target observable has been proved.

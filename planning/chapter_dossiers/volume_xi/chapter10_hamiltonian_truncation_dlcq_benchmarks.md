# Chapter 10: Hamiltonian Truncation, DLCQ, And Benchmark Protocols

## Source Position

Volume XI adds Hamiltonian regulator methods after stochastic and lattice
constructions, emphasizing certified approximation rather than informal
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
- `Q_s`, `theta_n`, `rho_I`: finite-volume fermion momentum set, rapidity,
  and free Bethe-state density used in the TFFSA spin matrix element.
- `H(h)`, `W`, `lambda_*(h)`, `g`: finite affine Hermitian spectral-flow
  family, perturbing matrix, simple eigenvalue branch, and finite spectral gap
  used in the Hellmann-Feynman derivative certificate.
- `x^pm`, `p^+`, `K`: light-front coordinates, longitudinal momentum, and
  harmonic resolution.
- `M^2`, `P^-`: invariant mass operator and light-front Hamiltonian.
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
- Proves the Feshbach-Schur complement identity that underlies Hamiltonian
  truncation counterterms and high-energy tail corrections.
- Defines finite residual certificates for Hermitian truncation matrices and
  proves the residual-to-spectrum and spectral-projector leakage bounds used
  to certify numerical eigenpairs before any continuum interpretation.
- Records the exact finite Schur self-energy
  `Sigma_P(E)=PHQ(QHQ-E)^{-1}QHP` and isolates the separate norm-bound
  obligation for replacing it by a local counterterm.
- Defines finite Krylov spectral certificates for large truncation matrices,
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
- Derives the finite energy-variance certificate: variance equals residual
  norm, bounds distance from the finite spectrum, and bounds leakage from a
  separated finite spectral cluster.
- Derives the ground-projector leakage estimate when the finite ground
  energy and gap are known by an independent certificate.
- Derives the tangent-gradient formula for a smooth normalized ansatz, so a
  variational stationary point is identified as tangent-space residual
  orthogonality rather than an eigenvector certificate.
- Derives the finite local-energy mean and variance identities used by
  sampled neural-state and variational Monte Carlo calculations.
- Defines DLCQ kinematics and the role of harmonic resolution, then packages
  the light-front compactification, parton partitions, zero-mode treatment,
  finite \(P^-\) or \(M^2\) operator, and finite-\(K\) continuum diagnostic
  into a DLCQ regulator datum.
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
- Records benchmark requirements for truncation methods.
- Connects the chapter to `planning/14_code_policy.md`,
  `qft_scripts/tcsa_ising_energy_benchmark.py`,
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
- `qft_scripts/tffsa_ising_spin_connected.py --smoke`: builds the finite
  zero-momentum connected Ising spin-field TFFSA block, checks Hermiticity,
  and reports the finite eigenvalues and free energies.
- `qft_scripts/tffsa_ising_spectral_flow.py --smoke`: diagonalizes the finite
  connected Ising TFFSA block across a small magnetic-coupling grid and checks
  Hellmann-Feynman slopes against centered finite differences at a separated
  finite spectral point.
- `qft_scripts/thooft_dlcq.py --smoke`: builds and diagonalizes the finite
  principal-value matrix for the large-N two-dimensional QCD meson equation
  at a small harmonic resolution, with a positivity smoke check.
- `qft_scripts/thooft_dlcq_extrapolation.py --smoke`: fits fixed finite
  DLCQ eigenvalue labels to a chosen polynomial in `K^{-omega}`, reporting
  residuals, conditioning, and the finite intercept-remainder amplification
  factor without asserting a continuum spectrum.
- `calculation-checks/numerical_extrapolation_checks.py`: exact rational
  regression check for the Lagrange-interpolation obstruction, Richardson
  cancellation, and integer-power extrapolation weights used in the chapter.
- `calculation-checks/hamiltonian_truncation_dlcq_checks.py`: finite
  regression check for the Ising-energy benchmark spectrum, the large-\(N\)
  two-dimensional QCD DLCQ quadratic-form identity, connected Ising TFFSA
  block normalization, finite Ising TFFSA spectral-flow derivative identities,
  finite large-`K` fit algebra, finite residual certification,
  spectral-projector leakage, the Feshbach determinant identity, and the
  Krylov/Lanczos Ritz-residual plus finite spectral-moment identities.  It
  also checks variational energy variance, ground-projector leakage,
  tangent-gradient, and local-energy mean/variance identities.

## Anti-Wrapper Audit

- 2026-05-29: strengthened the Schur-complement proposition into a
  Feshbach-Schur reduction with an explicit resolvent-distance
  bound on the eliminated \(Q\)-component, so the statement now records the
  estimate relevant to truncation control rather than only a block-matrix
  rearrangement.
- 2026-05-29 eighth pass: demoted the finite residual spectral certificate
  from proposition form to linear-algebra prose.  The residual-to-spectrum
  and leakage bounds remain as numbered equations because they are useful
  diagnostics, but their derivation is an elementary eigenbasis calculation.
- 2026-05-31 statmech numerical-evidence pass: added Krylov/Lanczos
  finite-spectral evidence machinery as derivational prose rather than a
  theorem wrapper, with exact residual and moment identities tied to
  seed-overlap and symmetry-sector coverage.
- 2026-05-31 second statmech numerical-evidence pass: added finite
  variational ansatz certificates for tensor-network/neural-state methods as
  derivational prose, with finite residual, variance, tangent-gradient, and
  local-energy identities rather than theorem wrappers.

# Chapter 10: Hamiltonian Truncation, DLCQ, And Benchmark Protocols

## Source Position

Volume XI adds Hamiltonian regulator methods after stochastic and lattice
constructions, emphasizing certified approximation rather than informal
numerics.

## Notation Inventory

- `H`, `Hilb`, `Hilb_Lambda`, `P_Lambda`: Hamiltonian, Hilbert space,
  truncated subspace, and projection.
- `H_Lambda^ren`, `c_a`: renormalized projected Hamiltonian and local
  counterterm coordinates.
- `E_n(Lambda)`: variational finite-subspace eigenvalue.
- `E_cut`: truncated conformal-space cutoff.
- `tau`, `h`: thermal and magnetic Ising deformation couplings.
- `r`, `p_r`, `H_r`, `H_N`: Neveu-Schwarz Majorana mode label, finite-circle
  momentum, two-dimensional Bogoliubov block, and finite direct-sum
  Hamiltonian for the Ising energy-deformation benchmark.
- `Q_s`, `theta_n`, `rho_I`: finite-volume fermion momentum set, rapidity,
  and free Bethe-state density used in the TFFSA spin matrix element.
- `x^pm`, `p^+`, `K`: light-front coordinates, longitudinal momentum, and
  harmonic resolution.
- `M^2`, `P^-`: invariant mass operator and light-front Hamiltonian.
- `M_K^2`, `x_n`, `gamma`: finite harmonic-resolution matrix for the
  large-N two-dimensional QCD meson principal-value operator, grid point, and
  coupling normalization.

## Claim Ledger

- Defines projected Hamiltonian regulator data with counterterms.
- Derives the Rayleigh-Ritz upper bound for discrete eigenvalues at fixed
  regulated Hamiltonian.
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
- Proves the Feshbach-Schur complement identity that underlies Hamiltonian
  truncation counterterms and high-energy tail corrections.
- Defines DLCQ kinematics and the role of harmonic resolution.
- Constructs a finite DLCQ-style matrix for the large-N two-dimensional QCD
  meson equation and proves positivity of its quadratic form.
- Records benchmark requirements for truncation methods.
- Connects the chapter to `planning/14_code_policy.md`,
  `qft_scripts/tcsa_ising_energy_benchmark.py`,
  `qft_scripts/thooft_dlcq.py`, and `tools/run_qft_scripts_smoke.sh`.

## Figure Ledger

No figure is included in this pass.  Future figures should include Hilbert
space cutoff towers, DLCQ momentum partitions, and benchmark extrapolation
plots.

## Companion Scripts

- `qft_scripts/tcsa_ising_energy_benchmark.py --smoke`: diagonalizes finite
  Ising thermal-deformation Bogoliubov blocks and checks their exact
  eigenvalues.
- `qft_scripts/thooft_dlcq.py --smoke`: builds and diagonalizes the finite
  principal-value matrix for the large-N two-dimensional QCD meson equation
  at a small harmonic resolution, with a positivity smoke check.

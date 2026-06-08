# Chapter 08: Cosmological Spacetimes and Particle Creation
Source-File: monograph/tex/volumes/volume_xii/chapter08_cosmological_spacetimes_particle_creation.tex

## Source Position

In the printed Volume XII order, time-dependent globally hyperbolic
backgrounds follow the Unruh and Hawking fixed-background horizon material
and precede semiclassical backreaction.  The chapter uses the microlocal
Hadamard, locally covariant, point-splitting, and trace-anomaly foundations
already established; the background-gauge/index-theory anomaly lane follows
after backreaction.  The chapter develops cosmological particle creation as a
precise relation between complex structures on the real symplectic solution
space, not as a slogan about ambiguity.

## Notation Inventory

- `a(t)`, `eta`, `mathcal H`: Robertson--Walker scale factor, conformal time,
  and conformal Hubble function \(a'/a\).
- `R`: scalar curvature of the spatially flat Robertson--Walker metric.
- `phi_k`, `chi_k`, `Omega_k`: Fourier mode, rescaled mode, and
  time-dependent effective frequency.
- `p=(d-2)/2`, `xi_c`: rescaling exponent and conformal-coupling constant.
- `S`, `sigma`, `J`, `H_J`, `F_J`: real solution space, symplectic form,
  compatible complex structure, one-particle Hilbert space, and Fock space.
- `u_k^{in/out}`, `alpha_k`, `beta_k`, `B_k`: asymptotic modes, Bogoliubov
  coefficients, and the \(2\times2\) mode matrix
  \(\begin{pmatrix}\alpha_k&\beta_k\\ \overline{\beta_k}&\overline{\alpha_k}\end{pmatrix}\).
- `W_k`, `W_k^{[2r]}`, `omega_{0,k}`, `V_{2,k}`, `Lambda_N`: adiabatic
  frequency, truncated WKB frequency, derivative-free zeroth-order frequency,
  second-order curvature potential, and finite-order adiabatic two-point
  function.
- `P(E)`, `chi(tau)`, `W(x,x')`: detector response, switching function, and
  two-point function.
- `H`, `nu`: de Sitter Hubble constant and Hankel index for Bunch--Davies
  modes.
- `rho_beta`, `P_beta`, `Omega_k^+`, `a_+`: produced-particle energy
  density, pressure, out conformal frequency, and future static scale factor
  used in the stress-tensor/backreaction bridge.
- `n_k(t)`, `S_n`, `D_diag`: time-dependent diagonal particle occupation,
  production source \(a^{-d}\int\Omega_k\dot n_k\), and the identically
  vanishing diagonal identity difference.
- `Delta T_miss`, `Delta rho_miss`, `Delta P_miss`, `C_miss`: full
  renormalized stress minus the diagonal particle stress, its homogeneous
  energy/pressure coordinates, and the omitted-stress divergence defect
  \(\dot{\Delta\rho}_{miss}+(d-1)H(\Delta\rho_{miss}+\Delta P_{miss})\).
- `C_d`, `Delta H_ret^2`, `B_rho`, `B_P`, `B_div`, `B_H`, `B_dotH`,
  `F_{f,L}`, `s_L`, `N_{rho,L}[f]`, `G_ret^* ell_H`: homogeneous FLRW
  response coefficient, retained produced Hubble-square coordinate,
  stress-coordinate/divergence/gravity remainder budgets, compact stress-noise
  test tensor, normalized spatial profile, smeared stress covariance, and
  retarded metric-observable pullback for the backreaction diagnostic.

## Claim Ledger

- Derives the spatially flat Robertson--Walker scalar mode equation with the
  explicit effective frequency
  \(k^2+a^2(m^2+\xi R)-p\mathcal H'-p^2\mathcal H^2\).
- Proves exact cancellation of the time-dependent terms for the massless
  conformally coupled scalar in arbitrary spacetime dimension.
- Defines compatible complex structures and one-particle Hilbert spaces from
  the real symplectic solution space.
- Proves the diagonal Shale--Stinespring criterion in a countable mode basis
  by the two-mode squeezed-vacuum and infinite tensor-product argument, and
  separates the finite-volume unitary-equivalence condition from the
  noncompact momentum-space particle-density diagnostic.
- Derives Bogoliubov normalization, the annihilator transformation, and
  phase-sensitive squeezed correlators from one explicit \(2\times2\) matrix:
  the annihilator column transforms by \(B_k^T\), the inverse relation uses
  \((B_k^{-1})^T\), and the adjoint is not the coefficient-comparison matrix.
  It states the in/out mode rephasing law for \(\alpha_k\), \(\beta_k\), and
  annihilators, then derives both \(\langle N_k^{\rm out}\rangle=|\beta_k|^2\)
  and \(\langle a_k^{\rm out}a_{-k}^{\rm out}\rangle=\alpha_k\overline{\beta_k}\).
- Gives the instantaneous frequency-jump example as a normalization check.
- Derives the exact Riccati equation for the adiabatic frequency, separates
  \(\Omega_k^2=\omega_{0,k}^2+V_{2,k}\) with \(V_{2,k}\) counted as second
  adiabatic order, records the corrected second-order frequency, and gives the
  truncated-WKB initial-data prescription with its positivity/turning-point
  boundary.
- Separates finite adiabatic order from full Hadamard regularity: finite order
  is a Sobolev-wavefront condition \(WF'^s(\Lambda_N)\subset C^+\) below a
  finite threshold, while full Hadamard regularity is the infinite-order
  microlocal spectrum condition.  Fourth-order adiabatic subtraction is stated
  only as the selected four-dimensional stress-subtraction coefficient match,
  not as a Hadamard claim.
- Records positivity of the switched detector response as direct
  positive-type smearing of the two-point function, with the pointlike
  worldline smearing understood as a limit of ordinary spacetime test
  functions.
- Derives the de Sitter \(\nu\) parameter and gives normalized
  Bunch--Davies Hankel modes with their past positive-frequency asymptotic.
- Converts out-region Bogoliubov particle data into the finite produced
  stress-tensor contribution
  \(\rho_\beta=a_+^{-d}\int\Omega_k^+|\beta_k|^2\) and
  \(P_\beta=a_+^{-d}\int k^2|\beta_k|^2/((d-1)\Omega_k^+)\), separating this
  from vacuum subtraction, finite curvature counterterms, and tail/adiabatic
  remainders.
- Records the homogeneous Friedmann response
  \(\delta H_t^2=2\kappa_d\delta\rho_\beta/((d-1)(d-2))\) as the retained
  source bridge from particle production to semiclassical backreaction.
- Adds the finite continuity identity
  \(\dot\rho_n+(d-1)H(\rho_n+P_n)=a^{-d}\int\Omega_k\dot n_k\), showing that
  a time-dependent particle diagnostic carries pressure work and a production
  source.  The chapter explicitly states that the resulting diagonal difference
  \(D_{diag}\) is an algebraic zero and not a residual for omitted coherence,
  basis, vacuum, geometric, or tail stress.
- Adds the omitted-stress conservation defect.  In a fixed renormalization
  scheme the full stress is decomposed as diagonal particle stress plus
  coherence, basis-change, vacuum, geometric, and tail pieces.  The controlled
  quantity is
  \({\mathcal C}_{miss}=\dot{\Delta\rho}_{miss}
  +(d-1)H(\Delta\rho_{miss}+\Delta P_{miss})\), with a declared time-window
  smearing/norm, state class, adiabatic/subtraction order, regulator, and order
  of limits.  If those estimates are absent, the comparison is a hypothesis or
  proof obligation rather than a controlled residual.
- Adds a finite FLRW produced-stress backreaction window:
  \(\Delta H_{\rm ret}^2=C_d\rho_n\) is admissible only after scheme transport,
  stress-coordinate budgets, omitted-stress divergence/pressure budgets, drift
  control, separate retarded gravitational-response remainders, and stress-noise
  bounds are declared.  The stress-noise diagnostic is a compact spacetime test-tensor covariance
  \(N(F_{f,L},F_{f,L})\), with normalized spatial averaging, explicit time-scale,
  spatial-scale, and volume dependence, Chapter 11 product-extension/Ward
  conventions, and retarded metric-response pushforward before comparison with a
  metric accuracy.
- States the backreaction boundary: particle production is a diagnostic of a
  state, not a closed semiclassical Einstein equation.

## Calculation Ledger

- `calculation-checks/cosmological_particle_creation_checks.py` checks the
  conformal-coupling cancellation, de Sitter \(\nu\)-parameter arithmetic,
  sudden-quench Bogoliubov normalization, the complex two-mode Bogoliubov
  matrix with genuinely complex \(\alpha\), the transpose-not-adjoint
  annihilator transformation, rephasing covariance, anomalous out-correlator
  phase, a power-law adiabatic Riccati identity, the finite adiabatic-order
  curvature split, the finite-order-versus-Hadamard negative control,
  truncated-WKB positivity, finite positive-type detector-response Gram forms,
  the out-region produced energy/pressure formulas, the required \(a_+^{-d}\)
  scale-factor power, the massless equation of state, and the Friedmann response
  coefficient, plus the time-dependent produced-stress continuity identity with
  negative controls against wrong pressure normalization, wrong scale-factor
  power, and treating ongoing production as a conserved fluid.  It includes an
  adversarial omitted-stress example in which the diagonal identity difference is
  exactly zero while the full-minus-diagonal stress and its divergence are
  nonzero.
  The same script now checks the finite backreaction-window budget, including
  scheme transport, coherence/basis/vacuum/geometric/tail stress-coordinate
  remainders, omitted-stress divergence control of the full-minus-retained
  Hubble drift, pressure-dependent Hubble drift, number-density-only failures,
  compact spacetime stress-noise smearing, pointlike/whole-slice negative
  controls, and retarded metric-noise tolerances.
- Related scripts: `calculation-checks/point_splitting_stress_checks.py` for
  de Sitter stress-tensor/anomaly arithmetic and
  `calculation-checks/hawking_bogoliubov_checks.py` for the black-hole
  Bogoliubov analogue.

## Figure Ledger

No figure is included in this pass.  Future figures should show an
asymptotically static scale factor with the in/out complex structures and a
timelike detector worldline sampling the two-point function.

## Residual Work

- Add a smooth exactly solvable scale-factor example, rather than only the
  sudden-jump normalization model.
- Develop interacting cosmological QFT and semiclassical backreaction beyond
  finite free-field produced-stress windows and fixed-background diagnostics.

## Audit Notes

- 2026-05-30 quoted-theorem proof-debt pass: replaced the diagonal
  Shale--Stinespring `quotedtheorem` by a local theorem with proof.  The pass
  also corrected the continuum wording: \(\int |\beta_{\mathbf k}|^2\,d\mathbf
  k\) is a finite-density/local diagnostic on a noncompact homogeneous slice,
  whereas global Fock-unitary equivalence is the Hilbert--Schmidt condition
  and, for exact continuum-diagonal multiplication, fails unless the
  multiplication part vanishes almost everywhere.
- 2026-06-04 issue #729 cosmological backreaction pass: added
  `ca:cosmology-out-produced-stress-tensor`, converting out-region particle
  production into a renormalized-stress source coordinate and homogeneous
  Friedmann response while keeping vacuum-subtraction, curvature-counterterm,
  and tail/remainder data separate.
- 2026-06-04 issue #729 produced-stress continuity pass: added
  `ca:cosmology-produced-stress-continuity`, deriving the finite continuity
  identity for time-dependent diagonal particle occupations.  The companion
  verifies the pressure-work cancellation, the source term
  \(a^{-d}\int\Omega_k\dot n_k\), and negative controls against pressure,
  scale-factor, and conserved-fluid shortcuts.
- 2026-06-05 issue #729 cosmological backreaction-window pass: added
  `ca:cosmology-produced-stress-backreaction-window`, turning the produced
  stress into a controlled finite FLRW source only after scheme transport,
  stress/gravity/tail budgets, continuity/drift control, and stress-noise
  bounds are supplied.  The companion script verifies the same bookkeeping and
  negative controls.
- 2026-06-08 issue #729 printed-order pass: updated the source-position
  dossier and added an opening dependency map.  The chapter now names the
  microlocal Hadamard state condition and the symplectic/complex-structure
  object it actually studies, while reserving renormalized source,
  interacting pAQFT, and backreaction claims for their stronger hypotheses.
- 2026-06-08 issue #844 semantic-status pass: reclassified the produced-stress
  continuity block from `controlledapproximation` to a proposition titled
  "Continuity identity for produced stress".  The exact diagonal finite-window
  identity is kept theorem-family visible; the surrounding use as a
  semiclassical source remains bounded by the later backreaction-window
  controlled approximation.
- 2026-06-08 issue #916 Bogoliubov phase pass: replaced the conjugated-alpha
  annihilator rule by a single \(2\times2\) mode-matrix derivation, separated
  transpose, adjoint, and inverse operations, and added complex-alpha finite
  regression coverage for particle number, anomalous correlators, and in/out
  rephasing.  This is a phase-sensitive operator-coordinate repair; the real
  sudden-quench example remains only a normalization check.
- 2026-06-08 issue #915 stress-noise pass: replaced the time-only
  \(N_\rho[f]\) diagnostic by a compact spacetime stress test tensor
  \(F_{f,L}=f(t)s_Lu\otimes u\), tied the covariance to the Chapter 11
  unordered stress-product extension and Ward identities, declared the
  time/spatial/volume scaling and infrared prescription, and required retarded
  metric covariance pushforward before tolerance comparisons.  The companion
  rejects pointlike spatial evaluation and unnormalized whole-slice smearing.
- 2026-06-08 issue #914 finite-adiabatic-order pass: separated
  derivative-free \(\omega_{0,k}\) data from the second-order curvature
  potential \(V_{2,k}\), replaced the old "sufficiently high finite order is
  Hadamard" wording with the Junker--Schrohe Sobolev-wavefront finite-order
  criterion, and restricted fourth-order adiabatic subtraction to the
  four-dimensional stress-tensor coefficient match.  The companion now has a
  negative control that passes the selected fourth-order subtraction gate while
  failing a full smooth-difference/Hadamard gate.
- 2026-06-08 issue #962 omitted-stress residual pass: ended the produced-stress
  proposition at the exact diagonal identity and replaced the old tautological
  continuity residual by a scheme-fixed full-minus-diagonal stress
  decomposition.  The new controlled block tracks coherence, basis-change,
  vacuum, geometric, and tail stress through \({\mathcal C}_{miss}\), with
  explicit window/norm and order-of-limits requirements.  The backreaction
  window now separates stress-coordinate error from retarded gravitational
  response and propagates omitted-stress divergence into the Hubble-drift error
  bound.

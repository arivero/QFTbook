# Chapter 08: Cosmological Spacetimes and Particle Creation

## Source Position

Volume XII now adds time-dependent globally hyperbolic backgrounds after
Hadamard states, stress tensors, trace anomalies, horizon effects,
background gauge fields, index theory, and global anomalies.  The chapter
develops cosmological particle creation as a precise relation between
complex structures on the real symplectic solution space, not as a slogan
about ambiguity.

## Notation Inventory

- `a(t)`, `eta`, `mathcal H`: Robertson--Walker scale factor, conformal time,
  and conformal Hubble function \(a'/a\).
- `R`: scalar curvature of the spatially flat Robertson--Walker metric.
- `phi_k`, `chi_k`, `Omega_k`: Fourier mode, rescaled mode, and
  time-dependent effective frequency.
- `p=(d-2)/2`, `xi_c`: rescaling exponent and conformal-coupling constant.
- `S`, `sigma`, `J`, `H_J`, `F_J`: real solution space, symplectic form,
  compatible complex structure, one-particle Hilbert space, and Fock space.
- `u_k^{in/out}`, `alpha_k`, `beta_k`: asymptotic modes and Bogoliubov
  coefficients.
- `W_k`: adiabatic frequency in the WKB ansatz.
- `P(E)`, `chi(tau)`, `W(x,x')`: detector response, switching function, and
  two-point function.
- `H`, `nu`: de Sitter Hubble constant and Hankel index for Bunch--Davies
  modes.
- `rho_beta`, `P_beta`, `Omega_k^+`, `a_+`: produced-particle energy
  density, pressure, out conformal frequency, and future static scale factor
  used in the stress-tensor/backreaction bridge.
- `n_k(t)`, `S_n`, `E_cont`: time-dependent diagonal particle occupation,
  production source \(a^{-d}\int\Omega_k\dot n_k\), and continuity residual
  for using produced stress as a backreaction input.

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
- Derives Bogoliubov normalization and the out-particle number in the
  in-vacuum from the Wronskian and the annihilator transformation.
- Gives the instantaneous frequency-jump example as a normalization check.
- Derives the exact Riccati equation for the adiabatic frequency and records
  the second-order solution.
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
- Adds the finite continuity certificate
  \(\dot\rho_n+(d-1)H(\rho_n+P_n)=a^{-d}\int\Omega_k\dot n_k\), showing that
  a time-dependent particle diagnostic becomes a backreaction source only
  together with pressure work and the production term; an out region with
  \(\dot n_k=0\) is the conserved produced-gas limit.
- States the backreaction boundary: particle production is a diagnostic of a
  state, not a closed semiclassical Einstein equation.

## Calculation Ledger

- `calculation-checks/cosmological_particle_creation_checks.py` checks the
  conformal-coupling cancellation, de Sitter \(\nu\)-parameter arithmetic,
  sudden-quench Bogoliubov normalization, a power-law adiabatic Riccati
  identity, finite positive-type detector-response Gram forms, the out-region
  produced energy/pressure formulas, the required \(a_+^{-d}\) scale-factor
  power, the massless equation of state, and the Friedmann response
  coefficient, plus the time-dependent produced-stress continuity identity
  with negative controls against wrong pressure normalization, wrong
  scale-factor power, and treating ongoing production as a conserved fluid.
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
  the free-field and fixed-background diagnostics.

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
  certificate for time-dependent diagonal particle occupations.  The companion
  verifies the pressure-work cancellation, the source term
  \(a^{-d}\int\Omega_k\dot n_k\), and negative controls against pressure,
  scale-factor, and conserved-fluid shortcuts.

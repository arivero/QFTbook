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

## Claim Ledger

- Derives the spatially flat Robertson--Walker scalar mode equation with the
  explicit effective frequency
  \(k^2+a^2(m^2+\xi R)-p\mathcal H'-p^2\mathcal H^2\).
- Proves exact cancellation of the time-dependent terms for the massless
  conformally coupled scalar in arbitrary spacetime dimension.
- Defines compatible complex structures and one-particle Hilbert spaces from
  the real symplectic solution space.
- States the diagonal Shale--Stinespring criterion to distinguish finite
  particle density from unitary equivalence of Fock representations.
- Derives Bogoliubov normalization and the out-particle number in the
  in-vacuum from the Wronskian and the annihilator transformation.
- Gives the instantaneous frequency-jump example as a normalization check.
- Derives the exact Riccati equation for the adiabatic frequency and records
  the second-order solution.
- Proves positivity of the switched detector response from positive type of
  the two-point function.
- Derives the de Sitter \(\nu\) parameter and gives normalized
  Bunch--Davies Hankel modes with their past positive-frequency asymptotic.
- States the backreaction boundary: particle production is a diagnostic of a
  state, not a closed semiclassical Einstein equation.

## Calculation Ledger

- `calculation-checks/cosmological_particle_creation_checks.py` checks the
  conformal-coupling cancellation, de Sitter \(\nu\)-parameter arithmetic,
  sudden-quench Bogoliubov normalization, a power-law adiabatic Riccati
  identity, and finite positive-type detector-response Gram forms.
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

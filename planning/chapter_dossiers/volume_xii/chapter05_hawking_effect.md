# Volume XII, Chapter 5 Dossier: The Hawking Effect
Source-File: monograph/tex/volumes/volume_xii/chapter05_hawking_effect.tex

## Logical Role

- Role in the monograph: derive Hawking thermality for fixed black-hole
  backgrounds from horizon regularity, collapse ray tracing, wave-packet
  Bogoliubov mixing, and exterior propagation.
- Immediate predecessor: Unruh effect and wedge modular theory.
- Immediate successor: cosmological spacetimes and particle creation.
- Later consumers: semiclassical backreaction and the separate
  background-gauge/index-theory anomaly lane.

## Definitions And Results

- Killing horizon and surface gravity convention
  `chi^nu nabla_nu chi^mu = kappa chi^mu`.
- Zeroth-law/constant-surface-gravity hypothesis for the Rindler normal form
  and Euclidean period.
- Rindler normal form for a nonextremal constant-`kappa` horizon, with the
  variable-`kappa(y)` failure mode recorded.
- Schwarzschild normalization `kappa=1/(4M)` and `T_H=1/(8 pi M)`.
- Static Euclidean regularity and the exact scope of the KMS conclusion.
- Rotating-horizon generator `chi = partial_t + Omega_H partial_phi`,
  rotating KMS weight `omega - m Omega_H`, angular chemical potential, and
  superradiant-sector boundary.
- Late-time collapse ray-tracing lemma from regular Kruskal coordinate `U`
  and affine past-null coordinate `v`.
- Null-mode Klein-Gordon product and singular Bogoliubov coefficient
  calculation.
- Wave-packet definition with frequency bin `j` and retarded-time bin `n`,
  including one-particle orthonormality/completeness.
- Late-time packet occupation controlled approximation giving the Planck-bin
  average in the stationary late-time regime for number bins with positive
  lower frequency.
- Infrared split: the `j=0` massless number bin is logarithmically divergent,
  while the corresponding energy-flux bin is finite after the extra factor of
  `omega`.
- Quantitative late-time packet estimate with a global tracing cutoff,
  smooth positive-frequency packet windows, ray-map inverse error
  `O(exp(-kappa u_n))`, and smooth-remainder Fourier derivative bounds.
- Closed-form positive-lower-edge Planck-bin average and regression check for
  the sign of the logarithm.
- Two-dimensional stress-tensor flux from the Schwarzian derivative of the
  exponential ray-tracing map.
- Trans-Planckian precursor-frequency estimate.
- Boulware, Hartle-Hawking, and Unruh states as state-selection properties.
  Their clean three-state taxonomy is stated for static bifurcate exteriors;
  rotating analogues require model-specific superradiance and regularity
  qualifications.
- Scalar Schwarzschild radial wave equation and greybody flux formula.
- Interacting horizon flux package: KMS greater/lesser functions determine the
  universal thermal ratio, while the spectral density, channel mixing,
  stress-tensor renormalization, greybody propagation, nonstationary tails, and
  backreaction corrections remain declared model-dependent inputs/residuals.
- Semiclassical back-reaction boundary, adiabatic mass-loss equation, and
  flux-to-mass backreaction window with drift, state-transport, gravitational,
  quasi-stationary, and flux-noise controls.
- Interacting Hawking theorem open problem.

## Symbols

| Symbol | Meaning |
| --- | --- |
| `chi` | horizon-generating Killing field |
| `kappa` | surface gravity in the normalization of `chi` |
| `Omega_H`, `tilde omega` | horizon angular velocity and rotating horizon energy `omega - m Omega_H` |
| `rho,t` | Rindler-normal distance and stationary time |
| `U,V` | regular Kruskal-type null coordinates |
| `beta_H` | inverse Hawking temperature `2 pi/kappa` |
| `T_H` | Hawking temperature `kappa/(2 pi)` |
| `u,v` | retarded and advanced null times on `I^+` and `I^-` |
| `v_0` | last escaping null ray |
| `C` | nonuniversal ray-tracing constant |
| `alpha_{omega omega'}, beta_{omega omega'}` | Bogoliubov coefficients between in and out modes |
| `epsilon` | frequency-bin width for Hawking packets |
| `p_{jn}^{out}` | outgoing wave packet localized in frequency bin `j` and time bin `n` |
| `h_j`, `zeta`, `E(x)`, `r_omega` | smooth packet window, global past-null cutoff, inverse ray-map error, and smooth traced-mode remainder |
| `p(u)` | ray-tracing function from `I^+` to `I^-` |
| `{p,u}` | Schwarzian derivative |
| `Gamma_l(omega)` | greybody transmission probability |
| `r_*` | Schwarzschild tortoise coordinate |
| `G_A^>(omega)`, `G_A^<(omega)` | interacting horizon-channel Wightman boundary values |
| `rho_A(omega)` | positive horizon spectral density `G_A^>-G_A^<` |
| `F_I^{ret}`, `R_I` | retained interacting flux on a frequency window and its residual |
| `L_I^{ret}(M_0)` | retained stress-flux luminosity on a mass chart |
| `R_flux`, `R_drift`, `R_state`, `R_grav` | flux, drift, state-transport, and gravitational residuals in the mass-loss window |
| `N_J` | integrated connected covariance of the retained flux observable on a retarded-time window |
| `epsilon_qs` | quasi-stationary control parameter for the mass-loss window |

## Claim Ledger

1. A nonextremal Killing horizon has Rindler normal form with acceleration
   scale `kappa` after a zeroth-law or bifurcate-horizon hypothesis supplies
   constant surface gravity.
2. If `kappa=kappa(y)`, the displayed coordinate transformation develops
   transverse terms and no single Euclidean period regularizes the whole
   cross-section.
3. Euclidean smoothness fixes period `2 pi/kappa` only in the static
   real-cone argument, provided the Euclidean object and Lorentzian analytic
   continuation exist.
4. Rotating horizons use the generator
   `chi = partial_t + Omega_H partial_phi` and the KMS weight
   `omega - m Omega_H`; superradiant modes require a separate scattering
   treatment and obstruct the generic static Hartle-Hawking story.
5. Regular Kruskal coordinate plus smooth collapse ray labeling gives
   `v_0-v = C exp(-kappa u) + O(exp(-2 kappa u))`.
6. The singular Fourier transform of the traced outgoing mode gives
   `|alpha|^2/|beta|^2 = exp(2 pi omega/kappa)` and the displayed
   `|beta|^2` density.
7. Continuous `|beta|^2` is not a particle number; Hawking quanta must be
   defined by wave-packet observables.
8. The packet occupation tends to the Planck-bin average at late retarded
   time only for positive-lower-edge number bins or other infrared-safe
   observables.
9. The `j=0` sharp number packet is infrared divergent in the idealized
   massless horizon calculation; energy flux remains finite because the
   stress tensor supplies an extra factor of `omega`.
10. The late-time remainder requires global support and Fourier derivative
   hypotheses.  Local smoothness across the last escaping ray does not by
   itself imply decay of the smooth contribution.
11. For a two-dimensional CFT, the exponential ray-tracing Schwarzian gives
   `T_uu = c kappa^2/(48 pi)`, matching the chiral thermal flux.
12. The trans-Planckian estimate is a domain-of-validity statement for the
   fixed-background continuum derivation.
13. Greybody factors are exterior scattering data, separate from the universal
   horizon Planck factor.
14. In an interacting QFT, the universal thermal factor is a KMS
    spectral-density relation.  The flux at infinity also requires the
    interacting spectral density, channel basis, greybody propagation,
    stress-tensor conversion, and residual budget.
15. The adiabatic mass-loss ODE is a controlled finite-window approximation
    only after the retained stress-flux luminosity, drift bound,
    state-transport error, gravitational EFT residual, quasi-stationary
    parameter, and integrated flux noise are all controlled.
16. Semiclassical back-reaction requires additional hypotheses and is not a
    consequence of the fixed-background Hawking calculation alone.

## Calculation Ledger

- `calculation-checks/hawking_bogoliubov_checks.py` verifies the
  Gamma-function norm, thermal ratio, negative-frequency coefficient,
  continuum normalization density, wave-packet Planck-bin average,
  packet Fourier orthogonality/completeness, the `j=0` infrared number
  divergence, finite low-frequency energy flux, exponential precursor
  blueshift, ray-map/smooth-remainder late-time packet bounds, the
  constant-`kappa` Rindler gate, variable-`kappa(y)` coordinate failure,
  rotating `omega-m Omega_H` KMS weights, superradiant-channel negative
  controls, Schwarzian flux, chiral Planck flux, and Schwarzschild temperature
  convention.  It also checks the interacting horizon KMS spectral-density
  package, greybody-weighted retained flux, residual-budget negative controls,
  stress-flux mass-loss bookkeeping, and the flux-to-mass backreaction window
  with drift, quasi-stationary, noise, and number-flux negative controls.

## Figures

- No figure is included.  A later figure pass should add a collapse Penrose
  diagram showing `I^-`, `I^+`, the last escaping ray `v_0`, the future
  horizon, and the exponential relation between `u` and `v`.

## Audit Notes

- 2026-06-04 issue #729 horizon-interaction pass: added the interacting
  horizon flux package so the chapter no longer treats the free Planck
  particle-number formula as the interacting stress-flux statement.  The
  companion is now an evidence-contract check with negative controls against
  overreading KMS thermality as a full interacting Hawking theorem.
- 2026-06-04 issue #729 backreaction-window pass: strengthened the
  fixed-background-to-semiclassical interface by requiring mass-loss drift,
  state/gravity residuals, quasi-stationary control, and flux-noise chart
  control before an interacting horizon flux is read as an evaporating metric.
- 2026-06-08 issue #729 printed-order pass: updated the source-position
  dossier and added an opening TeX paragraph that identifies the Hadamard or
  Unruh-type horizon regularity input as the microlocal state condition, while
  separating fixed-background propagation from interacting pAQFT corrections
  and metric backreaction.
- 2026-06-08 issue #908 infrared-packet pass: excluded the sharp `j=0` bin as
  a finite number observable, separated number and energy-flux infrared
  behavior, and replaced the unsupported smooth-remainder `o(1)` statement by
  a global-cutoff and Fourier-derivative late-time packet estimate.
- 2026-06-08 issue #907 horizon-hypothesis pass: made constant surface gravity
  an explicit zeroth-law/bifurcate-horizon input, restricted the real
  Euclidean cone proof to static horizons, added the rotating KMS generator
  and angular chemical-potential weight, and recorded superradiance/Kay-Wald
  qualifications for rotating state taxonomy.

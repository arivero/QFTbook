# Volume XII, Chapter 5 Dossier: The Hawking Effect

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
- Rindler normal form for a nonextremal horizon.
- Schwarzschild normalization `kappa=1/(4M)` and `T_H=1/(8 pi M)`.
- Euclidean regularity and the exact scope of the KMS conclusion.
- Late-time collapse ray-tracing lemma from regular Kruskal coordinate `U`
  and affine past-null coordinate `v`.
- Null-mode Klein-Gordon product and singular Bogoliubov coefficient
  calculation.
- Wave-packet definition with frequency bin `j` and retarded-time bin `n`.
- Late-time packet occupation controlled approximation giving the Planck-bin
  average in the stationary late-time regime.
- Closed-form Planck-bin average and regression check for the sign of the
  logarithm.
- Two-dimensional stress-tensor flux from the Schwarzian derivative of the
  exponential ray-tracing map.
- Trans-Planckian precursor-frequency estimate.
- Boulware, Hartle-Hawking, and Unruh states as state-selection properties.
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
   scale `kappa`.
2. Euclidean smoothness fixes period `2 pi/kappa`, provided the Euclidean
   object and Lorentzian analytic continuation exist.
3. Regular Kruskal coordinate plus smooth collapse ray labeling gives
   `v_0-v = C exp(-kappa u) + O(exp(-2 kappa u))`.
4. The singular Fourier transform of the traced outgoing mode gives
   `|alpha|^2/|beta|^2 = exp(2 pi omega/kappa)` and the displayed
   `|beta|^2` density.
5. Continuous `|beta|^2` is not a particle number; Hawking quanta must be
   defined by wave-packet observables.
6. The packet occupation tends to the Planck-bin average at late retarded
   time.
7. For a two-dimensional CFT, the exponential ray-tracing Schwarzian gives
   `T_uu = c kappa^2/(48 pi)`, matching the chiral thermal flux.
8. The trans-Planckian estimate is a domain-of-validity statement for the
   fixed-background continuum derivation.
9. Greybody factors are exterior scattering data, separate from the universal
   horizon Planck factor.
10. In an interacting QFT, the universal thermal factor is a KMS
    spectral-density relation.  The flux at infinity also requires the
    interacting spectral density, channel basis, greybody propagation,
    stress-tensor conversion, and residual budget.
11. The adiabatic mass-loss ODE is a controlled finite-window approximation
    only after the retained stress-flux luminosity, drift bound,
    state-transport error, gravitational EFT residual, quasi-stationary
    parameter, and integrated flux noise are all controlled.
12. Semiclassical back-reaction requires additional hypotheses and is not a
    consequence of the fixed-background Hawking calculation alone.

## Calculation Ledger

- `calculation-checks/hawking_bogoliubov_checks.py` verifies the
  Gamma-function norm, thermal ratio, negative-frequency coefficient,
  continuum normalization density, wave-packet Planck-bin average,
  exponential precursor blueshift, Schwarzian flux, chiral Planck flux, and
  Schwarzschild temperature convention.  It also checks the interacting
  horizon KMS spectral-density package, greybody-weighted retained flux,
  residual-budget negative controls, stress-flux mass-loss bookkeeping, and
  the flux-to-mass backreaction window with drift, quasi-stationary, noise,
  and number-flux negative controls.

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

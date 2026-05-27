# Volume XII, Chapter 5 Dossier: The Hawking Effect

## Logical Role

- Role in the monograph: derive Hawking thermality for fixed black-hole
  backgrounds from horizon regularity, collapse ray tracing, wave-packet
  Bogoliubov mixing, and exterior propagation.
- Immediate predecessor: Unruh effect and wedge modular theory.
- Immediate successor: background gauge fields and index-theoretic anomalies.

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
- Late-time packet occupation theorem giving the Planck-bin average.
- Closed-form Planck-bin average and regression check for the sign of the
  logarithm.
- Two-dimensional stress-tensor flux from the Schwarzian derivative of the
  exponential ray-tracing map.
- Trans-Planckian precursor-frequency estimate.
- Boulware, Hartle-Hawking, and Unruh states as state-selection properties.
- Scalar Schwarzschild radial wave equation and greybody flux formula.
- Semiclassical back-reaction boundary and adiabatic mass-loss equation.
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
10. Semiclassical back-reaction requires additional hypotheses and is not a
    consequence of the fixed-background Hawking calculation alone.

## Calculation Ledger

- `calculation-checks/hawking_bogoliubov_checks.py` verifies the
  Gamma-function norm, thermal ratio, negative-frequency coefficient,
  continuum normalization density, wave-packet Planck-bin average,
  exponential precursor blueshift, Schwarzian flux, chiral Planck flux, and
  Schwarzschild temperature convention.

## Figures

- No figure is included.  A later figure pass should add a collapse Penrose
  diagram showing `I^-`, `I^+`, the last escaping ray `v_0`, the future
  horizon, and the exponential relation between `u` and `v`.

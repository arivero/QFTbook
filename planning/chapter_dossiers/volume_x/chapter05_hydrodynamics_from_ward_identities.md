# Volume X, Chapter 5 Dossier: Hydrodynamics from Ward Identities

## Logical Role

- Role in the monograph: derive deterministic first-order hydrodynamics,
  entropy production, and the hydrodynamic pole structure from Ward
  identities and local thermodynamics after Kubo formulae have been defined.
- Immediate predecessor: spectral functions, Kubo formulae, and transport.
- Immediate successor: Schwinger--Keldysh hydrodynamic effective actions.

## Definitions And Results

- Local temperature, chemical potentials, and velocity field.
- Mostly-plus projector \(\Delta^{\mu\nu}=\eta^{\mu\nu}+u^\mu u^\nu\).
- Landau-frame condition \(u_\mu T^{\mu\nu}=-\varepsilon u^\nu\).
- Ideal stress tensor and current.
- Thermodynamic closure relations and Gibbs-Duhem identity.
- Ideal energy equation, Euler equation, charge equation, and entropy-current
  conservation.
- First-order shear, bulk, and charge-diffusion constitutive relations.
- Entropy-production formula fixing positivity of \(\eta\), \(\zeta\), and
  the conductivity matrix.
- Charge diffusion equation and Einstein relation \(D=\Sigma\chi^{-1}\).
- Linearized neutral stress tensor, shear pole, sound poles, and attenuation
  \(\Gamma_s=(\zeta+2\eta(d-1)/d)/(\varepsilon+p)\).
- Diffusive density retarded correlator
  \(G^R_{nn}=\chi Dk^2/(Dk^2-i\omega)+\text{analytic}\).
- Hydrodynamic scaling-limit boundary as a microscopic QFT claim.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(D=d+1\) | spacetime and spatial dimensions |
| \(u^\mu\) | future-timelike fluid velocity |
| \(T,\mu_A\) | temperature and chemical potentials |
| \(\varepsilon,p,n_A,s\) | energy density, pressure, charge densities, entropy density |
| \(w=\varepsilon+p\) | enthalpy density |
| \(\Delta^{\mu\nu}\) | spatial projector orthogonal to \(u^\mu\) |
| \(\vartheta\) | expansion \(\partial_\mu u^\mu\) |
| \(\sigma^{\mu\nu}\) | shear tensor |
| \(\eta,\zeta\) | shear and bulk viscosities |
| \(\Sigma_{AB}\) | conductivity matrix in \(J_A^\mu=n_Au^\mu-T\Sigma_{AB}\Delta^{\mu\nu}\partial_\nu(\mu_B/T)+\cdots\) |
| \(\chi_{AB}\) | charge susceptibility matrix |
| \(D_{AB}\) | diffusion matrix \(\Sigma_{AC}(\chi^{-1})_{CB}\) |
| \(c_s\) | speed of sound |
| \(\Gamma_s\) | sound attenuation constant |

## Claim Ledger

1. Projecting \(\partial_\mu T^{\mu\nu}_{(0)}=0\) along and orthogonal to
   \(u^\mu\) gives the ideal energy equation and Euler equation.
2. Current conservation gives the ideal charge equation.
3. The Gibbs-Duhem identity and first law imply conservation of
   \(S^\mu_{(0)}=su^\mu\) on ideal solutions.
4. In Landau frame the first-order parity-even stress and current are
   \(-\eta\sigma^{\mu\nu}-\zeta\Delta^{\mu\nu}\vartheta\) and
   \(-T\Sigma_{AB}\Delta^{\mu\nu}\partial_\nu(\mu_B/T)\).
5. Divergence of the first-order entropy current gives
   \[
     \partial_\mu S^\mu=
     \eta\sigma^2/(2T)+\zeta\vartheta^2/T
     +T\Sigma_{AB}\nabla(\mu_A/T)\nabla(\mu_B/T)+O(\partial^3),
   \]
   so the transport matrix positivity conditions follow.
6. Charge diffusion at constant \(T\) gives
   \(\omega=-i(\Sigma/\chi)k^2+\cdots\).
7. Linearized neutral hydrodynamics gives shear diffusion
   \(\omega=-i\eta k^2/(\varepsilon+p)+\cdots\) and sound poles
   \[
     \omega=\pm c_sk-\frac{i}{2}
     \frac{\zeta+2\eta(d-1)/d}{\varepsilon+p}k^2+\cdots .
   \]
8. Hydrodynamic correlator poles match the Kubo coefficients only after the
   thermodynamic and hydrodynamic scaling limits are specified.
9. The microscopic QFT theorem boundary requires local equilibration,
   clustering, analyticity, and control of nonconserved modes and long-time
   tails.

## Calculation Checks

- `calculation-checks/hydrodynamic_modes_checks.py` verifies the shear and
  sound dispersion equations, the entropy-production positivity structure,
  the diffusion Einstein relation, and the static limit of the diffusive
  density retarded correlator.

## Figures

- None in this chapter.

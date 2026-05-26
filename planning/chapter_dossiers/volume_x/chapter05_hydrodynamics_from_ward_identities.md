# Volume X, Chapter 5 Dossier: Hydrodynamics from Ward Identities

## Logical Role

- Role in the monograph: derive deterministic first-order hydrodynamics,
  entropy production, and the hydrodynamic pole structure from Ward
  identities, background-source response, and local thermodynamics after
  Kubo formulae have been defined.
- Immediate predecessor: spectral functions, Kubo formulae, and transport.
- Immediate successor: Schwinger--Keldysh hydrodynamic effective actions.

## Definitions And Results

- Local temperature, chemical potentials, and velocity field.
- Background metric/gauge source definitions of \(T^{\mu\nu}\) and
  \(J_A^\mu\), and the source Ward identities
  \(\nabla_\mu J_A^\mu=0\),
  \(\nabla_\mu T^\mu{}_\nu=F^A_{\nu\lambda}J_A^\lambda\).
- Mostly-plus projector \(\Delta^{\mu\nu}=\eta^{\mu\nu}+u^\mu u^\nu\).
- Landau-frame condition \(u_\mu T^{\mu\nu}=-\varepsilon u^\nu\).
- General hydrodynamic-frame decomposition and first-order frame
  transformations of energy and charge fluxes.
- Ideal stress tensor and current.
- Thermodynamic closure from the grand-canonical KMS pressure and the
  Gibbs-Duhem identity.
- Ideal energy equation, Euler equation, charge equation, and entropy-current
  conservation.
- First-order shear, bulk, and charge-diffusion constitutive relations.
- Entropy-production formula fixing positivity of \(\eta\), \(\zeta\), and
  the conductivity matrix.
- Single- and multi-charge diffusion equations, susceptibility geometry, and
  Einstein relation \(D=\Sigma\chi^{-1}\).
- Linearized neutral stress tensor, shear pole, sound poles, and attenuation
  \(\Gamma_s=(\zeta+2\eta(d-1)/d)/(\varepsilon+p)\).
- Diffusive density source-response kernel
  \(K^R_{nn}=\chi Dk^2/(Dk^2-i\omega)+\text{analytic}\), with the sign
  relation to the commutator-retarded convention stated explicitly.
- Hydrodynamic scaling-limit boundary as a microscopic QFT claim.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(D=d+1\) | spacetime and spatial dimensions |
| \(u^\mu\) | future-timelike fluid velocity |
| \(T,\mu_A\) | temperature and chemical potentials |
| \(g_{\mu\nu},A^A_\mu\) | background metric and Abelian gauge sources |
| \(\mathcal E^A_\mu\) | local-rest-frame electric covector \(F^A_{\mu\nu}u^\nu\) |
| \(\varepsilon,p,n_A,s\) | energy density, pressure, charge densities, entropy density |
| \(w=\varepsilon+p\) | enthalpy density |
| \(\Delta^{\mu\nu}\) | spatial projector orthogonal to \(u^\mu\) |
| \(q^\mu,\nu_A^\mu,\pi^{\mu\nu}\) | frame-dependent transverse energy flux, charge diffusion currents, and stress correction |
| \(\vartheta\) | expansion \(\partial_\mu u^\mu\) |
| \(\sigma^{\mu\nu}\) | shear tensor |
| \(\eta,\zeta\) | shear and bulk viscosities |
| \(\Sigma_{AB}\) | conductivity matrix in \(J_A^\mu=n_Au^\mu+\nu_A^\mu+\cdots\), with \(\nu_A^\mu=-T\Sigma_{AB}\Delta^{\mu\nu}\partial_\nu(\mu_B/T)\) when \(A^A_\mu=0\) |
| \(\chi_{AB}\) | charge susceptibility matrix |
| \(D_{AB}\) | diffusion matrix \(\Sigma_{AC}(\chi^{-1})_{CB}\) |
| \(K^R_{n_An_B}\) | density source-response kernel for the \(H-\int h_A n_A\) source convention |
| \(c_s\) | speed of sound |
| \(\Gamma_s\) | sound attenuation constant |

## Claim Ledger

1. Background-source variation defines \(T^{\mu\nu}\) and \(J_A^\mu\), and
   gauge/diffeomorphism invariance gives the source Ward identities.
2. Hydrodynamic frames are coordinate choices; first-order redefinitions
   shift \(q^\mu\) and \(\nu_A^\mu\) by
   \(-(\varepsilon+p)\delta u^\mu\) and \(-n_A\delta u^\mu\).
3. The grand-canonical pressure gives \(n_A=\partial p/\partial\mu_A\),
   \(s=\partial p/\partial T\), and
   \(\varepsilon+p=Ts+\mu_A n_A\).
4. Projecting \(\partial_\mu T^{\mu\nu}_{(0)}=0\) along and orthogonal to
   \(u^\mu\) gives the ideal energy equation and Euler equation.
5. Current conservation gives the ideal charge equation.
6. The Gibbs-Duhem identity and first law imply conservation of
   \(S^\mu_{(0)}=su^\mu\) on ideal solutions.
7. In Landau frame the first-order parity-even stress and current are
   \(-\eta\sigma^{\mu\nu}-\zeta\Delta^{\mu\nu}\vartheta\) and
   \(-T\Sigma_{AB}\Delta^{\mu\nu}\partial_\nu(\mu_B/T)\).
8. Divergence of the first-order entropy current gives
   \[
     \partial_\mu S^\mu=
     \eta\sigma^2/(2T)+\zeta\vartheta^2/T
     +T\Sigma_{AB}\nabla(\mu_A/T)\nabla(\mu_B/T)+O(\partial^3),
   \]
   so the transport matrix positivity conditions follow.
9. Charge diffusion at constant \(T\) gives
   \(\omega=-i(\Sigma/\chi)k^2+\cdots\).
10. Multi-charge diffusion has \(D=\Sigma\chi^{-1}\); if \(\chi\) is positive
    definite and \(\Sigma\) is symmetric positive semidefinite, \(D\) is
    similar to a symmetric positive semidefinite matrix and has nonnegative
    diffusion eigenvalues.
11. The density source-response matrix is
    \(K^R_{n_An_B}=k^2(Dk^2-i\omega)^{-1}_{AC}\Sigma_{CB}\) up to analytic
    contact terms, and its static limit is \(\chi_{AB}\).
12. Linearized neutral hydrodynamics gives shear diffusion
   \(\omega=-i\eta k^2/(\varepsilon+p)+\cdots\) and sound poles
   \[
     \omega=\pm c_sk-\frac{i}{2}
     \frac{\zeta+2\eta(d-1)/d}{\varepsilon+p}k^2+\cdots .
   \]
13. Hydrodynamic correlator poles match the Kubo coefficients only after the
   thermodynamic and hydrodynamic scaling limits are specified.
14. The microscopic QFT theorem boundary requires local equilibration,
   clustering, analyticity, and control of nonconserved modes and long-time
   tails.

## Calculation Checks

- `calculation-checks/hydrodynamic_modes_checks.py` verifies the shear and
  sound dispersion equations, the entropy-production positivity structure,
  the diffusion Einstein relation, the multi-charge susceptibility geometry,
  and the static limit of the diffusive density source-response kernel.

## Figures

- None in this chapter.

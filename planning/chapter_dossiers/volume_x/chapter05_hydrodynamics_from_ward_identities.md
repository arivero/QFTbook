# Volume X, Chapter 5 Dossier: Hydrodynamics from Ward Identities

## Logical Role

- Role in the monograph: derive deterministic first-order hydrodynamics,
  entropy production, and the hydrodynamic pole structure from Ward
  identities, background-source response, and local thermodynamics after
  Kubo formulae have been defined.
- Immediate predecessor: spectral functions, Kubo formulae, and transport.
- Immediate successor: Schwinger--Keldysh hydrodynamic effective actions.

## Definitions And Results

- First-order hydrodynamic datum \(\mathfrak D_{\rm hydro}\), aggregating
  the regulated Schwinger-Keldysh source functional, exact stress/current
  Ward identities, equilibrium thermodynamic manifold, local variables,
  Landau frame, ideal and first-gradient constitutive maps, and entropy
  positivity datum before the constitutive derivations begin.
- Local temperature, chemical potentials, and velocity field.
- Background metric/gauge source definitions of \(T^{\mu\nu}\) and
  \(J_A^\mu\), and the source Ward identities
  \(\nabla_\mu J_A^\mu=0\),
  \(\nabla_\mu T^\mu{}_\nu=F^A_{\nu\lambda}J_A^\lambda\).
- Hydrodynamic scaling family: slowly varying states and sources with an
  asymptotic constitutive expansion after thermodynamic limit and declared
  contact-term subtraction.
- Mostly-plus projector \(\Delta^{\mu\nu}=\eta^{\mu\nu}+u^\mu u^\nu\).
- Landau-frame condition \(u_\mu T^{\mu\nu}=-\varepsilon u^\nu\).
- General hydrodynamic-frame decomposition and first-order frame
  transformations of energy and charge fluxes, with Landau matching for
  scalar variables.
- Ideal stress tensor and current.
- Thermodynamic closure from the grand-canonical KMS pressure and the
  Gibbs-Duhem identity.
- Ideal energy equation, Euler equation, charge equation, and entropy-current
  conservation.
- Sourceful ideal Euler equation and reduction of acceleration plus the
  transverse temperature gradient to the charge thermodynamic force basis.
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
| \(\mathfrak D_{\rm hydro}\) | first-order parity-even hydrodynamic datum |
| \(\mathsf f\) | hydrodynamic frame choice, Landau matching in this chapter |
| \(\mathsf C^{(0)},\mathsf C^{(1)}\) | ideal and first-gradient constitutive maps |
| \(\mathsf E\) | entropy-current and positivity datum |
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
| \(\omega^{\mu\nu}\) | transverse vorticity |
| \(V_A^\mu\) | transverse sourceful thermodynamic force \(\Delta^{\mu\nu}[\mathcal E^A_\nu/T-\partial_\nu(\mu_A/T)]\) |
| \(\eta,\zeta\) | shear and bulk viscosities |
| \(\Sigma_{AB}\) | conductivity matrix in \(J_A^\mu=n_Au^\mu+\nu_A^\mu+\cdots\), with \(\nu_A^\mu=-T\Sigma_{AB}\Delta^{\mu\nu}\partial_\nu(\mu_B/T)\) when \(A^A_\mu=0\) |
| \(\chi_{AB}\) | charge susceptibility matrix |
| \(D_{AB}\) | diffusion matrix \(\Sigma_{AC}(\chi^{-1})_{CB}\) |
| \(K^R_{n_An_B}\) | density source-response kernel for the \(H-\int h_A n_A\) source convention |
| \(c_s\) | speed of sound |
| \(\Gamma_s\) | sound attenuation constant |

## Claim Ledger

1. The first-order hydrodynamic datum separates exact microscopic QFT input
   (source functional and Ward identities), equilibrium thermodynamics, frame
   choice, constitutive maps, and entropy positivity from the later
   hydrodynamic scaling assertion.
2. Background-source variation defines \(T^{\mu\nu}\) and \(J_A^\mu\), and
   gauge/diffeomorphism invariance gives the source Ward identities.
3. A constitutive relation is an asymptotic statement on hydrodynamic
   scaling families, not a finite-volume identity.
4. Hydrodynamic frames are coordinate choices; first-order redefinitions
   shift \(q^\mu\) and \(\nu_A^\mu\) by
   \(-(\varepsilon+p)\delta u^\mu\) and \(-n_A\delta u^\mu\).
5. The grand-canonical pressure gives \(n_A=\partial p/\partial\mu_A\),
   \(s=\partial p/\partial T\), and
   \(\varepsilon+p=Ts+\mu_A n_A\).
6. Projecting \(\partial_\mu T^{\mu\nu}_{(0)}=0\) along and orthogonal to
   \(u^\mu\) gives the ideal energy equation and Euler equation.
7. With external sources, the ideal Euler equation implies
   \(a^\mu+\Delta^{\mu\nu}\partial_\nu\log T
   =Tn_A V_A^\mu/(\varepsilon+p)\), so acceleration is not an independent
   first-order dissipative force.
8. Current conservation gives the ideal charge equation.
9. The Gibbs-Duhem identity and first law imply conservation of
   \(S^\mu_{(0)}=su^\mu\) on ideal solutions.
10. In Landau frame the first-order parity-even stress and current are
   \(-\eta\sigma^{\mu\nu}-\zeta\Delta^{\mu\nu}\vartheta\) and
   \(-T\Sigma_{AB}\Delta^{\mu\nu}\partial_\nu(\mu_B/T)\).
11. Divergence of the first-order entropy current gives
   \[
     \partial_\mu S^\mu=
     \eta\sigma^2/(2T)+\zeta\vartheta^2/T
     +T\Sigma_{AB}\nabla(\mu_A/T)\nabla(\mu_B/T)+O(\partial^3),
   \]
   so the transport matrix positivity conditions follow.
12. Charge diffusion at constant \(T\) gives
   \(\omega=-i(\Sigma/\chi)k^2+\cdots\).
13. Multi-charge diffusion has \(D=\Sigma\chi^{-1}\); if \(\chi\) is positive
    definite and \(\Sigma\) is symmetric positive semidefinite, \(D\) is
    similar to a symmetric positive semidefinite matrix and has nonnegative
    diffusion eigenvalues.
14. The density source-response matrix is
    \(K^R_{n_An_B}=k^2(Dk^2-i\omega)^{-1}_{AC}\Sigma_{CB}\) up to analytic
    contact terms, and its static limit is \(\chi_{AB}\).
15. Linearized neutral hydrodynamics gives shear diffusion
   \(\omega=-i\eta k^2/(\varepsilon+p)+\cdots\) and sound poles
   \[
     \omega=\pm c_sk-\frac{i}{2}
     \frac{\zeta+2\eta(d-1)/d}{\varepsilon+p}k^2+\cdots .
   \]
16. Hydrodynamic correlator poles match the Kubo coefficients only after the
   thermodynamic and hydrodynamic scaling limits are specified.
17. The microscopic QFT theorem boundary requires local equilibration,
   clustering, analyticity, and control of nonconserved modes and long-time
   tails.

## Calculation Checks

- `calculation-checks/hydrodynamic_modes_checks.py` verifies the shear and
  sound dispersion equations, the entropy-production positivity structure,
  the sourceful Euler thermodynamic-force reduction, the diffusion Einstein
  relation, the multi-charge susceptibility geometry, and the static limit of
  the diffusive density source-response kernel.

## Figures

- None in this chapter.

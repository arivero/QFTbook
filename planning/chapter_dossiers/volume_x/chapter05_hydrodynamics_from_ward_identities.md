# Volume X, Chapter 5 Dossier: Hydrodynamics from Ward Identities
Source-File: monograph/tex/volumes/volume_x/chapter05_hydrodynamics_from_ward_identities.tex

## Logical Role

- Role in the monograph: derive deterministic first-order hydrodynamics,
  entropy production, hydrodynamic pole structure, and the causal-evolution
  boundary from Ward identities, background-source response, and local
  thermodynamics after Kubo formulae have been defined.
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
- Complete retained slow-sector datum \(\mathcal E_{\rm slow}\): a
  basis-invariant spectral subspace of a regulated observable quotient
  \(\mathcal O_\lambda\), paired with a separate source space
  \(\mathcal J_\lambda\).  Contact terms are response-kernel scheme data, not
  quotient vectors.  Exact conserved-density directions are mandatory, but
  any Goldstone, critical, quasihydrodynamic, kinetic, elastic, orientational,
  or higher-form spectral direction or continuum window entering the declared
  hydrodynamic scaling window must also be retained.
- Paired slow/fast source subspaces are annihilators for the declared
  source-observable pairing:
  \(\mathcal E_{\rm slow}^\vee
  =\{j:\langle j,\mathcal E_{\rm fast}\rangle=0\}\) and
  \(\mathcal E_{\rm fast}^\vee
  =\{j:\langle j,\mathcal E_{\rm slow}\rangle=0\}\).  The direct source sum is
  automatic only for finite-dimensional perfect pairings; in Banach/Hilbert
  limits it is an explicit closed-complement/predual hypothesis.
- Thermodynamic susceptibility \(\chi^{\rm th}\) is defined as an equilibrium
  static-source derivative before it is identified with a retarded
  source-response limit.  For conserved densities the equality uses the
  zero-frequency-before-long-wavelength convention with contact terms fixed.
- Slow-sector completeness/complement-regularity controlled approximation:
  after projecting onto \(\mathcal E_{\rm slow}\) with the projector defined
  by the thermodynamic response/inverse-response pair
  \(\mathcal R:\mathcal J\to\mathcal O\),
  \(\mathcal A:\mathcal O\to\mathcal J\), or by an explicitly constructed
  effective generator \(\mathcal G\), the complement block \(A_{ff}^{-1}\)
  and the slow Schur complement for that same inverse-response pencil must
  remain uniformly regular in the hydrodynamic scaling window.
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
  the symmetric/Hermitian dissipative part of the conductivity matrix, with
  Hall-type antisymmetric response kept nondissipative.
- Single- and multi-charge diffusion equations, susceptibility geometry, and
  Einstein relation \(D=\Sigma\chi^{-1}\).
- Linearized neutral stress tensor, shear pole, sound poles, and attenuation
  \(\Gamma_s=(\zeta+2\eta(d-1)/d)/(\varepsilon+p)\).
- First-order shear diffusion as a parabolic equation with nonzero heat-kernel
  support outside the light cone when extrapolated beyond the scaling window.
- Boosted-frame high-\(k\) instability of the parabolic truncation as a
  frame/variable-choice warning.
- Linear MIS shear relaxation completion, telegrapher equation,
  hydrodynamic shear pole, transient nonhydrodynamic pole, and shear-sector
  stability/front-speed conditions.
- Retarded singularity taxonomy: exact retarded functions are holomorphic in
  the open upper half-plane; finite-volume spectral lines and
  thermodynamic-limit cuts may live on the real-axis boundary, while damped
  transient/resonance poles belong in the lower half-plane or on continued
  sheets.
- Diffusive density source-response kernel
  \(K^R_{nn}=\chi Dk^2/(Dk^2-i\omega)+\text{analytic}\), with the sign
  relation to the commutator-retarded convention stated explicitly and with
  \(\lim_{\mathbf k\to0}\lim_{\omega\to0}\) as the static susceptibility
  convention.
- Omitted-order-parameter memory-kernel negative control: integrating out a
  relaxational scalar gives
  \(-\lambda^2/(\Gamma_\phi+\kappa_\phi k^2-i\omega)\), which is analytic
  only when \(\Gamma_\phi\) remains microscopic.
- Hydrodynamic scaling-limit boundary as a microscopic QFT claim about
  complete slow-sector identification plus complement regularity.

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
| \(D_\eta\) | shear diffusion constant \(\eta/(\varepsilon+p)\) |
| \(\Pi\) | transient shear stress in the linear causal-completion example |
| \(\tau_\pi\) | shear-stress relaxation time in the MIS example |
| \(v_T\) | shear-sector front speed \((D_\eta/\tau_\pi)^{1/2}\) |
| \(\mathcal O_\lambda(\mathbf k)\) | regulated observable quotient after null vectors, Ward equivalences, and declared improvements |
| \(\mathcal J_\lambda(\mathbf k)\) | source space paired contragrediently with \(\mathcal O_\lambda\) |
| \(\mathcal R_\lambda(z,\mathbf k)\) | source-response map \(\mathcal J_\lambda\to\mathcal O_\lambda\) |
| \(\chi^{\rm th}_\lambda\) | thermodynamic static susceptibility \(\mathcal J_\lambda\to\mathcal O_\lambda\), defined by the equilibrium source derivative and identified with a retarded static limit only after declaring contact terms and order of limits |
| \(\mathsf G^{\rm KM}_\lambda\) | optional Kubo-Mori metric on observables, kept distinct from the source-response map until a source convention identifies the duals |
| \(\mathcal L_{\rm mic}\) | exact finite-regulator Hamiltonian Liouvillian, used for Kubo-Mori projection but not identified with dissipative hydrodynamic poles |
| \(\mathcal A_\lambda(z,\mathbf k)\) | thermodynamic inverse-response or memory pencil \(\mathcal O_\lambda\to\mathcal J_\lambda\) defining the slow window and Schur-complement test |
| \(\mathcal G_\lambda(\mathbf k)\) | optional effective dissipative generator constructed from \(\mathcal A_\lambda\) |
| \(P_{\rm slow,\lambda}\) | projector onto the retained slow observable subspace, defined from the declared pencil or effective generator |
| \(\mathcal E_{\rm slow}\) | retained slow spectral subspace in the declared scaling family |
| \(\mathcal E_{\rm slow}^\vee\) | annihilator paired slow source subspace \(\{j:\langle j,\mathcal E_{\rm fast}\rangle=0\}\), not an abstract observable dual |
| \(\mathcal E_{\rm fast}^\vee\) | annihilator paired fast source subspace \(\{j:\langle j,\mathcal E_{\rm slow}\rangle=0\}\) |
| \(A_{ff}^{-1}\) | complement inverse block appearing in the Schur complement after fast modes are integrated out |
| \(\Gamma_\phi\) | sample nonconserved order-parameter relaxation rate in the omitted-mode negative control |

## Claim Ledger

1. The first-order hydrodynamic datum separates exact microscopic QFT input
   (source functional and Ward identities), equilibrium thermodynamics, frame
   choice, constitutive maps, and entropy positivity from the later
   hydrodynamic scaling assertion.
2. Background-source variation defines \(T^{\mu\nu}\) and \(J_A^\mu\), and
   gauge/diffeomorphism invariance gives the source Ward identities.
3. A constitutive relation is an asymptotic statement on hydrodynamic
   scaling families, not a finite-volume identity.
4. The retained slow sector is a basis-invariant observable subspace paired
   with a source space, not a list of preferred operator names, source
   directions, or diagonal relaxation entries.  Operator bases transform by
   \(M\), sources contragrediently by \(M^{-\mathsf T}\), and the
   response and thermodynamic susceptibility maps transform as
   \(\mathcal R'=M\mathcal R M^{\mathsf T}\) and
   \(\chi'=M\chi M^{\mathsf T}\), while the inverse-response pencil
   transforms as \(\mathcal A'=M^{-\mathsf T}\mathcal A M^{-1}\).  Any
   Kubo-Mori metric on observables is separate bilinear metric data.  The
   paired source blocks in the Schur complement are annihilators under a
   perfect or declared topological source-observable pairing; a degenerate
   pairing does not induce the source direct sum.  The normal-fluid chapters use
   \(\mathcal E_{\rm slow}^{\rm normal}
   =\operatorname{span}\{T^{00},T^{0i},J_A^0\}\), and this is valid only when
   no additional spectral direction, Jordan block, or continuum window enters
   the hydrodynamic scaling window.
5. Hydrodynamic frames are coordinate choices; first-order redefinitions
   shift \(q^\mu\) and \(\nu_A^\mu\) by
   \(-(\varepsilon+p)\delta u^\mu\) and \(-n_A\delta u^\mu\).
6. The grand-canonical pressure gives \(n_A=\partial p/\partial\mu_A\),
   \(s=\partial p/\partial T\), and
   \(\varepsilon+p=Ts+\mu_A n_A\).
7. Projecting \(\partial_\mu T^{\mu\nu}_{(0)}=0\) along and orthogonal to
   \(u^\mu\) gives the ideal energy equation and Euler equation.
8. With external sources, the ideal Euler equation implies
   \(a^\mu+\Delta^{\mu\nu}\partial_\nu\log T
   =Tn_A V_A^\mu/(\varepsilon+p)\), so acceleration is not an independent
   first-order dissipative force.
9. Current conservation gives the ideal charge equation.
10. The Gibbs-Duhem identity and first law imply conservation of
   \(S^\mu_{(0)}=su^\mu\) on ideal solutions.
11. In Landau frame the first-order parity-even stress and current are
   \(-\eta\sigma^{\mu\nu}-\zeta\Delta^{\mu\nu}\vartheta\) and
   \(-T\Sigma_{AB}\Delta^{\mu\nu}\partial_\nu(\mu_B/T)\).
12. Divergence of the first-order entropy current gives
   \[
     \partial_\mu S^\mu=
     \eta\sigma^2/(2T)+\zeta\vartheta^2/T
     +T\Sigma_{AB}\nabla(\mu_A/T)\nabla(\mu_B/T)+O(\partial^3),
   \]
   so the transport matrix positivity conditions apply to the
   symmetric/Hermitian dissipative sector.  Antisymmetric Hall-type response
   gives no entropy production and is not constrained as a positive measure.
13. Charge diffusion at constant \(T\) gives
   \(\omega=-i(\Sigma/\chi)k^2+\cdots\).
14. Multi-charge diffusion has \(D=\Sigma\chi^{-1}\); if \(\chi\) is positive
    definite and \(\Sigma\) is symmetric positive semidefinite, \(D\) is
    similar to a symmetric positive semidefinite matrix and has nonnegative
    diffusion eigenvalues.
15. The density source-response matrix is
    \(K^R_{n_An_B}=k^2(Dk^2-i\omega)^{-1}_{AC}\Sigma_{CB}\) up to analytic
    contact terms.  Its thermodynamic static susceptibility is
    \(\chi_{AB}\) only in the static-source order
    \(\lim_{\mathbf k\to0}\lim_{\omega\to0}\); the opposite homogeneous
    dynamic order can remove the diffusive denominator and does not define the
    equilibrium susceptibility.
16. Linearized neutral hydrodynamics gives shear diffusion
   \(\omega=-i\eta k^2/(\varepsilon+p)+\cdots\) and sound poles
   \[
     \omega=\pm c_sk-\frac{i}{2}
     \frac{\zeta+2\eta(d-1)/d}{\varepsilon+p}k^2+\cdots .
   \]
17. The corresponding first-order shear PDE is parabolic; its heat kernel has
    instantaneous spatial support when treated as an exact initial-value
    equation.
18. Boosting the parabolic diffusion pole outside its hydrodynamic regime
    produces a high-\(k\) growing branch, so frame/variable choice and regime
    bounds are part of the causal-evolution problem.
19. A linear MIS shear relaxation sector produces
    \(\tau_\pi\omega^2+i\omega-D_\eta k^2=0\), with a hydrodynamic shear pole
    and a transient pole at \(-i/\tau_\pi\); shear-sector stability and
    subluminal front speed require \(w>0\), \(\eta\ge0\), \(\tau_\pi>0\), and
    \(D_\eta/\tau_\pi\le1\).
20. Retarded analyticity/positivity supplies exact QFT causality and Kubo
    positivity.  The exact pole-location statement is absence of
    singularities in the open upper half-plane; finite-volume spectral lines
    and thermodynamic-limit cuts can sit on the real-axis boundary, while
    lower-half-plane poles describe damped transients or continued-sheet
    resonances.  This does not by itself prove finite-truncation hyperbolicity
    or nonlinear well-posedness; those are formulation-dependent assumptions.
21. A nonconserved scalar with
    \((\Gamma_\phi+\kappa_\phi k^2-i\omega)\phi=\lambda X+h_\phi\) can be
    integrated out as a local analytic correction only when \(\Gamma_\phi\)
    remains outside the hydrodynamic scaling window.  If \(\Gamma_\phi\) scales
    to zero, the scalar belongs to \(\mathcal E_{\rm slow}\).  In a mixed
    multi-field problem the invariant retained object is the projector for the
    declared thermodynamic pencil \(\mathcal A\), or for an effective
    generator \(\mathcal G\) constructed from it, while complement regularity
    is tested through the Schur complement of the same pencil; in a kinetic
    continuum, a lower edge entering the hydrodynamic window is a slow
    spectral channel rather than a finite pole.  The exact finite
    Hamiltonian Liouvillian gives oscillatory lines and projection identities,
    not dissipative relaxation eigenvalues before the thermodynamic/scaling
    limit.
22. Hydrodynamic correlator poles match the Kubo coefficients only after the
   thermodynamic and hydrodynamic scaling limits are specified.
23. The microscopic QFT theorem boundary requires local equilibration,
   clustering, analyticity, proof of slow-sector completeness, complement
   regularity, and control of long-time tails.

## Audit Notes

- 2026-06-04 causality pass: added the first-order shear heat-kernel
  acausality derivation, boosted-frame parabolic instability diagnostic,
  linear MIS shear relaxation completion, explicit stability/front-speed
  ledger, and theorem/assumption boundary for retarded analyticity,
  hyperbolicity, and nonlinear well-posedness.
- 2026-06-04 issue #821 re-audit: corrected the retarded-analyticity
  boundary from "exact singularities lie in the lower half-plane" to
  holomorphy in the open upper half-plane, explicitly separating real-axis
  finite-volume lines, thermodynamic-limit cuts, and lower-half-plane
  transient/resonance poles.
- 2026-06-05 evidence re-audit for #725: repaired the companion check for the
  retarded singularity taxonomy.  The check now constructs a finite
  Gibbs/Lehmann retarded response from a three-level system and derives its
  real transition lines before testing upper-half-plane analyticity, instead
  of only sampling distances to preselected real points.  The negative control
  is an actual denominator-root list with a pole in the open upper half-plane.
- 2026-06-08 issue #884 pass: replaced the conserved-density-only foundation
  by a complete retained slow-sector criterion, scoped the chapter to the
  ordinary normal fluid, added a complement-regularity hypothesis, and inserted
  the omitted-order-parameter memory-kernel negative control.
- 2026-06-08 issue #940 pass: sharpened the slow-sector criterion from a
  named-operator/scalar-rate set to a basis-invariant spectral subspace, gave
  \(P_{\rm slow}\) a Riesz/window construction for the declared spectral
  object, formulated complement regularity through the Schur complement of the
  operator actually inverted, and added operator-mixing and continuum
  lower-edge negative controls.  The #944 pass refines the spaces and
  generator typing of this criterion.
- 2026-06-08 issue #944 pass: separated regulated observable quotients from
  paired source spaces, moved contact terms into response-kernel scheme data,
  placed hydrodynamic fields in \(T\mathcal M_{\rm eq}\) with the
  susceptibility/frame map to density fluctuations, and made the
  thermodynamic memory/inverse-response pencil or a constructed effective
  generator the object that defines the slow window.  The finite Hamiltonian
  Liouvillian is now explicitly only a microscopic projection tool unless an
  additional limit theorem identifies it with the dissipative spectrum.
- 2026-06-08 issue #947 pass: corrected the response arrows so that
  \(\mathcal R,\chi:\mathcal J\to\mathcal O\) and
  \(\mathcal A:\mathcal O\to\mathcal J\), separated the Kubo-Mori observable
  metric from the source-response susceptibility, and typed the Schur
  complement as
  \(\mathcal E_{\rm slow}\to\mathcal E_{\rm slow}^\vee\) rather than an
  observable-to-\(\mathcal J^*\) map.
- 2026-06-08 issue #960 pass: defined
  \(\mathcal E_{\rm slow}^\vee\) and
  \(\mathcal E_{\rm fast}^\vee\) as annihilator source subspaces under a
  perfect or declared topological source-observable pairing, rejected
  degenerate pairings as source-splitting data, and separated
  \(\chi^{\rm th}\) as an equilibrium source derivative from the retarded
  zero-frequency limit.  The static conserved-density convention is
  \(\lim_{\mathbf k\to0}\lim_{\omega\to0}\), not an untyped origin value.
- 2026-06-08 issue #942 synchronization: matched the entropy/Onsager
  discussion to Chapter 4's Hermitian dissipative conductivity projection,
  keeping antisymmetric Hall-type response outside the positive entropy
  production matrix.

## Calculation Checks

- `calculation-checks/hydrodynamic_modes_checks.py` verifies the shear and
  sound dispersion equations, the entropy-production positivity structure,
  the sourceful Euler thermodynamic-force reduction, the diffusion Einstein
  relation, the multi-charge susceptibility geometry, and the static limit of
  the diffusive density source-response kernel with its order-of-limits
  convention.  It also checks the
  first-order heat-kernel acausal-support diagnostic, boosted high-\(k\)
  instability negative control, the retarded singularity taxonomy through an
  explicit finite Gibbs/Lehmann construction, and the MIS shear relaxation
  hydrodynamic/transient poles with a subluminal-front-speed condition.  It
  also checks the slow-sector completeness boundary by verifying that an
  omitted relaxational order parameter with a vanishing gap produces a
  nonlocal memory kernel rather than an analytic normal-fluid coefficient.
  The issue #940/#960 extensions check that diagonal entries of a non-normal
  relaxation matrix are basis dependent while the slow Riesz projector
  transforms covariantly, that sources must transform contragrediently to
  observable basis changes, that annihilator source subspaces transform
  covariantly and recover the same finite Schur blocks, that a degenerate
  source-observable pairing is rejected, that the thermodynamic susceptibility
  is an equilibrium source derivative rather than the homogeneous dynamic
  conserved-density limit, and that the response/inverse-response pair obeys the
  covariance laws
  \(\mathcal R'=M\mathcal R M^{\mathsf T}\) and
  \(\mathcal A'=M^{-\mathsf T}\mathcal A M^{-1}\), that the Schur complement
  maps retained observables to retained paired sources while
  \(\mathcal A:\mathcal O\to\mathcal J^*\) is rejected, that a finite
  Hamiltonian Liouvillian has oscillatory spectral lines rather than
  dissipative relaxation poles, and that a continuum of relaxation rates
  whose lower edge scales to zero produces branch-cut memory rather than a
  finite-pole correction.

## Figures

- None in this chapter.

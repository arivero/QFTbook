# Chapter 12: QCD Phase Structure, Plasma, and Dense Matter

## Source Position

Volume X now includes a dedicated chapter for QCD phases rather than treating
them as a side remark inside screening.  The chapter follows KMS, Euclidean
thermal path integrals, Schwinger--Keldysh response, hydrodynamics, and
thermal gauge screening, and supplies the phase-structure bridge requested in
GitHub issue #628.

## Notation Inventory

- `N_c`, `N_f`: number of colors and Dirac fundamental quark flavors.
- `beta=1/T`, `mu_B`, `mu_q=mu_B/N_c`: inverse temperature, baryon chemical
  potential, and quark chemical potential.
- `Z_{a,V}`, `p(T,mu_B,m)`: finite-regulator thermal partition function and
  thermodynamic pressure.
- `Lambda=(N_tau,N_s^3,a)`, `zeta=e^{a mu_q}`: finite thermal lattice and
  quark fugacity.
- `mathcal Z_Lambda`: finite-regulator Lee--Yang zero locus.
- `h`, `X_Lambda`, `overline O_Lambda`: source, integrated observable, and
  intensive observable entering susceptibility definitions.
- `P_R(x)`, `ell(T)`: normalized Polyakov loop and center order parameter.
- `nu_Lambda`, `S_eff,Lambda`, `u_square`, `kappa`: exact finite-regulator
  Polyakov-loop effective measure, its density action when it exists,
  fundamental plaquette character coefficient, and Wilson hopping parameter.
- `P=diag(e^{i theta_j})`: constant Polyakov holonomy used in the one-loop
  high-temperature potential.
- `f_g(P)`, `f_q(P)`: gluon and quark one-loop holonomy free-energy
  densities.
- `Sigma(T)`, `rho(lambda)`: chiral condensate and thermodynamic Dirac
  eigenvalue density.
- `Sigma_m(T)`, `tau^a`, `P^a`, `A_mu^a`, `chi_pi^{ab}`: positive
  per-flavor massive chiral condensate, trace-delta flavor generators,
  nonsinglet pseudoscalar density, nonsinglet axial current, and
  pseudoscalar susceptibility.
- `U`, `F`, `B`, `M_pi`: chiral effective field, half-trace-normalized pion
  decay constant, leading mass-source constant, and pion mass in the
  low-temperature chiral EFT.
- `p_SB`, `Delta=epsilon-3p`: Stefan--Boltzmann pressure and trace anomaly.
- `s`, `n_B`, `epsilon`, `c_s^2`: entropy density, baryon density, energy
  density, and adiabatic sound speed extracted from pressure derivatives.
- `g_3^2=g^2T`, `m_D`: static magnetic coupling and Debye mass.
- `C_A`, `T_R`, `I_B`, `I_F`: adjoint quadratic index, representation
  trace index, and the Bose/Fermi thermal susceptibility integrals entering
  the static HTL Debye mass.
- `v^\mu=(1,mathbf v)`, `W_a(x,mathbf v)`, `mathcal K_R`: hard-particle
  velocity vector, adjoint HTL auxiliary field, and retarded induced-current
  kernel.
- `theta_q`, `theta_B`: imaginary quark and baryon chemical-potential
  angles, related by `theta_B=N_c theta_q`.
- `x=mu_B/T`, `kappa_n^B`, `chi_n^B`, `R(T)`: dimensionless baryon source,
  baryon-number cumulants, susceptibilities, and Cauchy--Hadamard radius.
- `Lambda_H`, `psi_v`, `ell_parallel`, `ell_perp`: high-density effective
  theory shell scale, patch quark field, and residual momentum components.
- `N_ch(0)`, `Delta`: channel density of states at the Fermi surface and the
  superconducting gap entering the BCS logarithm.
- `T_1 dot T_2`, `C_2(R)`: one-gluon exchange color operator and quadratic
  Casimir used to identify the attractive dense-quark pairing channel.
- `D_T(omega,k_perp)`, `lambda_mag`, `Lambda_M`: HDL transverse magnetic
  propagator, leading-log magnetic gap coefficient, and matching scale for
  the dense color-superconducting gap equation.
- `Delta_L`, `Delta_R`: CFL pairing amplitudes.
- `varphi_L`, `varphi_R`, `B_L`, `B_R`, `Sigma`: gauge-covariant
  antisymmetric CFL diquarks and the gauge-invariant baryon-superfluid and
  chiral composites used to diagnose the physical CFL symmetry realization.

## Claim Ledger

- Defines a QCD phase datum requiring pressure, exact symmetries, order
  parameters, limit prescriptions, and status labels.
- Adds a finite-lattice thermal gauge datum and proves finite-regulator
  analyticity: finite lattice partition functions are entire in finite
  couplings and masses and Laurent-polynomial in fugacity.
- Defines thermodynamic phase transitions through limiting pressure
  nonanalyticity or nonunique source-selected Gibbs/KMS states, and proves
  that zero-free complex neighborhoods with uniform analytic convergence
  exclude pressure singularities.
- Proves the source-curvature susceptibility identity, making divergent
  susceptibilities statements about integrated connected correlators.
- Defines center deconfinement in pure Yang--Mills by the Polyakov-loop order
  parameter with the correct source/infinite-volume limiting order.
- Proves that nonzero-\(N\)-ality Polyakov loops vanish at finite volume and
  zero center-breaking source.
- Separates center deconfinement from the zero-temperature Wilson-loop area
  law and from the crossover use of Polyakov loops with dynamical fundamental
  quarks.
- Defines the exact finite-regulator Polyakov-loop effective measure as the
  pushforward of the lattice path-integral measure, proves the character
  expansion and pure-gauge center selection rule, derives the leading
  strong-coupling nearest-neighbor tube interaction, and derives the leading
  heavy-quark center-breaking source term.
- Derives the one-loop Polyakov-holonomy potential from thermal oscillator
  sums, including the adjoint trace formula
  `tr_adj(P^n)=|tr_F P^n|^2-1` and the antiperiodic fundamental-quark term.
- Proves that the pure-glue one-loop holonomy potential is minimized at
  center holonomies, computes the uniform center-symmetric holonomy cost, and
  records fundamental quarks as an explicit center source.
- Defines the chiral condensate as a mass-source derivative and proves the
  Banks--Casher relation under an explicit spectral-density hypothesis.
- Fixes the chiral condensate convention as the positive per-flavor
  source response, with the flavor-summed scalar expectation equal to
  `-N_f Sigma_m`, and distinguishes the spatial volume from the Euclidean
  thermal four-volume in the Banks--Casher normalization.
- Proves the integrated nonsinglet axial Ward identity
  `2m chi_pi^{ab}=-<bar q {tau^a,tau^b} q>` in trace-delta flavor
  normalization and derives the flavor-symmetric consequence
  `m chi_pi^{ab}=delta^{ab} Sigma_m`.
- Derives the finite-temperature GMOR relation as a pole-saturation
  consequence with the normalization conversion between trace-delta and
  half-trace flavor generators stated explicitly.
- Defines the leading low-temperature chiral effective datum, proves
  `Sigma=F^2 B` and `M_pi^2=2Bm`, and derives the one-loop pion-gas
  correction
  `Sigma(T)/Sigma(0)=1-(N_f^2-1)T^2/(12N_f F^2)+O(T^4/F^4)` with its
  domain of validity stated.
- Derives the massless free QCD pressure at zero and nonzero baryon chemical
  potential.
- Derives the thermodynamic derivative identities used to turn the QCD
  pressure into entropy density, baryon density, energy density, interaction
  measure, fixed-`mu_B/T` trace-anomaly diagnostic, and the `mu_B=0`
  sound-speed formula.
- Records the HTL domain as a controlled approximation and proves the
  magnetic \(g^6T^4\) Linde scale by dimensional analysis of the static
  magnetic theory.
- Derives the static HTL color susceptibility and Debye mass in the
  monograph trace convention from hard-particle Bose/Fermi thermal integrals,
  including the \(SU(N_c)\) specialization
  `m_D^2=g^2T^2(2N_c/3+N_f/3)`.
- Defines the retarded HTL induced-current kernel in the mostly-plus
  convention, derives it from the gauge-covariant auxiliary kinetic equation
  `(v.D)W=v^i F_{i0}`, proves transversality, and evaluates the longitudinal
  angular integral with its Landau cut.
- Defines transport coefficients through Kubo spectral limits rather than
  phenomenological language.
- Proves the origin of the finite-density sign problem from loss of
  \(\gamma_5\)-Hermiticity at real chemical potential.
- Defines imaginary chemical potential as a thermal boundary-condition
  twist, proves finite-regulator Roberge--Weiss periodicity
  `Z(theta_q+2*pi*k/N_c)=Z(theta_q)`, proves positivity for vectorlike
  pairs, and separates imaginary-chemical-potential nonanalyticities from
  real-density critical endpoints.
- Defines baryon-number susceptibilities as finite-regulator source
  derivatives at \(x=\mu_B/T=0\), proves the cumulant identities, and
  separates radius-of-convergence diagnostics from claims about a real QCD
  critical endpoint.
- States the high-density effective-theory scale separation, defines patch
  fields near the quark Fermi surface, derives the Fermi-surface measure and
  density of states, derives the tree-level patch action including the
  transverse curvature term, and computes the zero-temperature dense-quark
  HDL Debye coefficient in the monograph trace convention.
- Derives the BCS logarithm from the Fermi-surface shell as a controlled
  instability of a specified attractive channel, separating the universal
  logarithmic mechanism from the QCD-specific gap prefactor.
- Derives the one-gluon exchange color factors for
  `square tensor square = Sym^2 square plus wedge^2 square` in the
  trace-delta convention, identifies the antisymmetric channel as attractive,
  derives the HDL magnetic leading-log gap equation and solves its reduced
  logarithmic integral equation to obtain the trace-delta exponent
  `exp[-3*pi^2/(2g)]` up to leading-log accuracy,
  proves the exchange symmetry that pairs color antisymmetry with flavor
  antisymmetry in spin-zero \(s\)-wave pairing, defines the CFL condensate
  datum, constructs gauge-invariant local and Wilson-line CFL diagnostics,
  proves the gauge-averaging statement excluding a gauge-covariant diquark
  one-point function as a physical local order parameter, and proves the
  physical Goldstone count.
- Separates Wilson-loop, Polyakov-loop, 't Hooft-loop, center-vortex, and
  dual-superconductor criteria for confinement.

## Figure Requirements

- Future figures should show the \((T,\mu_B)\) plane with only status-labeled
  regions, and a separate operator diagram distinguishing Wilson loops,
  Polyakov loops, and disorder lines.  No figure is included in this pass.

## Calculation Checks

- `calculation-checks/qcd_phase_checks.py`: exact finite checks for the
  Stefan--Boltzmann coefficients, baryon-chemical-potential coefficients,
  Banks--Casher kernel normalization, Linde magnetic-scale power counting,
  fugacity Laurent-polynomial shift, source-curvature susceptibility
  identity, one-loop Polyakov-holonomy potential coefficients,
  chiral Ward-identity and GMOR normalization factors, low-temperature
  chiral effective theory coefficients, static HTL Debye-mass normalization,
  retarded HTL angular-kernel transversality bookkeeping, thermodynamic
  derivative identities, Roberge--Weiss angle-periodicity bookkeeping,
  Polyakov-loop effective-measure center-charge bookkeeping,
  high-density Fermi-surface and dense-HDL coefficient bookkeeping,
  dense one-gluon-exchange color-factor bookkeeping,
  magnetic leading-log gap coefficient bookkeeping,
  baryon-number cumulants and radius estimators, CFL gauge-invariant
  composite charge bookkeeping, and CFL Goldstone count.

## Open Issues

- The chapter is a first dedicated Vol X response to #628.  It does not close
  the issue because a full unprecedented-depth treatment still needs
  dedicated derivations of Polyakov-loop effective potentials, stronger
  lattice-continuum status ledgers, and substantially more quantitative QGP
  and dense-QCD examples.
- 2026-05-27 finite-regulator pass: added the analyticity/Lee--Yang/source
  susceptibility layer so that the chapter defines phase transitions through
  limiting analytic structure and connected correlators before discussing
  QCD-specific order parameters.
- 2026-05-27 holonomy pass: added a controlled one-loop high-temperature
  Polyakov-holonomy derivation, center-minimum proof, center-symmetric
  holonomy energy cost, and fundamental-quark center-source term.
- 2026-05-27 Polyakov-effective-measure pass: added the exact finite-lattice
  Polyakov-loop marginal measure, its character expansion and center
  selection rule, the leading strong-coupling tube interaction, and the
  leading heavy-quark hopping source.
- 2026-05-27 baryon-susceptibility pass: added finite-regulator cumulant
  definitions, explicit first/second/fourth cumulant formulas, the
  Cauchy--Hadamard diagnostic, and ratio-estimator status hypotheses.
- 2026-05-27 chiral-Ward pass: fixed the per-flavor condensate sign and
  Euclidean-volume normalization, added the integrated nonsinglet axial Ward
  identity, and derived the finite-temperature GMOR statement only as a
  stated pole-saturation consequence.
- 2026-05-27 low-temperature chiral EFT pass: added the leading chiral
  effective datum, tree-level source normalization, and one-loop pion-gas
  correction to the condensate as a controlled asymptotic statement rather
  than a proof of chiral restoration.
- 2026-05-27 static HTL pass: added the hard-particle color-susceptibility
  derivation of the Debye mass in trace-delta convention and paired it with
  exact arithmetic checks for the Bose/Fermi susceptibility integrals and
  \(SU(3)\), \(N_f=3\) coefficient.
- 2026-05-27 retarded HTL pass: added the gauge-covariant auxiliary-field
  derivation of the retarded angular kernel, the component transversality
  proof in mostly-plus convention, the longitudinal logarithm, and the
  Landau-cut interpretation.
- 2026-05-27 QGP thermodynamic-observable pass: added pressure-derivative
  identities for energy density, trace anomaly, fixed-`mu_B/T` reduced
  pressure, and `mu_B=0` sound speed, with the conformal Stefan--Boltzmann
  benchmark checked exactly.
- 2026-05-27 Roberge--Weiss pass: added the finite-regulator imaginary
  chemical-potential theorem, positivity statement for vectorlike pairs,
  Roberge--Weiss transition status remark, and exact angle-periodicity
  bookkeeping checks.
- 2026-05-27 high-density EFT pass: added the patch decomposition, density
  of states, tree-level HDET action, zero-temperature HDL Debye coefficient,
  and BCS logarithm derivation before the CFL order-parameter discussion.
- 2026-05-27 CFL color-factor pass: added the trace-delta one-gluon exchange
  color-factor derivation, the spin-zero exchange-symmetry derivation, and a
  proposition-level physical Goldstone count.
- 2026-05-27 magnetic-gap pass: added the HDL transverse magnetic
  leading-log kernel, its trace-delta coefficient, and the differential
  equation proof of the leading color-superconducting gap exponent.
- 2026-05-27 CFL gauge-invariant diagnostics pass: added local
  gauge-invariant composites for baryon-superfluid and chiral order, the
  Wilson-line diquark correlator, and the finite-volume gauge-averaging proof
  that the diquark one-point function is not itself a physical local order
  parameter.

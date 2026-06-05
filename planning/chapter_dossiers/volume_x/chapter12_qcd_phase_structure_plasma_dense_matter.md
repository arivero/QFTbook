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
- `C_F`, `lambda_NFL`, `Lambda_NFL`, `Z(p0)`: trace-delta fundamental
  Casimir, leading cold dense non-Fermi-liquid self-energy coefficient,
  finite matching scale, and the logarithmic patch residue in the unpaired
  high-density regime.
- `Pi_phys`, `G_Lambda(f)`, `Q_A`, `mu_A`: finite-regulator physical-state
  projector, Gauss-law generator, gauge-invariant global charges, and their
  thermodynamic sources.
- `Q_em`, `mu_Q`, `A_0^a`: electromagnetic flavor generator, its global
  neutrality source, and temporal color-gauge background coordinates used in
  gauge-fixed neutrality equations.
- `A_mu`, `a_mu^Q`, `q_Q`, `tilde A_mu`, `tilde G_mu`: ordinary photon,
  color gauge field component parallel to the CFL electromagnetic Cartan
  generator, its trace-delta norm, and the massless/massive rotated
  photon-gluon combinations in ideal CFL.
- `xi_a(p)`, `delta_eff`, `p_F,a`, `delta_C`: mass-stressed residual energy,
  pairwise effective half-mismatch, shifted Fermi momentum, and the
  two-species Clogston scale.
- `T_1 dot T_2`, `C_2(R)`: one-gluon exchange color operator and quadratic
  Casimir used to identify the attractive dense-quark pairing channel.
- `D_T(omega,k_perp)`, `lambda_mag`, `Lambda_M`: HDL transverse magnetic
  propagator, leading-log magnetic gap coefficient, and matching scale for
  the dense color-superconducting gap equation.
- `Delta_L`, `Delta_R`: CFL pairing amplitudes.
- `varphi_L`, `varphi_R`, `B_L`, `B_R`, `Sigma`: gauge-covariant
  antisymmetric CFL diquarks and the gauge-invariant baryon-superfluid and
  chiral composites used to diagnose the physical CFL symmetry realization.
- `C_E`, `C_M`, `F_H`, `v_H`, `m_E`, `m_M`: gauge-invariant static
  screening correlators and the low-energy CFL Higgs-screening coefficients.
- `F_pi`, `F_B`, `v_pi`, `v_B`, `phi_B`, `vartheta_B`: CFL chiral and
  baryon-superfluid collective-mode coefficients, local baryon coset angle,
  and the equivalent `2 phi_B` charge-two order-coordinate phase.
- `G_QCD^0`, `Z_3^V`, `n_ijk`, `E_cB`: faithful connected QCD
  flavor-baryon symmetry, its diagonal flavor-center quotient, the quotient
  background center cocycle, and the color-baryon `U(3)` lift used to
  globalize quark baryon charge `1/3`.
- `A_L`, `A_R`, `B`, `F_L`, `F_R`, `F_B`, `D_B phi_B`: lifted local chiral
  flavor and baryon background fields used in the de Rham CFL anomaly
  calculation, their curvatures, and the baryon-Goldstone covariant one-form.
- `mathcal T_QCD`, `chi_ab`, `Sigma_ab`, `J_inc^i`, `D_eta`, `D_B`,
  `Gamma_s`: QCD hydrodynamic transport datum, conserved-charge
  susceptibility and conductivity matrices, momentum-orthogonal baryon
  current, shear diffusion constant, projected baryon diffusion eigenvalue,
  and sound attenuation coefficient used in the microscopic response-window
  comparison.

## Claim Ledger

- Defines a QCD phase datum requiring pressure, exact symmetries, order
  parameters, limit prescriptions, and status labels.
- Adds an explicit operational spine tying the chapter's finite-regulator,
  order-parameter, response-function, baryon-density, high-density, and CFL
  subsections back to that phase datum rather than leaving them as parallel
  technical modules.
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
- 2026-05-30 proof-substance follow-up: expanded the integrated nonsinglet
  axial Ward proof to display the local distributional Ward identity on the
  thermal torus, the periodic delta contact term, the Euclidean
  `P^a=bar q i gamma_5 tau^a q` sign convention, the vanishing of the
  nonsinglet one-point function by vector flavor symmetry, and the exact
  flavor-symmetric singlet projection.  `qcd_phase_checks.py` now verifies the
  contact-term sign and Ward-normalization bookkeeping in addition to the
  GMOR normalization.
- Records the finite-temperature GMOR relation as a conditional
  pole-saturation consequence of the integrated axial Ward identity, with the
  normalization conversion between trace-delta and half-trace flavor
  generators stated explicitly.
- Defines the leading low-temperature chiral effective datum, proves
  `Sigma=F^2 B` and `M_pi^2=2Bm`, and derives the one-loop pion-gas
  correction
  `Sigma(T)/Sigma(0)=1-(N_f^2-1)T^2/(12N_f F^2)+O(T^4/F^4)` with its
  domain of validity stated.
- Derives the massless free QCD pressure at zero and nonzero baryon chemical
  potential as a worked free-gas calculation rather than theorem-family
  content.
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
  angular integral with its Landau cut as worked prose rather than
  theorem-family content.
- Defines transport coefficients through Kubo spectral limits rather than
  phenomenological language, records the additional microscopic
  response-window estimate and coupled charge-diffusion matrix needed before
  those coefficients imply hydrodynamic poles of QCD correlators, and derives
  the finite-density momentum projection
  `J_inc^i=J_B^i-(n_B/w)T^{0i}` needed to remove the convective Drude sector
  before identifying the intrinsic baryon-diffusion conductivity.
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
- Derives the leading cold dense non-Fermi-liquid quark self-energy from
  Landau-damped magnetic exchange in HDET, including the trace-delta
  coefficient `lambda_NFL=g^2 C_F/(12 pi^2)`, the `SU(3)` specialization
  `2g^2/(9 pi^2)`, the collinear `1/3` logarithm, and the logarithmic
  vanishing of the perturbative patch residue.
- Derives the BCS logarithm from the Fermi-surface shell as a controlled
  instability of a specified attractive channel, separating the universal
  logarithmic mechanism from the QCD-specific gap prefactor.
- Defines finite-regulator global-charge ensembles with the physical
  gauge-invariant projector, proves that Gauss-law generators annihilate the
  physical projector and therefore cannot be assigned independent physical
  chemical potentials, formulates color neutrality as temporal-gauge
  stationarity in gauge-fixed saddle calculations, and proves ideal CFL
  electric neutrality at zero electric source from traceless
  \(Q_{\rm em}\) and diagonal \(SU(3)_V\) invariance.
- Derives mass and chemical-potential shifts of dense-quark Fermi surfaces,
  including \(p_F=\mu-m^2/(2\mu)+O(m^4/\mu^3)\), the pairwise effective
  half-mismatch, the strange-light stress scales \(m_s^2/(2\mu_q)\) and
  \(m_s^2/(4\mu_q)\), and the Clogston scale
  \(\delta_C=\Delta_0/\sqrt2\) in a controlled two-species constant-density
  comparison.
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
  one-point function as a physical local order parameter, defines
  gauge-invariant static electric and magnetic screening exponents, derives
  the CFL Higgs screening mass matrix from the trace-delta effective action,
  derives the rotated electromagnetic photon-gluon mass matrix and its
  exact null eigenvector, proves the physical Goldstone count, derives the
  ideal CFL chiral-octet and baryon-phonon dispersions from the leading
  low-energy action, and identifies the rotated unbroken electromagnetic
  \(U(1)\) in the same transformation convention as the CFL orientation
  field.
- Derives the faithful connected global symmetry used in the CFL anomaly
  discussion as
  `(SU(3)_L x SU(3)_R x U(1)_B)/Z_3^V`, explains why quark baryon charge
  `1/3` is globally defined through color-baryon quotient/lift data rather
  than an independent cube root of an ordinary baryon line, and records that
  the section works on spin four-manifolds without imposing an additional
  spin-charge quotient.
- Scopes the CFL anomaly calculation to a lifted local/de Rham background
  chart with vanishing center cocycles: computes the UV six-form polynomial in
  half-trace flavor normalization, derives the pure chiral coefficient \(N_c\),
  derives the mixed baryon-flavor coefficient \(N_cq_B/2=1/2\), and matches
  these local coefficients in CFL by the level-\(N_c\) gauged WZW functional
  of \(\Sigma\) plus the baryon Goldstone inflow representative
  `-(D_B phi_B/2pi) wedge (tr F_L^2-tr F_R^2)/(2(2pi)^2)`.
- States the residual `Z_2` stabilizer of the source-selected charge-two CFL
  baryon order parameter and separates this compact Goldstone normalization
  from the stronger, not-claimed global torsion/large-gauge anomaly matching
  problem on arbitrary quotient bundles.
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
  dense non-Fermi-liquid self-energy coefficient bookkeeping,
  dense one-gluon-exchange color-factor bookkeeping,
  magnetic leading-log gap coefficient bookkeeping,
  baryon-number cumulants and radius estimators, dense neutrality
  bookkeeping, CFL gauge-invariant composite charge bookkeeping, CFL
  faithful-global-symmetry center quotients, color-baryon lift obstruction
  cancellation, charge-two order-parameter stabilizer bookkeeping, CFL rotated
  electromagnetic mass-matrix bookkeeping, CFL screening-sector and
  collective-mode count bookkeeping, dense
  Fermi-surface stress bookkeeping, lifted local CFL anomaly-matching
  coefficient bookkeeping, QCD hydrodynamic response-window,
  coupled-diffusion, and momentum-projected baryon-current bookkeeping, and
  CFL Goldstone count.

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
- 2026-06-03 issue #630 QCD hydrodynamics bridge: added a controlled
  response-window datum for deriving hydrodynamic shear, diffusion, and sound
  poles from microscopic QCD retarded kernels.  The chapter now separates
  Kubo coefficient definitions from the additional residual estimate needed
  to exclude extra nonconserved low-frequency singularities, treats charge
  diffusion as the eigenvalue problem for `Sigma chi^{-1}` away from a
  decoupled baryon channel, and aligns the displayed shear Kubo example with
  the chapter's
  \(\rho=-2\operatorname{Im}G^R\) convention by using \(1/(2\omega)\).
- 2026-05-27 Roberge--Weiss pass: added the finite-regulator imaginary
  chemical-potential theorem, positivity statement for vectorlike pairs,
  Roberge--Weiss transition status remark, and exact angle-periodicity
  bookkeeping checks.
- 2026-05-27 high-density EFT pass: added the patch decomposition, density
  of states, tree-level HDET action, zero-temperature HDL Debye coefficient,
  and BCS logarithm derivation before the CFL order-parameter discussion.
- 2026-05-27 non-Fermi-liquid pass: added the controlled HDL unpaired dense
  regime, the derivation of the \(ip_0\log(\Lambda_{\rm NFL}/|p_0|)\)
  self-energy coefficient, and the logarithmic patch-residue consequence.
- 2026-05-27 neutrality pass: added the finite-regulator distinction between
  global charge sources and gauge constraints, the Gauss-law projector proof
  of zero color charge, the gauge-fixed temporal-background stationarity
  interpretation of color neutrality, and the ideal CFL electric-neutrality
  derivation.
- 2026-05-27 dense-stress pass: added the mass/chemical-potential Fermi
  surface mismatch expansion, the strange-light stress scale, and the
  controlled two-species Clogston comparison.
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
- 2026-05-27 CFL screening and collective-mode pass: added gauge-invariant
  static screening correlators, the CFL Higgs screening effective action and
  mass-matrix derivation, and the leading chiral-octet/baryon-phonon
  collective-mode action and dispersion derivation.
- 2026-06-04 CFL rotated-electromagnetic response pass: added the exact
  photon-gluon mass matrix in ideal CFL, identified the massless rotated
  photon and screened orthogonal combination, and paired the statement with
  exact trace-delta charge and determinant checks.
- 2026-06-04 chapter-spine pass: added an operational spine after the QCD
  phase specification and a closing bridge in the confinement-comparison
  section, so the chapter explicitly relates phase labels to pressure,
  symmetry, source, response, and limiting data.
- 2026-05-27 CFL anomaly-matching pass: added the local UV anomaly polynomial
  for chiral flavor plus baryon backgrounds, the level-\(N_c\) WZW matching
  statement for the CFL chiral field, and the baryon-Goldstone mixed-anomaly
  inflow representative.
- 2026-06-05 issue #791 pass: replaced the direct-product background wording
  by the faithful connected symmetry and quotient/lift background data,
  corrected the CFL baryon-phase compactness to remember the charge-two order
  stabilizer, and scoped the anomaly proposition to the lifted local/de Rham
  polynomial rather than a full torsion global anomaly statement.

## Anti-Wrapper Audit

- 2026-05-29: demoted the BCS logarithm from proposition/proof to a worked
  paragraph.  The calculation remains because it fixes the shell density of
  states and the exponential scale, but it is the elementary mean-field
  Fermi-surface integral once the model gap equation has been assumed.
- 2026-05-29 ninth pass: demoted the dense-matter mass/chemical-potential
  mismatch expansion from proposition form to a worked Fermi-surface
  expansion.  The formulas remain numbered because the strange-light stress
  scale is used in the subsequent controlled BCS comparison.

# Volume II, Chapter 19 Dossier: QCD Renormalization, Asymptotic Freedom, And DIS

## Source Position

- Primary local source: second-sequence handwritten material, pages 182--210.
- Immediate predecessor: gauge fixing, ghosts, and BRST cohomology.
- Immediate successor in the source order: anomalies and chiral symmetry.
- Immediate successor in the compiled Volume IV sequence: jets,
  infrared-safe observables, and hadronization.
- Role in the monograph: derive the one-loop QCD beta function using the
  background-field 1PI effective action, then use asymptotic freedom to set up
  the short-distance analysis of deep inelastic scattering.

## Source And Reference Controls

- `SRC-QFT-PDF`: `references/253b lecture notes 2023.pdf`, pages 182--210;
  pages 182--201 were rendered to `/private/tmp/qft253b_qcd_beta_pages-*.png`
  for the beta-function repair pass.
- `SRC-BEN-COMPARISON`: `references/253b transcribed lecture notes.tex`,
  section "Yang-Mills Feynman rules and the one-loop QCD beta function", used
  only as a comparison layer.
- `SRC-EXTERNAL`: standard background-field and dimensional-regularization
  checks are allowed as guardrails.  The heat-kernel identity now used to
  compute determinant coefficients is derived in the chapter from the
  proper-time representation and flat-space coefficient, rather than imported
  as an external table.
- `SRC-EXTERNAL-ENERGY-CORRELATORS`: Basham--Brown--Ellis--Love for the
  original energy-energy correlator in \(e^+e^-\) annihilation,
  Larkoski--Salam--Thaler for jet energy correlation functions, and
  Komiske--Metodiev--Thaler for energy-flow polynomials.  These references
  control terminology and examples; the chapter gives its own detector
  definition from the stress tensor and its own soft/collinear continuity
  estimate.
- `SRC-CHECK-EEC-SUDAKOV`:
  `calculation-checks/energy_correlator_sudakov_checks.py` verifies the
  rational logarithmic integral in the back-to-back EEC Sudakov factor and
  the trace-delta/half-trace conversion of the one-loop cusp coefficient.
- `SRC-CHECK-QCD-CUSP-LARGE-SPIN`:
  `calculation-checks/qcd_cusp_large_spin_checks.py` verifies the Euclidean
  cusped-Wilson-line angular integral, smooth-line subtraction, Lorentzian
  lightlike limit, \(D_0\) Mellin harmonic-number identity, large-spin sign,
  and trace-normalization invariance of \(g^2C_R\).

## Construction Task

The chapter must define and derive:

- QCD fields \(q^i_{I\alpha}\), color/flavor/spinor indices, and the
  \(SU(N_c)\) group constants \(C_A,T_R,C_R,T_F,C_F\) in the
  monograph/stringbook trace normalization
  \(\operatorname{tr}_{\square}(t^a t^b)=\delta^{ab}\), so
  \(C_A=2N_c\), \(T_F=1\), and \(C_F=(N_c^2-1)/N_c\);
- the renormalized coupling and beta function;
- the ordinary Lorenz-gauge Faddeev--Popov operator, ghost action, ghost
  propagator, ghost-loop sign, ghost-gluon vertex, absence of a local
  \(\bar c c A A\) vertex in Lorenz gauge, covariant-gauge gluon propagator,
  and cubic/quartic gluon self-interaction terms in the
  \(-F^2/(4g^2)\) normalization;
- the background split \(A_\mu=\widetilde A_\mu+a_\mu\);
- the background covariant derivative and background curvature;
- the background-field gauge condition \(\widetilde D^\mu a_\mu=0\);
- the background gauge transformation under which \(\widetilde A_\mu\)
  transforms as a connection and the quantum variables transform
  homogeneously;
- the gauge-invariant dimension-four term in \(\Gamma[\widetilde A]\);
- the one-loop quadratic operators \(D_A,D_\psi,D_{\rm gh}\) and determinant
  ratio;
- the constant-background extraction of the logarithmic coefficient, including
  the distinction between \(\operatorname{Tr}\) and \(\operatorname{tr}\);
- the rotational average for four loop momenta in \(D=4-\epsilon\);
- the basic logarithmic integral with IR cutoff \(|k|>\mu\);
- the flat-space heat-kernel coefficient for Laplace-type operators, the
  adjoint trace sign, and the quark, ghost, and vector determinant
  coefficients;
- the coefficient
  \(b=\frac{11}{12}C_A-\frac{N_f}{3}T_R\);
- the conversion from bare-coupling independence to
  \(\beta(g)=-g^3(11C_A/3-4T_RN_f/3)/(16\pi^2)+O(g^5)\), and hence
  \(\beta(g)=-(11N_c-2N_f)g^3/(24\pi^2)+O(g^5)\) for fundamental
  quarks in this trace normalization;
- dimensional transmutation and the perturbative domain of the one-loop
  running coupling;
- the explicit status of the four-dimensional pure Yang--Mills continuum
  existence and positive mass-gap problem as an open Clay Millennium problem,
  with spectral/confinement uses marked as nonperturbative inputs;
- the two-loop Banks--Zaks alternative as a perturbative infrared fixed-point
  diagnostic, with \(a=g^2/(16\pi^2)\),
  \(\beta_a=-2B_0a^2-2B_1a^3+O(a^4)\), the universal two-loop coefficient
  \(B_1=\frac{34}{3}C_A^2-(\frac{20}{3}C_AT_R+4C_RT_R)N_f\), the analytic
  coupling-redefinition check preserving \(B_0\) and \(B_1\), and the
  controlled domain stated;
- for fundamental \(SU(N_c)\) quarks in the monograph trace convention, the
  formulas
  \(B_0=\frac{2}{3}(11N_c-2N_f)\),
  \(B_1=\frac{136}{3}N_c^2-(\frac{52}{3}N_c-\frac4{N_c})N_f\), the window
  \(\frac{34N_c^3}{13N_c^2-3}<N_f<\frac{11}{2}N_c\), the expansion
  \(\epsilon_{\rm BZ}=(11N_c-2N_f)/3\),
  \(a_*=\epsilon_{\rm BZ}/(25N_c^2-11)+O(\epsilon_{\rm BZ}^2)\), and
  \(\omega_{\rm BZ}=4\epsilon_{\rm BZ}^2/(25N_c^2-11)+O(\epsilon_{\rm BZ}^3)\);
- Wilson lines, open gauge-invariant quark-antiquark operators, rectangular
  Wilson loops, static potentials, and the distinction between pure
  Yang--Mills area-law diagnostics and QCD with dynamical fundamental quarks;
- the 't Hooft large-\(N_c\) limit in the monograph trace convention, including
  \(\lambda=g^2N_c\), its conversion to the common half-trace convention,
  the \(SU(N_c)\) completeness relation
  \(\sum_a(t^a)^i{}_j(t^a)^k{}_\ell
  =\delta^i{}_\ell\delta^k{}_j
  -N_c^{-1}\delta^i{}_j\delta^k{}_\ell\), double-line notation, the
  single-trace adjoint action normalization, the ribbon-graph power
  \(N_c^{V-E+F}=N_c^{2-2h-b}\), the explicit planar-versus-one-handle
  theta-graph \(N_c^{-2}\) suppression, single-trace factorization,
  fixed-\(N_f\) and Veneziano quark-boundary counting, and the leading
  large-\(N_c\) scaling of meson, glueball, baryon, and vacuum amplitudes,
  including baryon operator normalization, fixed-\(N_f\) order of limits,
  Hartree pair-counting, spin-flavor symmetry of the color-antisymmetric
  baryon operator, rotor splittings, and the boundary of the contracted
  \(SU(2N_f)\) large-\(N_c\) interpretation;
- the QCD-string flux-tube sector from rectangular Wilson-loop spectral data,
  including the static-source Hilbert-space expansion, the asymptotic string
  tension, \(N\)-ality and screening, the static-gauge effective worldsheet
  action, the Gaussian transverse determinant, the open and closed Luscher
  terms, the Nambu--Goto reference expansion, and the controlled-approximation
  boundary separating universal effective-string terms from lattice-matched
  coefficients;
- the excited flux-tube oscillator spectrum, including open-string oscillator
  levels, closed-string left/right levels, longitudinal momentum, level
  matching, Gaussian large-\(L\) level energies, and the Nambu--Goto reference
  square-root spectra and \(1/L^3\) expansions;
- the operational extraction of the string tension from Wilson loops,
  Polyakov-loop correlators, and transfer-matrix spectral data, with local
  perimeter/corner renormalizations separated from the area coefficient and
  the zero-temperature string tension distinguished from the finite-temperature
  center-symmetry order parameter;
- baryonic static-source sectors built from \(SU(N_c)\) junction operators,
  including the \(SU(3)\) \(Y\)-string potential, the Steiner/Fermat
  \(2\pi/3\) condition, the formula
  \(L_Y^2=(a^2+b^2+c^2+4\sqrt3\,\Delta)/2\), its collapsed
  \(120^\circ\) boundary case, and the distinction from pairwise
  \(\Delta\)-ansatz fits;
- closed winding flux tubes as finite-volume sectors created by spatial
  Polyakov loops, the boundary between these sectors and local glueball
  channels, the large-\(N_c\) relation \(g_s\sim 1/N_c\) as color-topology
  counting rather than a derivation of confinement, and the special simplicity
  of \(D=3\) effective-string tests;
- heavy-quark effective theory as the Wilson-line limit of a dynamical
  massive colored field, including the mostly-plus velocity convention
  \(v^2=-1\), the transverse projector \(D_\perp^\mu\), the projected
  spinor field \(h_v\), the finite-regulator HQET datum, the static
  propagator as a Wilson transporter, static spin/flavor symmetry, the
  free residual-dispersion derivation, and the controlled status of the
  \(1/m_Q\) expansion;
- heavy-light and heavy-to-heavy HQET current matching, including the explicit
  mostly-plus factor of \(\ii\) in Hermitian vector and axial currents,
  QCD/HQET residual-state normalization, \(f_H\sqrt M\) scaling, the recoil
  variable \(w=-v\cdot v'\), the Isgur-Wise function as a light-cloud overlap,
  zero-recoil normalization from the heavy-flavor charge, and the controlled
  status of subleading current and action insertions;
- NRQCD and pNRQCD as the heavy-pair expansion, including Pauli quark and
  charge-conjugated antiquark fields, the leading Schrödinger action, the
  NRQCD operator datum, gauge-invariant singlet and octet quarkonium bilocals
  with equal-time Wilson transporters, the pNRQCD singlet action, the
  tree-level attractive singlet Coulomb potential in the trace-delta
  convention, and the hard/soft/ultrasoft scale-separation hypothesis;
- heavy-quark mass coordinates and static energies, including the
  gauge-invariant Wilson-loop definition of the renormalized static energy,
  finite mass/potential scheme transformations, potential-subtracted mass
  subtraction at leading order, and a careful status statement for
  heavy-quark renormalon language as perturbative scheme information rather
  than a nonperturbative mass definition;
- the distinction between colored gauge-fixed fields and physical external
  states in QCD, with confinement stated as a nonperturbative spectral
  hypothesis rather than a theorem derived from the continuum QCD Lagrangian;
- a labeled open problem for physical QCD asymptotic completeness, separating
  the construction of hadronic wave operators and detector limits from
  asymptotic freedom, factorization, mass gap, and confinement hypotheses;
- the energy-flow detector as a weak limit of stress-tensor flux quadratic
  forms on the physical scattering domain;
- calorimetric final-state measures, smeared \(k\)-point energy correlators,
  contact terms at coincident detector directions, and the total-energy sum
  rule;
- the soft and collinear continuity estimate for smeared detector observables;
- the normalized \(e^+e^-\) energy-energy correlator and its contact term at
  zero opening angle;
- the eventwise EEC zeroth and first moment sum rules in the center-of-mass
  frame, including the exact coincident-detector contact weight;
- the back-to-back EEC factorization datum in impact-parameter space, the
  convention \(b_{\rm F}=2e^{-\gamma_E}\), and the leading fixed-coupling
  Sudakov factor
  \(\exp[-\Gamma_{\rm cusp}^q L_b^2/2]\) with
  \(\Gamma_{\rm cusp}^q=g^2C_F/(4\pi^2)+O(g^4)\), now presented as a
  scoped endpoint calculation rather than theorem form;
- the tree-level resolved collinear EEC coefficient, derived from the ordered
  detector weight \(2x(1-x)\) multiplying the real final-state splitting
  kernels, with exact coefficients
  \(\frac32C_F\), \(\frac{14}{5}C_A\), and \(\frac15T_F\) per quark flavor;
- multipoint jet energy correlators and energy-flow polynomials as polynomial
  functionals of calorimetric data;
- DIS kinematics, inclusive final-state sums, the leading electromagnetic
  amplitude, the non-time-ordered hadronic tensor, the current-conservation
  tensor decomposition, support in \(x_B\), the discontinuity of the
  time-ordered forward Compton amplitude, twist-two operators, Wilson lines,
  the regulated gauge-invariant matrix-element principle for QCD quantities,
  the gauge-covariance proof for open light-ray operators, integrated quark and
  gluon PDF definitions with Wilson-line dressing, convolution
  renormalization, Euclidean equal-time spatial bilocals and quasi-/pseudo-PDF
  coordinates as matching observables rather than definitions of PDFs,
  large-momentum matching as a distributional controlled approximation with
  finite-regulator error terms, factorization assumptions with a compact-\(x_B\)
  distributional power-remainder bound, the replacement of abelian
  Bloch--Nordsieck cancellation by nonabelian PDF renormalization for incoming
  colored partons, unambiguous \(D_0\)-based DGLAP kernels, number and momentum
  sum-rule checks in prose rather than proposition form, the small-\(x\)
  boundary as a regulated Wilson-line dipole
  problem with a leading BFKL kernel datum, transverse kernel covariance, and
  the Mellin eigenvalue
  \(\chi(\gamma)=2\psi(1)-\psi(\gamma)-\psi(1-\gamma)\), TMDs as
  soft-subtracted transverse light-ray matrix elements with Collins--Soper
  rapidity evolution, Drell--Yan as a timelike current-current Wightman tensor
  with past-pointing TMD staples and an explicit Glauber-status datum,
  small-\(q_\perp\) color-singlet TMD factorization data, GPDs as off-forward
  light-ray matrix elements, GPD polynomiality from local twist-two
  covariance, logarithmic scaling violation, and the endpoint/large-spin cusp
  boundary of the DIS factorization statement, now anchored by an explicit
  cusped-Wilson-line definition, one-loop angular-integral derivation, and
  the relation
  \(P_{{\rm ns},N}=-\Gamma_{\rm cusp}^q\log N+O(N^0)\) for the matrix-element
  evolution eigenvalue.
- Euclidean current sum rules as color-singlet current-correlator identities,
  including the subtracted dispersion representation, spacelike OPE input,
  Borel--Laplace functional, Borel transform of the dispersion kernel,
  inverse-power OPE terms, the controlled Borel-window datum, and the
  logarithmic mass estimator as a spectral weighted average.

## Claim Ledger

1. The background-field gauge preserves a gauge symmetry acting on
   \(\widetilde A\), so the dimension-four background effective action is
   proportional to \(\widetilde F^a_{\mu\nu}\widetilde F^{a\mu\nu}\).
2. The ordinary covariant-gauge Faddeev--Popov action produces scalar
   kinetic operators for ghosts with Grassmann statistics, no two-gluon ghost
   seagull in Lorenz gauge, and a gluon propagator multiplied by \(g^2\)
   because the connection normalization puts \(1/g^2\) in the Yang--Mills
   kinetic term.
3. The one-loop determinant ratio follows from Gaussian integration over
   quarks, ghosts, and gauge fluctuations, with Grassmann and bosonic signs
   stated.
4. A nearly constant background field in a box extracts the logarithmic
   coefficient of the local curvature term; the box size supplies the IR
   scale.
5. The Dirac determinant coefficient follows from applying the heat-kernel
   coefficient to \(-\slashed{\widetilde D}^{\,2}\), including the
   \(\frac12\) relating the first-order determinant to the squared operator.
6. The ghost coefficient \(1/12\) and vector determinant coefficient
   \(-5/3\) follow from the scalar adjoint Laplacian and the background
   Feynman-gauge one-form operator, with the adjoint trace sign stated.
   Their weighted sum gives
   \(-\frac12(-5/3)+1/12=11/12\) for the pure-gauge part in the source
   normalization.
7. Bare-coupling independence in dimensional regularization gives the
   one-loop beta function after \(\lambda^2(\mu)=\mu^\epsilon g^2(\mu)\) is
   introduced.
8. A perturbative two-loop zero near the upper edge of asymptotic freedom is a
   controlled Banks--Zaks fixed-point diagnostic, not a statement about
   ordinary low-flavor QCD.  In the monograph's trace convention the leading
   small-\(\epsilon_{\rm BZ}\) fixed-point coordinate is
   \(a_*=\epsilon_{\rm BZ}/(25N_c^2-11)+O(\epsilon_{\rm BZ}^2)\), and the
   coupling perturbation has
   \(\omega_{\rm BZ}=4\epsilon_{\rm BZ}^2/(25N_c^2-11)+O(\epsilon_{\rm BZ}^3)\).
   The \(O(\epsilon_{\rm BZ}^2)\) location is not fixed by the two-loop beta
   function alone.
9. The one-loop running coupling and dimensional transmutation do not prove
   four-dimensional continuum Yang--Mills existence, mass gap, or confinement.
   The pure Yang--Mills existence and mass-gap problem is the Clay Millennium
   problem; QCD spectral confinement and flux-tube statements require separate
   nonperturbative input or a regulated/lattice context.
10. A rectangular Euclidean Wilson loop extracts the static potential between
   external color sources; an area law in pure Yang--Mills is a confinement
   diagnostic, while dynamical fundamental matter can break the flux tube.
11. In the trace convention
   \(\operatorname{tr}_{\square}(t^at^b)=\delta^{ab}\), the large-\(N_c\)
   coupling held fixed is \(\lambda=g^2N_c\), equal to one half of the common
   half-trace 't Hooft coupling because \(g_{\rm ht}^2=2g^2\).  The leading
   color-flow propagator and the
   Euler characteristic of the associated ribbon surface give
   \(N_c^{V-E+F}=N_c^{2-2h-b}\), while the \(SU(N_c)\) trace subtraction is
   explicitly subleading.  The planar and one-handle theta graphs have the
   same \(V,E\) and two different face counts, giving an \(N_c^{-2}\)
   nonplanar suppression at fixed \(\lambda\).
12. Normalized single-trace adjoint observables factorize at large \(N_c\)
   with connected two-point fluctuations of order \(N_c^{-2}\).  Fixed-flavor
   quark loops are suppressed as additional boundaries, while Veneziano
   scaling restores their leading order.  Meson, glueball, and baryon scaling
   statements depend on separate spectral assumptions about the existence of
   the corresponding color-singlet states.  Large-\(N_c\) baryons are treated
   in the fixed-\(N_f\) limit with color-antisymmetric \(SU(N_c)\) operators;
   the Hartree pair-counting gives \(M_B=O(N_c)\), collective rotor splittings
   give \(\Delta M=O(N_c^{-1})\) at fixed spin, and contracted spin-flavor
   symmetry is used only under the stated low-energy and confinement
   hypotheses.
13. The QCD string is defined through line-operator/static-source sectors, not
    through perturbative colored fields.  Under the effective-string
    hypotheses that the only gapless worldsheet modes are the transverse
    displacements, the Gaussian determinant gives the universal open and
    closed Luscher terms \(-\pi(D-2)/(24L)\) and
    \(-\pi(D-2)/(6L)\), while later coefficients require symmetry constraints
    and matching data.
14. Excited flux-tube levels are organized first by the oscillator Hilbert
    space of the transverse worldsheet fields.  The open generating function
    is \(\prod_{n\ge1}(1-q^n)^{-(D-2)}\), closed flux tubes carry left and
    right levels satisfying \(N_L-N_R=q\), and the Nambu--Goto formulas are
    reference spectra rather than definitions of the QCD string.
15. The string tension is the coefficient of the large-rectangle area term
    after local line renormalizations are separated, equivalently the
    large-\(L\) slope of the transfer-matrix ground-state energy in the
    static-source sector under the stated spectral assumptions.  Baryonic
    string sectors require junction line operators; for three sources with
    all angles below \(120^\circ\), the leading \(Y\)-network length obeys
    \(L_Y^2=(a^2+b^2+c^2+4\sqrt3\,\Delta)/2\).  Closed winding flux tubes are
    clean finite-volume sectors, while identifying local glueballs with
    closed strings is an additional large-\(N_c\)/effective-string
    organization, not a theorem following from the Luscher determinant.
15a. HQET is formulated as a finite-regulator Wilsonian expansion around a
     timelike velocity \(v^2=-1\).  The leading heavy propagator is the
     fundamental Wilson transporter along \(x(s)=x_0+sv\), the static action
     has heavy spin/flavor symmetry because it contains no projected spin
     operator, and the first kinetic correction is fixed by the free residual
     dispersion \(E_{\rm res}=|\mathbf k|^2/(2m_Q)-|\mathbf k|^4/(8m_Q^3)+\cdots\)
     together with reparametrization compatibility.  The uniform
     \(1/m_Q\) expansion is recorded as a controlled matrix-element estimate,
     not as a consequence of the static Wilson-line identity alone.
15aa. Heavy-light currents are matched as renormalized operator-valued
      distributions in the same finite-regulator datum as the HQET action.
      With the monograph mostly-plus spinor convention, physical vector and
      axial currents include the explicit factor \(\ii\).  The state
      normalization
      \(|H(Mv+k)\rangle_{\rm QCD}=\sqrt M\,|H_v(k)\rangle_{\rm HQET}\)
      gives \(f_H\sqrt M=C_A F_H+O(\Lambda_{\rm had}/m_Q)\), while the
      zero-recoil Isgur-Wise normalization follows from the heavy-flavor
      Noether charge of the leading static theory after the current
      normalization is fixed by a background heavy-flavor connection.
15b. NRQCD is a separate heavy-pair datum with Pauli fields \(\psi,\chi\),
     local gauge-covariant operators, and a velocity power counting.  The
     quarkonium singlet bilocal
     \(\chi^\dagger W(\mathbf x_2,\mathbf x_1)\psi/\sqrt{N_c}\) is gauge
     invariant by endpoint cancellation, while the octet bilocal transforms at
     the chosen center point.  Potential NRQCD treats \(V_S(r;\mu)\) as a
     bilocal matching coefficient; at weak coupling the tree singlet color
     factor is \(-C_F\) and
     \(V_S^{(0)}(r)=-g^2C_F/(4\pi r)\), with
     \(g_{\rm ht}^2=2g^2\) and \(C_F^{\rm ht}=C_F/2\) leaving the product
     invariant.
15c. Heavy-quark masses in HQET/NRQCD/pNRQCD are scheme coordinates, not
     physical colored-particle spectral masses in confining QCD.  The
     gauge-invariant static energy is extracted from a renormalized
     rectangular Wilson loop.  A finite shift
     \(m'\!=m+\delta m\), \(V'\!=V-2\delta m\) leaves
     \(2m+V\) and \(2m+E_n\) invariant.  The leading potential-subtracted
     subtraction is
     \(\delta m_{\rm PS}^{(0)}=g^2C_F\mu_f/(4\pi^2)\), and renormalon
     terminology is confined to specified perturbative expansions and
     summation prescriptions.
16. Colored quark and gluon fields are not physical asymptotic states in the
   QCD confinement scenario; deriving this spectral property from the
   four-dimensional continuum QCD Lagrangian is open, so the manuscript uses it
   as a nonperturbative physical hypothesis when discussing phenomenology.
   Physical scattering statements must be formulated in terms of
   gauge-invariant states or controlled high-energy factorization data.
17. Energy correlators are nonperturbative detector observables once the
    stress-tensor flux limit is constructed on the physical Hilbert space.
18. Smeared detector observables are continuous under soft emission and
    collinear recombination, and this supplies the measurement-function input
    for KLN/factorization finiteness at fixed perturbative order.
19. The energy-energy correlator and energy-flow polynomials are formulated in
    terms of positive calorimetric measures rather than colored parton labels.
19a. Including the coincident-detector contact term, the eventwise EEC
     distribution has unit zeroth moment and vanishing first \(\cos\chi\)
     moment in a color-singlet center-of-mass frame; removing the contact term
     removes the weight \(\sum_r z_r^2\) from the separated-angle
     distribution.
19b. In the small-angle endpoint, the first resolved real-emission EEC
     coefficient is obtained by multiplying the final-state splitting
     probability by the ordered detector weight \(2x(1-x)\).  This weight
     cancels the real-kernel endpoint poles and gives the exact integrals
     \(\Gamma_q^{\rm EEC}=\frac32C_F\),
     \(\Gamma_{g\to gg}^{\rm EEC}=\frac{14}{5}C_A\), and
     \(\Gamma_{g\to q\bar q}^{\rm EEC}=\frac15T_F\) per flavor.
19c. In the back-to-back endpoint, the impact-parameter factorization datum
     yields the leading fixed-coupling Sudakov factor
     \(W_{\rm LL}(b,Q)=W(b,\mu_b)
     \exp[-\Gamma_{\rm cusp}^qL_b^2/2]\), where
     \(L_b=\log(Q^2b^2/b_{\rm F}^2)\),
     \(b_{\rm F}=2e^{-\gamma_E}\), and
     \(\Gamma_{\rm cusp}^q=g^2C_F/(4\pi^2)+O(g^4)\) in the trace-delta
     convention.
20. DIS is controlled by an inclusive Wightman current-current tensor; the
    time-ordered forward Compton amplitude supplies its discontinuity, and the
    short-distance OPE applies to the time-ordered product before analytic
    continuation to the physical inclusive tensor.
21. The leading-twist local operators and the gauge-invariant light-ray
    operators are two presentations of the same short-distance data; asymptotic
    freedom changes Bjorken scaling into logarithmic scaling violation governed
    by anomalous dimensions.
22. In QCD, partonic initial-state collinear singularities are not removed by
    an abelian Bloch--Nordsieck final-state sum.  They are absorbed into the
    renormalized Wilson-line light-ray operators defining PDFs, and the
    resulting factorization-scale dependence is governed by DGLAP evolution.
22a. QCD quantities involving colored fields must be grounded as regulated
     gauge-invariant matrix elements.  Wilson lines are part of the operator
     definition whenever exposed color indices at separated points are
     connected, and ultraviolet, cusp, endpoint, and rapidity subtractions are
     part of the datum when the geometry of the operator requires them.
22b. The leading-order DGLAP kernels are written with the explicit
     \(D_0=(1-x)^{-1}_+\) distribution to avoid the ambiguous shorthand
     \((1+x^2)/(1-x)_+\).  With this convention the kernels obey quark-number
     and momentum-column sum rules exactly; the calculation is retained as a
     distributional check rather than theorem form.  The nonsinglet Mellin moment is
     \(C_F[-2H_{N-1}-1/N-1/(N+1)+3/2]\), giving the one-loop cusp coefficient
     \(g^2C_F/(4\pi^2)\) in the monograph trace normalization.
22c. Inclusive DIS factorization is recorded as a leading-twist datum with a
     distributional remainder estimate on compact Bjorken-\(x\) intervals.  The
     threshold \(x\to1\) and small-\(x\) limits are separate boundary problems,
     not consequences of the compact-\(x\) statement.
22ca. Euclidean equal-time spatial bilocals are gauge-invariant Wilson-line
      matrix elements in a finite regulator.  Their quasi-PDF Fourier
      transforms and pseudo-Ioffe-time coordinates are matching observables for
      light-ray PDFs, not alternate definitions of those PDFs.  The
      large-momentum relation is stated distributionally against test functions
      and carries explicit hadron-mass, higher-twist, lattice-spacing,
      finite-volume, and endpoint qualifications.  Finite scheme changes of
      light-ray PDFs act by inverse transformation on the matching kernel, and
      charge preservation is a column-sum condition on that kernel.
22cc. The small-\(x\) boundary is grounded in regulated Wilson-line dipole
      matrix elements rather than colored parton scattering states.  The
      leading fixed-coupling BFKL kernel is written with the monograph
      trace-delta coefficient \(g^2C_A/(8\pi^3)\), equivalently
      \(\bar\alpha_s=g^2C_A/(4\pi^2)\) multiplying the \(1/(2\pi)\)-normalized
      transverse integral.  Its dipole kernel measure is invariant under
      transverse translations, rotations, scalings, and inversion, and its
      Mellin eigenvalue is
      \(2\psi(1)-\psi(\gamma)-\psi(1-\gamma)\), with
      \(\chi(1/2)=4\log2\) and the quadratic diffusion coefficient
      \(-14\zeta(3)\) on the line \(\gamma=1/2+\ii\nu\).
22cd. Drell--Yan is formulated as a timelike current-current Wightman tensor
      between two hadron states.  The leading-power kinematic variables obey
      \(x_Ax_B=Q^2/s\) and \(y=\frac12\log(x_A/x_B)\).  The TMD factorization
      datum uses past-pointing staples, \(\zeta_A\zeta_B=Q^4\), a \(Y\)-term,
      a power-remainder topology, and an explicit Glauber item.  The finite
      Glauber lemma proves only the tensor-product unitarity identity
      \(\operatorname{Tr}[(M\otimes1)(1\otimes U)\rho(1\otimes U^\dagger)]
      =\operatorname{Tr}[(M\otimes1)\rho]\); applying this identity to QCD
      requires the leading-region, color-flow, rapidity, and measurement
      hypotheses to be proven or stated.
22d. TMDs are transverse-separated Wilson-line matrix elements with a soft
     subtraction and an independent rapidity renormalization scale.  The
     Collins--Soper kernel is defined by rapidity evolution, its
     \(\mu\)-dependence is fixed by the lightlike cusp coefficient, and finite
     TMD scheme changes preserve the mixed-derivative consistency equation.
22e. GPDs are off-forward light-ray matrix elements.  Their Mellin moments are
     polynomials in the skewness \(\xi\) because the corresponding local
     twist-two matrix elements decompose into finitely many Lorentz-covariant
     tensors built from \(P\) and \(\Delta\).
23. Physical QCD asymptotic completeness remains an open large-time problem:
    one must construct wave operators from stable color-singlet asymptotic
    spaces, treat resonances through analytic scattering data, include
    massless Goldstone modes when chiral limits are taken, and prove that
    detector observables such as energy flow are limits on the same scattering
    domain.
24. QCD current sum rules are linear functionals of color-singlet current
    correlators.  The Borel transform kills subtraction polynomials, maps
    \((s+Q^2)^{-1}\) to \(M^{-2}e^{-s/M^2}\), and maps
    \((Q^2)^{-m}\) to \(((m-1)!(M^2)^m)^{-1}\).  A pole-plus-continuum
    extraction is a controlled approximation only after the OPE truncation,
    spectral ansatz, and Borel-window error estimates are stated; the
    logarithmic mass estimator is exactly a weighted average over the retained
    spectral atoms.

## Figure Requirements

- Ordinary covariant-gauge rules figure: ghost propagator, ghost-gluon
  vertex with momentum convention, gluon propagator, absence of the
  \(\bar c c A A\) vertex, and cubic/quartic gluon self-interactions.
- Background-field logic figure: split, background covariance, determinant
  ratio, and invariant curvature coefficient.
- Constant-background box figure showing the IR scale \(L\sim\mu^{-1}\).
- Running-coupling/dimensional-transmutation figure if the discussion is
  expanded beyond the displayed one-loop solution.
- Banks--Zaks beta-shape figure distinguishing a perturbative fixed point from
  continued strong-coupling flow.
- Wilson-line/Wilson-loop figure distinguishing open flux-tube operators from
  rectangular loop extraction of \(V(L)\).
- Large-\(N_c\) double-line topology figure: leading adjoint color-flow
  propagator, planar theta graph, and one-handle theta graph with the
  \(F=3\) versus \(F=1\) face count and \(N_c^{-2}\) suppression marked.
- QCD-string figure: static-source flux tube and the associated worldsheet
  transverse fluctuations.
- Baryonic \(Y\)-string figure: three static sources, a color junction, and
  \(2\pi/3\) Fermat/Steiner meeting angles.
- Energy-flow detector figure: stress-tensor flux through a large sphere,
  smeared angular test functions, and the induced calorimetric measure on
  \(S^2\).
- Energy-energy correlator figure: two calorimeters at opening angle \(\chi\),
  with coincident-angle contact contribution marked separately.
- DIS inclusive-scattering kinematics figure.
- DIS factorization figures must distinguish operator definitions from
  parton-model mnemonics.
- Future TMD figures should distinguish unsubtracted beam matrix elements,
  soft Wilson-line factors, rapidity subtraction, and the final
  impact-parameter convolution.

## Audit Notes

- The Ben Lou transcription has the ghost coefficient in the determinant
  summary as \(1/2\); the handwritten page shows \(1/12\).  The manuscript
  follows the handwritten source and the arithmetic
  \(5/6+1/12=11/12\).
- The ordinary Lorenz-gauge Feynman-rule block was patched on 2026-05-22.
  The manuscript uses \(\bar c\) rather than \(b\) for the antighost, records
  the source's ghost propagator and ghost-gluon momentum convention, and keeps
  these as Green-function rules rather than colored external-state rules.
  The repaired figure was rendered against handwritten pages 182--184 on
  2026-05-22.
- Do not collapse the beta-function derivation to a final coefficient.  The
  background-field covariance and determinant comparison are part of the
  conceptual content.
- 2026-05-22 follow-up: the manuscript no longer leaves the ghost and vector
  determinant coefficients as asserted values.  It derives the heat-kernel
  logarithmic coefficient, the adjoint trace sign, the Dirac square, the
  scalar ghost coefficient, and the one-form vector coefficient before
  forming \(b=\frac{11}{12}C_A-\frac{N_f}{3}T_R\).
- Do not introduce perturbative \(S\)-matrix diagrams for colored external
  states.  QCD external-state statements must respect the earlier
  nonperturbative scattering and BRST/physical-Hilbert-space framework.
- Keep 1PI RG, Wilsonian RG, and physical scaling/factorization statements
  separate unless the connecting map is stated.
- The DIS block was expanded on 2026-05-22 to restore the source chain from
  inclusive final-state sums to the hadronic tensor, forward Compton
  discontinuity, OPE, local twist-two operators, light-ray operators, and
  logarithmic scaling violation.
- 2026-05-24 issue #491 pass: expanded detector observables into a detailed
  energy-correlator treatment, including the energy-flow detector hypothesis,
  calorimetric measures, smeared correlators, contact terms, soft/collinear
  continuity estimates, \(e^+e^-\) EEC normalization, and energy-flow
  polynomial definitions.
- 2026-05-26 issue #519 pass: added the eventwise EEC moment identities and
  exact finite-event calculation check for zeroth moment, first moment, and
  contact weight.
- 2026-05-27 issue #519 collinear pass: added the tree-level resolved
  collinear EEC coefficient derivation, clarified the status of the result
  relative to the full small-angle light-ray/OPE theorem, and added
  `calculation-checks/energy_correlator_collinear_checks.py`.
- 2026-05-29 issue #519 back-to-back pass: added the cusp-controlled
  leading Sudakov factor for the back-to-back EEC in impact-parameter space,
  separated its scope from the full endpoint theorem, and added
  `calculation-checks/energy_correlator_sudakov_checks.py`.
- 2026-05-29 continuing anti-wrapper audit: demoted the eventwise EEC
  sum-rule proposition to detector-observable prose.  The identities remain
  exact and nonperturbative, but their derivation is energy-momentum
  conservation plus the definition of the calorimetric distribution.
- 2026-05-28 issue #630 small-\(x\) pass: added the regulated dipole datum,
  gauge-invariance proof, leading-logarithmic BFKL/BK status statement,
  transverse kernel covariance proof, Mellin-eigenvalue derivation by analytic
  regularization, and `calculation-checks/qcd_bfkl_small_x_checks.py`.
- 2026-05-28 issue #630 Drell--Yan/Glauber pass: added the Drell--Yan
  hadronic tensor, leading-power kinematics, TMD factorization datum with
  past-pointing staples, finite tensor-product unitarity lemma for the
  algebraic content of Glauber cancellation, and
  `calculation-checks/qcd_drell_yan_glauber_checks.py`.
- 2026-05-24 issue #490 pass: the compiled Volume IV successor chapter now
  develops jets, IRC-safe measurement functions, parton showers,
  fragmentation functions, and hadronization as the final-state observable
  continuation of the QCD chapter.
- 2026-05-24 issue #260 pass: added the cross-reference from QCD factorization
  back to the Abelian-scope Bloch--Nordsieck remark and stated that
  initial-state collinear singularities of colored partons are absorbed into
  renormalized PDFs rather than canceled by a final-state inclusive sum.
- 2026-05-24 issue #261 pass: added an explicit mass-gap status remark after
  dimensional transmutation, identifying pure four-dimensional Yang--Mills
  continuum existence plus a positive mass gap as the Clay Millennium problem
  and separating it from perturbative running-coupling statements.
- 2026-05-24 issue #262 pass: revised the confinement wording so the
  color-singlet asymptotic-state property is stated as a nonperturbative
  spectral hypothesis/physical input, with the derivation from the
  four-dimensional continuum QCD Lagrangian flagged as open.
- 2026-05-24 issue #263 pass: connected the Wilson-loop area-law diagnostic to
  the strong-coupling theorem in the new lattice Yang--Mills chapter and
  separated that finite-cutoff result from the continuum four-dimensional
  confinement problem.
- 2026-05-24 issue #332 pass: added a labeled open problem for asymptotic
  completeness of physical QCD, explicitly distinguishing the hadronic
  Hilbert-space wave-operator theorem from asymptotic freedom, factorization,
  mass gap, and spectral confinement inputs.
- 2026-05-25 issue #463 pass: expanded the Banks--Zaks discussion from a
  diagnostic paragraph into an explicit two-loop derivation in the monograph
  gauge-generator convention, including scheme-invariance of \(B_0,B_1\), the
  fundamental-representation window, the \(\epsilon_{\rm BZ}\) fixed-point
  coordinate, the IR-attractive exponent, the integer-\(N_f\)/Veneziano
  caveat, and `calculation-checks/banks_zaks_two_loop_checks.py`.
- 2026-05-25 issue #468 pass: added the 't Hooft large-\(N_c\) expansion as a
  full QCD-chapter section before the QCD-string discussion, with
  trace-normalization conversion, double-line completeness, ribbon-graph
  Euler-characteristic derivation, explicit planar/nonplanar theta-graph
  power comparison, single-trace factorization, fixed-\(N_f\) versus
  Veneziano quark-boundary counting, and
  `calculation-checks/large_n_topology_checks.py`.
- 2026-05-25 issue #504 completion pass: expanded the large-\(N_c\) baryon
  material from mass scaling to the actual baryon operator, fixed-\(N_f\)
  order of limits, Hartree pair-counting, spin-flavor symmetry of the
  color-antisymmetric baryon wavefunction, collective rotor splittings,
  chiral-soliton compatibility, contracted \(SU(2N_f)\) status, and the
  distinct Veneziano-limit caveat; extended
  `calculation-checks/large_n_topology_checks.py` accordingly.
- 2026-05-25 issue #492 pass: deepened the QCD-string section by deriving the
  open and closed Luscher terms from the free transverse worldsheet
  determinant, adding the Nambu--Goto reference expansion only as a reference
  effective-string coordinate, and recording
  `calculation-checks/qcd_string_luscher_checks.py`.
- 2026-05-25 issue #492 follow-up: added the excited flux-tube level
  structure, including open oscillator degeneracies, closed level matching,
  and Nambu--Goto reference spectra through \(1/L^3\), with the calculation
  check extended accordingly.
- 2026-05-25 issue #492 completion pass: added static-observable and lattice
  extraction logic for the string tension, a transfer-matrix proposition
  equating the area coefficient with the static-potential slope, baryonic
  junction operators and the \(Y\)-string Steiner-length derivation with a new
  figure, closed winding flux tubes versus local glueball channels,
  large-\(N_c\) string-coupling counting, and the \(D=3\) effective-string
  testbed; extended `calculation-checks/qcd_string_luscher_checks.py` to
  verify the displayed baryonic geometry.
- 2026-05-27 issue #630 A1 pass: added the QCD-wide regulated
  gauge-invariant matrix-element datum, upgraded the DIS/PDF block with
  Wilson-line gauge covariance, normalized quark and gluon light-ray PDF
  definitions, explicit separation between nonperturbative operator
  definitions and colored parton-model language, convolution renormalization,
  compact-\(x\) factorization status with a distributional remainder, exact
  \(D_0\)-based DGLAP sum-rule calculation, and endpoint/large-spin cusp discussion.
- 2026-05-27 issue #630 TMD/GPD pass: added soft-subtracted TMD operator data,
  Collins--Soper scale-integrability condition, finite TMD scheme transformations,
  small-\(q_\perp\) color-singlet factorization data, off-forward GPD
  definitions, a proof of GPD polynomiality from local twist-two covariance,
  and `calculation-checks/qcd_tmd_gpd_checks.py`.
- 2026-05-29 anti-wrapper audit: demoted the Collins--Soper consistency
  calculation from proposition form to coordinate-integrability prose, making
  explicit that the substantive QCD input is the regulated Wilson-line TMD
  definition, rapidity renormalization, the cusp anomalous dimension, and the
  kernel calculation.
- 2026-05-27 QCD HQET pass: added heavy-quark effective theory as a
  Wilson-line limit after the QCD-string/static-source discussion, with
  explicit mostly-plus velocity and projector conventions, the HQET regulator
  datum, a proof of the static propagator/Wilson-transporter identity, static
  spin/flavor symmetry, residual-dispersion derivation, controlled
  \(1/m_Q\)-expansion status, and `calculation-checks/qcd_hqet_checks.py`.
- 2026-05-27 QCD NRQCD/pNRQCD pass: corrected the half-trace large-\(N_c\)
  conversion to \(g_{\rm ht}^2=2g^2\) and
  \(\lambda_{\rm ht}=2\lambda\), then added the heavy-pair datum,
  gauge-invariant singlet/octet bilocals, pNRQCD singlet action, tree-level
  singlet color-factor proof, scale-separation status, and
  `calculation-checks/qcd_nrqcd_checks.py`.
- 2026-05-27 QCD heavy-mass/static-energy pass: added the Wilson-loop static
  energy as the gauge-invariant anchor for heavy-quark mass coordinates,
  proved constant mass/potential scheme invariance, derived the leading
  potential-subtracted mass coefficient, stated the renormalon status
  carefully, and added
  `calculation-checks/qcd_heavy_mass_static_energy_checks.py`.
- 2026-05-27 QCD HQET current/symmetry pass: added heavy-light current
  matching, mostly-plus current normalization, QCD/HQET state normalization,
  decay-constant scaling, heavy-to-heavy recoil kinematics, the Isgur-Wise
  function, zero-recoil normalization from the heavy-flavor charge, controlled
  subleading-current status, and
  `calculation-checks/qcd_hqet_current_checks.py`.
- 2026-05-29 anti-wrapper pass: demoted three QCD spectroscopy/kinematics
  wrappers to worked paragraphs: the leading weak-coupling \(1S\) hyperfine
  contact coordinate, the unequal-mass elastic partial-wave projection, and
  the quarkonium \(J^{PC}\) rule.  The formulas remain because they fix
  conventions and coordinates, but the removed proof environments were
  first-order perturbation, Legendre-projection, or Clebsch--Gordan/parity
  calculations rather than theorem-level arguments.  The one-loop instanton
  density factor and subtracted \('t Hooft\)-kernel positivity statements were
  retained for later strengthening rather than demotion, since their content
  involves RG covariance and quadratic-form positivity.
- 2026-05-29 follow-up: demoted the two-flavor contracted baryon spin-flavor
  algebra to a worked paragraph.  The algebra remains explicit, but the proof
  is finite Pauli-matrix bookkeeping plus large-\(N_c\) scaling of matrix
  elements, not a standalone theorem-level claim.
- 2026-05-29 seventh anti-wrapper pass: demoted the pseudoscalar-meson--baryon
  partial-wave \(J^P\) rule to representation-theory prose and expanded the
  smeared energy-flow continuity lemma so the soft and collinear bounds are
  stated as continuity of finite-energy calorimetric measures.

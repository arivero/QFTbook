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
  the trace-delta/half-trace conversion of the one-loop cusp coefficient; it
  also checks the back-to-back \(q_T^2\)-test pullback and a finite
  measured-bin residual budget that fails if the large-\(b\) component is
  silently omitted.
- `SRC-CHECK-EEC-TRACK`:
  `calculation-checks/energy_correlator_track_checks.py` verifies the selected
  calorimetric measure identities, track-function collinear moment ledger,
  selected endpoint-atom gluing equations, and measured-EEC residual-budget
  inequality.
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
  theta-graph \(N_c^{-2}\) suppression, the regulated genus-truncation
  bound separating formal topology from a controlled observable
  approximation, single-trace factorization, fixed-\(N_f\) and Veneziano
  quark-boundary counting, and the leading
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
- the asymptotic multiplication-operator model for smeared energy detectors
  on the outgoing hadronic direct-integral representation, including
  self-adjointness for real tests, positivity for nonnegative tests,
  the Hamiltonian domain bound, strongly commuting detector products, and
  the product-measure origin of coincident-detector contact terms;
- calorimetric final-state measures, smeared \(k\)-point energy correlators,
  contact terms at coincident detector directions, and the total-energy sum
  rule;
- the soft and collinear continuity estimate for smeared detector observables;
- the normalized \(e^+e^-\) energy-energy correlator and its contact term at
  zero opening angle;
- the eventwise EEC zeroth and first moment sum rules in the center-of-mass
  frame, including the exact coincident-detector contact weight;
- contact-inclusive EEC Legendre moments are positive calorimetric multipoles:
  \(M_{\ell,X}=\frac{4\pi}{2\ell+1}\sum_a|\sum_r z_r
  Y_{\ell a}(\mathbf n_r)|^2\ge0\), with \(M_1\) the momentum square and
  \(M_2=\frac32\operatorname{tr}Q^2\); separated-angle data alone do not
  preserve these constraints after the contact atom is deleted;
- the ordered three-detector eventwise distribution
  \(E_{3,X}(\zeta_{12},\zeta_{13},\zeta_{23})\), with unit total moment,
  vanishing pairwise angular moments in a color-singlet center-of-mass event,
  and explicit all-same and pair-contact diagonal strata;
- the distributional endpoint-matching ledger for the full normalized EEC:
  an open-interval matched distribution \(\mathcal R\), explicit endpoint
  atoms \(K_+\delta(1-\zeta)\) and \(K_-\delta(1+\zeta)\), and the two exact
  detector moment equations fixing or testing the endpoint coordinates in a
  declared subtraction scheme;
- the back-to-back EEC factorization datum in impact-parameter space, the
  convention \(b_{\rm F}=2e^{-\gamma_E}\), and the leading fixed-coupling
  Sudakov factor
  \(\exp[-\Gamma_{\rm cusp}^q L_b^2/2]\) with
  \(\Gamma_{\rm cusp}^q=g^2C_F/(4\pi^2)+O(g^4)\), now presented as a
  scoped endpoint calculation rather than theorem form;
- the tested back-to-back recoil chart: the pullback
  \(\varphi_Q(q_T^2)=\varphi(-1+2q_T^2/Q^2)\) following
  \(z=(1-\zeta)/2\) and \(1-z=q_T^2/Q^2\), the corresponding
  \(\dd\sigma/\dd\zeta=(Q^2/2)\dd\sigma/\dd q_T^2\) Jacobian, the separation
  of the open recoil integral from the endpoint atom \(K_-^\tau\), the
  large-\(b\) nonperturbative boundary, and the measured-bin residual
  decomposition for factorization, evolution, matching, large-\(b\), Glauber,
  and power errors;
- the tree-level resolved collinear EEC coefficient, derived from the ordered
  detector weight \(2x(1-x)\) multiplying the real final-state splitting
  kernels, with exact coefficients
  \(\frac32C_F\), \(\frac{14}{5}C_A\), and \(\frac15T_F\) per quark flavor;
- track selectors and charged-energy correlators as selected hadronic
  calorimetric measures, with selected-energy moment identities and the
  binomial moment ledger for track-function collinear splitting;
- the measured EEC prediction budget, including the exact selected hadronic
  observable, selected-energy and selected-momentum moment constraints,
  overlap-subtracted bulk/small-angle/back-to-back charts, endpoint atoms
  \(K_\pm^\tau\), nonperturbative track or fragmentation inputs, and a
  residual functional separating perturbative, endpoint, and hadronization
  errors;
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
  finite-regulator error terms, a common QCD factorization dependency ladder
  separating exact observables, operator coordinates, subtractions,
  coefficients, scale transport, boundary mechanisms, remainders, and limiting
  statements, factorization assumptions with a compact-\(x_B\)
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
  with an integrated two-PDF collinear factorization coordinate, transform-space
  two-leg RG cancellation, an explicit tested Wightman-to-factorization
  residual budget, past-pointing TMD staples, and an explicit Glauber-status
  datum,
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
   function alone.  The chapter now states this as a controlled perturbative
   fixed-point datum rather than a nonperturbative conformal-window theorem:
   a regulator construction and a scaling limit staying in the small-coupling
   neighborhood are separate inputs.
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
17a. On the outgoing hadronic scattering representation, a smeared detector is
     multiplication by
     \(m_f(Y)=\sum_{r\in Y}p_r^0f(\widehat{\mathbf p}_r)\).  This gives
     self-adjointness, positivity, the bound
     \(|m_f|\leq\|f\|_\infty E_{\rm tot}\), common product domains controlled
     by powers of the outgoing Hamiltonian, and the precise product-measure
     meaning of coincident detector directions.  The stress-tensor flux
     construction must be shown to agree with this multiplication model on
     scattering states.
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
19aa. The ordered three-detector distribution has unit total moment and three
      vanishing pairwise angular moments in the same center-of-mass
      convention.  Its separated support omits the all-same contact
      \(\sum_r z_r^3\) and the three pair-contact strata
      \(\sum_{r\ne t} z_r^2z_t\), so separated three-detector data do not
      satisfy the full moment identities without explicit contact coordinates.
19ab. Connected energy correlators are cumulants of detector random variables
      over the event ensemble.  They are distinct from contact-subtracted
      separated-detector observables: diagonal strata of
      \(\mu_X^{\otimes k}\) remain inside a fixed event even when ensemble
      cumulants vanish for a deterministic final state.
19b. In the small-angle endpoint, the first resolved real-emission EEC
     coefficient is obtained by multiplying the final-state splitting
     probability by the ordered detector weight \(2x(1-x)\).  This weight
     cancels the real-kernel endpoint poles and gives the exact integrals
     \(\Gamma_q^{\rm EEC}=\frac32C_F\),
     \(\Gamma_{g\to gg}^{\rm EEC}=\frac{14}{5}C_A\), and
     \(\Gamma_{g\to q\bar q}^{\rm EEC}=\frac15T_F\) per flavor.
19ba. A selected track-energy correlator is defined by a selector \(\tau\) on
      stable hadron species and the positive measure
      \(\mu_X^\tau=\sum_r\tau(a_r)p_r^0\delta_{\mathbf n_r}\).  Its
      two-point moments are \(e_\tau(X)^2\) and
      \(|\mathbf p_\tau(X)|^2\), and perturbative track-function
      bookkeeping follows the binomial collinear moment formula
      \(M_{i\to jk}^{(n)}(z)=\sum_a\binom{n}{a}
      z^a(1-z)^{n-a}M_j^{(a)}M_k^{(n-a)}\).
19bb. The small-angle light-ray OPE is now specified as a renormalized datum:
      a gauge-invariant light-ray operator space, operator coordinates,
      ultraviolet and rapidity subtraction schemes, mixing kernels, and
      coefficient distributions in \(\rho=1-\cos\chi\).  The separated real
      coefficient \(\Gamma_a^{\rm EEC}/\rho\) is promoted to a plus
      distribution plus a scheme-dependent \(\delta(\rho)\) contact term only
      after virtual terms and operator renormalization are declared in the
      same scheme.
19bba. The protected total-energy row in the small-angle EEC light-ray chart
       is now tied to the explicit one-loop timelike quark/gluon kernel.  With
       the trace-delta color factors and \(D_0=(1-x)^{-1}_+\), the first
       energy-fraction moment matrix is
       \(\begin{psmallmatrix}-4C_F/3&2N_fT_F/3\\4C_F/3&-2N_fT_F/3\end{psmallmatrix}\),
       so \((1\ 1)K=0\).  The plus prescription and the gluon
       \(\delta(1-x)\) coefficient are both load-bearing endpoint/contact
       ingredients in preserving detector normalization.
19bc. Endpoint resolution changes are distributional identities: for
      \(0<\rho_a<\rho_b\),
      \(D_{\rho_b}=D_{\rho_a}+\mathbf 1_{\rho_a<\rho<\rho_b}/\rho
      -\log(\rho_b/\rho_a)\delta(\rho)\).  Moving the boundary of the
      small-angle chart therefore shifts an ordinary separated-angle annulus
      into the compensating coincident-detector contact coordinate, preserving
      constant tests and making the contact convention checkable.
19bd. A finite small-angle light-ray calculation must specify the
      renormalized mixing chart, not only the anomalous-dimension matrix:
      regulated light-ray composites, the subtraction matrix \(Z\), the
      finite operator coordinates \(\mathbb O=Z^{-1}\mathbb O^{\rm reg}\),
      the paired coefficient row \(C=C^{\rm reg}Z\), the protected
      energy-moment row, and any finite scheme change \(R\).  The chart
      derives \(\gamma=Z^{-1}\mu dZ/d\mu\), \(\mu dC/d\mu=C\gamma\), and the
      transformed matrix
      \(\gamma'=R^{-1}\gamma R+R^{-1}\mu dR/d\mu\); a finite truncation is
      only a controlled approximation after a remainder functional for
      omitted light-ray operators is supplied.
19be. Solving the finite light-ray mixing problem means transporting the
      coefficient row and operator column by the same ordered matrix:
      \(\partial_tU=U\gamma\), \(C(t)=C(t_0)U\), and
      \(\mathbb O(t)=U^{-1}\mathbb O(t_0)\).  If a rapidity scale is also
      present, the ultraviolet and rapidity connections must satisfy
      \(\partial_t\eta-\partial_r\gamma+[\gamma,\eta]=0\) in the same
      endpoint scheme; nonzero curvature is an obstruction to
      path-independent endpoint coordinates unless additional operators or
      scheme-change walls are supplied.  In the minimal cusp-log block,
      \(\gamma_{\rm cusp}(t,r)=\Gamma_{\rm cusp}(t)rA\) forces
      \(\eta_{\rm cusp}=G_{\rm cusp}(t)A\) with
      \(G'_{\rm cusp}=\Gamma_{\rm cusp}\); the opposite rapidity sign gives
      curvature \(-2\Gamma_{\rm cusp}A\) in the chapter's operator convention.
19bf. A retained finite light-ray basis has its own projected curvature.  If
      the full ultraviolet/rapidity connection is flat and \(P_L\) projects to
      the retained labels, then the curvature computed from the retained block
      alone is
      \(\partial_t\eta_{LL}-\partial_r\gamma_{LL}+[\gamma_{LL},\eta_{LL}]
      =\eta_{LQ}\gamma_{QL}-\gamma_{LQ}\eta_{QL}\).  The right-hand side is
      the omitted-operator channel.  It must be bounded as a remainder or
      removed by enlarging the light-ray/contact-coordinate chart; finite
      retained coordinate changes conjugate this curvature and cannot erase it.
19bfa. The retained endpoint chart becomes an observable statement only after
       it is paired with detector tests.  For
       \(V_L(\varphi;t)=C_L(\varphi;t)O_L(t)+K_L(\varphi;t)\), the row-column
       anomalous-dimension terms cancel between \(C_L\) and \(O_L\), and the
       endpoint representative row \(D_L(\varphi;t)\) cancels only against the
       compensating contact derivative in \(K_L\).  The remaining variation is
       \(E_C(\varphi;t)O_L(t)+C_L(\varphi;t)E_O(t)+E_K(\varphi;t)\), with a
       finite detector-test norm bound.  Thus omitted light-ray channels,
       projected curvature, loop truncation, and endpoint matching defects must
       appear as residuals in the observable transport budget, not as invisible
       notation choices.
19bg. The EEC program is now organized by a proof-status ladder: detector
      measure/contact algebra, CFT fixed-point light-ray charts, QCD
      renormalized light-ray endpoint charts, perturbative endpoint
      mixing/factorization calculations, and final endpoint gluing to the full
      normalized detector observable.  The ladder states explicitly that exact
      detector identities, finite light-ray charts, tree-level endpoint
      coefficients, and cusp-log flatness checks are separate layers and do not
      by themselves prove the all-order light-ray OPE/mixing theorem or the full
      endpoint-matched EEC prediction.
19c. In the back-to-back endpoint, the impact-parameter factorization datum
     yields the leading fixed-coupling Sudakov factor
     \(W_{\rm LL}(b,Q)=W(b,\mu_b)
     \exp[-\Gamma_{\rm cusp}^qL_b^2/2]\), where
     \(L_b=\log(Q^2b^2/b_{\rm F}^2)\),
     \(b_{\rm F}=2e^{-\gamma_E}\), and
     \(\Gamma_{\rm cusp}^q=g^2C_F/(4\pi^2)+O(g^4)\) in the trace-delta
     convention.
19ca. A back-to-back endpoint formula contributes to a measured EEC only
      after it is turned into a tested recoil chart.  Angular tests pull back
      by \(\varphi_Q(q_T^2)=\varphi(-1+2q_T^2/Q^2)\), equivalently
      \(q_T^2=Q^2(1+\zeta)/2\); the open \(q_T>0\) recoil distribution is kept
      separate from the endpoint atom
      \(K_-^\tau\); and the large-\(b\) region must be supplied by a
      nonperturbative shape or fitted prescription, or counted as an
      excluded-bin residual.  The recoil error entering the measured EEC
      budget is therefore a sum of factorization, evolution/truncation,
      matching/overlap, large-\(b\), Glauber, and power terms, not merely the
      fixed-coupling cusp logarithm.
19d. With column-vector light-ray operators
     \(\mu\,d\mathbb O_A/d\mu=-\gamma_{AB}\otimes\mathbb O_B\), the
     coefficient distributions obey
     \(\mu\,dC_A/d\mu=C_B\otimes\gamma_{BA}\).  The energy-sum functional is
     a left null vector of the mixing kernels in a detector-normalized scheme,
     so RG evolution preserves the EEC zeroth moment while the declared
     contact convention fixes how weight is displayed at \(\rho=0\).
19e. Endpoint matching for the normalized EEC is a distributional gluing
     datum, not an additional physical observable.  After the bulk,
     small-angle, and back-to-back formulae are overlap-subtracted on
     \((-1,1)\), their moments \(I_0,I_1\) and the endpoint atoms
     \(K_+,K_-\) obey \(I_0+K_++K_-=1\) and \(I_1+K_+-K_-=0\).  If the
     coincident-detector contact coordinate \(K_+\) is fixed independently,
     these equations become a scheme-consistency test on the endpoint
     calculation.
19ea. The measured selected EEC is the hadronic observable
      \(\mathcal O_\tau[\varphi;Q]=\sum_XW_X(Q)\langle E_{2,X}^\tau,\varphi\rangle\).
      Its exact moment constraints are
      \(\mathcal O_\tau[1]=A_\tau=\sum_XW_Xe_\tau(X)^2\) and
      \(\mathcal O_\tau[\zeta]=B_\tau=\sum_XW_X|\mathbf p_\tau(X)|^2\).
      A perturbative prediction must assemble overlap-subtracted bulk,
      small-angle, and back-to-back charts, lift partonic coefficients by
      track or fragmentation data when \(\tau\ne1\), and choose endpoint atoms
      satisfying
      \(I_0^\tau+K_+^\tau+K_-^\tau=A_\tau\) and
      \(I_1^\tau+K_+^\tau-K_-^\tau=B_\tau\).  The residual budget separates
      open-chart errors, endpoint atom errors, and hadronization or
      shape-function effects.
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
22aa. The forward PDF light-ray definitions contain the local twist-two tower
      as their zero-separation Taylor coefficients after matching local and
      bilocal subtraction schemes.  With the chapter's non-centered bilocal
      convention, the quark \(N\)-th moment is represented by the left-endpoint
      operator
      \(\bar q(-i\overleftarrow D_n)^N\gamma\cdot n\,q\); the minus sign is
      fixed by the free-target phase \(\exp(i\lambda P\cdot n)\).  For the
      gluon PDF, the conventional \(1/x\) in the light-ray definition shifts
      the local derivative order to \(N-1\) for the \(N\)-th moment.  The
      symmetric traceless tensor tower is a change of local coordinates on the
      same leading-twist data, while off-forward total derivatives are kept in
      the GPD polynomiality discussion.
22ab. An integrated PDF is now defined as a renormalized light-ray
      matrix-element datum rather than as a probability density or parton
      counting function.  The datum includes the target hadron state, lightlike
      direction, Wilson-line geometry, finite regulator, convolutional
      subtraction map, factorization scale, and distribution space in \(x\)
      with endpoint contact conventions.  Support, positivity, probability
      interpretation, and appearance in DIS are later spectral or
      factorization claims, not part of the operator definition.
22b. The leading-order DGLAP kernels are written with the explicit
     \(D_0=(1-x)^{-1}_+\) distribution to avoid the ambiguous shorthand
     \((1+x^2)/(1-x)_+\).  With this convention the kernels obey quark-number
     and momentum-column sum rules exactly; the calculation is retained as a
     distributional check rather than theorem form.  The nonsinglet Mellin moment is
     \(C_F[-2H_{N-1}-1/N-1/(N+1)+3/2]\), giving the one-loop cusp coefficient
     \(g^2C_F/(4\pi^2)\) in the monograph trace normalization.
22bc. QCD factorization claims now pass through a common dependency ladder:
      exact color-singlet observable, gauge-invariant operator coordinate,
      subtraction and coefficient maps, dual scale transport, boundary or
      leading-region mechanism, power-remainder topology, and any regulator
      limit.  Compact DIS, Drell--Yan/TMD factorization, and small-\(x\)
      JIMWLK use different entries in this ladder, so finite checks of
      individual identities are explicitly inputs to, not replacements for,
      process-level factorization theorems.
22bd. The leading small-\(x\) inclusive-DIS dipole channel is now an
      instantiated measured-observable bridge rather than an abstract
      Wilson-line statement: the transverse/longitudinal photon wave-function
      weights define the tested bin, rapidity-separation cancellation is
      written as an equality between target JIMWLK evolution and projectile
      impact-factor subtraction, BK/JIMWLK errors are pushed through the same
      photon kernel, and endpoint/finite-\(Q\) tails remain declared
      remainders with explicit retained-bin estimates.  The small-\(x\)
      section now also carries point-of-use primary citations for the
      BFKL kernel/eigenvalue, virtual-photon dipole representation, Balitsky/BK
      hierarchy, and JIMWLK Wilson-line evolution.
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
22ccd. The CGC/JIMWLK layer is now formulated first as a finite compact
       Wilson-line rapidity-evolution datum on
       \(SU(N_c)^{\Lambda_\perp}\).  The weak observable equation and the
       strong density equation are related by Haar integration by parts, the
       divergence-form generator preserves total probability, and the dipole
       observable generates the first Balitsky-hierarchy equation before any
       BK product closure is imposed.  Removing the transverse and rapidity
       regulators remains the continuum theorem boundary.
22cce. The continuum JIMWLK theorem boundary is now sharpened as a projective
       Wilson-line state limit.  A successful limit must supply compatible
       cylinder representatives, state convergence, generator convergence,
       uniform rapidity control, closed positivity/Markov properties, and a
       process map with impact factors and power-remainder topology.  The
       displayed weak-equation error budget separates this projective theorem
       from the finite BK closure estimate, which controls only one projected
       dipole subsystem.
22ccf. The measured small-\(x\) prediction now has a separate observable-map
       budget.  The exact tested DIS, diffractive, or forward-production
       functional is compared with a Wilson-line coordinate only after
       impact-factor matching, rapidity subtraction, projective regulator
       removal, finite evolution/truncation, BK or moment-closure residuals,
       and power remainders are supplied in the same measurement topology.
       The companion finite check verifies the residual telescope and shows
       that dropping the impact-factor or closure entry under-budgets the
       example observable.
22cd. Drell--Yan is formulated as a timelike current-current Wightman tensor
      between two hadron states.  The leading-power kinematic variables obey
      \(x_Ax_B=Q^2/s\) and \(y=\frac12\log(x_A/x_B)\).  When the lepton-pair
      transverse momentum is integrated, the collinear factorized coordinate is
      a double convolution of two integrated PDFs with
      \(C^{DY}_{ij}\); in transform space the paired auxiliary-scale
      cancellation is
      \(\mu dC/d\mu=-P_A^T C-C P_B\), and finite PDF scheme changes require
      \(C'=(R_A^{-1})^T C R_B^{-1}\).  The Born measured-channel anchor now
      evaluates the virtual-photon coefficient
      \(C_{q\bar q}^{0}=4\pi\alpha_{\rm em}^2e_q^2
      (3N_cQ^2s)^{-1}\delta(1-z_A)\delta(1-z_B)\), including the \(1/s\)
      rapidity-bin Jacobian and the \(d\xi/\xi\) delta-kernel normalization,
      so the factorized coordinate reduces to the tested
      \(q\bar q+\bar q q\) PDF product before higher-order residuals are
      discussed.  The integrated theorem-boundary budget
      now tests the exact Wightman functional against compact \((Q^2,y)\)
      functions and separates leading-region, soft, Glauber, power, and
      regulator residuals in the dual test-function norm; RG covariance of the
      factorized coordinate does not bound these residuals.  The
      small-\(q_\perp\) TMD datum instead uses past-pointing staples,
      \(\zeta_A\zeta_B=Q^4\), a \(Y\)-term, a power-remainder topology, and an
      explicit Glauber item.  The finite Glauber lemma proves only the
      tensor-product unitarity identity
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
- 2026-05-30 issue #519 light-ray OPE bookkeeping pass: added the
  renormalized small-angle EEC endpoint datum, coefficient/operator RG
  consistency derivation, plus-distribution/contact-term convention, moment
  functional constraint, and
  `calculation-checks/energy_correlator_light_ray_ope_checks.py`.
- 2026-06-01 issue #519 endpoint-resolution pass: added the distributional
  identity relating two small-angle plus-prescription boundaries, the
  separated-annulus term, and the compensating \(\delta(\rho)\) contact shift;
  extended `calculation-checks/energy_correlator_light_ray_ope_checks.py`
  with exact rational checks of the identity on polynomial endpoint tests.
- 2026-06-01 issue #519 finite-light-ray-mixing pass: added the finite
  renormalized light-ray mixing chart for small-angle EEC, including
  \(Z^{-1}dZ\), coefficient/operator pairing, finite scheme-change covariance,
  protected moment-row bookkeeping, and a controlled truncation datum with an
  explicit omitted-operator remainder requirement; extended
  `calculation-checks/energy_correlator_light_ray_ope_checks.py` with exact
  rational matrix checks.
- 2026-06-02 issue #519 finite-transport pass: added the ordered transport
  and flatness consistency conditions for the finite small-angle light-ray
  mixing chart, including
  \(C(t)=C(t_0)U\), \(\mathbb O(t)=U^{-1}\mathbb O(t_0)\), the protected
  moment-row transport law, and the two-scale flatness condition
  \(\partial_t\eta-\partial_r\gamma+[\gamma,\eta]=0\); extended
  `calculation-checks/energy_correlator_light_ray_ope_checks.py` with exact
  nilpotent-matrix checks of transport invariance, derivative-term signs in
  the flatness equation, and curvature obstruction.
  The chapter now states explicitly that this is a structural chart
  consistency condition, not a concrete loop-level small-angle EEC flatness
  calculation in a specified rapidity scheme.
- 2026-06-02 anti-inflation follow-up: strengthened the same finite
  light-ray mixing paragraph so a finite retained basis must state the
  projected curvature, escaping curvature components, contact-coordinate
  compensations, and omitted-operator remainder.  This prevents the finite
  algebraic flatness check from being read as a scheme-specific QCD loop
  calculation.
- 2026-06-02 cusp-log flatness follow-up: added the minimal cusp-log
  rapidity chart
  \(\gamma_{\rm cusp}(t,r)=\Gamma_{\rm cusp}(t)rA\),
  \(\eta_{\rm cusp}=G_{\rm cusp}(t)A\), \(G'_{\rm cusp}=\Gamma_{\rm cusp}\),
  and the wrong-sign curvature obstruction \(-2\Gamma_{\rm cusp}A\);
  extended `calculation-checks/energy_correlator_light_ray_ope_checks.py` with
  exact rational checks of the derivative flatness and sign obstruction.
- 2026-06-02 projected-curvature follow-up: added the retained/omitted block
  identity
  \(\mathcal F_{LL}^{\rm trunc}=\eta_{LQ}\gamma_{QL}-\gamma_{LQ}\eta_{QL}\)
  for a finite small-angle light-ray basis.  The text now distinguishes a true
  two-scale inconsistency from curvature induced by omitted operator channels,
  records finite scheme covariance of the curvature, and requires either a
  remainder estimate or an enlarged light-ray/contact chart.  The companion
  script now checks the block identity and scale-dependent scheme covariance
  exactly over rational matrices.
- 2026-06-03 issue #519 endpoint-transport-budget pass: added the finite
  endpoint observable transport proposition for
  \(V_L(\varphi;t)=C_L(\varphi;t)O_L(t)+K_L(\varphi;t)\).  It proves that the
  coefficient/operator anomalous-dimension pieces and endpoint-representative
  row cancel only with the matching contact derivative, leaving a detector-test
  residual bound built from \(E_C,E_O,E_K\).  Extended
  `calculation-checks/energy_correlator_light_ray_ope_checks.py` with exact
  rational checks of the cancellation, the wrong-contact-sign defect, and the
  finite residual norm bound.
- 2026-05-31 issue #519 detector-algebra pass: added the outgoing
  direct-integral multiplication model for smeared energy detectors, including
  positivity, self-adjointness, Hamiltonian domain bounds, product domains,
  and the product-measure origin of diagonal contact terms; expanded
  `calculation-checks/energy_correlator_sum_rule_checks.py` to verify the
  finite-event detector-product algebra exactly.
- 2026-06-01 issue #519 endpoint-gluing pass: added the distributional
  endpoint matching ledger for the normalized EEC, solving the two exact
  detector moment equations for the contact and back-to-back endpoint atoms
  when they are left as matching coordinates, and extended
  `calculation-checks/energy_correlator_sum_rule_checks.py` to verify the
  finite rational endpoint-coordinate algebra.
- 2026-06-02 issue #519 connected/contact pass: inserted the detector-algebra
  distinction between ensemble-connected cumulants and coincident-detector
  contact strata.  The chapter now gives the partition formula for connected
  energy-correlator cumulants and the three-detector contact-stratum
  decomposition of the eventwise product measure; the finite-event companion
  script verifies that deterministic ensemble cumulants can vanish while
  diagonal detector contacts remain nonzero.
- 2026-06-02 issue #519 three-detector moment pass: added the ordered
  \(E_{3,X}(\zeta_{12},\zeta_{13},\zeta_{23})\) distribution, its unit
  total moment, its three vanishing pairwise angular moments in the
  center-of-mass frame, and its all-same and pair-contact diagonal strata.
  Extended `energy_correlator_sum_rule_checks.py` with exact rational checks
  of the three-detector moments and contact weights.
- 2026-06-03 issue #519 EEC multipole pass: added contact-inclusive
  Legendre-moment positivity for the eventwise EEC, deriving the spherical
  harmonic square formula, the \(\ell=1\) momentum-square reduction, and the
  \(\ell=2\) quadrupole norm.  Extended
  `energy_correlator_sum_rule_checks.py` with exact rational checks that the
  full detector measure has nonnegative \(M_0,M_1,M_2\), while deleting the
  coincident detector atom makes the first separated Legendre moment negative
  in a center-of-mass event.
- 2026-06-03 issue #519 architecture pass: added a proof-status ladder at the
  start of the light-ray endpoint subsection, separating detector
  measure/contact identities, CFT light-ray charts, QCD renormalized endpoint
  charts, perturbative mixing/factorization calculations, and endpoint gluing.
  The ladder records that the many finite detector and finite-chart checks are
  inputs to the modern EEC program rather than a substitute for the all-order
  light-ray OPE/mixing theorem or complete endpoint-matched prediction.
- 2026-06-04 issue #519 measured-EEC pass: added the observable-level
  prediction budget for full calorimetric and selected-track EECs, tying the
  exact hadronic detector definition to overlap-subtracted bulk, small-angle,
  and back-to-back charts, endpoint atoms, track or fragmentation inputs, and a
  residual functional separating perturbative, endpoint, and hadronization
  errors.  Extended `calculation-checks/energy_correlator_track_checks.py`
  with selected endpoint-atom gluing and measured-residual finite checks.
- 2026-06-04 issue #519 back-to-back recoil-budget pass: upgraded the
  Sudakov endpoint from a scoped leading-log display to a tested recoil chart
  feeding the measured-EEC budget.  The manuscript now states the
  \(q_T^2\)-test pullback, separates the open recoil integral from the
  endpoint atom \(K_-^\tau\), records the large-\(b\) nonperturbative
  boundary, and decomposes the recoil residual into factorization,
  evolution, matching, large-\(b\), Glauber, and power terms.  Extended
  `calculation-checks/energy_correlator_sudakov_checks.py` with exact checks
  of the pullback and a residual budget that fails if the large-\(b\)
  component is omitted.
- 2026-06-04 issue #748 recoil-normalization correction: restored the
  standard physical EEC back-to-back map \(z=(1-\zeta)/2\) and
  \(1-z=q_T^2/Q^2\), replacing the previous missing-half pullback by
  \(\zeta=-1+2q_T^2/Q^2\) and recording the induced
  \(\dd\sigma/\dd\zeta=(Q^2/2)\dd\sigma/\dd q_T^2\) Jacobian.  The Sudakov
  companion now derives the pullback from the independent \(z\) and recoil
  definitions and includes a negative control for the old no-half map.
- 2026-06-04 issue #519 timelike-momentum pass: added
  `prop:qcd-eec-timelike-momentum-sum-rule`, making the protected
  total-energy row in the small-angle EEC light-ray chart concrete at one
  loop.  The text computes the first energy moments of the timelike
  quark-singlet/gluon kernel, including the plus-prescribed quark pole and
  the gluon \(\delta(1-x)\) coefficient, and obtains the matrix
  \(\begin{psmallmatrix}-4C_F/3&2N_fT_F/3\\4C_F/3&-2N_fT_F/3\end{psmallmatrix}\)
  with vanishing column sums.  The EEC light-ray companion now checks the
  rational first moments for several \(SU(N_c)\) and \(N_f\) choices and
  includes negative controls for omitting the gluon endpoint delta or the
  quark plus prescription.
- 2026-06-02 issue #519 track-energy pass: added selected calorimetric
  measures for track and charged-energy correlators, derived the selected EEC
  moment identities, introduced track functions as nonperturbative
  factorization data for selected-energy fractions, and derived the binomial
  collinear moment ledger plus contact/separated two-detector weights.  Added
  `calculation-checks/energy_correlator_track_checks.py` to verify the exact
  finite selected-measure and track-function arithmetic.
- 2026-05-29 continuing anti-wrapper audit: demoted the eventwise EEC
  sum-rule proposition to detector-observable prose.  The identities remain
  exact and nonperturbative, but their derivation is energy-momentum
  conservation plus the definition of the calorimetric distribution.
- 2026-05-28 issue #630 small-\(x\) pass: added the regulated dipole datum,
  gauge-invariance proof, leading-logarithmic BFKL/BK status statement,
  transverse kernel covariance proof, Mellin-eigenvalue derivation by analytic
  regularization, and `calculation-checks/qcd_bfkl_small_x_checks.py`.
- 2026-05-31 issue #630 CGC/JIMWLK theorem-boundary pass: added the finite
  Wilson-line rapidity-evolution datum on a compact product of \(SU(N_c)\)
  variables, the weak/strong Fokker--Planck duality by Haar integration by
  parts, probability conservation, the Balitsky-hierarchy interpretation of
  the dipole observable, and finite compact-diffusion checks in
  `calculation-checks/qcd_bfkl_small_x_checks.py`.
- 2026-06-01 issue #630 BK-closure boundary pass: inserted the finite dipole
  projection between the Wilson-line diffusion and the continuum BK equation,
  defined the connected double-dipole closure coordinate
  \(E_{\mathbf x\mathbf y}^{\rm BK}\), derived the finite \(S\)- and
  \(N\)-variable closed BK equations only after the decorrelation input, and
  added the explicit \(d(Y)\le \int_0^Y e^{3L(Y-s)}\varepsilon(s)\,ds\)
  finite Gronwall estimate.  The paired script
  `calculation-checks/qcd_bfkl_small_x_checks.py` now verifies the exact
  closure algebra, fixed points, unit-cube inward boundary, and \(3L\)
  Lipschitz ledger.
- 2026-06-03 issue #630 continuum JIMWLK projective-limit pass: inserted the
  projective Wilson-line state convergence package for removing the transverse
  regulator from finite compact-manifold JIMWLK.  The chapter now requires
  compatible cylinder representatives, state and generator convergence,
  uniform rapidity control, positivity/Markov closure, and a factorization map
  to measured small-\(x\) observables, with an explicit weak-equation residual
  budget.  The paired script
  `calculation-checks/qcd_bfkl_small_x_checks.py` now checks the finite-step
  residual inequality, a vanishing projective error schedule, and the
  obstruction from a nonzero generator error.
- 2026-06-04 issue #630 measured small-\(x\) observable-map pass: added the
  impact-factor/process bridge from the projective Wilson-line state to exact
  tested DIS, diffractive, and forward-production functionals.  The new
  residual budget separates impact-factor matching, rapidity subtraction,
  projective regulator removal, finite evolution/truncation, BK or
  moment-closure residuals, and power remainders.  The paired
  `calculation-checks/qcd_bfkl_small_x_checks.py` exact example checks the
  telescope and includes negative controls for omitted impact-factor and
  closure entries.
- 2026-06-04 issue #630 leading inclusive-DIS dipole continuation: instantiated
  the measured small-\(x\) bridge for the virtual-photon channel, including
  transverse and longitudinal \(q\bar q\) wave-function weights, the
  photon-kernel convolution defining the tested bin, the rapidity-separation
  cancellation equation, BK/JIMWLK error propagation through the measured
  kernel, and endpoint/finite-\(Q\) retained-bin estimates.  The companion
  `calculation-checks/qcd_bfkl_small_x_checks.py` now verifies the kernel
  symmetries, photon-weighted BK error image, rapidity-subtraction sign, and
  endpoint spin-factor primitives, so this pass is a physical DIS-channel
  instantiation rather than another abstract residual ledger.  The same pass
  added point-of-use primary references for BFKL, virtual-photon dipole DIS,
  Balitsky/BK evolution, and the JIMWLK Wilson renormalization group.
- 2026-05-28 issue #630 Drell--Yan/Glauber pass: added the Drell--Yan
  hadronic tensor, leading-power kinematics, TMD factorization datum with
  past-pointing staples, finite tensor-product unitarity lemma for the
  algebraic content of Glauber cancellation, and
  `calculation-checks/qcd_drell_yan_glauber_checks.py`.  The 2026-06-03
  integrated-factorization continuation inserted the two-PDF collinear
  factorization coordinate for \(d\sigma/dQ^2dy\), separated it from the
  small-\(q_\perp\) TMD formula, and extended the companion check with exact
  transform-space RG-cancellation and finite scheme-covariance tests.  The
  2026-06-04 theorem-boundary continuation added a tested residual budget
  between the exact Wightman functional and the factorized coordinate,
  separating leading-region, soft, Glauber, power, and regulator residuals; the
  companion check keeps the residual nonzero while verifying that exact
  RG-covariance of the factorized coordinate does not erase it.
  The 2026-06-04 inclusive-projection continuation makes the Glauber residual
  operational: after the regulated eikonal action is identified, the tested
  color-singlet observable must either commute with the unobserved Glauber
  unitary or leave a norm-bounded commutator residual.  The paired check adds a
  negative control in which a spectator-resolving measurement gives a nonzero
  but bounded residual.  The 2026-06-04 Born measured-channel continuation
  adds `prop:qcd-drell-yan-born-rapidity-bin`, deriving the virtual-photon
  rapidity-bin coefficient, the \(1/s\) Jacobian from
  \((\xi_A,\xi_B)\mapsto(Q^2,y)\), and the convolution identity
  \(\int_x^1 d\xi\,f(\xi)\xi^{-1}\delta(1-x/\xi)=f(x)\).  The companion check
  adds exact symbolic tests and negative controls for omitting the Jacobian or
  using the wrong delta-kernel normalization.
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
- 2026-06-02 issue #630 conformal-window rigor pass: added the controlled
  Banks--Zaks status datum distinguishing the perturbative small-coupling
  fixed-point expansion from a nonperturbative theorem about the conformal
  window.  Extended the exact Banks--Zaks check to verify the two-loop
  derivative \(-2B_0^2/B_1\) at the zero and its IR-attractive sign.
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
- 2026-06-02 issue #630 PDF datum boundary pass: inserted
  Definition~\(\ref{def:qcd-renormalized-integrated-pdf-datum}\), making the
  integrated PDF a renormalized Wilson-line light-ray matrix-element datum
  with target state, lightlike direction, Wilson-line geometry, finite
  regulator, subtraction map, factorization scale, and distribution topology
  fixed.  The pass separates this definition from support, positivity,
  probability language, and factorized appearance in DIS, which remain
  additional spectral/factorization statements.
- 2026-06-01 issue #630 PDF moment pass: added the local-moment extraction
  from the Wilson-line light-ray definitions, including the left-endpoint
  \(-i\overleftarrow D_n\) sign convention, the gluon \(1/x\) moment-index
  shift, and a paired exact phase-normalization check in
  `calculation-checks/qcd_dglap_checks.py`.
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
- 2026-05-29 continuing anti-wrapper audit: demoted the quarkonium
  fine/hyperfine spin algebra and the linear elastic pole-coordinate
  calculation from proposition form to worked prose.  The formulas remain
  because they fix spectroscopy coordinates, but the proofs are finite
  angular-momentum algebra and a one-complex-variable linearization rather
  than theorem-level QFT arguments.
- 2026-05-29 seventh anti-wrapper pass: demoted the pseudoscalar-meson--baryon
  partial-wave \(J^P\) rule to representation-theory prose and expanded the
  smeared energy-flow continuity estimate so the soft and collinear bounds are
  stated as continuity of finite-energy calorimetric measures.
- 2026-06-01 anti-wrapper follow-up: demoted the smeared energy-flow
  soft/collinear continuity estimate from lemma/proof form to worked prose.
  The finite-measure and Lipschitz bounds remain because they fix the exact
  sense in which energy-correlator observables are continuous under soft
  additions and collinear recombinations, but the calculation is not a
  theorem-family result.
- 2026-06-02 anti-wrapper follow-up: demoted the antisymmetric \(k\)-string
  Casimir ratio from lemma/proof form to trace-normalization prose.  The
  Fierz calculation remains in the QCD-string section because it fixes the
  trace-delta convention behind the comparison function
  \(R_k^{\rm Casimir}\), but the argument is finite representation algebra,
  not a standalone QFT theorem.
- 2026-05-30 quoted-theorem pass: replaced the leading ERBL diagonalization
  quoted theorem by a proved proposition.  The pass corrected the eigenvalue
  normalization for the kernel as written:
  \(\int V\varphi_n=-(\gamma_n^{(0)}/2)\varphi_n\), so the Gegenbauer
  moment equation uses \(\alpha_s/(4\pi)\gamma_n^{(0)}\).  The manuscript now
  displays the finite plus-prescribed polynomial action and the coefficient
  reduction to the Gegenbauer recurrence; `qcd_exclusive_pion_checks.py`
  now verifies the exact kernel eigenvalue through the rational polynomial
  action rather than checking only anomalous-dimension signs.
- 2026-05-30 general-method placement pass: removed the local GEVP
  basis-covariance proof from the QCD spectroscopy discussion and redirected
  it to the general finite-volume correlator-matrix section in Volume XI.
  The QCD chapter now keeps only the QCD-specific content: interpolating
  operator-source families, source-subspace interpretation, finite-volume
  scattering map, and continuum/chiral/heavy-quark/infinite-volume
  extrapolation data.  The spectroscopy wording avoids overloading the
  separate contact-term/source-coordinate notion of a source-coordinate system.
- 2026-05-30 figure semantic audit: corrected the DIS light-ray factorization
  figure so the gauge transporter is the open Wilson segment
  \(W[\lambda n,0]\).  The caption now states explicitly that this segment
  makes the bilocal quark operator gauge invariant.
- 2026-05-30 specialized-method cleanup follow-up: verified that the QCD
  spectroscopy section itself no longer exposes the finite-volume
  correlator-matrix/GEVP machinery.  The chapter now keeps only the
  QCD-specific operator families, finite-volume energies, stable-mass or
  sheet-labeled pole outputs, and source-overlap coordinate status.  Mentions
  of GEVP-style analysis were removed from the light-meson, baryon-resonance,
  and spectroscopy-hierarchy paragraphs so that general numerical machinery is
  not taught inside a specialized QCD discussion without a concrete extracted
  QCD result.
- 2026-05-31 structural navigation pass for issue #706: introduced
  substance-aligned subsection anchors in the long QCD blocks without changing
  formulae.  The new anchors separate the background-field beta-function
  ledger, large-\(N_c\) planar/volume-reduction/baryon material, spectroscopy
  finite-volume and pole-coordinate material, light-meson Roy/Roy--Steiner
  material, current-matrix-element material, integrated PDF/light-ray
  definitions, DIS factorization/DGLAP evolution, and exclusive-pion
  light-ray/ERBL/form-factor material.  A line-count audit now gives at least
  three subsections in every section of this chapter longer than 500 source
  lines; this is a navigational repair, not a claim that QCD depth-pass-B is
  complete.
- 2026-06-02 issue #630 operator-RG convention pass: replaced the ambiguous
  "bare light-ray operator" wording by a finite-regulator light-ray operator
  coordinate \(\mathbb O_a^\Lambda\), separated regularization from
  renormalization in the convolutional coordinate map, derived DGLAP as the
  infinitesimal RG equation of the renormalized Wilson-line light-ray
  operator coordinates, and wrote the DIS coefficient RG equation as the
  dual cancellation condition.  `calculation-checks/qcd_dglap_checks.py`
  now includes a rational finite-channel check of \(df=P f\), \(dC=-CP\),
  and \(d(Cf)=0\).
- 2026-06-03 issue #630 factorization-architecture pass: inserted the common
  QCD factorization dependency ladder before the DIS hypothesis, organizing
  compact DIS, TMD/Drell--Yan, and small-\(x\)/JIMWLK claims as process
  comparisons from exact color-singlet observables to factorized coordinates
  with named operator, subtraction, coefficient, scale-transport, boundary,
  remainder, and limiting errors.  `calculation-checks/qcd_dglap_checks.py`
  now verifies the finite additive budget and detects omitted boundary,
  Glauber, and projective-state terms.
- 2026-06-03 style-density follow-up for issue #726: changed the integrated
  PDF definition heading and opening sentence from repeated "datum" language
  to "coordinate" language.  Labels and mathematical content were left
  unchanged; the change only reduces internal-process diction in the
  reader-facing PDF section.
- 2026-06-04 issue #630 large-\(N_c\) rigor-boundary pass: added
  `ca:qcd-large-n-genus-truncation-remainder-bound`, which upgrades the planar
  counting section from fixed-ribbon graph power counting to an operational
  criterion for a quoted large-\(N_c\) observable approximation.  The new block
  requires coefficient bounds, a genus-tail bound, and uniform regulator or
  limit-interchange control before planar dominance, volume reduction, baryon
  scaling, or QCD-string language is treated as a nonperturbative statement.
  `large_n_topology_checks.py` now verifies a finite genus-truncation
  bound and an order-of-limits negative control.
- 2026-06-04 issue #832 factorization-ledger source pass: the Ch.~19 DIS
  light-ray figure and `eq:qcd-common-factorization-budget` are now explicit
  ledger occurrences in Ch.~19b.  The figure is grouped as operator-coordinate
  source evidence for DIS, while the common budget is recorded as comparison
  architecture rather than a theorem for a single process.

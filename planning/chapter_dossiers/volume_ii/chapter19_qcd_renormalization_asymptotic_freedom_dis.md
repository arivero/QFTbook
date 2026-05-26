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
- multipoint jet energy correlators and energy-flow polynomials as polynomial
  functionals of calorimetric data;
- DIS kinematics, inclusive final-state sums, the leading electromagnetic
  amplitude, the non-time-ordered hadronic tensor, the current-conservation
  tensor decomposition, support in \(x_B\), the discontinuity of the
  time-ordered forward Compton amplitude, twist-two operators, Wilson lines,
  factorization assumptions, the replacement of abelian Bloch--Nordsieck
  cancellation by nonabelian PDF renormalization for incoming colored
  partons, and logarithmic scaling violation.

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
   coupling held fixed is \(\lambda=g^2N_c\), equal to twice the common
   half-trace 't Hooft coupling.  The leading color-flow propagator and the
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
23. Physical QCD asymptotic completeness remains an open large-time problem:
    one must construct wave operators from stable color-singlet asymptotic
    spaces, treat resonances through analytic scattering data, include
    massless Goldstone modes when chiral limits are taken, and prove that
    detector observables such as energy flow are limits on the same scattering
    domain.

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
- 2026-05-26 issue #519 pass: added the eventwise EEC sum-rule proposition
  and exact finite-event calculation check for zeroth moment, first moment,
  and contact weight.
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

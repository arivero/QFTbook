# Volume II, Chapter 19 Dossier: QCD Renormalization, Asymptotic Freedom, And DIS

## Source Position

- Primary local source: second-sequence handwritten material, pages 182--210.
- Immediate predecessor: gauge fixing, ghosts, and BRST cohomology.
- Immediate successor in the source order: anomalies and chiral symmetry.
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

## Construction Task

The chapter must define and derive:

- QCD fields \(q^i_{I\alpha}\), color/flavor/spinor indices, and the
  \(SU(N_c)\) group constants \(C_A,T_R,C_R,T_F,C_F\);
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
  \(\beta(g)=-g^3(11C_A/3-4T_RN_f/3)/(16\pi^2)+O(g^5)\);
- dimensional transmutation and the perturbative domain of the one-loop
  running coupling;
- the two-loop Banks--Zaks alternative as a perturbative infrared fixed-point
  diagnostic, with its controlled domain stated;
- Wilson lines, open gauge-invariant quark-antiquark operators, rectangular
  Wilson loops, static potentials, and the distinction between pure
  Yang--Mills area-law diagnostics and QCD with dynamical fundamental quarks;
- the distinction between colored gauge-fixed fields and physical external
  states in QCD;
- DIS kinematics, inclusive final-state sums, the leading electromagnetic
  amplitude, the non-time-ordered hadronic tensor, the current-conservation
  tensor decomposition, support in \(x_B\), the discontinuity of the
  time-ordered forward Compton amplitude, twist-two operators, Wilson lines,
  factorization assumptions, and logarithmic scaling violation.

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
   ordinary low-flavor QCD.
9. A rectangular Euclidean Wilson loop extracts the static potential between
   external color sources; an area law in pure Yang--Mills is a confinement
   diagnostic, while dynamical fundamental matter can break the flux tube.
10. Colored quark and gluon fields are not physical asymptotic states of QCD;
   physical scattering statements must be formulated in terms of gauge-invariant
   states or controlled high-energy factorization data.
11. DIS is controlled by an inclusive Wightman current-current tensor; the
    time-ordered forward Compton amplitude supplies its discontinuity, and the
    short-distance OPE applies to the time-ordered product before analytic
    continuation to the physical inclusive tensor.
12. The leading-twist local operators and the gauge-invariant light-ray
    operators are two presentations of the same short-distance data; asymptotic
    freedom changes Bjorken scaling into logarithmic scaling violation governed
    by anomalous dimensions.

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

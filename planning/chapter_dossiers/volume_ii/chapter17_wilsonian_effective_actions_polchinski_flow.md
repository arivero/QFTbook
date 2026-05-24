# Volume II, Chapter 17 Dossier: Wilsonian Effective Actions And Polchinski Flow

## Source Position

- Primary local source: second-sequence handwritten material, pages 147--156.
- Immediate predecessor: statistical Ising model, scaling limits, and
  universality.
- Immediate successor in the source order: Yang-Mills theory and matter
  fields.
- Role in the monograph: construct the Wilsonian effective action with a
  smooth floating cutoff, derive the shell-integration identity and its
  infinitesimal Wilson-Polchinski form, then reinterpret perturbative
  renormalizability as the existence of a controlled continuum limit in
  Wilsonian coupling space.

## Source And Reference Controls

- `SRC-QFT-PDF`: `references/253b lecture notes 2023.pdf`, pages 147--156;
  checked against rendered page images in
  `monograph/tex/build/source_visual_trace/`.
- `SRC-BEN-COMPARISON`: `references/253b transcribed lecture notes.tex`,
  corresponding Wilsonian/Polchinski section, used only as a comparison layer.
- `SRC-EXTERNAL`: Polchinski's 1984 effective-Lagrangian paper and Rosten's
  exact-RG review, used only to guard terminology and theorem boundaries.  The
  chapter follows the local logical order and conventions.
- `SRC-EXTERNAL-BOUNDS`: Polchinski's smooth-cutoff perturbative
  renormalizability argument, Salmhofer's rigorous RG framework, and
  Brydges--Kennedy tree/Mayer expansion technology, together with
  Glimm--Jaffe's constructive scalar-field framework, used to separate proved
  perturbative or constructive estimates from assumptions in the local
  finite-coordinate continuum-limit theorem.
- `SRC-AUDIT`: page-level source and figure audit completed on 2026-05-22 in
  `planning/build_audits/2026-05-22_wilsonian_effective_actions_source_figures.md`.

## Construction Task

The chapter must define and derive:

- Euclidean scalar Wilsonian action
  \(S_\Lambda=S_{\mathrm{kin},\Lambda}+L_\Lambda\) with a smooth UV cutoff;
- cutoff profile \(\chi(t)\), \(\chi_\Lambda(k)=\chi(k^2/\Lambda^2)\), and
  regulated propagator \(C_\Lambda(k)\);
- the general momentum-space expansion of \(L_\Lambda[\phi]\);
- the source-supported generating functional condition
  \(Z_{\Lambda'}[J]=Z_\Lambda[J]\) for \(\widetilde J\) supported below
  \(\Lambda'\);
- the propagator decomposition
  \(C_\Lambda=C_{\Lambda'}+\widehat C_{\Lambda,\Lambda'}\);
- the finite-regulator Gaussian pushforward proposition and its proof by
  characteristic functions of independent Gaussian random variables;
- the separate continuum Wilsonian pushforward hypothesis, distinguishing
  convergence of the interacting source functional from convergence of the
  pushforward or infinitesimal Wilson-Polchinski flow;
- the Gaussian field split \(\phi=\phi'+\phi_{\mathrm{sh}}\), including the
  shell kinetic term, and the notation convention that hats are reserved for
  covariance differences such as \(\widehat C_{\Lambda,\Lambda'}\), not for
  shell fields;
- the shell-integration formula defining \(L_{\Lambda'}[\phi']\);
- the infinitesimal Wilson-Polchinski equation, with functional-derivative
  conventions;
- the field-independent Gaussian normalization as the vacuum-energy
  coordinate: it may be fixed separately, and the displayed Polchinski
  equation is the interaction flow modulo that constant because functional
  derivatives annihilate it;
- the analytic status of the Wilson-Polchinski equation in three nested
  settings:
  finite-regulator \(C^2\) functions on a finite-dimensional mode space, the
  Fr\'echet coefficient topology on smooth vertex kernels, and a weighted
  Banach RG chart \(\mathcal B_{\Lambda}^{m,a}\) for theorem-level estimates;
- the notion of solution in each setting: ordinary finite-regulator
  \(C^1\)-in-\(\Lambda\) solution, coefficientwise formal perturbative
  solution, and Banach-norm solution after identifying scales by
  dimensionless momenta;
- the finite-shell derivation of the Wilson-Polchinski sign from
  \(\Lambda'=\Lambda-\delta\Lambda\);
- the diagrammatic meaning of its two terms: connecting two vertices and
  contracting two legs at one vertex;
- the linearized scaling-coordinate convention
  \(\dd u_\alpha/\dd\log\Lambda=-y_\alpha u_\alpha+\cdots\), with
  \(y_\alpha=D-\Delta_\alpha\);
- the sign bridge to the earlier 1PI thermal coordinate:
  \(\dd\tau/\dd\log\mu=-y_t\tau+\cdots\) uses the same increasing-scale
  convention, while the infrared-oriented variables
  \(s_{\rm W}=\log(\Lambda_0/\Lambda)\) and
  \(s_{\rm 1PI}=\log(\mu_0/\mu)\) both reverse the sign, so positive relevance
  exponents grow toward the infrared after the Wilsonian--1PI matching map is
  specified;
- the fact that a codimension statement about a critical surface requires a
  specified \(C^k\) Banach RG chart and a differentiable endpoint map, not
  merely the linearized eigenvalue calculation;
- the finite-reference critical-surface theorem: if the relevant-coordinate
  endpoint map is \(C^k\) and its derivative in the relevant block is
  invertible, its zero set is a \(C^k\) embedded Banach submanifold of
  codimension equal to the number of relevant coordinates;
- the \(D=4\) massless scalar toy truncation
  \(L_\Lambda=\int(g_4\phi^4+g_6\phi^6)\), with
  \(\lambda_4=g_4\), \(\lambda_6=\Lambda^2g_6\);
- the beta-function convention
  \(\beta_A=\Lambda\,\dd\lambda_A/\dd\Lambda\) for projected Wilsonian
  coordinates;
- the two-coupling Wilsonian flow, the transverse coordinate
  \(h=\lambda_6+\frac b2\lambda_4^2\), and its canonical suppression
  \(h(\Lambda)=h(\Lambda_*)(\Lambda/\Lambda_*)^2+\cdots\) toward the IR;
- the induced beta function for the retained marginal coordinate after
  irrelevant couplings are eliminated along the RG trajectory, with a clear
  warning that comparison to a 1PI beta function requires a coordinate
  redefinition;
- the Wilsonian formulation of perturbative renormalizability as the existence
  of a \(\Lambda_0\to\infty\) limit after tuning bare couplings to hold
  physical coordinates fixed at \(\Lambda_R\);
- the explicit continuum-limit estimate showing that the memory of
  \(\lambda_6(\Lambda_0)=0\) is suppressed by
  \((\Lambda_R/\Lambda_0)^2\);
- the limitation that this perturbative finite-coordinate estimate is not a
  constructive existence theorem for non-Gaussian four-dimensional
  \(\lambda\phi^4\) scaling limits, in view of the known triviality theorem
  for the specified positive lattice scalar and nearest-neighbor
  ferromagnetic Ising-type families;
- a conditional finite-coordinate Wilsonian continuum-limit theorem for a split
  \(z=(u,v)\) into retained renormalized coordinates and irrelevant
  coordinates, including:
  - the projected flow
    \(\dd u/\dd t=B(u,v)\),
    \(\dd v/\dd t=Av+F(u,v)\);
  - the backward semigroup bound
    \(\|e^{A\tau}\|\le C_A e^{\omega\tau}\) for \(\tau\le0\);
  - the variation-of-constants formula separating direct irrelevant
    boundary memory from the generated integral;
  - the finite-coordinate continuum graph
    \(v=V_R(u_R)\) at the reference scale when the generated integral
    converges after tuning \(u(t_R)=u_R\);
  - the existence of the retained-coordinate limit
    \[
      z_R(t_0;u_R)\to (u_R,V_R(u_R))
    \]
    after tuning the relevant coordinates at \(\Lambda_R\);
  - the estimate
    \(v(t_R)=V_R(u_R)
      +O((\Lambda_R/\Lambda_0)^{\min(\omega,\omega_F)})\), where
    \(\omega_F\) is the convergence rate of the generated-integral
    remainder;
  - convergence of every continuous finite-coordinate observable or projected
    low-momentum kernel functional \(Q(z_R)\), with the same power bound when
    \(Q\) is Lipschitz;
  - an explicit status paragraph that the estimate is conditional: the
    irrelevant semigroup bound and the uniform generated-integral convergence
    must be proved in a chosen normed Wilsonian setting, and are not supplied
    by the finite-coordinate algebra alone;
  - a comparison with proved results: Polchinski gives order-by-order
    perturbative cutoff-control after fixing relevant parts, Salmhofer gives
    rigorous RG estimates in specified small-coupling settings, and
    Brydges--Kennedy supplies iterative expansion technology for constructive
    applications, and Glimm--Jaffe-type constructions give non-Gaussian
    \(\phi^4_2/\phi^4_3\) examples under their own hypotheses, while
    nonperturbative continuum existence remains model-dependent;
- the role of finite dimensionless irrelevant bare couplings in lattice
  regularizations.
- the bridge to BPHZ and 1PI coordinates: finite-regulator equality of
  low-source connected functionals, Legendre transform to 1PI kernels, finite
  matching from Wilsonian local coordinates to 1PI subtraction coordinates,
  and the distinction between a Wilsonian vertex and a 1PI vertex.
- a finite-order BPHZ--Wilsonian matching theorem that:
  - fixes a BPHZ forest-formula scheme, a low source/classical-field test
    space, finite 1PI projectors, and finite Wilsonian coordinate projectors;
  - defines the matching map
    \(M_I^{(\ell,N)}(u;\Lambda,\mu,\mathfrak b)
      =\Pi_I\Gamma^{<,(\le\ell)}_{\Lambda,N}[u]\);
  - proves the finite-dimensional low-mode Legendre-transform step from
    equality of connected functionals and Hessian invertibility;
  - proves a Wilsonian Taylor-remainder lemma giving
    \(O((\mu/\Lambda)^{p_N})\) suppression from the chosen Banach norm and
    the first omitted excess scaling exponent;
  - obtains the finite coordinate change by the finite-dimensional implicit
    function theorem when the selected Jacobian is invertible;
  - states the fixed-loop perturbative scope and separates massive BPHZ,
    BPHZL, and dimensional-regularization/MS coordinate systems.
- a one-loop quartic scalar matching calculation that:
  - splits the regulated bubble into low-low, high-high, and mixed covariance
    assignments;
  - identifies the high-high part as the Wilsonian quartic vertex correction;
  - identifies the low-low part as the remaining low-field 1PI loop;
  - treats the mixed part as local matching data and omitted irrelevant
    coordinates in the low-momentum derivative expansion;
  - writes the BPHZ-subtracted 1PI four-point kernel and the matching map
    from \(u_4(\Lambda;\mathcal S_\mu)\) to \(g(\mu)\).

## Claim Ledger

1. A Wilsonian effective action at scale \(\Lambda\) is a cutoff-dependent
   functional whose low-momentum generating functional is held fixed.
2. The smooth cutoff can be placed in the quadratic kernel, giving a regulated
   Gaussian covariance and a general local interaction functional.
3. Lowering \(\Lambda\) is represented exactly, at the formal path-integral
   level, by a decomposition of Gaussian covariance and integration over an
   independent shell field.
3a. The Gaussian pushforward is a finite-regulator theorem about Gaussian
    measures on finite-dimensional vector spaces.  A nonperturbative continuum
    Wilsonian flow additionally requires convergence of the interacting
    source functionals and convergence of the pushforward or vector field in a
    specified topology.
3b. The \(\phi\)-independent normalization in the shell Gaussian integral is
    the vacuum-energy coordinate.  Retaining it adds only
    \(\Lambda\partial_\Lambda c_\Lambda\) to the left side of the flow; the
    functional derivatives in the Polchinski equation annihilate it, so the
    displayed interaction equation is written modulo this constant.
4. Before the shell source term is discarded, the split generating functional
   contains \(J(\phi'+\phi_{\mathrm{sh}})\); the
   \(J\phi_{\mathrm{sh}}\) term vanishes only by the regulated support
   assumption on the source.
5. The infinitesimal shell-integration identity gives a functional differential
   equation for \(L_\Lambda\).
5a. The Wilson-Polchinski equation has a stated topology only after choosing
    its setting.  At finite regulator the derivative is an ordinary derivative
    of \(C^2\) functions on a finite mode space; in perturbation theory it is
    coefficientwise in the Fr\'echet topology of smooth vertex kernels; in a
    theorem-level RG argument it is a Banach-space vector-field equation in a
    specified weighted norm.
6. Locality of the Wilsonian action is a derivative expansion assumption tied
   to smooth cutoffs and scales below the cutoff, not a finite-operator
   ansatz.
7. With \(t=\log\Lambda\), relevance exponents obey
   \(\dd u/\dd t=-yu+\cdots\); positive \(y\) grows toward the infrared, while
   negative \(y\) is irrelevant.  This is the same increasing-scale sign
   convention as the Wilson--Fisher 1PI equation
   \(\dd\tau/\dd\log\mu=-y_t\tau+\cdots\); with IR-oriented variables
   \(s_{\rm W}\) and \(s_{\rm 1PI}\), both equations acquire \(+y\) linear
   terms.
7a. A smooth codimension statement about a critical surface is certified only
    after choosing a \(C^k\) Banach or finite-dimensional RG chart and proving
    the endpoint-map submersion condition.  Linearized relevant eigenvalues
    identify the candidate tuning directions; they do not prove nonlinear
    manifold structure.
8. In the quartic-sextic toy truncation, the irrelevant coupling approaches a
   cutoff-dependent function of the marginal coupling along IR flow; the
   transverse memory of the ultraviolet boundary condition is suppressed by
   the canonical irrelevant power.
9. Perturbative renormalizability is formulated by a limiting procedure:
   remove the UV cutoff while tuning bare couplings so selected physical
   couplings at a fixed reference scale remain fixed.
10. The perturbative argument requires explicit hypotheses on small couplings,
   mild beta-function variation, and control of omitted irrelevant operators.
10a. In four-dimensional scalar \(\lambda\phi^4\), these hypotheses must be
     distinguished from the known constructive result that the standard
     positive lattice scalar and nearest-neighbor ferromagnetic Ising-type
     critical scaling limits are Gaussian; the Wilsonian estimate explains
     local perturbative suppression of irrelevant boundary data but does not
     prove a non-Gaussian continuum scalar theory.
11. Lattice QFT fits the same logic because finite dimensionless irrelevant
   lattice couplings correspond to dimensionful coefficients suppressed by
   powers of the UV cutoff.
12. In a finite local projection, cutoff removal separates into two estimates:
    direct memory of irrelevant bare coordinates is power-suppressed by the
    irrelevant semigroup, and the continuum graph is selected by the generated
    integral after retained coordinates are tuned.
12a. The generated-integral convergence hypothesis is stronger than formal
     perturbative coefficientwise existence.  Renormalon diagnostics identify
     particular ways in which momentum-region integrations can create
     factorial perturbative growth and require nonperturbative/OPE/effective
     matching data.
12b. The finite-coordinate continuum-limit theorem is a conditional existence
     theorem for the retained-coordinate limit at \(\Lambda_R\).  Its
     semigroup and generated-integral hypotheses are analytic inputs.  At
     fixed perturbative order or in constructive models they must be replaced
     by proved bounds in a specified Banach/normed setting; in the displayed
     finite-coordinate discussion they are imposed assumptions.
13. The Wilsonian action \(L_\Lambda\) is an action for remaining low modes,
    not the 1PI effective action; it must be followed by low-mode integration
    and a Legendre transform before comparison with 1PI coordinates.
14. BPHZ, Wilsonian, and 1PI descriptions are related by maps.  BPHZ supplies
    local Taylor subtractions, Wilsonian RG supplies Gaussian pushforward in
    cutoff space, and 1PI RG supplies finite projected coordinates at a
    subtraction scale.
14a. The finite-order BPHZ--Wilsonian comparison is a theorem only after the
     low-mode 1PI Legendre transform, BPHZ scheme, Wilsonian coordinate
     projection, matching map, Banach remainder estimate, and finite
     Jacobian-invertibility hypothesis are stated.  The matching map is
     \(M_I=\Pi_I\Gamma^<_{\Lambda,N}\), computed from retained Wilsonian
     coordinates and remaining low-mode integration.
14b. BPHZ Taylor local parts are Wilsonian local-coordinate data: a prepared
     subgraph subtraction gives a finite external-momentum polynomial, whose
     Fourier transform is a local vertex.  Minimal BPHZ subtractions land in
     relevant or marginal coordinates by power counting, while
     oversubtractions add a finite retained list of irrelevant operator
     coordinates.
14c. The finite matching map can be constructed recursively in the loop
     expansion.  At each order the already computed lower-order coordinates
     determine an inhomogeneous term, and the selected tree-level Jacobian is
     inverted to solve for the next Wilsonian coordinate coefficient.
15. Beta-function components in Wilsonian and 1PI coordinates are comparable
    only after a matching map is chosen; under finite coordinate changes they
    transform by the chain rule.
16. In the one-loop quartic example, the full regulated bubble decomposes by
    covariance assignment.  The mixed covariance terms are represented in the
    exact Wilsonian computation by generated vertices and low-mode
    integration; in a finite low-momentum projection their Taylor expansion is
    part of the local matching map.

## Figure Requirements

- Smooth cutoff profile, lowered cutoff profile, and shell support.
- Propagator split into low field and shell field.
- Shell integration as a graphical replacement of old propagators.
- Wilson-Polchinski equation with its two diagrammatic terms.
- Quartic-sextic toy flow, including IR attraction of \(\lambda_6\) to the
  slaved curve and the sign-convention dependence of the vertical coordinate.
- Continuum-limit flow diagram with UV cutoff \(\Lambda_0\), physical scale
  \(\Lambda_R\), fixed \(\lambda_4^R\), and limiting
  \(\lambda_6(\Lambda_R)\).
- Finite-coordinate cutoff-removal estimate diagram showing the separation
  between direct irrelevant boundary memory and the generated integral along
  the tuned trajectory.
- BPHZ--Wilsonian--1PI bridge diagram showing the bare regulated action,
  BPHZ \(R\)-operation, Wilsonian pushforward, low-source connected
  functional, Legendre transform, and coordinate projections.
- One-loop quartic matching diagram showing the split of the full regulated
  bubble into high-high, low-low, and mixed contributions and their images in
  Wilsonian, low-field 1PI, and local matching data.

## Audit Notes

- No reader-facing page references, course labels, or claims about rewriting
  pedagogy.
- Avoid compressed descriptions of renormalizability; state the limiting
  problem and the hypotheses.
- Keep the relevance sign convention consistent with the earlier chapters:
  \(y=D-\Delta\) and flow in \(\log\Lambda\) has linear term \(-yu\).  Do not
  infer a physical sign mismatch with the 1PI thermal coordinate; both
  equations are differentiated with respect to increasing scale, and both grow
  toward the infrared after changing to
  \(s=\log(\hbox{reference scale}/\hbox{running scale})\).
- In the two-coordinate toy figures, call the renormalized trajectory a curve,
  not a surface.
- Do not introduce Yang-Mills content in this chapter.
- Do not treat axiomatic QFT frameworks as the foundation of this construction.
- The compiled pages checked in the 2026-05-22 audit were physical PDF
  pages 243--252.  The continuum-limit figure was adjusted to show visible RG
  trajectory arrows toward \(\Lambda_R\), matching the source sketch more
  faithfully.
- 2026-05-22 follow-up: added a terminal bridge section proving, at finite
  regulator and for low source support, how Wilsonian connected functionals
  match the original regulated connected functional; 1PI equality enters only
  after Legendre transformation.  The section separates BPHZ locality,
  Wilsonian cutoff flow, and 1PI subtraction-scale flow.
- 2026-05-22 continuum-estimate pass: added a finite-coordinate local
  cutoff-removal section that states the hypotheses for a projected
  Wilsonian continuum graph and proves the power suppression of irrelevant
  boundary memory from the semigroup estimate.
- 2026-05-22 one-loop-matching pass: added a worked quartic scalar example
  inside the BPHZ--Wilsonian--1PI bridge.  The example defines the bubble
  functional \(\mathcal B_{A,B}\), proves the covariance split into
  low-low/high-high/mixed terms, writes the Wilsonian quartic vertex
  correction, states the BPHZ-subtracted 1PI four-point kernel, and derives
  the matching map from the Wilsonian quartic coordinate to the 1PI
  subtraction coordinate.
- 2026-05-24 issue pass: addressed #223 by adding a renormalon caveat to the
  finite-coordinate cutoff-removal estimate, emphasizing that the Wilsonian
  generated-integral hypothesis contains information beyond formal
  perturbation theory.
- 2026-05-24 issue pass: addressed #224 by inserting the scalar triviality
  theorem boundary into the perturbative Wilsonian continuum-limit discussion.
- 2026-05-24 issue pass: addressed #229 by adding a status remark after the
  finite-coordinate cutoff-removal theorem.  The remark states that
  hypotheses (ii) and (iv) are imposed unless separately proved, identifies
  what Polchinski, Salmhofer, and Brydges--Kennedy type estimates actually
  provide, and separates constructive \(\phi^4_2/\phi^4_3\) existence from
  four-dimensional scalar triviality.
- 2026-05-24 issue pass: addressed #230 by adding the Banach RG chart
  definition and finite-reference critical-surface theorem.  The theorem uses
  the Banach-space implicit function theorem to promote the tuned endpoint set
  to a \(C^k\) codimension-\(r\) submanifold only under an explicit endpoint
  submersion hypothesis; the text now distinguishes this from the bare
  linearized eigenvalue count.
- 2026-05-24 issue pass: addressed #231 by specifying the function-space and
  topology status of the Wilson-Polchinski equation.  The manuscript now
  separates the finite-regulator \(C^2\) setting, the Fr\'echet topology on
  vertex kernels for formal perturbation theory, and weighted Banach RG charts
  for theorem-level existence and estimate claims.
- 2026-05-24 issue #309 pass: separated the finite-regulator Gaussian
  pushforward theorem from the continuum Wilsonian interpretation.  The
  manuscript now proves the finite-dimensional Gaussian convolution by
  characteristic functions and states the additional continuum hypothesis as
  two independent convergence requirements: the interacting source-functional
  limit and the pushforward/vector-field limit.
- 2026-05-24 deep-proof pass: replaced the previous structural
  BPHZ--Wilsonian comparison proposition with a finite-loop theorem.  The new
  version constructs the matching map, proves the low-mode Legendre-transform
  step, proves the Taylor-remainder power estimate from the Wilsonian norm,
  obtains coordinate inversion by the finite-dimensional implicit function
  theorem, and states the perturbative/scheme scope explicitly.
- 2026-05-24 issue #325 pass: upgraded the finite-coordinate cutoff-removal
  estimate to a labeled conditional Wilsonian continuum-limit theorem.  The
  theorem now states the retained-coordinate limit
  \(z_R(t_0;u_R)\to(u_R,V_R(u_R))\), proves it from the semigroup and
  generated-integral hypotheses, and records convergence of continuous
  projected low-energy quantities with a Lipschitz error estimate when
  applicable.
- 2026-05-24 issue #497 pass: added the formal comparison datum, the
  proposition identifying BPHZ Taylor local parts with Wilsonian local
  coordinates, and the recursive loop-order construction of the matching map;
  cross-links were added back to the BPHZ finite-parts and normal-product
  discussions.
- 2026-05-24 issue #358 pass: added the vacuum-energy normalization note after
  the Wilson-Polchinski derivation, explaining why the
  \(\phi\)-independent shell normalization is absent from the displayed
  functional-derivative flow.
- 2026-05-24 issue #359 pass: made the shell/Fourier notation unambiguous:
  the shell field is \(\phi_{\mathrm{sh}}\), while hats are reserved for
  covariance differences such as \(\widehat C_{\Lambda,\Lambda'}\).

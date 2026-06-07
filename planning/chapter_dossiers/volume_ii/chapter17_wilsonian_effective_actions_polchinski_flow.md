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
- `SRC-EXTERNAL`: Polchinski's 1984 effective-Lagrangian paper, Wetterich's
  effective-average-action paper, Morris' continuous-RG treatment, and
  Rosten's exact-RG review, used only to guard terminology and theorem
  boundaries.  The chapter follows the local logical order and conventions.
- `SRC-EXTERNAL-EFT`: Appelquist--Carazzone decoupling, Weinberg's
  phenomenological-Lagrangian viewpoint, and Georgi's EFT review, used only as
  source anchors for the operational EFT-prediction and heavy-light matching
  material.  The scalar one-loop closure example is a self-contained
  background-field pole calculation in the chapter's stated normalization.
- `SRC-EXTERNAL-EFT-POSITIVITY`: Adams--Arkani-Hamed--Dubovsky--Nicolis--
  Rattazzi's analyticity/causality positivity paper and the local dispersion
  machinery of Volume II Chapter 7, used as theorem-boundary anchors for the
  conditional forward scalar positivity bound.  The chapter derives the
  contour, subtraction, pole-subtraction, optical-theorem, and basis-projection
  steps locally.
- `SRC-EXTERNAL-FERMI-SURFACE`: Polchinski's TASI Fermi-surface EFT notes,
  Shankar's RG review, Luttinger--Ward/Luttinger, and Oshikawa's
  flux-insertion argument, used as terminology and theorem-boundary anchors.
  The chapter's finite-density section keeps the finite-regulator setup,
  patch-RG shell calculation, Landau response status, and flux identity
  logically separate, and now points LSMOH phase constraints to their
  theorem-level home in Volume IX Chapter 7.
- `SRC-EXTERNAL-BOUNDS`: Polchinski's smooth-cutoff perturbative
  renormalizability argument, Salmhofer's rigorous RG framework, and
  Kopper--Muller-type perturbative cutoff estimates, together with
  Brydges--Kennedy tree/Mayer expansion technology and Glimm--Jaffe's
  constructive scalar-field framework, used to separate proved perturbative
  or constructive estimates from assumptions in the local finite-coordinate
  continuum-limit theorem.
- `SRC-AUDIT`: page-level source and figure audit completed on 2026-05-22 in
  `planning/build_audits/2026-05-22_wilsonian_effective_actions_source_figures.md`.

## Construction Task

The chapter must define and derive:

- Euclidean scalar Wilsonian action
  \(S_\Lambda=S_{\mathrm{kin},\Lambda}+L_\Lambda\) with a smooth
  nonincreasing UV cutoff profile;
- cutoff profile \(\chi(t)\), \(\chi_\Lambda(k)=\chi(k^2/\Lambda^2)\), and
  regulated propagator \(C_\Lambda(k)\), with the later plateau condition
  separated from generic non-plateau smooth profiles;
- the general momentum-space expansion of \(L_\Lambda[\phi]\);
- the source-supported generating functional condition
  \(Z_{\Lambda'}[J]=Z_\Lambda[J]\) only under the exact annihilator condition
  \(\widehat C_{\Lambda,\Lambda'}J=0\), with plateau cutoffs as the
  source-independent smooth-cutoff realization and source-dependent vertices
  or leakage estimates required for non-plateau profiles;
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
- the effective average action as a separate finite-regulator construction:
  a full regulated Euclidean action \(S_N\), an infrared quadratic regulator
  \(R_{\kappa,N}\), the source coordinate
  \(\mathcal J=-J\), the connected functional \(W_{\kappa,N}[\mathcal J]\),
  the average field
  \(\varphi=\delta W_{\kappa,N}/\delta\mathcal J\), and the modified Legendre
  transform
  \(\Gamma_{\kappa,N}=\langle\mathcal J,\varphi\rangle
    -W_{\kappa,N}[\mathcal J]-\Delta S_{\kappa,N}[\varphi]\);
- the distinction between the Wilsonian ultraviolet cutoff \(\Lambda\) and
  the effective-average-action infrared scale \(\kappa\);
- the Legendre Hessian identity
  \(\Gamma_{\kappa,N}^{(2)}+R_{\kappa,N}
    =(W_{\kappa,N}^{(2)})^{-1}\), including the derivative cancellation in the
  modified Legendre transform;
- the finite-regulator Wetterich equation
  \[
    \partial_t\Gamma_{\kappa,N}[\varphi]
    =
    \frac12\operatorname{Tr}_{E_N}
    [(\Gamma_{\kappa,N}^{(2)}+R_{\kappa,N})^{-1}
      \partial_tR_{\kappa,N}],
    \qquad t=\log\kappa,
  \]
  with proof from differentiating \(W_{\kappa,N}\), decomposing the full
  second moment into mean and connected parts, and using the Hessian identity;
- the continuum status of the Wetterich equation: after the finite regulator
  is suppressed, the trace formula requires a specified topology and uniform
  convergence of the regulated traces, not just the formal observation that
  \(\partial_tR_\kappa\) is shell-supported;
- the constant-field/local-potential projection
  \[
    \partial_tU_\kappa(v)
    =
    \frac12\int_p
      \frac{\partial_tR_\kappa(p)}
      {Z_\kappa p^2+R_\kappa(p)+U_\kappa''(v)}
  \]
  and the status of this equation as a projection of the exact flow rather
  than a theorem for the full effective average action;
- the illustrative optimized-regulator result
  \( \partial_t U_\kappa(v)=
    v_D\kappa^D/[1+U_\kappa''(v)/(Z_\kappa\kappa^2)]\)
  with
  \(v_D=[D2^{D-1}\pi^{D/2}\Gamma(D/2)]^{-1}\), accompanied by the warning that
  a nonsmooth step-function regulator must be justified as a smooth limit or
  in an appropriate function space;
- the comparison between Wilson-Polchinski and Wetterich flows: they are exact
  identities for different cutoff-dependent objects, and a Legendre-type
  relation requires compatible cutoff kernels, invertibility, and a specified
  continuum or perturbative limit;
- the gauge-theory caveat for effective-average-action flows: an infrared
  regulator must be part of a background-field or BV/BRST construction with
  the corresponding modified Ward or Slavnov--Taylor identity;
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
- the finite-reference critical-surface construction: if the
  relevant-coordinate endpoint map is \(C^k\) and its derivative in the
  relevant block is invertible, the Banach implicit-function theorem makes its
  zero set a \(C^k\) embedded Banach submanifold of codimension equal to the
  number of relevant coordinates; the dossier records this as an
  implicit-function consequence, not as an independent QFT theorem;
- an operational EFT-prediction specification that includes the observable class,
  kinematic domain, high-scale or bottom-up input, regulator/renormalization
  prescription, retained field/symmetry data, a regulated operator module
  with observable-dependent equivalence/projection maps, expansion parameters,
  matching/RG data, infrared/external-state prescription, and topology or norm
  for the omitted contribution;
- the output form
  \(\mathcal O_{\rm phys}=\mathcal O_{\rm EFT}^{[N]}+R_N\), with \(R_N\)
  classified as an exact finite-regulator identity, fixed-order perturbative
  remainder, asymptotic remainder, nonperturbative theorem in a stated model,
  conditional UV inference, or heuristic coefficient-size estimate;
- the distinction between top-down matching and bottom-up coefficient input,
  including the warning that positivity/analyticity constraints are
  conditional UV restrictions on coefficients rather than the definition or
  justification of an EFT;
- a source-aware local field-redefinition identity carrying the action,
  measure Jacobian, source term, and observable representative together, and
  the resulting warning that EOM operators may be removed from an on-shell
  matched basis only with the corresponding source/observable transformation;
- a conditional forward scalar positivity section, built after the EFT
  prediction specification rather than before it, including:
  - an assumption list for Lorentz invariance or an equivalent macrocausal
    substitute, unitarity, crossing, locality, mass gap, stable external
    particles, first-sheet analyticity, real analyticity, polynomial
    boundedness/subtractions, and explicit subtraction or regulation of
    first-sheet poles and massless forward singularities;
  - the crossing-symmetric variable \(\nu=s-2m^2\) at \(t=0\), the
    pole-subtracted amplitude \(\mathcal M_{\rm sub}\), and the threshold/cut
    domain in the \(\nu\)-plane;
  - the twice-subtracted forward dispersion formula with both right and crossed
    cuts, subtraction constants, stable-pole terms treated by prior explicit
    subtraction, and a named large-contour term;
  - the folded identical-scalar formula and coefficient sum rule
    \(a_2=(2/\pi)\int d\nu\,\operatorname{Im}\mathcal M_{\rm sub}/\nu^3\) when
    the large contour vanishes;
  - the optical-theorem normalization that makes the absorptive part
    nonnegative;
  - the conversion of \(a_2\) into a weighted cross-section moment
    \(\int ds\,\sqrt{s(s-4m^2)}\sigma_{\rm abs}^{\rm sub}(s)/(s-2m^2)^3\),
    with a finite-window residual
    \(a_2-c_\infty-B(S_0)=T(S_0)\), positive tail \(T(S_0)\), contour-status
    bookkeeping, and the failure interpretation when a matched low-energy
    coefficient lies below the measured window moment after the contour and
    remainder accounting are fixed;
  - the map from the EFT low-energy coefficient to the on-shell forward
    amplitude coordinate \(\kappa_{\rm amp}\), with EOM and field-redefinition
    representatives killed only by the declared observable projection;
  - failure modes from massless \(t\)-channel exchange, IR logs,
    photons/gravitons, unstable external particles, non-forward/spinning/gauge
    extensions, insufficient high-energy boundedness, nonlocal UV behavior, and
    EFTs without a local Poincare-invariant UV-completion map.
- a general finite-density Fermi-surface EFT section with a finite-volume
  \(U(1)\)-charge setup, exact Green functions, density and Fermi-surface
  diagnostics, and a strict separation of thermodynamic, zero-temperature, and
  low-frequency limits;
- a smooth patch cover of a Fermi surface with partition-of-unity fields,
  normal/tangential coordinates, free patch propagator, the
  Shankar--Polchinski shell scaling, a curvature-resolved scaling window, and
  the patch density-of-states match for density/compressibility;
- the interaction architecture for Fermi-surface EFT: generic phase-space
  suppression, forward/Landau coordinates and response status, the Cooper
  shell logarithm with \(O(\Lambda/E_F)\) remainder, the BCS eigenvalue flow
  \(d\lambda/d\ell=-\lambda^2\), the attractive-channel instability scale, and
  Pomeranchuk stability;
- quasiparticle observable definitions through the retarded pole, including
  residue, effective velocity, lifetime, Landau interaction, Ward-identity
  scope, and failure zones;
- theorem-status discipline for Luttinger counts: Luttinger--Ward functional
  assumptions, Green-function zero caveats, exact finite-volume flux
  momentum-shift algebra, the separate Fermi-liquid interpretation hypotheses,
  and modified-count examples from broken translations, topological sectors,
  Mott/zero surfaces, superconductors, and non-Fermi liquids;
- non-Fermi-liquid boundary examples from gapless boson/gauge-field coupling,
  with control parameters and formal scaling status separated from constructed
  fixed-point claims, plus an explicit bridge to the dense-QCD HDET section;
- a regulated operator-basis paragraph using a filtration by physical,
  evanescent, EOM, BRST/BV-exact, and boundary/defect sectors, with any direct
  sum treated as a noncanonical scheme-dependent splitting;
- a one-loop evanescent mixing/projection example with the concrete
  four-fermion representative \(E_{16}=O_3-16Q\), the projection
  \(\Pi_QE_{16}=-4\epsilon Q\), the closed-trace Gram projection as a distinct
  scheme check, an Abelian spectator-exchange graph whose UV numerator
  produces \(O_3\) with residue \(2g^2/(d\,16\pi^2)\), the finite evanescent
  split component and its compensating \(O(\epsilon)\) graph-residue term, plus
  a separate regulated \(E_{16}\)-counterterm matrix whose insertion produces
  the nonzero finite physical coefficient and the representative-change
  countershift;
- a power-counting paragraph that treats canonical, loop, chiral, velocity,
  large-\(N\), endpoint, or multi-parameter filtrations as error organizations
  only after counterterm closure, coefficient assumptions, logarithmic mixing,
  kinematic regions, and remainder status have been stated;
- a scalar heavy-light model with \(K_M=-\partial^2+M^2\), a tree-level
  nonlocal kernel \(K_M^{-1}\), its local expansion and low-momentum remainder
  bound, an explicit \(\overline{\rm MS}\) one-loop four-light matching
  calculation comparing the full heavy bubble, EFT light loop, matched local
  insertions, finite scheme coordinate, and first omitted \(Q/M\) terms, plus
  RG running below \(M\) and cancellation of the artificial matching scale;
- a concrete massive scalar EFT retaining \(\phi^4\) and
  \(\phi^6/\mathcal M^2\), with a one-loop background-field pole calculation
  showing closure through canonical excess two and the first omitted
  \(\phi^8/\mathcal M^4\) operator identified as the counterterm needed to
  extend the renormalized specification to canonical excess four, with its
  Wilson-coefficient dimension kept separate from external-momentum powers;
- a same-EFT local field redefinition
  \(\phi=\psi+a\psi^3/\mathcal M^2\), carrying the action, regulator
  Jacobian, source term, composite representatives, Wilson coefficients, and
  the on-shell four-point observable together;
- the scoped decoupling statement for fixed-loop nonexceptional low-energy
  amplitudes, together with the boundaries from mass-dependent versus
  mass-independent schemes, relevant parameters, symmetry breaking, anomalies,
  Wess--Zumino/topological terms, thresholds, infrared singularities, and
  heavy couplings that scale with mass;
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
    \(\|e^{A\tau}\|\le K_A e^{\omega\tau}\) for \(\tau\le0\);
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
  low-source connected functionals under an admissible plateau split,
  Legendre transform of the restricted low-source functional to 1PI kernels,
  finite matching from Wilsonian local coordinates to 1PI subtraction
  coordinates, and the distinction between a Wilsonian vertex and a 1PI
  vertex.
- a finite-order BPHZ--Wilsonian controlled approximation that:
  - fixes a BPHZ forest-formula scheme, a low source/classical-field test
    space strictly inside the cutoff plateau, finite 1PI projectors, and
    finite Wilsonian coordinate projectors;
  - defines the matching map
    \(M_I^{(\ell,N)}(u;\Lambda,\mu,\mathfrak b)
      =\Pi_I\Gamma^{<,(\le\ell)}_{\Lambda,N}[u]\);
  - defines \(\Gamma^<\) as the Legendre transform after restricting the
    connected source functional to the finite low-source space, not as a
    restriction of a full Legendre transform;
  - proves the finite-dimensional low-source Legendre-transform step from
    equality of connected functionals and Hessian invertibility;
  - proves a Wilsonian Taylor-remainder lemma giving
    \(O((\mu/\Lambda)^{p_N})\) suppression from the chosen Banach norm and
    the first omitted excess scaling exponent;
  - proves that the BPHZ forest operation is linear in vertex labels and
    commutes with the additive split
    \(L_\Lambda=L_\Lambda^{(N)}+v_{\perp,N}\), so subtracted graphs with a
    \(v_{\perp,N}\)-insertion are still controlled by the Wilsonian remainder
    norm;
  - requires the \(\Lambda_0\to\infty\) limit to be taken along a tuned
    Polchinski-flow counterterm trajectory, with UV-cutoff local coordinates
    chosen as functions of \(\Lambda_0\) to hold fixed renormalized boundary
    data;
  - states that the bounded-chart hypothesis is perturbative order by order,
    or nonperturbative only for trajectories for which the asserted norm
    bounds are actually proved;
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
   functional obtained by Gaussian pushforward.  A source-independent
   low-source generating functional is held fixed only for source directions
   annihilating the integrated covariance; for smooth non-plateau profiles the
   exact comparison requires source-dependent Wilsonian vertices or a leakage
   theorem.
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
   \(J\phi_{\mathrm{sh}}\) term vanishes only when
   \(\widehat C_{\Lambda,\Lambda'}J=0\).  For a smooth source-independent
   theorem with nonzero open low-momentum support, this is enforced by an
   admissible cutoff plateau.
5. The infinitesimal shell-integration identity gives a functional differential
   equation for \(L_\Lambda\).
5a. The Wilson-Polchinski equation has a stated topology only after choosing
    its setting.  At finite regulator the derivative is an ordinary derivative
    of \(C^2\) functions on a finite mode space; in perturbation theory it is
    coefficientwise in the Fr\'echet topology of smooth vertex kernels; in a
    theorem-level RG argument it is a Banach-space vector-field equation in a
    specified weighted norm.
5b. The effective average action is a modified Legendre transform of an
    infrared-regulated connected functional, not another name for the
    Wilsonian action.  Its finite-regulator Hessian satisfies
    \(\Gamma_\kappa^{(2)}+R_\kappa=(W_\kappa^{(2)})^{-1}\).
5c. The Wetterich equation follows exactly at finite regulator by
    differentiating the modified Legendre transform at fixed average field,
    decomposing the source-dependent second moment into connected and mean
    parts, and applying the Hessian identity.  Its continuum use requires
    separate trace-convergence and regulator-removal estimates.
5d. The local-potential flow is a projection of the exact Wetterich equation:
    it becomes a closed scalar equation only after the derivative-expansion
    ansatz is imposed, and omitted operators are then an approximation error
    to be estimated rather than absent from the exact theory.
5e. Wilson-Polchinski and Wetterich flows are related only after compatible
    cutoff kernels and a Legendre matching map have been chosen; arbitrary
    truncations of the two equations need not be equivalent.
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
   the canonical irrelevant power.  Figure `fig:quartic-sextic-ir-flow` must
   therefore show distinct characteristics approaching distinct neighborhoods
   of the attracting curve, not several trajectories merging into one finite
   point.
9. Perturbative renormalizability is formulated by a limiting procedure:
   remove the UV cutoff while tuning regulator-dependent action coordinates
   so selected physical couplings at a fixed reference scale remain fixed.
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
    not the 1PI effective action; it must be followed by integration over the
    remaining cutoff field and a Legendre transform on the chosen source
    space before comparison with 1PI coordinates.
14. BPHZ, Wilsonian, and 1PI descriptions are related by maps.  BPHZ supplies
    local Taylor subtractions, Wilsonian RG supplies Gaussian pushforward in
    cutoff space, and 1PI RG supplies finite projected coordinates at a
    subtraction scale.
14a. The finite-order BPHZ--Wilsonian comparison is a controlled
     approximation whose substance is conditional on the low-mode 1PI Legendre
     transform, BPHZ scheme, Wilsonian coordinate projection, matching map,
     Banach remainder estimate, and finite Jacobian-invertibility hypothesis.
     The matching map is
     \(M_I=\Pi_I\Gamma^<_{\Lambda,N}\), where \(\Gamma^<\) is the Legendre
     transform of the connected functional restricted to the finite
     low-source space; it is not the restriction of a previously formed full
     Legendre transform.
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
14d. The exact source-independent matching implication uses an admissible plateau
     cutoff.  A non-plateau smooth cutoff is a different comparison datum:
     source-dependent vertices must be retained, or a profile-dependent
     leakage estimate must be proved and added to the stated remainder.
14e. The \(\Lambda_0\to\infty\) step in the BPHZ--Wilsonian comparison is a
     tuned Polchinski-flow counterterm trajectory, not a fixed UV-cutoff
     coordinate limit.  The UV-cutoff local coordinates are functions of
     \(\Lambda_0\) chosen to hold the selected renormalized boundary data
     fixed.
14f. The BPHZ forest operation commutes with the retained/omitted Wilsonian
     vertex split because it is linear in vertex kernels and depends on graph
     topology, subtraction points, and subtraction degrees.  The Wilsonian
     norm hypothesis must include the finite family of Taylor-subtracted
     kernels produced by graphs containing at least one omitted vertex.
15. Beta-function components in Wilsonian and 1PI coordinates are comparable
    only after a matching map is chosen; under finite coordinate changes they
    transform by the chain rule.
16. In the one-loop quartic example, the full regulated bubble decomposes by
    covariance assignment.  The mixed covariance terms are represented in the
    exact Wilsonian computation by generated vertices and low-mode
    integration; in a finite low-momentum projection their Taylor expansion is
    part of the local matching map.
17. An EFT prediction is a specification of an observable problem, not merely a
    local Lagrangian or a list of operators.  The reader-facing output must be
    an observable approximation plus a named remainder meaning.
18. Top-down EFTs use a specified high-scale model and matching map; bottom-up
    EFTs use coefficients fixed by data or other nonperturbative input and
    need not have a local Lorentz-invariant UV completion.  Analyticity and
    positivity bounds are conditional UV constraints, not the definition of
    the EFT.
18a. The forward scalar positivity bound is a conditional statement about an
     already-defined on-shell amplitude observable.  After first-sheet stable
     poles and known infrared singularities are subtracted, crossing about
     \(\nu=s-2m^2=0\), the twice-subtracted contour formula, the declared
     large-circle coordinate, and the optical theorem imply
     \(a_2=(2/\pi)\int_{\nu_{\rm th}}^\infty
     d\nu\,\operatorname{Im}\mathcal M_{\rm sub}/\nu^3+c_\infty\).
     Equivalently it is the weighted moment of the subtracted absorptive
     cross-section measure, so the finite-window comparison is the observable
     residual \(a_2-c_\infty-B(S_0)=T(S_0)\ge0\).  The bounded coefficient is
     the projected amplitude coordinate
     \(\kappa_{\rm amp}\), not an arbitrary Wilson coefficient in a redundant
     operator basis.
19. Local field redefinitions are exact finite-regulator changes of variables
    only when the Jacobian, source coupling, and observable representative are
    transformed together.  EOM removal changes off-shell Green functions and
    basis coefficients unless the observable map is also carried along.
20. Operator reduction is regulator- and observable-dependent: the regulated
    local module is filtered by physical, evanescent, EOM, BRST/BV-exact, and
    boundary/defect sectors; a direct-sum coordinate split is a noncanonical
    scheme choice; BRST-exact terms require an anomaly-free physical cohomology
    setting; and boundary terms remain physical whenever boundary, defect, edge,
    charge, or boundary-observable data are part of the setup.
21. The concrete \(E_{16}=O_3-16Q\) example has
    \(\Pi_QO_3=(16-4\epsilon)Q\), hence \(\Pi_QE_{16}=-4\epsilon Q\), in the
    open-spinor NDR projection; the closed-trace Gram pairing would give
    \(3d-2\), so it is recorded as a distinct scheme.  The repaired one-loop
    example uses an Abelian spectator exchange between the two right fermion
    legs: the UV angular average sends the Dirac numerator to
    \((\ell^2/d)O_3\), the scalar pole gives \(2/\epsilon\), and the complete
    projected \(Q\)-pole residue is \(8g^2/(16\pi^2)\).  Splitting the pole
    residue at \(d=4\) exposes a finite evanescent split component
    \(-C_Qg^2/(8\pi^2)\), which is compensated by the \(O(\epsilon)\) part of
    \(2/d\) and therefore is not a net Wilson-coefficient shift.  A separate
    regulated \(E_{16}\)-counterterm matrix with \(Z^{(1)}_{EE}=u\) gives
    \(\delta{\cal L}_{\rm ct}^{(E)}=C_EuE_{16}/\epsilon\); projecting the
    renormalized amplitude gives \(C_Q^{\rm phys}=C_Q-4C_Eu\), with finite
    countershifts under \(E_{16}\mapsto O_3-(16+\alpha\epsilon)Q\).
22. Power counting is a closure and error organization: logs and anomalous-dimension
    mixing do not lower the declared order, and new kinematic regions require
    new expansion parameters or a changed prediction specification.
23. In the heavy-light scalar model, tree-level heavy exchange gives an exact
    nonlocal \(K_M^{-1}\) kernel whose derivative expansion has a concrete
    \(Q/M\) remainder away from thresholds.
24. The one-loop heavy-light matching is now an observable comparison: the
    \(\overline{\rm MS}\) heavy bubble fixes \(c_H^{\overline{\rm MS}}=0\),
    the full four-light kernel and EFT kernel both include the light bubble in
    the same scheme, the local \(P_a^2/M^2\) insertion is matched, finite
    bubble-scheme shifts are compensated by the threshold coordinate, and the
    first omitted heavy terms are bounded by explicit \(Q^4/M^6\) and
    \(Q^4/M^4\) estimates.
25. In the massive scalar EFT with \(\phi^4+\phi^6/\mathcal M^2\), the
    one-loop background-field pole produces retained \(\phi^4\) and
    \(\phi^6/\mathcal M^2\) counterterms and first generates
    \(\phi^8/\mathcal M^4\) outside the target canonical excess.  The
    generated pole is not a finite remainder; it marks the \(c_8\) counterterm
    required for a \(k=4\) extension, and its eight-point contact scaling is
    distinct from lower-point loop or mass-suppressed effects.
26. The local redefinition \(\phi=\psi+a\psi^3/\mathcal M^2\) shifts
    \(\lambda\), the derivative operator coefficient, and \(c_6\), carries a
    regulator Jacobian and transformed sources/composites, and leaves the
    on-shell four-point kernel invariant only after all these pieces are
    included.
27. Decoupling is scoped: fixed-loop asymptotic expansion, exact
    finite-regulator large-\(M\) expansion, and nonperturbative decoupling are
    different claims with different hypotheses.

## Figure Requirements

- Smooth cutoff profile, lowered cutoff profile, and shell support.
- Propagator split into low field and shell field.
- Shell integration as a graphical replacement of old propagators.
- Wilson-Polchinski equation with its two diagrammatic terms.
- Wilsonian-versus-effective-average-action diagram showing that shell
  integration leaves a remaining-field action \(L_\Lambda\), whereas the
  effective average action integrates all modes with an IR regulator and then
  performs a modified Legendre transform.
- Quartic-sextic toy flow, including IR attraction of \(\lambda_6\) to the
  slaved curve and the sign-convention dependence of the vertical coordinate.
- Continuum-limit flow diagram with UV cutoff \(\Lambda_0\), physical scale
  \(\Lambda_R\), fixed \(\lambda_4^R\), and limiting
  \(\lambda_6(\Lambda_R)\).
- Finite-coordinate cutoff-removal estimate diagram showing the separation
  between direct irrelevant boundary memory and the generated integral along
  the tuned trajectory.
- BPHZ--Wilsonian--1PI bridge diagram showing the UV-regulated action,
  BPHZ \(R\)-operation, Wilsonian pushforward, low-source connected
  functional with source support inside the plateau, Legendre transform, and
  coordinate projections.
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
  BPHZ--Wilsonian comparison discussion with a finite-loop controlled
  approximation.  The new
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
- 2026-05-25 issue #497 closure pass: added a fixed-loop comparison remark
  deriving the equivalence of the BPHZ and Polchinski-Wilsonian
  renormalizability criteria in the massive, nonexceptional,
  finite-projector setting already established in the controlled matching
  comparison.  The
  proof runs in both directions, constructs the coordinate assignment through
  local Taylor parts and low-mode 1PI projectors, and states the
  \((\mu/\Lambda)^{p_N}\) irrelevant-coordinate error rather than claiming a
  theorem about existence of a nonperturbative continuum QFT.
- 2026-05-25 clarification pass: added an explicit status remark after the
  corollary spelling out that the two-way implication is a fixed-loop
  finite-coordinate perturbative theorem.  BPHZ is perturbative by definition;
  the separate nonperturbative problem is whether a Wilsonian or constructive
  continuum theory exists and has the BPHZ-renormalized series as its
  perturbative asymptotic expansion in the chosen coordinates.
- 2026-05-25 issue #570 pass: closed the six proof gaps in the
  BPHZ--Polchinski comparison theorem.  The chapter now distinguishes the
  exact source-dependent smooth-cutoff pushforward from the
  source-independent plateau theorem; proves the exact low-source identity
  under \(C_>J=0\); defines low 1PI kernels as Legendre transforms of the
  restricted source functional; requires the \(\Lambda_0\to\infty\) step to
  follow a tuned Polchinski-flow counterterm trajectory; records the
  perturbative/nonperturbative status of the bounded-chart hypothesis; and
  proves that the BPHZ forest operation commutes with the
  retained/omitted-vertex split before the Wilsonian Taylor-remainder bound is
  applied.
- 2026-05-24 issue #358 pass: added the vacuum-energy normalization note after
  the Wilson-Polchinski derivation, explaining why the
  \(\phi\)-independent shell normalization is absent from the displayed
  functional-derivative flow.
- 2026-05-24 issue #359 pass: made the shell/Fourier notation unambiguous:
  the shell field is \(\phi_{\mathrm{sh}}\), while hats are reserved for
  covariance differences such as \(\widehat C_{\Lambda,\Lambda'}\).
- 2026-05-25 issue #459 pass: added the effective-average-action construction
  and finite-regulator Wetterich theorem.  The manuscript now defines
  \(R_{\kappa,N}\), \(W_{\kappa,N}\), \(\varphi\), and
  \(\Gamma_{\kappa,N}\), proves the Legendre Hessian identity, derives the
  Wetterich equation at finite regulator, states the continuum trace status,
  gives the constant-field local-potential projection, and separates this
  infrared-regulated 1PI flow from the Wilson-Polchinski Wilsonian action
  flow.
- 2026-06-04 issue #782 pass: added the operational EFT-prediction
  specification, remainder classification, bottom-up/top-down distinction,
  source-aware
  field-redefinition identity, power-counting closure criterion, and a
  heavy-light scalar matching section with tree-level nonlocal kernel
  expansion, one-loop hard threshold matching, RG matching-scale cancellation,
  and scoped decoupling/nondecoupling boundaries.  Added
  `calculation-checks/eft_prediction_calculus_checks.py` to verify the heavy
  kernel expansion, threshold-log cancellation, and the initial
  field-redefinition/source algebra; issue #823 replaced the formal
  remainder-classification block with the concrete one-loop scalar EFT closure
  example.
- 2026-06-04 issue #823 pass: replaced the formal power-counting and Gaussian
  field-redefinition evidence with a concrete scalar EFT calculation.  The
  chapter now derives the one-loop poles from \((V''(\phi))^2\), shows
  retained \(\phi^4\)/\(\phi^6\) closure and the generated
  \(\phi^8/\mathcal M^4\) truncation boundary, and carries the same EFT through
  a local \(\phi=\psi+a\psi^3/\mathcal M^2\) basis change with Jacobian,
  sources, composites, Wilson-coordinate shifts, and an on-shell four-point
  observable check.
- 2026-06-04 issue #827 pass: corrected the scalar-EFT closure interpretation
  so canonical excess four no longer becomes a universal \(Q^4/\mathcal M^4\)
  momentum law.  The generated \(\phi^8\) pole is now a truncation-boundary
  counterterm signal; an explicit \(c_8\) minimal-subtraction extension is
  stated, and eight-point contact scaling is separated from lower-point
  contractions controlled by loops, light masses, and scheme-dependent
  counterterms.
- 2026-06-04 issue #824 pass: replaced the unconditional operator quotient in
  the EFT prediction specification with a regulated operator module plus
  observable-dependent equivalence/projection maps.  The chapter now keeps
  evanescent representatives through one-loop mixing and matching, states the
  hypotheses for EOM and BRST-exact removal, retains boundary/defect/edge
  sectors when they are physical input, and gives the finite
  \(O(\epsilon)\times1/\epsilon\) evanescent Wilson-coefficient shift example.
- 2026-06-04 issue #825 pass: replaced the symbolic evanescent
  \(\epsilon\)-times-pole template with a concrete color-singlet left-current
  four-fermion example.  The chapter now derives
  \(\Pi_QO_3=(16-4\epsilon)Q\) and a placeholder scalar-bubble pole model for
  the finite projection mechanism.  The later issue #836/#841 passes replace
  that placeholder graph logic by the explicit spectator-exchange cancellation
  test plus a separate renormalized counterterm-matrix calculation.
- 2026-06-05 issue #836 pass: upgraded the evanescent example from a scalar
  spectator-pole placeholder to an explicit Abelian spectator-exchange graph.
  The manuscript now states the renormalizable spectator interaction, the
  open-spinor projector and closed-trace-projection negative control, the
  amputated four-point numerator, the UV angular average to \(O_3/d\), the
  scalar \(2/\epsilon\) pole, the complete projected \(Q\)-pole residue, and
  the finite evanescent split plus \(O(\epsilon)\)-residue compensation.  The
  later issue #841 pass below narrows this as a cancellation test, not a net
  finite Wilson-coefficient shift.
- 2026-06-05 issue #841 evanescent-counterterm pass: retained the Abelian
  spectator-exchange graph as a cancellation/consistency example and added the
  actual next-step renormalized mixing calculation.  The TeX now displays the
  regulated basis \(([Q]_R,[E_{16}]_R)\), the counterterm matrix
  \(Z^{(1)}=\begin{psmallmatrix}0&0\\0&u\end{psmallmatrix}\), the counterterm
  insertion \(C_EuE_{16}/\epsilon\), the projected physical coordinate
  \(C_Q^{\rm phys}=C_Q-4C_Eu\), and the finite representative change
  \(C_Q\mapsto C_Q+\alpha C_Eu\) under
  \(E_{16}\mapsto O_3-(16+\alpha\epsilon)Q\).  The companion EFT check now
  verifies zero net finite remainder in the concrete \(Q\)-insertion graph,
  nonzero finite shift from the counterterm matrix, omission of the matrix as a
  negative control, and finite-scheme invariance.
- 2026-06-05 issue #816 pass: completed the promised one-loop heavy-light
  observable matching.  The chapter now evaluates the regulated
  \(\overline{\rm MS}\) heavy bubble, derives \(c_H^{\overline{\rm MS}}=0\),
  writes the full and EFT four-light kernels with the common light loop,
  matches the local \(P_a^2/M^2\) insertion, displays finite scheme-coordinate
  cancellation, and proves explicit first-omitted heavy-momentum bounds.  The
  companion EFT check now compares the full and EFT kernels directly instead
  of only differentiating a symbolic threshold-log coordinate.
- 2026-06-05 issue #784 pass: added the general finite-density
  Fermi-surface EFT section.  The new section is architecture-first: finite
  \(U(1)\) regulator setup and exact Green functions; patch cover, no
  double-counting, scaling, curvature window, and density/compressibility
  matching; generic/forward/Cooper channel separation; one-loop Cooper shell
  calculation with explicit remainder and BCS eigenvalue instability scale;
  quasiparticle observables and Landau-response status; Luttinger--Ward and
  flux-insertion routes kept distinct with assumptions; modified-count phases;
  and controlled/non-controlled non-Fermi-liquid boundaries.  Added
  `calculation-checks/fermi_surface_eft_checks.py` for density-of-states,
  shell-log, BCS-flow, Pomeranchuk, and flux-momentum arithmetic checks.
- 2026-06-05 issue #777 cross-reference pass: pointed the finite-density
  flux-insertion paragraph to the new LSMOH theorem-boundary section in Volume
  IX Chapter 7, preserving the distinction between Fermi-volume counting and
  gapped-phase constraints.
- 2026-06-05 issue #779 pass: added the conditional forward scalar positivity
  section after the EFT prediction specification and field-redefinition
  discussion.  The new section starts from an observable amplitude, states the
  assumption list, derives the twice-subtracted forward dispersion relation
  with both cuts, subtraction constants, pole subtraction, and a large-contour
  term,
  folds the identical-scalar cuts to obtain the \(2/\pi\) coefficient sum rule,
  uses the optical theorem for positivity, projects the EFT coefficient modulo
  EOM/field-redefinition representatives, and records failure modes.  The
  companion `calculation-checks/eft_prediction_calculus_checks.py` now verifies
  the finite normalization, pole-subtraction, contour, massless-pole, and
  basis-projection algebra.
- 2026-06-06 issue #844 Wilsonian/positivity observable pass: connected the
  formal forward coefficient to a finite-window cross-section moment.  The
  manuscript now defines the subtracted absorptive measure
  \(\sigma_{\rm abs}^{\rm sub}\), writes
  \(a_2=\frac2\pi\int ds\,\sqrt{s(s-4m^2)}
  \sigma_{\rm abs}^{\rm sub}(s)/(s-2m^2)^3+c_\infty\), splits a finite window
  \(B(S_0)\) and positive tail \(T(S_0)\), and explains what a violation of the
  lower bound would diagnose.  The companion check now verifies the
  optical-theorem flux factor and finite-window split as a finite
  normalization/regression check, not as an independent empirical scattering
  construction.
- 2026-06-06 issue #755/#844/#505 coherence pass: re-audited the reader-facing
  EFT-prediction and positivity surface after the calculation additions.  The
  manuscript now uses visible "prediction specification", "assumptions", and
  "scope" language while preserving stable labels and all equations; the flow
  is observable problem, regulator/projection/matching inputs, named
  remainder, then conditional positivity.  This was a physics-architecture and
  prose-coherence repair, not a new lemma or formula annex.
- 2026-06-06 issue #844 positivity residual re-audit: promoted the
  finite-window comparison to the explicit observable residual
  \(a_2-c_\infty-B(S_0)=T(S_0)\ge0\), and connected the EFT coefficient through
  the prediction remainder \(R_N^{(2)}\).  The companion check now rejects the
  shortcut that compares \(a_2\) with \(B(S_0)\) while retaining a contour
  coordinate.

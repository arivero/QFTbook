# Volume II, Chapter 15 Dossier: Wilson-Fisher Fixed Point And Scaling Operators

## Source Position

- Primary local source: second-sequence handwritten material, pages 124--135.
- Immediate predecessor: the stress-tensor trace identity and conformal
  currents at fixed points.
- Immediate successor in the source order: the statistical Ising model.
- Role in the monograph: give the first perturbatively controlled non-Gaussian
  fixed point, then compute the first operator dimensions from the same
  renormalized-operator logic developed in the preceding chapters.

## Source And Reference Controls

- `SRC-QFT-PDF`: `references/253b lecture notes 2023.pdf`, pages 124--135;
  checked against rendered page images in
  `monograph/tex/build/source_visual_trace/`.
- `SRC-BEN-COMPARISON`: `references/253b transcribed lecture notes.tex`, the
  Wilson-Fisher/scaling-operator section, used only as a comparison layer.
- `SRC-EXTERNAL`: standard Wilson-Fisher and scaling-operator facts, with
  Rosten's exact RG review kept in mind for fixed-point and scaling-operator
  terminology.  The construction in the chapter remains tied to the local
  source order and to 1PI/MS coordinates already introduced.
- `SRC-EXTERNAL-ISING-DATA`: the nonperturbative fixed-point entries in the
  comparison table are external data, not derived in the chapter: 3D Ising
  conformal-bootstrap dimensions from El-Showk--Paulos--Poland--Rychkov--
  Simmons-Duffin--Vichi, Kos--Poland--Simmons-Duffin--Vichi,
  Simmons-Duffin's spectrum paper, and the later mixed-correlator
  stress-tensor bootstrap; 2D entries from the Ising minimal model
  \(\mathcal M(3,4)\) / Onsager-BPZ solution.
- `SRC-EXTERNAL-ON-LARGEN`: the \(O(N)\) large-\(N\) saddle and nonlinear
  sigma-model relation are checked against Moshe--Zinn-Justin,
  `Quantum Field Theory in the Large N Limit: a Review`, arXiv:hep-th/0306133,
  but the chapter derives the finite-cutoff saddle, gap equation, critical
  exponent, and sigma-model matching explicitly.

## Construction Task

The chapter must define and derive:

- scalar quartic theory in \(D=4-\epsilon\) dimensions with
  \(\mathcal L_E=\frac12(\partial\phi)^2+\frac12m_0^2\phi^2
  +\frac1{4!}g_0\phi^4\);
- the dimensional-regularization status of the calculation: graph-level
  meromorphic continuation of finite-dimensional loop-momentum integrals in
  \(D=4-\epsilon\), applied coefficient by coefficient in perturbation theory,
  rather than a field-configuration-space measure in noninteger dimension;
- the formal-series status of \(\beta^\epsilon(\lambda)\), anomalous
  dimensions, \(\lambda_*(\epsilon)\), and the resulting scaling dimensions;
- the tuning of \(m_0^2\) as the condition for a massless infrared limit;
- the reminder that \(m_0^2\) is a bare cutoff coordinate, not a spectral pole
  mass;
- the restriction to the \(\mathbb Z_2\)-even RG chart when odd sources are
  not introduced;
- the dimensionless 1PI quartic coupling
  \(\lambda(\mu)=-\mu^{-\epsilon}Z(\mu)^2\Gamma^{(4)}\) at the symmetric
  Euclidean subtraction point;
- the scheme distinction between the symmetric momentum-subtraction chart
  \((\lambda_{\rm MOM},Z_{\rm MOM})\) and the minimal-subtraction pole chart
  \((\lambda_{\rm MS},Z_\phi^{\rm MS})\), including why the displayed
  \(O(\epsilon^2)\) value of \(\eta\) is unchanged by finite analytic
  reparametrization at this order;
- the part-opening \(Z\)-factor convention: \(Z_\phi^{\rm MS}\) is the
  minimal-subtraction pole factor appearing in the formal
  \(4-\epsilon\)-dimensional graph calculation, not the Kallen--Lehmann/LSZ
  pole residue \(Z_\phi^{\rm pole}\);
- the notation convention that \(\lambda(\mu)\), not \(\lambda_4(\mu)\), is the
  running dimensionless quartic coordinate when a single chart is under
  discussion; explicit subscripts such as \(\lambda_{\rm MOM}\) and
  \(\lambda_{\rm MS}\) are used when scheme distinctions matter; \(\delta g_4\)
  denotes a source perturbation for \(O_4=\phi^4\), not a second running-coupling
  symbol;
- the one-loop formula for \(\lambda(\mu)\) in terms of \(g_0\);
- the beta function
  \(\beta(\lambda)=-\epsilon\lambda+
  (3/(16\pi^2)+O(\epsilon))\lambda^2+O(\lambda^3)\);
- the fixed point
  \(\lambda_*=16\pi^2\epsilon/3+O(\epsilon^2)\) and its IR attractiveness
  for decreasing \(\mu\) after the massless endpoint condition is imposed;
- the two-loop minimal-subtraction pole map for
  \(x=\lambda_{\rm MS}/(16\pi^2)\),
  \[
    g_0/(16\pi^2)=\mu^\epsilon
    [x+3x^2/\epsilon+x^3(9/\epsilon^2-17/(6\epsilon))+O(x^4)],
  \]
  together with the derivation of
  \(\beta_x^\epsilon=-\epsilon x+3x^2-\frac{17}{3}x^3+O(x^4)\);
- the two-loop \(\phi^2\) source pole
  \(\log Z_{2,\rm src}^{\rm MS}
    =(-x+\frac{5}{12}x^2)/\epsilon+\hbox{double poles}+O(x^3)\)
  and the resulting
  \(\gamma_2(x)=x-\frac56x^2+O(x^3)\);
- the two-loop NLO Wilson-Fisher data for the one-component scalar:
  \(x_*=\epsilon/3+17\epsilon^2/81+O(\epsilon^3)\),
  \(\eta=\epsilon^2/54+O(\epsilon^3)\),
  \(\Delta_\phi=1-\epsilon/2+\epsilon^2/108+O(\epsilon^3)\),
  \(\Delta_{\phi^2}=2-2\epsilon/3+19\epsilon^2/162+O(\epsilon^3)\),
  \(y_t=2-\epsilon/3-19\epsilon^2/162+O(\epsilon^3)\),
  \(\nu=1/2+\epsilon/12+7\epsilon^2/162+O(\epsilon^3)\), and
  \(\omega=\epsilon-17\epsilon^2/27+O(\epsilon^3)\);
- the \(O(N)\) vector generalization with
  \(S_E=\int[\frac12(\partial\phi^i)^2+\frac12r_0\phi^i\phi^i
  +\frac{g_0}{4!}(\phi^i\phi^i)^2]\), the quartic vertex tensor
  \((g_0/3)(\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}
  +\delta_{il}\delta_{jk})\), and the singlet source
  \(S=\frac12\phi^i\phi^i\);
- the two-loop \(O(N)\) MS pole map
  \[
    g_0/(16\pi^2)=\mu^\epsilon\left[
    x+\frac{N+8}{3}\frac{x^2}{\epsilon}
    +x^3\left(\frac{(N+8)^2}{9\epsilon^2}
      -\frac{3N+14}{6\epsilon}\right)+O(x^4)\right],
  \]
  the source and field poles
  \(\log Z_{S,\rm src}^{\rm MS}
    =[-(N+2)x/3+5(N+2)x^2/18]/\epsilon+\cdots\),
  \(\log Z_\phi^{\rm MS}=-(N+2)x^2/(36\epsilon)+\cdots\), and the derived
  \(O(N)\) formulas for \(\beta_x^\epsilon\), \(\gamma_S\), \(\gamma_\phi\),
  \(x_*\), \(\eta\), \(\Delta_\phi\), \(\Delta_S\), \(y_t\), \(\nu\), and
  \(\omega\);
- the large-\(N\) collective coordinate \(u=Nx\), with
  \(\beta_u^\epsilon=-\epsilon u+u^2/3+O(1/N)\) and
  \(u_*=3\epsilon+O(1/N)\);
- the finite-cutoff Hubbard--Stratonovich/spherical-model saddle:
  introduce \(\rho=\phi^2/N\) and an auxiliary \(\sigma\), derive
  \(S_{\rm eff}/N=\int[U(\rho)-\sigma\rho/2]
  +\frac12\operatorname{Tr}_\Lambda\log(-\partial^2+\sigma)\), the gap
  equations \(U'(\rho)=m^2/2\), \(\rho=\Omega_D(m)\), and the critical
  expansion
  \(\Omega_D(m)-\Omega_D(0)=-K_Dm^{D-2}+O(m^2\Lambda^{D-4})\);
- the \(N=\infty\) dimensions
  \(\Delta_\phi=(D-2)/2\), \(\eta=0\), \(\Delta_\sigma=2\), and
  \(\nu=1/(D-2)\), derived from the vector propagator and the
  \(\sigma\)-bubble kernel \(B_D(p)\propto |p|^{D-4}\);
- the relation to the \(O(N)\) nonlinear sigma model in \(D=2+\tilde\epsilon\),
  including the constrained action, matching large-\(N\) saddle, and
  \(\beta_{\mathfrak g}
  =\tilde\epsilon\mathfrak g-(N-2)\mathfrak g^2/(2\pi)+O(\mathfrak g^3)\)
  for \(N>2\), with \(N=2\) separated as the BKT case;
- the formal status of \(\lambda_*(\epsilon)\): the perturbative calculation
  recursively determines coefficients of a formal small-\(\epsilon\) series
  for a zero of the beta vector field, not by itself an honest
  nonperturbative fixed-point existence theorem;
- the local uniqueness statement in the one-component \(\mathbb Z_2\)-even
  quartic chart: after writing \(\lambda=\epsilon u\), the nonzero branch
  \(u=16\pi^2/3+O(\epsilon)\) is uniquely determined near that root by the
  nonvanishing derivative of \(-u+(3/(16\pi^2))u^2\);
- the limitation that this local uniqueness does not classify other fixed
  points obtained from different field content, multicritical interactions,
  multi-coupling gauge/Yukawa systems, or decoupled products;
- the distinction between the dimensionless bare coordinate
  \(\mu^{-\epsilon}g_0\) and the finite renormalized 1PI coordinate
  \(\lambda(\mu)\);
- the field dimension
  \(\Delta_\phi=1-\epsilon/2+O(\epsilon^2)\);
- the two-loop sunset coefficient controlling \(\gamma_\phi\), including the
  symmetry factor \(1/6\), the massless two-point integral evaluation, and the
  resulting pole
  \(\partial\Sigma^{(2)}/\partial k^2
  =-\lambda^2/[12(16\pi^2)^2\epsilon]+\cdots\);
- the sign derivation from the negative self-energy derivative pole to the
  positive field anomalous dimension, through
  the pole part of \(Z_\phi^{\rm MS}\) and
  \(\frac12\beta_{\rm MS}(\lambda)\partial_\lambda\log Z_\phi^{\rm MS}\);
- why an \(x\)-independent \(\phi^2\) source is an IR-bad subtraction in the
  massless theory;
- why this infrared obstruction is not a failure of the local
  scaling-degree/contact-term extension theorem, whose hypotheses require an
  already-defined separated-point distribution;
- the momentum-dependent source definition for \(\phi^2\);
- the one-loop anomalous dimension
  \(\gamma_{2*}=\epsilon/3+O(\epsilon^2)\) and
  \(\Delta_{\phi^2}=2-2\epsilon/3+O(\epsilon^2)\);
- the mass perturbation as the relevant direction dual to \([O_2]\);
- the thermal eigenvalue
  \(y_t=D-\Delta_{\phi^2}=2-\epsilon/3+O(\epsilon^2)\);
- the source-space no-mixing condition behind the preceding formula: relevant
  exponents are eigenvalues of the even-scalar linearized source-RG matrix, and
  in the one-component \(\mathbb Z_2\)-even calculation the thermal block is
  one-dimensional after removing identity and redundant directions;
- the dimensionless mass/temperature coordinate
  \(\tau(\mu)=\mu^{-y_t}t\), its linearized flow
  \(\dd\tau/\dd\log\mu=-y_t\tau+\cdots\), and the linearized massless
  endpoint condition \(\tau=0\);
- the convention bridge to the Wilsonian chapter: the displayed 1PI equation is
  differentiated with respect to the increasing subtraction scale \(\mu\); with
  the infrared-oriented variable \(s_{\rm 1PI}=\log(\mu_0/\mu)\) it becomes
  \(\dd\tau/\dd s_{\rm 1PI}=y_t\tau+\cdots\), matching the Wilsonian
  \(s_{\rm W}=\log(\Lambda_0/\Lambda)\) orientation after a finite coordinate
  matching has been specified;
- the correlation-length exponent
  \(\nu=1/y_t=1/2+\epsilon/12+7\epsilon^2/162+O(\epsilon^3)\);
- the odd source \(h[\phi]\) and its eigenvalue
  \(y_h=D-\Delta_\phi
  =3-\epsilon/2-\epsilon^2/108+O(\epsilon^3)\), explaining that the
  one-tuning-condition statement is inside the \(\mathbb Z_2\)-even subspace,
  while a codimension-one submanifold statement requires the Banach-chart
  endpoint theorem from the Wilsonian chapter;
- the scaling of two-point functions in momentum and position space;
- the point-splitting interpretation of the properly renormalized
  \(\phi^2\) operator;
- the equation-of-motion relation
  \(\phi^3\propto \Box\phi\), its classical normalization
  \(\kappa_{\rm cl}=6/g_R\) when
  \([\phi^3]_\mu=\kappa_*(\mu)\Box\phi\), and the descendant dimension
  \(\Delta_{\phi^3}=\Delta_\phi+2\);
- the quartic operator anomalous dimension
  \(\omega=\beta'(\lambda_*)=\epsilon-17\epsilon^2/27+O(\epsilon^3)\) and
  \(\Delta_{\phi^4}=D+\omega
  =4-17\epsilon^2/27+O(\epsilon^3)>D\);
- the comparison table for \(d=4-\epsilon\), \(d=3\), and \(d=2\), with the
  last two rows explicitly not presented as consequences of the first-order
  epsilon expansion and with the third column labeled by a generic
  \(O_{\rm irr}\), not by \(\phi^4\), because lower-dimensional fixed-point CFTs
  have their own scaling operators;
- the provenance of the \(d=3\) numerical table entries and the \(d=2\) exact
  entries, including the identification of the \(d=3\) third-column entry with
  the leading \(\mathbb Z_2\)-even scalar irrelevant primary
  \(\varepsilon'\), and of the \(d=2\) irrelevant scalar entry with
  \(T\bar T\);
- the asymptotic status of the Wilson--Fisher epsilon expansion and the
  separate role of resummation when extracting finite-\(\epsilon\) numerical
  estimates.
- scaling coordinates as a finite local RG chart: the projected beta vector
  field, its linearization at the fixed point, relevant eigenvalues
  \(y_A=D-\Delta_A\), irrelevant eigenvalues
  \(\omega_\rho=\Delta_\rho-D\), and the endpoint-map definition of the
  critical surface, with a cross-reference to the finite-reference
  critical-surface theorem that supplies smooth codimension only under an
  explicit endpoint-map submersion hypothesis.
- dangerously irrelevant coordinates as properties of an irrelevant RG
  coordinate together with a specified observable and scaling sector, including
  the observable scaling form whose \(w\to0\) limit is singular;
- the canonical scalar/Ising equation-of-state example above four dimensions:
  the Gaussian dimensions \(y_t=2\), \(y_h=(D+2)/2\), \(y_g=4-D<0\), the
  Landau equation \(h=tM+gM^3/6\), the ordered solution
  \(M^2=-6t/g\), the singular scaling-function behavior
  \({\mathcal M}(-1,0,w)\sim(6/w)^{1/2}\), and the resulting mean-field
  exponents \(\beta_{\rm mag}=1/2\), \(\delta=3\), and hyperscaling failure;
- the upper-critical-dimensional \(D=4\) leading-log derivation from
  \(\dd x/\dd L=-3x^2+\cdots\) and
  \(\dd t/\dd L=(2-x+\cdots)t\), giving
  \(\xi\asymp |t|^{-1/2}(\log(1/|t|))^{1/6}\) and
  \(M\asymp |t|^{1/2}(\log(1/|t|))^{1/3}\) in the ordered sector.

## Claim Ledger

1. In \(4-\epsilon\) dimensions the classical relevance of \(g_0\) and the
   one-loop screening term can balance.
1a. The \(4-\epsilon\) graph integrals in the chapter are dimensional
    regularization: meromorphic continuation of loop-momentum graph
    coefficients, with subtractions and RG functions defined coefficient by
    coefficient in a formal perturbative expansion.
2. The nonzero perturbative zero is a formal small-\(\epsilon\) fixed-point
   coordinate.  Each finite truncation gives a zero up to higher-order
   residuals; existence of an exact RG fixed point or nonperturbative
   continuum QFT requires separate constructive, lattice, Wilsonian, or
   summability input.
3. In the one-component \(\mathbb Z_2\)-even quartic chart, the nonzero
   small-coupling branch is unique near
   \(\lambda=(16\pi^2/3)\epsilon\) as a formal branch; this is not a global
   classification of fixed points in scalar, gauge, or product theory spaces.
4. The fixed point is attractive in the infrared along the quartic direction.
4a. At two loops in the one-component scalar MS chart,
    \(x_*=\epsilon/3+17\epsilon^2/81+O(\epsilon^3)\).  This follows from the
    pole map and the fixed-regulator equation for \(g_0\), not from a separate
    assumption about the fixed point.
4b. The two-loop source and field pole coefficients give
    \(\gamma_2=x-\frac56x^2+\cdots\) and
    \(\gamma_\phi=x^2/12+\cdots\).  Substituting \(x_*\) yields
    \(\nu=1/2+\epsilon/12+7\epsilon^2/162+\cdots\) and
    \(\eta=\epsilon^2/54+\cdots\).  A next coefficient of \(\eta\) would require
    the three-loop field pole.
4c. The quartic irrelevant exponent is the linearized beta derivative
    \(\omega=\partial_x\beta_x^\epsilon(x_*)=
    \epsilon-17\epsilon^2/27+O(\epsilon^3)\), so the quartic-direction
    scaling dimension is \(D+\omega\).
4d. For \(O(N)\), the one-component calculation is recovered by \(N=1\), while
    the singlet exponents for finite \(N\) are obtained by tensor contractions
    in the quartic vertex.  The displayed \(O(N)\) formulas concern the
    singlet thermal block and the vector field; non-singlet operator sectors
    require separate representation-block diagonalization.
4e. In the \(N\to\infty\) sequence, \(x_*\to0\) but \(u_*=Nx_*\) stays finite.
    The large-\(N\) saddle gives \(\eta=0\), \(\Delta_\sigma=2\), and
    \(\nu=1/(D-2)\), and agrees with the large-\(N\) limit of the
    \(4-\epsilon\) expansion.
4f. The \(O(N)\) nonlinear sigma model provides a \(2+\epsilon\) chart of the
    same critical family for \(N>2\); the \(N=2\) case is not described by the
    perturbative fixed point because the one-loop coefficient vanishes.
5. The mass parameter must be tuned separately; inside the
   \(\mathbb Z_2\)-even subspace the fixed point is reached by imposing the
   massless endpoint condition.  Calling the tuned set a codimension-one
   submanifold requires the Banach-chart theorem and its endpoint-map
   nondegeneracy hypothesis.
6. Operator dimensions at the fixed point come from the same renormalized
   operator construction as before.
7. The \(\phi^2\) source must carry momentum to avoid an infrared-singular
   subtraction; this is an infrared kinematic condition, distinct from the
   ultraviolet definition of the local composite operator.
8. Without the \(\mathbb Z_2\) restriction, the odd source for \(\phi\) is
   also relevant.
9. The mass/temperature perturbation has eigenvalue
   \(y_t=D-\Delta_{\phi^2}\), hence
   \(\nu=1/y_t\) in the perturbative calculation.  The sign in
   \(\dd\tau/\dd\log\mu=-y_t\tau+\cdots\) is the increasing-scale convention; it
   becomes positive when the flow is parameterized by an infrared-oriented scale
   variable, as in the Wilsonian cutoff comparison.
10. Properly renormalized composite operators are finite local fields;
   unregulated products of distributions at coincident points are not
   definitions.
11. \(\phi^3\) is an equation-of-motion descendant of \(\phi\) at the fixed
   point.  In the action normalization
   \(g_R\phi^4/4!\), the classical proportionality coefficient in
   \([\phi^3]_\mu=\kappa_*(\mu)\Box\phi\) is
   \(\kappa_{\rm cl}=6/g_R(\mu)\); finite composite-operator conventions change
   it by a relative \(1+O(g_R)\) factor.
12. \(\phi^4\) is irrelevant at the interacting fixed point even though it is
   needed to reach that fixed point.
13. A finite critical surface is an endpoint condition \(u(\mu_R)=0\) in a
    local RG chart.  Its codimension is a theorem only when the endpoint map
    is \(C^k\) and submersive in the relevant coordinates; the linearized
    eigenvalue count alone is not that theorem.
13a. An irrelevant coordinate can be dangerously irrelevant only relative to
     a specified observable and scaling sector.  In the scalar/Ising
     equation of state above four dimensions, the quartic coordinate flows to
     zero at the Gaussian fixed point but the ordered magnetization and
     free-energy scaling functions are singular as \(g b^{4-D}\to0\).  This
     gives mean-field order-parameter exponents and invalidates naive
     hyperscaling, while preserving the Gaussian endpoint of separated
     critical correlators.
14. The epsilon expansion is a small-\(\epsilon\) asymptotic expansion unless a
    stronger summability result is stated.  The \(d=3\) and \(d=2\) entries in
    the dimension table are not obtained by evaluating a convergent Taylor
    series at \(\epsilon=1,2\).
15. The numerical \(d=3\) entries in the comparison table are imported
    conformal-bootstrap data for the Ising CFT and must carry provenance.  The
    exact \(d=2\) entries are minimal-model data; the dimension-four scalar
    irrelevant entry is \(T\bar T\), not an independent Virasoro primary.

## Figure Requirements

- Symmetric 1PI definition of the quartic coupling and the one-dimensional
  Wilson-Fisher flow.
- Comparison of the dimensionless bare coupling and the finite
  renormalized coupling at the fixed point.
- \(\phi^2\) operator renormalization figure: bad zero-momentum insertion,
  good momentum-carrying source, and one-loop graph.
- Critical surface figure in the \(\mathbb Z_2\)-even slice showing the
  relevant mass direction and the \(\tau=0\) trajectory into the
  Wilson-Fisher fixed point.
- Momentum-to-position scaling figure for \(\phi^2\) correlators.
- Operator-spectrum figure for \(\phi^3\) as descendant and \(\phi^4\) as
  irrelevant.

## Audit Notes

- 2026-05-22 source-certification pass: handwritten 253b pages 124--135 were
  checked against rendered source images and comparison transcriptions.  The
  manuscript now includes the finite-\(\epsilon\) one-loop coupling, the
  intermediate derivative used to extract \(\beta(\lambda)\), the fixed point
  and its IR direction, the bare/renormalized coupling distinction,
  \(O_1\) and \(O_2\) anomalous dimensions, the momentum-source cure for the
  \(\phi^2\) infrared subtraction, one-loop \(\gamma_2\), correlator scaling,
  the nonlocality caveat for modewise \([O_2(x)]\), point splitting, the
  \(O_3\) descendant relation, the \(O_4\) source analysis including the
  zero-source-momentum check, \(\gamma_{4*}=\beta'(\lambda_*)\), and the
  low-lying dimension table.
- 2026-05-24 issue #347 pass: removed the stray \(\lambda_4\) notation from the
  \(\phi^2\) anomalous-dimension and \(O_4\) linearized-RG sections; the chapter
  now uses \(\lambda\) uniformly for the quartic running coordinate.
- 2026-05-24 issue #348 pass: inserted the sunset-integral derivation of the
  field anomalous-dimension coefficient, showing the \(1/6\) graph symmetry
  factor, the two massless two-point integrations, the pole
  \(I(k)=-k^2/[2(4\pi)^4\epsilon]+\cdots\), and the resulting \(1/12\).
- 2026-05-24 issue #349 pass: inserted the residue-renormalization sign derivation
  from
  \(\partial_{k^2}\Sigma^{(2)}|_{\rm div}<0\)
  to \(\gamma_\phi>0\), displaying the pole part
  \(Z_\phi^{\rm MS}=1-a(\lambda)/\epsilon+\cdots\) and the fixed-regulator
  derivative with
  \(\beta_{\rm MS}(\lambda)=-\epsilon\lambda+O(\lambda^2)\).
- 2026-05-24 issue #350 pass: separated the symmetric momentum-subtraction
  chart from the minimal-subtraction pole chart; the two-loop sunset
  anomalous-dimension computation now uses \(Z_\phi^{\rm MS}\) and
  \(\lambda_{\rm MS}\), while the text states the finite-reparametrization
  argument that leaves \(\eta=\epsilon^2/54+O(\epsilon^3)\) unchanged at the
  displayed order.
- 2026-05-24 issue #351 pass: inserted the even-scalar source-space
  linearization \(d g^A/d\log\mu=-M^A{}_B g^B+O(g^2)\), stated that \(y_t\) is an
  eigenvalue after diagonalizing possible operator mixing, and explained why the
  one-component \(\mathbb Z_2\)-even thermal block is one-dimensional at the
  displayed order.
- Do not say that the epsilon expansion proves the \(d=3\) or \(d=2\) fixed
  points.
- Do not say that the perturbative zero of the \(4-\epsilon\) beta function is
  an honest fixed point of a nonperturbative RG flow unless a separate
  existence theorem or summability-and-reconstruction argument is supplied.
- Do not turn the one-coupling uniqueness statement into a global
  classification.  Name the chart and neighborhood, and contrast it with
  \(O(N)\), multicritical, gauge/Yukawa, and product fixed-point problems.
- Do not present the epsilon expansion as convergent.  If numerical
  finite-\(\epsilon\) extraction is discussed, state the resummation
  prescription and assumptions.
- Do not quote fixed-point numerical or exact table data without naming its
  external origin when it is not derived in the chapter.
- Do not present composite operators as unregulated products of fields.
- Do not describe the Wilson-Fisher fixed point as an attractor for arbitrary
  massive scalar theories; the mass direction must be tuned away.
- When saying the critical surface has codimension one, state both the
  \(\mathbb Z_2\)-even restriction and the Banach-chart endpoint-map
  hypotheses; the odd field source is relevant in the full local chart.
- Keep the Ising model itself for the next chapter.
- No reader-facing source-page references or course-note references.
- At the start of the chapter, classify dimensional regularization as a
  graph-level formal coefficientwise analytic continuation and state that the
  Wilson--Fisher beta functions, anomalous dimensions, and scaling dimensions
  are formal perturbative series unless a separate summability or
  constructive theorem is supplied.
- 2026-05-22 local-RG-chart pass: added a section making scaling coordinates
  into a finite projected RG chart, defining the critical surface as a
  relevant-coordinate endpoint condition, and deriving the linear tuning
  powers between \(\Lambda_0\) and \(\mu_R\).  This prepares the Ising
  universality statement to use the Wilsonian cutoff-removal estimate without
  treating universality as an informal identification of microscopic actions.
- 2026-05-24 issue pass: addressed #222 by qualifying the Wilson--Fisher
  dimension table with the asymptotic nature of the epsilon expansion and the
  need for separate Borel/conformal-Borel resummation assumptions at
  \(\epsilon=1\).
- 2026-05-24 issue pass: addressed #227 by replacing the unqualified
  perturbative-domain statement with a formal-series status convention for
  \(\lambda_*(\epsilon)\) and by recording that nonperturbative existence
  requires separate input.
- 2026-05-24 issue pass: addressed #228 by adding the local uniqueness
  argument for the one-component \(\mathbb Z_2\)-even quartic branch and by
  separating it from other fixed-point problems.
- 2026-05-24 issue pass: addressed #230 by replacing unqualified
  codimension-one critical-surface language with a linearized endpoint
  condition plus a cross-reference to the Banach-chart finite-reference
  critical-surface theorem.  The dossier now records that smoothness and
  codimension require a \(C^k\) endpoint map and submersion hypothesis.
- 2026-05-24 issue #238 pass: added provenance for the nonperturbative entries
  in the low-lying-dimension comparison table.  The \(d=3\) row now records
  numerical conformal-bootstrap origins and identifies the third column
  with \(\varepsilon'\); the \(d=2\) row is identified as exact Ising
  minimal-model data with \(\sigma\), \(\varepsilon\), and \(T\bar T\).
- 2026-05-24 issue #363 pass: renamed the comparison table's third column from
  \(\Delta_{\phi^4}\) to \(\Delta_{O_{\rm irr}}\), defining \(O_{\rm irr}\) as
  the leading nonredundant \(\mathbb Z_2\)-even scalar irrelevant deformation.
  The \(d=2\) entry is explicitly \(T\bar T\), not an unrenormalized fourth power
  of the spin field.
- 2026-05-24 issue #302 pass: added
  `def:wilson-fisher-dimensional-regularization-status`, making the
  dimensional-regularization and formal-series status explicit at the top of
  the chapter.
- 2026-05-24 issue #356 pass: normalized the equation-of-motion descendant
  coefficient by adding \(\kappa_{\rm cl}=6/g_R(\mu)\) and the convention
  dependence
  \(\kappa_*(\mu)=6g_R(\mu)^{-1}(1+O(g_R(\mu)))=6/g_R(\mu)+O(1)\).
- 2026-05-24 issue #433 pass: tied the Wilson--Fisher use of
  \(Z_\phi^{\rm MS}\) to the part-opening dictionary, so the sunset
  anomalous-dimension calculation is explicitly an MS pole-factor computation
  and not an LSZ residue normalization.
- 2026-05-25 issue #460 pass: added the two-loop \(N=1\) MS pole map,
  the \(\phi^2\) source pole, the algebra deriving
  \(\beta_x^\epsilon\), \(\gamma_2\), \(\gamma_\phi\), \(x_*\), \(\eta\),
  \(\Delta_\phi\), \(\Delta_{\phi^2}\), \(y_t\), \(\nu\), and \(\omega\), and
  updated the critical-surface, magnetic-exponent, quartic-irrelevant, and
  comparison-table formulas.  Added
  `calculation-checks/wilson_fisher_epsilon_checks.py` as a rational
  arithmetic regression check for the displayed epsilon-expansion algebra.
- 2026-05-25 issue #461 pass: added the \(O(N)\) Wilson-Fisher family, including
  the quartic tensor normalization, the finite-\(N\) two-loop singlet
  exponent algebra, the large-\(N\) collective coordinate \(u=Nx\), the
  Hubbard--Stratonovich/spherical-model saddle, and the \(2+\epsilon\)
  nonlinear sigma-model chart.  Added
  `calculation-checks/on_wilson_fisher_epsilon_checks.py` to check the
  rational \(O(N)\) epsilon-expansion formulas and the \(N=1\) reduction.
- 2026-05-25 issue #462 pass: added a chart-level definition of dangerously
  irrelevant coordinates, the \(D>4\) scalar/Ising equation-of-state derivation
  showing the singular quartic dependence of the ordered saddle, and the
  \(D=4\) leading-log derivation for \(\xi\) and ordered magnetization from the
  marginally irrelevant quartic flow.

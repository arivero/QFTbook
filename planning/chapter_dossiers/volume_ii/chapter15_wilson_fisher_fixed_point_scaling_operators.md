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
- the correlation-length exponent
  \(\nu=1/y_t=1/2+\epsilon/12+O(\epsilon^2)\);
- the odd source \(h[\phi]\) and its eigenvalue
  \(y_h=D-\Delta_\phi=3-\epsilon/2+O(\epsilon^2)\), explaining that the
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
  \(\gamma_{4*}=\beta'(\lambda_*)=\epsilon+O(\epsilon^2)\) and
  \(\Delta_{\phi^4}=4+O(\epsilon^2)>D\);
- the comparison table for \(d=4-\epsilon\), \(d=3\), and \(d=2\), with the
  last two rows explicitly not presented as consequences of the first-order
  epsilon expansion.
- the provenance of the \(d=3\) numerical table entries and the \(d=2\) exact
  entries, including the identification of the \(d=3\) \(\phi^4\) column with
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
   \(\nu=1/y_t\) in the perturbative calculation.
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
  numerical conformal-bootstrap origins and identifies the \(\phi^4\) column
  with \(\varepsilon'\); the \(d=2\) row is identified as exact Ising
  minimal-model data with \(\sigma\), \(\varepsilon\), and \(T\bar T\).
- 2026-05-24 issue #302 pass: added
  `def:wilson-fisher-dimensional-regularization-status`, making the
  dimensional-regularization and formal-series status explicit at the top of
  the chapter.
- 2026-05-24 issue #356 pass: normalized the equation-of-motion descendant
  coefficient by adding \(\kappa_{\rm cl}=6/g_R(\mu)\) and the convention
  dependence
  \(\kappa_*(\mu)=6g_R(\mu)^{-1}(1+O(g_R(\mu)))=6/g_R(\mu)+O(1)\).

# Volume II, Chapter 12 Dossier: The 1PI Renormalization Group

## Source Position

- Primary local source: second-sequence handwritten material, pages 97--110.
- Immediate predecessor: subdivergences and forest formulas.
- Immediate successor in the source order: renormalized operators and minimal
  subtraction.
- Role in the monograph: introduce scale-dependent coordinates on the
  renormalized 1PI effective action after locality of counterterms and
  subdivergence subtractions have been established.  This chapter is the 1PI,
  momentum-subtraction renormalization group; the Wilsonian construction is
  mentioned only to locate it as the later finite-cutoff action flow.

## Source And Reference Controls

- `SRC-QFT-PDF`: `references/253b lecture notes 2023.pdf`, pages 97--110;
  checked against rendered page images in
  `monograph/tex/build/source_visual_1pi_rg/` and compiled pages
  `/tmp/qft_ch32_rg_audit-215.png` through
  `/tmp/qft_ch32_rg_audit-226.png` on 2026-05-22.
- `SRC-BEN-COMPARISON`: `references/253b transcribed lecture notes.tex`,
  lines around the source-page block 97--110, used only as a comparison layer.
- `SRC-EXTERNAL`: exact-RG material in Rosten for the later Wilsonian
  comparison; standard BPHZ/locality controls from the previous chapter.  This
  chapter itself stays in Euclidean 1PI momentum-subtraction language and makes
  no foundational use of an axiomatic framework.

## Construction Task

The chapter must define:

- the ambient Euclidean perturbative setting and UV regulator;
- the status of that UV regulator as a cutoff class from
  `tab:regulator-integration-status-catalog`, with dimensional
  regularization separated as meromorphic graph assignment rather than a
  finite-regulator measure;
- the bare and renormalized scalar quartic Lagrangian in four dimensions;
- the exact connected two-point function, the self-energy
  \(\Sigma_R(k)\), and the scale-dependent field normalization \(Z(\mu)\);
- the scale-normalized field \([\phi]_\mu=Z(\mu)^{-1/2}\phi_R\);
- the symmetric Euclidean subtraction point for the four-point 1PI vertex;
- the running quartic coupling \(g(\mu)\) as a coordinate on the 1PI effective
  action;
- the one-loop finite relation between \(g(\mu)\) and \(g_R=g(0)\);
- nearby-scale comparison \(g(\mu')\) versus \(g(\mu)\);
- the beta function as a differential comparison of renormalized coordinates;
- the one-loop solution and Landau scale in four-dimensional scalar quartic
  theory, with perturbative domain stated;
- the separation between the spectral pole mass \(m_*\), a finite-subtraction
  mass coordinate \(m_R\), an MS/running relevant coordinate \(\lambda_2(\mu)\),
  and a cutoff or lattice bare coordinate \(m_0^2\);
- the rigorous triviality theorem for the standard four-dimensional positive
  lattice \(\lambda\phi^4\) and nearest-neighbor ferromagnetic Ising-type
  scaling-limit problems, separated from the perturbative Landau-scale
  argument and from broader UV-completion questions;
- general 1PI coordinates \(g_I(\mu)\) from Taylor coefficients of 1PI
  vertices;
- dimensionless coordinates
  \(\lambda_I(\mu)=\mu^{d_I-D}g_I(\mu)\);
- a renormalization chart for connected noncoincident correlators, including
  the bare-to-renormalized parameter map and field factor \(Z_\phi\);
- the Callan--Symanzik equation derived from \(\mu\)-independence of bare
  correlators, with the derivative conventions stated;
- the separation between auxiliary-scale dependence and dimensional
  homogeneity, including displayed dimensionful parameters;
- fixed-point field scaling dimensions as
  \(\Delta_\phi=d_\phi^{\rm eng}+\gamma_{\phi,\ast}\);
- logarithmic consistency in a cutoff expansion and the condition
  \(c_1=-b_1^2\);
- finite scheme redefinitions and the induced transformation of beta
  functions.
- the multi-coupling jet transformation law for beta functions, including the
  second-coordinate-derivative terms that enter the quadratic jet when the
  linear beta-function matrix \(M\) is nonzero.
- the precise sense in which the one-loop quadratic tensor is
  scheme-independent only for purely marginal coordinates after fixing the
  leading linear normalization, while the one-coupling two-loop invariance has
  no componentwise multi-coupling analogue without extra structure.
- the scheme-equivalence theorem for matched physical observables, stated with
  hypotheses on finite analytic matching, common regulated observable data,
  field/source coordinate normalizations, and infrared safety.
- the distinction between formal perturbative series, asymptotic expansions,
  convergent series, and Borel summability.
- the renormalon diagnostic as an observable- and scheme-dependent
  Borel-plane obstruction tied to momentum regions and running couplings.

## Claim Ledger

1. A scale-dependent 1PI coupling is a renormalized coordinate obtained by
   evaluating a specified 1PI vertex, with external field normalization fixed
   at the same scale.
1a. The symbol \(\Lambda\) denotes a cutoff regulator class; when the
    calculation is done dimensionally, the regulated object is a formal
    meromorphic graph assignment in \(D=d-\varepsilon\), not a measure on
    fields.
2. In four-dimensional scalar quartic theory, the one-loop four-point bubble
   changes the quartic coordinate while \(Z(\mu)=1+O(g_R^2)\) at that order.
3. The corresponding one-loop two-point tadpole is independent of \(k^2\), so
   it does not change the field normalization at this order.
4. The relation between \(g(\mu')\) and \(g(\mu)\) is finite after the UV
   regulator is removed when the counterterms of the previous chapters have
   been fixed.
5. Comparing nearby scales produces a differential equation whose right-hand
   side is the beta function in the chosen coordinate system.
6. For \(\mu\gg m_R\), the one-loop scalar quartic beta function is
   \(3g^2/(16\pi^2)+O(g^3)\) in the conventions of the source notes.
7. The pole mass is spectral data from an isolated Kallen--Lehmann atom.  The
   finite mass coordinate \(m_R\), the running relevant coordinate
   \(\lambda_2(\mu)\), and the bare cutoff coordinate \(m_0^2\) are related to
   it only after the subtraction scheme, matching condition, and scaling-limit
   spectral hypotheses have been specified.
8. The integrated one-loop equation resums leading logarithms, with validity
   controlled by the smallness of the running coupling throughout the interval
   being compared.
9. The one-loop scalar quartic flow has a perturbative Landau scale
   \(\mu_0=\mu'\exp(16\pi^2/(3g(\mu')))\); perturbation theory gives no
   controlled description at scales where the running coupling is large.
9a. The standard reflection-positive four-dimensional lattice
    \(\lambda\phi^4\) and nearest-neighbor ferromagnetic Ising-type critical
    or near-critical scaling limits covered by the Aizenman--Duminil-Copin
    theorem are Gaussian.  This is a nonperturbative
    constructive/probabilistic theorem, not a consequence of the one-loop
    Landau-scale equation, and it does not by itself rule out an exotic
    ultraviolet-complete local QFT agreeing with formal \(\phi^4_4\)
    perturbation theory to all orders.
10. For a general local operator \(O_I\) with mass dimension \(d_I\), the
   dimensionless coordinate \(\lambda_I(\mu)=\mu^{d_I-D}g_I(\mu)\) can have an
   autonomous beta function once explicit dimensionful ratios are encoded in
   the coordinate choice or treated as additional couplings.
11. The quadratic derivative coordinate satisfies
    \(g_{2,2}(\mu)=1-Z(\mu)\) in the chapter's self-energy and projector
    convention; the mass coordinate is
    \(\lambda_2(\mu)=\mu^{-2}Z(\mu)
    [g_2^{\rm bare}-\Sigma(k)|_{k^2=\mu^2}]\).
12. The Callan--Symanzik equation for noncoincident elementary-field
    correlators follows from differentiating
    \(G_{0,\Lambda}^{(n)}=Z_\phi^{n/2}G_R^{(n)}\) at fixed bare data.
13. Dimensional homogeneity is independent of the Callan--Symanzik equation;
    combining the two gives the fixed-point field dimension
    \(d_\phi^{\rm eng}+\gamma_{\phi,\ast}\).
14. The absence of explicit cutoff logarithms in beta functions imposes
   relations among higher logarithmic coefficients; at the displayed order,
   \(c_1=-b_1^2\).
15. A finite redefinition
    \(\widetilde\lambda=f(\lambda)=\lambda+\alpha\lambda^2+\cdots\) transforms
    beta functions by the chain rule; for one classically marginal coupling,
    the first two perturbative coefficients are invariant while later
    coefficients depend on the scheme.
15a. For several couplings, the beta function is a vector-field jet.  The
    linearization \(M\) transforms by similarity at a fixed point.  The
    quadratic jet \(B\) receives second-coordinate-derivative terms unless
    \(M=0\).  Thus one-loop tensor universality off the Gaussian point is a
    tensorial statement only in the purely marginal case with fixed linear
    normalization; the single-coupling \(b_2\) invariance has no general
    componentwise multi-coupling analogue.
16. If two schemes are finite analytic coordinate charts on the same regulated
    path-integral action family, and if the same on-shell or infrared-safe
    observable has a perturbative cutoff-removal limit after the matching map,
    then the two perturbative expansions agree after applying that matching
    map.  Off-shell kernels, beta-function components, anomalous-dimension
    matrices, and coincident-point contact conventions are chart-dependent
    representatives, not themselves physical invariants.
17. Perturbative beta functions and anomalous dimensions are generally formal
    or asymptotic expansions in a specified chart.  Their coefficients may be
    meaningful and scheme-related even when the infinite series has zero radius
    of convergence.  Borel summability, when available, is a separate analytic
    theorem requiring hypotheses on the Borel transform and singularities.
18. Renormalon statements must be made with an observable or coefficient
    function, expansion coordinate, scheme, and factorization prescription
    specified; they should not be presented as properties of the beta function
    alone.  In controlled running-coupling or bubble-chain analyses, integration
    over infrared or ultraviolet momentum regions can produce factorial growth
    and Borel singularities; positive-ray ambiguities require matching to
    nonperturbative or effective-field-theory data.

## Figure Requirements

- A scale-dependent 1PI-coordinate figure: field normalization, symmetric
  four-point vertex, and nearby-scale comparison.
- A subdiagram-reuse figure showing a lower-order scale-dependent 1PI
  subgraph appearing inside a larger graph.
- A scalar quartic one-loop vertex figure showing the tree vertex, the three
  distinct bubble channels, and local counterterm.
- A Landau-scale running figure with the perturbative domain separated from
  the strong-coupling region.
- A logarithmic-consistency figure showing nested one-loop subgraphs,
  permuted channels, and the double-logarithm condition.
- A scheme-change diagram showing coordinate charts on the same renormalized
  theory family.

## Audit Notes

- No reader-facing source-page references.
- Do not introduce perturbative scattering amplitudes in this chapter.
- The Wilsonian RG is only located for comparison; the construction appears
  later.
- State all regulators, fields, momenta, subtraction points, and scheme
  choices before formulas using them.
- Do not let the Callan--Symanzik equation appear as an asserted textbook
  formula.  It must be derived from the renormalization chart and from
  \(\mu\)-independence of bare quantities.
- Keep operator-insertion Callan--Symanzik equations in the next chapter; this
  chapter should only state the elementary noncoincident correlator equation
  and the handoff to operator mixing.
- The main text should explain the 1PI RG by its constructed data and finite
  comparisons, with any limitations placed in remarks after the construction.
- Scheme independence must be stated as a matched-observable theorem, not as
  equality at identical numerical coupling values in two schemes.
- Do not generalize the single-coupling \(b_1,b_2\) invariance to arbitrary
  multi-coupling beta-function components.  State the vector-field jet formula
  and the hypotheses under which the quadratic one-loop tensor is meaningful.
- Do not identify \(m_R\), \(\lambda_2(\mu)\), or \(m_0^2\) with a physical
  pole mass unless the pole equation or the scaling-limit spectral hypothesis
  has been stated.
- Do not identify a perturbative expansion with a convergent definition unless
  convergence or summability has actually been proved.
- 2026-05-22 page-level source/figure audit complete.  Handwritten pages
  97--110 were checked through
  `monograph/tex/build/source_visual_1pi_rg/253b_rg-097.png` through
  `253b_rg-110.png`; compiled pages were checked as
  `/tmp/qft_ch32_rg_audit-215.png` through
  `/tmp/qft_ch32_rg_audit-226.png`.
- 2026-05-24 issue pass: addressed #221 by adding a labeled scheme-equivalence
  theorem for matched physical observables, using regulated path-integral
  action parameters rather than a separate ``bare Lagrangian'' terminology.
- 2026-05-24 issue pass: addressed #222 by adding an asymptotic-series,
  large-order, and Borel-summability discussion to the 1PI RG chapter.
- 2026-05-24 issue pass: addressed #223 by adding a cautious renormalon
  discussion that avoids universal claims about all perturbative series and
  ties ambiguities to specified observables and matching data.
- 2026-05-24 issue pass: addressed #224 by stating the standard
  four-dimensional scalar triviality theorem at the Landau-scale discussion,
  with theorem-boundary language separating it from perturbative RG and from
  broader UV-completion questions.
- 2026-05-24 issue #234 pass: added the mass-data distinction.  The manuscript
  now defines the spectral pole mass from an isolated Kallen--Lehmann atom,
  separates it from finite-subtraction, MS/running, and lattice bare mass
  coordinates, proves the pole equation in the 1PI convention, and records the
  lattice correlation-length relation to the continuum gap.
- 2026-05-24 issue #239 pass: added the multi-coupling scheme-change jet
  formula for beta functions.  The manuscript now states exactly when the
  quadratic one-loop tensor is scheme-independent, why quadratic coefficients
  are coordinate-dependent when the linear beta-function matrix is present,
  and why the single-coupling two-loop invariant does not become a
  componentwise multi-coupling invariant.

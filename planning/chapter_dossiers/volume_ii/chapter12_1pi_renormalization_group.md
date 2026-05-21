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
  `monograph/tex/build/source_visual_1pi_rg/`.
- `SRC-BEN-COMPARISON`: `references/253b transcribed lecture notes.tex`,
  lines around the source-page block 97--110, used only as a comparison layer.
- `SRC-EXTERNAL`: exact-RG material in Rosten for the later Wilsonian
  comparison; standard BPHZ/locality controls from the previous chapter.  This
  chapter itself stays in Euclidean 1PI momentum-subtraction language and makes
  no foundational use of an axiomatic framework.

## Construction Task

The chapter must define:

- the ambient Euclidean perturbative setting and UV regulator;
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
- general 1PI coordinates \(g_I(\mu)\) from Taylor coefficients of 1PI
  vertices;
- dimensionless coordinates
  \(\lambda_I(\mu)=\mu^{d_I-D}g_I(\mu)\);
- logarithmic consistency in a cutoff expansion and the condition
  \(c_1=-b_1^2\);
- finite scheme redefinitions and the induced transformation of beta
  functions.

## Claim Ledger

1. A scale-dependent 1PI coupling is a renormalized coordinate obtained by
   evaluating a specified 1PI vertex, with external field normalization fixed
   at the same scale.
2. In four-dimensional scalar quartic theory, the one-loop four-point bubble
   changes the quartic coordinate while \(Z(\mu)=1+O(g_R^2)\) at that order.
3. The relation between \(g(\mu')\) and \(g(\mu)\) is finite after the UV
   regulator is removed when the counterterms of the previous chapters have
   been fixed.
4. Comparing nearby scales produces a differential equation whose right-hand
   side is the beta function in the chosen coordinate system.
5. For \(\mu\gg m_R\), the one-loop scalar quartic beta function is
   \(3g^2/(16\pi^2)+O(g^3)\) in the conventions of the source notes.
6. The integrated one-loop equation resums leading logarithms, with validity
   controlled by the smallness of the running coupling throughout the interval
   being compared.
7. The one-loop scalar quartic flow has a perturbative Landau scale
   \(\mu_0=\mu'\exp(16\pi^2/(3g(\mu')))\); perturbation theory gives no
   controlled description at scales where the running coupling is large.
8. For a general local operator \(O_I\) with mass dimension \(d_I\), the
   dimensionless coordinate \(\lambda_I(\mu)=\mu^{d_I-D}g_I(\mu)\) can have an
   autonomous beta function once explicit dimensionful ratios are encoded in
   the coordinate choice or treated as additional couplings.
9. The absence of explicit cutoff logarithms in beta functions imposes
   relations among higher logarithmic coefficients; at the displayed order,
   \(c_1=-b_1^2\).
10. A finite redefinition
    \(\widetilde\lambda=f(\lambda)=\lambda+\alpha\lambda^2+\cdots\) transforms
    beta functions by the chain rule; for one classically marginal coupling,
    the first two perturbative coefficients are invariant while later
    coefficients depend on the scheme.

## Figure Requirements

- A scale-dependent 1PI-coordinate figure: field normalization, symmetric
  four-point vertex, and nearby-scale comparison.
- A scalar quartic one-loop vertex figure showing the tree vertex, bubble
  channels, and local counterterm.
- A Landau-scale running figure with the perturbative domain separated from
  the strong-coupling region.
- A logarithmic-consistency figure showing nested one-loop subgraphs fixing
  the double logarithm.
- A scheme-change diagram showing coordinate charts on the same renormalized
  theory family.

## Audit Notes

- No reader-facing source-page references.
- Do not introduce perturbative scattering amplitudes in this chapter.
- The Wilsonian RG is only located for comparison; the construction appears
  later.
- State all regulators, fields, momenta, subtraction points, and scheme
  choices before formulas using them.
- The main text should explain the 1PI RG by its constructed data and finite
  comparisons, with any limitations placed in remarks after the construction.

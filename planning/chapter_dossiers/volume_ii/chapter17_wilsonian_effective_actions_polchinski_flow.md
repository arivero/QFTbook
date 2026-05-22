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
- the Gaussian field split \(\phi=\phi'+\widehat\phi\), including the shell
  kinetic term;
- the shell-integration formula defining \(L_{\Lambda'}[\phi']\);
- the infinitesimal Wilson-Polchinski equation, with functional-derivative
  conventions;
- the finite-shell derivation of the Wilson-Polchinski sign from
  \(\Lambda'=\Lambda-\delta\Lambda\);
- the diagrammatic meaning of its two terms: connecting two vertices and
  contracting two legs at one vertex;
- the linearized scaling-coordinate convention
  \(\dd u_\alpha/\dd\log\Lambda=-y_\alpha u_\alpha+\cdots\), with
  \(y_\alpha=D-\Delta_\alpha\);
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
- the role of finite dimensionless irrelevant bare couplings in lattice
  regularizations.
- the bridge to BPHZ and 1PI coordinates: finite-regulator equality of
  low-source connected functionals, Legendre transform to 1PI kernels, finite
  matching from Wilsonian local coordinates to 1PI subtraction coordinates,
  and the distinction between a Wilsonian vertex and a 1PI vertex.

## Claim Ledger

1. A Wilsonian effective action at scale \(\Lambda\) is a cutoff-dependent
   functional whose low-momentum generating functional is held fixed.
2. The smooth cutoff can be placed in the quadratic kernel, giving a regulated
   Gaussian covariance and a general local interaction functional.
3. Lowering \(\Lambda\) is represented exactly, at the formal path-integral
   level, by a decomposition of Gaussian covariance and integration over an
   independent shell field.
4. Before the shell source term is discarded, the split generating functional
   contains \(J(\phi'+\widehat\phi)\); the \(J\widehat\phi\) term vanishes only
   by the regulated support assumption on the source.
5. The infinitesimal shell-integration identity gives a functional differential
   equation for \(L_\Lambda\).
6. Locality of the Wilsonian action is a derivative expansion assumption tied
   to smooth cutoffs and scales below the cutoff, not a finite-operator
   ansatz.
7. With \(t=\log\Lambda\), relevance exponents obey
   \(\dd u/\dd t=-yu+\cdots\); positive \(y\) grows toward the infrared, while
   negative \(y\) is irrelevant.
8. In the quartic-sextic toy truncation, the irrelevant coupling approaches a
   cutoff-dependent function of the marginal coupling along IR flow; the
   transverse memory of the ultraviolet boundary condition is suppressed by
   the canonical irrelevant power.
9. Perturbative renormalizability is formulated by a limiting procedure:
   remove the UV cutoff while tuning bare couplings so selected physical
   couplings at a fixed reference scale remain fixed.
10. The perturbative argument requires explicit hypotheses on small couplings,
   mild beta-function variation, and control of omitted irrelevant operators.
11. Lattice QFT fits the same logic because finite dimensionless irrelevant
   lattice couplings correspond to dimensionful coefficients suppressed by
   powers of the UV cutoff.
12. The Wilsonian action \(L_\Lambda\) is an action for remaining low modes,
    not the 1PI effective action; it must be followed by low-mode integration
    and a Legendre transform before comparison with 1PI coordinates.
13. BPHZ, Wilsonian, and 1PI descriptions are related by maps.  BPHZ supplies
    local Taylor subtractions, Wilsonian RG supplies Gaussian pushforward in
    cutoff space, and 1PI RG supplies finite projected coordinates at a
    subtraction scale.
14. Beta-function components in Wilsonian and 1PI coordinates are comparable
    only after a matching map is chosen; under finite coordinate changes they
    transform by the chain rule.

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
- BPHZ--Wilsonian--1PI bridge diagram showing the bare regulated action,
  BPHZ \(R\)-operation, Wilsonian pushforward, low-source connected
  functional, Legendre transform, and coordinate projections.

## Audit Notes

- No reader-facing page references, course labels, or claims about rewriting
  pedagogy.
- Avoid compressed descriptions of renormalizability; state the limiting
  problem and the hypotheses.
- Keep the relevance sign convention consistent with the earlier chapters:
  \(y=D-\Delta\) and flow in \(\log\Lambda\) has linear term \(-yu\).
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

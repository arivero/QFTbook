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

## Claim Ledger

1. A Wilsonian effective action at scale \(\Lambda\) is a cutoff-dependent
   functional whose low-momentum generating functional is held fixed.
2. The smooth cutoff can be placed in the quadratic kernel, giving a regulated
   Gaussian covariance and a general local interaction functional.
3. Lowering \(\Lambda\) is represented exactly, at the formal path-integral
   level, by a decomposition of Gaussian covariance and integration over an
   independent shell field.
4. The infinitesimal shell-integration identity gives a functional differential
   equation for \(L_\Lambda\).
5. Locality of the Wilsonian action is a derivative expansion assumption tied
   to smooth cutoffs and scales below the cutoff, not a finite-operator
   ansatz.
6. With \(t=\log\Lambda\), relevance exponents obey
   \(\dd u/\dd t=-yu+\cdots\); positive \(y\) grows toward the infrared, while
   negative \(y\) is irrelevant.
7. In the quartic-sextic toy truncation, the irrelevant coupling approaches a
   cutoff-dependent function of the marginal coupling along IR flow; the
   transverse memory of the ultraviolet boundary condition is suppressed by
   the canonical irrelevant power.
8. Perturbative renormalizability is formulated by a limiting procedure:
   remove the UV cutoff while tuning bare couplings so selected physical
   couplings at a fixed reference scale remain fixed.
9. The perturbative argument requires explicit hypotheses on small couplings,
   mild beta-function variation, and control of omitted irrelevant operators.
10. Lattice QFT fits the same logic because finite dimensionless irrelevant
   lattice couplings correspond to dimensionful coefficients suppressed by
   powers of the UV cutoff.

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

## Audit Notes

- No reader-facing page references, course labels, or claims about rewriting
  pedagogy.
- Avoid slogan-level descriptions of renormalizability; state the limiting
  problem and the hypotheses.
- Keep the relevance sign convention consistent with the earlier chapters:
  \(y=D-\Delta\) and flow in \(\log\Lambda\) has linear term \(-yu\).
- In the two-coordinate toy figures, call the renormalized trajectory a curve,
  not a surface.
- Do not introduce Yang-Mills content in this chapter.
- Do not treat axiomatic QFT frameworks as the foundation of this construction.

# 2026-05-22 Wilsonian Effective Actions Source/Figure Audit

## Scope

- Source block: `references/253b lecture notes 2023.pdf`, pages 147--156.
- Manuscript home:
  `monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex`.
- Rendered source images checked:
  `monograph/tex/build/source_visual_trace/253b_trace-147.png` through
  `monograph/tex/build/source_visual_trace/253b_trace-156.png`.
- Rendered manuscript pages checked after rebuild:
  physical PDF pages 243--252 of `monograph/tex/main.pdf`.

## Source Content Checked

- Wilsonian scalar action in Euclidean signature,
  \(S_\Lambda=S_{\mathrm{kin},\Lambda}+L_\Lambda\), with the cutoff in the
  quadratic kernel.
- Smooth cutoff profile \(\chi(k^2/\Lambda^2)\), regulated propagator, and
  the figure showing low-momentum plateau and ultraviolet suppression.
- General momentum-space expansion of \(L_\Lambda[\phi]\).
- Equality \(Z_{\Lambda'}[J]=Z_\Lambda[J]\) for sources supported below the
  lowered cutoff.
- Covariance split \(C_\Lambda=C_{\Lambda'}+\widehat C_{\Lambda,\Lambda'}\),
  field split \(\phi=\phi'+\widehat\phi\), and shell kinetic term.
- The source-supported split of \(Z_\Lambda[J]\), including the
  \(J(\phi'+\widehat\phi)\) term before the shell-source contribution is
  removed.
- Shell-integration formula defining \(L_{\Lambda'}[\phi']\).
- Wilson--Polchinski equation, its sign from
  \(\Lambda'=\Lambda-\delta\Lambda\), and the two diagrammatic terms.
- Quartic-sextic toy flow in \(D=4\), dimensionless variables
  \(\lambda_4=g_4\), \(\lambda_6=\Lambda^2g_6\), the transverse combination
  \(h=\lambda_6+\frac b2\lambda_4^2\), and the induced marginal beta function.
- Wilsonian continuum-limit formulation with \(\Lambda_0\to\infty\),
  fixed \(\lambda_4(\Lambda_R)=\lambda_4^R\), existence of
  \(\lim_{\Lambda_0\to\infty}\lambda_6(\Lambda_R)\), and finite irrelevant
  bare couplings in lattice regularizations.

## Manuscript Changes

- Added the explicit split generating functional before using source support:
  the displayed formula now contains
  \(J(x)(\phi'(x)+\widehat\phi(x))\) and then states the regulated support
  condition under which the \(J\widehat\phi\) term vanishes.
- Improved the continuum-limit figure by adding visible mid-trajectory RG
  arrows and the label "RG flow toward \(\Lambda_R\)" so the direction of the
  source sketch is not hidden at the endpoint.

## Rendered Figure Check

- Figure 35.1: smooth cutoff profile and lowered-cutoff shell support match the
  source cutoff sketch.
- Figure 35.2: propagator split and shell integration show low field,
  independent shell field, dashed shell contraction, and resulting low-field
  interaction.
- Figure 35.3: Wilson--Polchinski diagram displays both terms with the correct
  relative minus sign and shell-line weight.
- Figure 35.4: quartic-sextic flow shows IR attraction toward the slaved curve
  \(\lambda_6=-\frac b2\lambda_4^2+O(\lambda_4^3)\).
- Figure 35.5: continuum-limit diagram now shows ultraviolet-regulated actions on
  \(\lambda_6(\Lambda_0)=0\), flow toward the fixed reference scale, increasing
  cutoff direction, the \(\lambda_4^R\) slice, and the limiting value as
  \(\Lambda_0\to\infty\).

## Verification

- `tools/build_monograph.sh` completed successfully after the manuscript
  changes.
- Strict monograph text audit was clean.
- Rendered PDF page check was performed on pages 243--252; no cropped equations
  or overlapping labels were found in the audited Wilsonian block.

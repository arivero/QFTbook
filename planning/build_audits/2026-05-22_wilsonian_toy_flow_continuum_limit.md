# Wilsonian Toy Flow And Continuum-Limit Audit

Date: 2026-05-22

Scope:
- `monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex`
- `planning/chapter_dossiers/volume_ii/chapter17_wilsonian_effective_actions_polchinski_flow.md`

Changes:
- Made the projected Wilsonian beta-function convention explicit:
  \[
    \beta_A(\lambda)=\Lambda\frac{\dd\lambda_A}{\dd\Lambda}.
  \]
- Replaced the compressed quartic-sextic discussion with the transverse
  coordinate
  \[
    h=\lambda_6+\frac b2\lambda_4^2,
  \]
  and displayed its canonical suppression
  \[
    h(\Lambda)=h(\Lambda_*)\left(\frac{\Lambda}{\Lambda_*}\right)^2+\cdots.
  \]
- Clarified that the quartic beta function obtained after eliminating
  \(\lambda_6\) is the induced beta function in the Wilsonian coordinate
  system, and that comparison with a 1PI beta function requires a finite
  coordinate redefinition.
- Expanded the continuum-limit argument for the boundary condition
  \(\lambda_6(\Lambda_0)=0\), showing explicitly that the memory of this
  ultraviolet condition at fixed \(\Lambda_R\) is suppressed by
  \((\Lambda_R/\Lambda_0)^2\).
- Corrected the two-coordinate continuum-limit figure to call the
  renormalized trajectory a curve rather than a surface.
- Adjusted the quartic-sextic flow figure label so the rendered equation is
  not crossed by arrows or the attracting curve.

Verification:
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`
- Rendered and inspected PDF pages 245--248, then re-rendered pages 246--248
  after the figure-label adjustment.

Residual risks:
- The toy model remains a two-coordinate projection. Its purpose is to display
  the exact-RG mechanism of irrelevant-coordinate slaving, not to compute the
  complete scalar \(\phi^4\) beta function in a specified renormalization
  convention.

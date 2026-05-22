# Wilsonian Relevance Sign Convention Audit

Date: 2026-05-22

Scope:
- `monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex`
- `planning/chapter_dossiers/volume_ii/chapter17_wilsonian_effective_actions_polchinski_flow.md`

Changes:
- Inserted a finite-shell derivation of the Wilson-Polchinski sign for
  \(\Lambda'=\Lambda-\delta\Lambda\), starting from the Gaussian convolution
  identity and comparing the expansion of \(L_{\Lambda-\delta\Lambda}\).
- Fixed the linearized scaling-coordinate convention to
  \[
    \frac{\dd u_\alpha}{\dd\log\Lambda}
    =
    -y_\alpha u_\alpha+O(u^2),
    \qquad
    y_\alpha=D-\Delta_\alpha .
  \]
- Reworded relevance and irrelevance accordingly: positive \(y_\alpha\)
  grows under infrared lowering of the cutoff, while negative \(y_\alpha\)
  gives an irrelevant direction.
- Corrected the irrelevant-coordinate suppression factor to
  \[
    u_i(\Lambda_R)
    =
    \left(\frac{\Lambda_R}{\Lambda_0}\right)^{-y_i}u_i(\Lambda_0)+\cdots,
    \qquad y_i<0,
  \]
  with suppression exponent \(-y_i=\Delta_i-D>0\).
- Updated the chapter dossier so future development preserves the same
  sign convention.

Verification:
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`
- Rendered and inspected PDF pages 242--244, covering the Wilson-Polchinski
  equation figure, the finite-shell sign derivation, the linearized-flow
  convention, and the irrelevant-coordinate suppression formula.

Residual risks:
- The chapter still gives only a scalar-field presentation of the exact
  RG equation. Later gauge-field chapters should introduce gauge-compatible
  cutoff flow with their own regulator and Ward/Slavnov-Taylor bookkeeping,
  rather than reusing this scalar derivation without qualification.

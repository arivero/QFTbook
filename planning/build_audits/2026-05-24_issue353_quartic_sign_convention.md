# 2026-05-24 Issue #353 Quartic Sign Convention Audit

## Issue

GitHub issue #353 flagged that the momentum-subtraction quartic coordinate
\[
  g(\mu)=-Z_{\rm MOM}(\mu)^2\Gamma_R^{(4)}
\]
uses a sign convention that was not explicitly related to the minimal-
subtraction coefficient convention.

## Edits

- Added the tree-level convention
  \[
    \Gamma_{\rm tree}^{(4)}=-g_R .
  \]
- Stated that the explicit minus sign in \(g(\mu)\) makes the 1PI coordinate
  agree with the positive coefficient of \(\phi^4/4!\) in the Euclidean action.
- Added a label to the scalar-quartic minimal-subtraction section and linked the
  sign convention to the coefficient relation
  \[
    g^\epsilon=\mu^\epsilon\left[
      \lambda+\frac{3}{16\pi^2}\frac{\lambda^2}{\epsilon}+\cdots
    \right].
  \]
- Clarified that the momentum-subtraction and minimal-subtraction formulas use
  the same positive quartic-coordinate orientation; the explicit minus appears
  only when extracting the coordinate from the 1PI vertex.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports 757 pages.

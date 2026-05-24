# 2026-05-24 Issue #351 Thermal No-Mixing Audit

## Issue

GitHub issue #351 flagged that the Wilson--Fisher chapter used
\[
  y_t=D-\Delta_{\phi^2}
\]
and then \(\nu=1/y_t\), without stating that the thermal source is already a
linearized scaling coordinate.  In a sector with operator mixing, the relevant
exponent is an eigenvalue of the linearized source-RG matrix.

## Edits

- Added the finite even-scalar source-space notation \(g^A O_A\), with identity
  and redundant equation-of-motion or total-derivative directions removed.
- Displayed the linearized source RG
  \[
    \frac{d g^A}{d\log\mu}=-M^A{}_B g^B+O(g^2).
  \]
- Stated that relevant exponents are eigenvalues of \(M^A{}_B\), after
  diagonalizing operator mixing.
- Explained why, in the one-component \(\mathbb Z_2\)-even scalar theory at the
  displayed order, the thermal block is one-dimensional: the identity is vacuum
  energy, \([O_2]_\mu\) is the only nontrivial relevant even scalar in the block,
  and the quartic direction is irrelevant at \(O(\epsilon)\).
- Stated how the formula changes in a theory with a degenerate even scalar:
  \(t\) must be replaced by an eigen-coordinate and \(y_t\) is the corresponding
  matrix eigenvalue.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 756 pages.

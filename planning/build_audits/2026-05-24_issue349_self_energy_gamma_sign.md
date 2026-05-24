# 2026-05-24 Issue #349 Self-Energy Pole and Gamma Sign Audit

## Issue

GitHub issue #349 flagged that the Wilson--Fisher chapter displayed the
negative divergent coefficient
\[
  \left.\partial_{k^2}\Sigma^{(2)}(k)\right|_{\rm div}
  =
  -\frac{\lambda^2}{12(16\pi^2)^2}\frac1\epsilon
\]
and then immediately wrote a positive field anomalous dimension, without
displaying the intervening sign derivation.

## Edits

- Added the intermediate coefficient
  \(a(\lambda)=\lambda^2/[12(16\pi^2)^2]\).
- Displayed the pole part of the residue condition
  \[
    Z=(1-\partial_{k^2}\Sigma)^{-1}
    =
    1-a(\lambda)/\epsilon+O(\lambda^3,\epsilon^0).
  \]
- Displayed the fixed-regulator derivative
  \[
    \frac12\mu\frac{d}{d\mu}\log Z
    =
    \frac12\beta(\lambda)\partial_\lambda[-a(\lambda)/\epsilon]
    =
    a(\lambda)+O(\lambda^3),
  \]
  using \(\beta(\lambda)=-\epsilon\lambda+O(\lambda^2)\).

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 755 pages.

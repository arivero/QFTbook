# 2026-05-24 Issue #350 Scheme Separation Audit

## Issue

GitHub issue #350 flagged that the Wilson--Fisher chapter defined a finite
momentum-subtraction residue factor
\[
  Z_{\rm MOM}(\mu)
  =
  \left(1-\partial_{k^2}\Sigma\right)^{-1}_{k^2=\mu^2}
\]
but then used a minimal-subtraction pole computation for
\(\gamma_\phi\), without saying which scheme was operative.

## Edits

- Identified the symmetric Euclidean subtraction formulas as the
  momentum-subtraction chart \((\lambda_{\rm MOM},Z_{\rm MOM})\).
- Stated that \(Z_{\rm MOM}\) is a finite residue normalization and must not be
  identified with a pole-subtraction field factor.
- Rewrote the scaling-operator calculation to use the minimal-subtraction pole
  chart explicitly:
  \[
    \phi_0=(Z_\phi^{\rm MS})^{1/2}\phi_{\rm MS},
    \qquad
    Z_\phi^{\rm MS}=1+\sum_{r\ge 1}Z_{\phi,r}/\epsilon^r .
  \]
- Replaced the ambiguous \(Z\) in the two-loop sign derivation by
  \(Z_\phi^{\rm MS}\) and wrote the pole projection explicitly.
- Added the finite-reparametrization check:
  \[
    \phi'=F(\lambda)^{-1}\phi,\qquad
    \gamma_\phi'=\gamma_\phi+\beta\,\partial_\lambda\log F,
  \]
  so the exact fixed-point value is scheme-independent, and at the displayed
  order the finite coupling shift changes \(\gamma_\phi=A\lambda_*^2+\cdots\)
  only at \(O(\epsilon^3)\).
- Updated the Wilson--Fisher chapter dossier.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 756 pages.

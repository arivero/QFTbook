# 2026-05-24 Issue #348 Sunset Coefficient Derivation Audit

## Issue

GitHub issue #348 flagged that the Wilson--Fisher chapter asserted
\[
  \left.\frac{\partial\Sigma^{(2)}(k)}{\partial k^2}\right|_{\rm div}
  =
  -\frac{\lambda^2}{12(16\pi^2)^2}\frac1\epsilon
\]
without deriving the load-bearing \(1/12\) coefficient used for
\(\eta=\epsilon^2/54+O(\epsilon^3)\).

## Edits

- Added the sunset graph structure
  \[
    \Sigma_{\rm sun}^{(2)}(k)=\frac{\lambda^2}{6}\mu^{2\epsilon}
    \int_{p,q}\frac1{p^2q^2(p+q+k)^2}.
  \]
- Displayed the first massless two-point integration over \(q\).
- Displayed the remaining massless two-point integral over \(p\), giving
  \[
    I(k)=-\frac{k^2}{2(4\pi)^4}\frac1\epsilon+\cdots .
  \]
- Explained that the \(1/2\) comes from \(\Gamma(3)^{-1}\), equivalently the
  Feynman-parameter normalization, and that multiplying by the sunset symmetry
  factor \(1/6\) gives \(1/12\).
- Updated the Wilson--Fisher chapter dossier.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 755 pages.

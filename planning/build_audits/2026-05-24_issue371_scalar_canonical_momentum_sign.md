# Issue 371: Free-Scalar Canonical Momentum Sign

## Scope

GitHub issue #371 noted that Volume I, Chapter 6 gave
\(\Pi=\partial_t\phi\) for the free scalar but did not display the
signature-dependent calculation from the covariant mostly-plus Lagrangian.

## Fix

- Added the explicit derivative
  \[
    \frac{\partial\mathcal L}{\partial(\partial_0\phi)}
    =
    -\eta^{0\nu}\partial_\nu\phi
    =
    -\partial^0\phi
    =
    \partial_0\phi
    =
    \partial_t\phi .
  \]
- Stated that the cancellation comes from the minus sign in the covariant
  kinetic term and the mostly-plus index raise
  \(\partial^0=\eta^{00}\partial_0=-\partial_0\).
- Updated the Chapter 6 dossier notation and claim ledgers.

## Verification Plan

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

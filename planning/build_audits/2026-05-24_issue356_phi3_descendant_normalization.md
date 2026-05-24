# 2026-05-24 Issue #356 Phi-Cubed Descendant Normalization Audit

## Issue

GitHub issue #356 flagged that the Wilson--Fisher descendant relation
\[
  [\phi^3]_\mu=\kappa_*(\mu)\,\Box\phi
\]
did not anchor the normalization of \(\kappa_*(\mu)\).

## Edits

- Inserted the named proportionality coefficient
  \(\kappa_*(\mu)\) in the descendant relation.
- Derived the classical normalization from the action convention
  \(g_R(\mu)\phi^4/4!\):
  \[
    \kappa_{\rm cl}(\mu)=\frac{3!}{g_R(\mu)}=\frac{6}{g_R(\mu)}.
  \]
- Stated the scheme/convention dependence of the finite composite-operator
  normalization as
  \[
    \kappa_*(\mu)
    =
    \frac{6}{g_R(\mu)}(1+O(g_R(\mu)))
    =
    \frac{6}{g_R(\mu)}+O(1).
  \]
  The relative form records the perturbative normalization cleanly; the
  additive form makes explicit that finite composite-operator choices shift
  the coefficient by \(O(1)\), not by a universal number.
- Updated the Wilson--Fisher chapter dossier with the normalization claim.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports 757 pages.

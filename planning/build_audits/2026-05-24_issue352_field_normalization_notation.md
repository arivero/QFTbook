# 2026-05-24 Issue #352 Field-Normalization Notation Audit

## Issue

GitHub issue #352 flagged that chapter 10 used three nearby symbols,
\(Z_R\), \(Z(\mu)\), and \(Z_\phi\), without giving the reader a translation
map among the initial renormalized-field convention, the finite
momentum-subtraction field rescaling, and the total bare-to-renormalized field
factor entering the Callan--Symanzik equation.

## Edits

- Renamed the finite scale-dependent momentum-subtraction factor in chapter 10
  from \(Z(\mu)\) to \(Z_{\rm MOM}(\mu)\).
- Added Definition~\(\ref{def:three-field-normalization-factors}\), which
  separates:
  \(Z_R\), the cutoff-dependent initial reference factor;
  \(Z_{\rm MOM}(\mu)\), the finite rescaling
  \([\phi]_\mu=Z_{\rm MOM}(\mu)^{-1/2}\phi_R^{\rm ref}\);
  and \(Z_\phi\), the total bare-to-chart factor
  \(\phi_R^{\rm chart}=Z_\phi^{-1/2}\phi_0\).
- Displayed the product relation
  \[
    Z_\phi^{\rm chart}=Z_\phi^{\rm ref}Z_{\rm MOM}(\mu).
  \]
- Stated that if the reference field is normalized by the same
  momentum-subtraction condition at \(\mu_{\rm ref}\), then
  \(Z_{\rm MOM}(\mu_{\rm ref})=1\); the cutoff dependence is in
  \(Z_\phi^{\rm ref}\), not in the finite rescaling.
- Updated the chapter dossier.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 756 pages.

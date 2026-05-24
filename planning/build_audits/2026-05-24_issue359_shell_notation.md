# 2026-05-24 Issue #359 Shell Notation Audit

## Issue

GitHub issue #359 flagged a possible collision between a hatted shell-field
notation and the use of tildes/Fourier modes in the Wilson-Polchinski
derivation.

## Edits

- Added an explicit notation sentence in the Wilsonian shell-split paragraph:
  the shell field is always \(\phi_{\mathrm{sh}}\), while
  \(\widehat C_{\Lambda,\Lambda'}\) denotes the covariance difference.
- Stated that the shell field is not denoted by \(\widehat\phi\).
- Updated the chapter dossier to replace the residual
  \(\widehat\phi\) shell notation by \(\phi_{\mathrm{sh}}\), including the
  source-support claim \(J\phi_{\mathrm{sh}}=0\).
- Recorded the convention that hats are reserved for covariance differences,
  not shell fields.

## Verification

- `rg -n -F "\\widehat\\phi" monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex planning/chapter_dossiers/volume_ii/chapter17_wilsonian_effective_actions_polchinski_flow.md` returns no matches.
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports 757 pages.

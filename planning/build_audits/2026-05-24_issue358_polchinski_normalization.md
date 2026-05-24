# 2026-05-24 Issue #358 Polchinski Normalization Audit

## Issue

GitHub issue #358 flagged that the Wilsonian shell integration defined
\[
  \exp\{-L_{\Lambda'}[\phi']\}
\]
only up to a \(\phi'\)-independent normalization, while the subsequent
Wilson-Polchinski derivation did not explain why that normalization is absent
from the displayed functional-derivative flow.

## Edits

- Added a paragraph immediately after the Wilson-Polchinski derivation.
- Identified the omitted field-independent normalization as the vacuum-energy
  coordinate \(c_\Lambda\).
- Stated that retaining it replaces \(L_\Lambda[\phi]\) by
  \(L_\Lambda[\phi]+c_\Lambda\), adding only
  \(\Lambda\partial_\Lambda c_\Lambda\) to the left side of the flow.
- Stated explicitly that the functional derivatives on the right side
  annihilate \(c_\Lambda\), so the displayed Polchinski equation is the
  interaction flow modulo the vacuum-energy normalization.
- Updated the chapter dossier so the construction task and claim ledger record
  this convention.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports 757 pages.

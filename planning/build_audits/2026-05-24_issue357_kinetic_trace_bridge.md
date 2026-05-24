# 2026-05-24 Issue #357 Kinetic Trace Bridge Audit

## Issue

GitHub issue #357 flagged that the stress-tensor chapter checked scale
invariance of the free kinetic term and then wrote the bare trace identity
\[
  T^\mu{}_\mu=\sum_I\delta_I(\epsilon)g_I^\epsilon O_I
\]
without saying explicitly why the kinetic term no longer appears.

## Edits

- Labeled the direct kinetic-variation calculation as
  `eq:volume-ii-kinetic-scale-invariance-check`.
- Inserted the bridge statement before the first-order interaction variation:
  the full variation is the sum of kinetic and interaction variations, the
  kinetic part vanishes in the engineering convention for compactly supported
  dilatation variations, and therefore the nonderivative trace term comes only
  from the interaction coordinates.
- Updated the stress-tensor chapter dossier so the claim ledger records that
  the bare trace identity has only interaction terms precisely because the
  kinetic contribution has vanished.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports 757 pages.

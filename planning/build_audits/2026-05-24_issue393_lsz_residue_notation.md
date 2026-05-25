# Issue #393 LSZ Residue Notation Pass

## Scope

- GitHub issue #393: standardize the one-particle pole residue notation across
  the scattering chapters.
- Manuscript locus:
  `monograph/tex/volumes/volume_i/chapter13_lsz_reduction_and_the_s_matrix.tex`.
- Planning locus:
  `planning/chapter_dossiers/volume_i/chapter13_lsz_reduction.md`.

## Content Changed

- Replaced the LSZ one-particle residue \(Z\) by \(Z_\phi\) throughout the
  LSZ chapter.
- Preserved the source-functional notation \(Z[J]\), \(Z_-[J]\), and
  \(Z_E[J_E]\), so the generating functional and the one-particle residue are
  no longer denoted by the same symbol in the same chapter.
- Updated the interpolating-field rescaling paragraph to use
  \(Z_{\phi'}=|a|^2Z_\phi\).
- Verified that the Bethe--Salpeter chapter already states the convention
  relating the unamputated amplitude to \(Z_\phi\) and the LSZ-normalized
  amplitude.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`: 771 pages.

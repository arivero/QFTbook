# Issue 434: Partial-Wave Amplitude Symbol

Date: 2026-05-24.

Issue:

- GitHub #434 flagged that Volume I introduced the ordered \(16\pi\)
  partial-wave amplitude as \(a_\ell(s)\), while the later bound-state chapter
  used \(\mathcal M_\ell(s)\) for the same projected coefficient.

Fix:

- Renamed the bound-state chapter's projected partial-wave coefficient to
  \(a_\ell(s)\) in the expansion, projection formula, \(S_\ell\) relation,
  below-threshold pole formula, and pole figure label.
- Added an explicit sentence that the bound-state chapter is using the ordered
  \(16\pi\) convention fixed in the cross-section/unitarity chapter.
- Updated the Volume I and Volume II dossiers so \(a_\ell(s)\) is recorded as
  the common ordered \(16\pi\) partial-wave amplitude.

Verification:

- `rg -n -F "\\mathcal M_\\ell"` over the affected manuscript and dossier
  files now returns only historical audit-note references to the rename.
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports 785 pages.

# Ninth-Chapter Development Pass Build Audit

Date: 2026-05-25.

Scope:
- Added ninth chapters to Volumes VI-XII and included them in the corresponding
  volume manifests.
- Added matching chapter dossiers for each new chapter.
- Updated the master architecture and systematic development matrix to record
  the ninth-chapter pass.

Verification:
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `rg -n -P '\\over(?![A-Za-z])' monograph/tex`: no raw TeX `\over`
  occurrences.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean; final PDF
  `monograph/tex/main.pdf` has 1096 pages.

Rendered PDF spot checks:
- Chapter 70 opening rendered from physical page 922.
- Chapter 79 opening rendered from physical page 956.
- Chapter 88 opening rendered from physical page 984.
- Chapter 97 opening rendered from physical page 1010.
- Chapter 106 opening rendered from physical page 1038.
- Chapter 115 opening rendered from physical page 1068.
- Chapter 124 opening rendered from physical page 1094.

Corrections made during verification:
- Removed math-mode commands from chapter and section titles that feed PDF
  bookmarks.
- Split two long checklist displays into two-line gathered displays to remove
  overfull hboxes.

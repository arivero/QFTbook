# Eighth-Chapter Development Pass Build Audit

Date: 2026-05-25.

Scope:
- Added eighth chapters to Volumes VI-XII and included them in the corresponding
  volume manifests.
- Added matching chapter dossiers for each new chapter.
- Updated the master architecture and systematic development matrix to record
  the eighth-chapter pass.

Verification:
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `rg -n -P '\\over(?![A-Za-z])' monograph/tex`: no raw TeX `\over`
  occurrences.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean; final PDF
  `monograph/tex/main.pdf` has 1071 pages.

Rendered PDF spot checks:
- Chapter 69 opening rendered from physical page 917.
- Chapter 77 opening rendered from physical page 947.
- Chapter 85 opening rendered from physical page 971.
- Chapter 93 opening rendered from physical page 994.
- Chapter 101 opening rendered from physical page 1019.
- Chapter 109 opening rendered from physical page 1046.
- Chapter 117 opening rendered from physical page 1069.

Corrections made during verification:
- Corrected the Volume XII Chapter 8 cross-reference to the actual
  point-splitting stress-tensor chapter label.
- Broke the Witten-Donaldson/Seiberg-Witten comparison chain into an aligned
  display to avoid an overfull hbox.
- Shortened one open-problem display title in the supersymmetric moduli-space
  chapter to avoid a marginal overfull hbox.
- Confirmed the sine-Gordon and affine-Toda action signs against the declared
  mostly-plus Lorentzian convention.

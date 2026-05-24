# Issue 515 AQFT Theorem References

Date: 2026-05-24

Scope:
- Strengthened `monograph/tex/volumes/volume_iv/chapter04_superselection_sectors_and_locality_properties.tex`.
- Addressed GitHub issue #515 on deep AQFT theorems stated without proof
  sources.

Changes:
- Added per-theorem proof references to the Doplicher--Roberts reconstruction
  theorem, including the DHR sector papers, the compact-group duality theorem,
  and the field-algebra reconstruction paper.
- Added per-theorem proof references to the Tomita--Takesaki modular
  automorphism theorem, including Takesaki's Lecture Notes in Mathematics
  volume and the operator-algebra monograph formulation.
- Added per-theorem proof references to the Bisognano--Wichmann wedge theorem,
  including the 1975 scalar-field paper, the 1976 general Wightman-field
  paper, and Haag's AQFT account.

Verification:
- `git diff --check` clean.
- `tools/audit_monograph_text.sh` clean.
- `tools/audit_chapter_dossiers.sh` clean.
- `tools/build_monograph.sh` clean; rebuilt
  `monograph/tex/main.pdf`.

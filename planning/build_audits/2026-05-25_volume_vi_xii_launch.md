# 2026-05-25 Volume VI--XII Launch Audit

## Scope

- Launched compiled Volumes VI--XII through `monograph/tex/main.tex`.
- Added first chapters for integrable QFT, supersymmetric QFT,
  topological/cohomological QFT, global structure, thermal QFT and
  hydrodynamics, constructive/lattice/numerical QFT, and curved-spacetime QFT.
- Recorded the full open-issue review as a subject-development map instead of
  an old-to-new closure queue.

## Verification Plan

- Run `git diff --check`.
- Run `tools/audit_monograph_text.sh`.
- Run `tools/audit_chapter_dossiers.sh`.
- Run `tools/build_monograph.sh`.
- Inspect the compiled page count with `pdfinfo monograph/tex/main.pdf`.
- Render representative pages from the new volume openings after the build.

## Verification Results

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean after fixing a duplicate KMS label and an
  overfull route display in the constructive opening chapter.
- `pdfinfo monograph/tex/main.pdf`: 912 pages.
- Rendered and inspected physical PDF pages 881, 885, 889, 892, 895, 899, and
  903, corresponding to the printed chapter openings 857, 861, 865, 868, 871,
  875, and 879 for Volumes VI--XII.

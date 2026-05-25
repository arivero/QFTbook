# 2026-05-25 Systematic Second-Chapter Development Audit

## Scope

- Added second compiled chapters for Volumes VI--XII.
- Tightened the harness to state the monograph's frontier-development
  standard and local-reference-intake protocol.
- Replaced negative contrast in new drafts with positive object-level
  definitions where feasible.
- Demoted entanglement/replica material out of the compiled CFT spine and into
  `deprecated/volume_iii_premature_topics/`, pending an AQFT/local-algebraic
  treatment.
- Sharpened Volume VII on particle multiplets versus off-shell superfield
  variables, supersymmetric Wilsonian schemes, the unsettled status of
  manifest supersymmetric regularization, localization data, and examples in
  \(2D\), \(3D\), \(4D\), and \(6D\).
- Sharpened Volume VIII to include Witten--Donaldson theory and the
  Donaldson/Seiberg--Witten relation as an RG comparison problem with an
  explicit theorem-status ledger.

## Verification Plan

- Run `git diff --check`.
- Run `tools/audit_monograph_text.sh`.
- Run `tools/audit_chapter_dossiers.sh`.
- Run `tools/build_monograph.sh`.
- Inspect `pdfinfo monograph/tex/main.pdf`.
- Render representative pages from the added chapters after the clean build.

## Verification Results

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `rg -n '\\over([^A-Za-z]|$)' monograph/tex`: no active primitive `\over`
  occurrences.
- `tools/build_monograph.sh`: clean after fixing an overfull heading in the
  Donaldson--SW open problem.
- `pdfinfo monograph/tex/main.pdf`: 931 pages.
- Rendered representative pages:
  `/private/tmp/qft_second_chapters_render/susy_final2-889.png`,
  `/private/tmp/qft_second_chapters_render/susy_final2-891.png`, and
  `/private/tmp/qft_second_chapters_render/tqft_final_more-899.png`.

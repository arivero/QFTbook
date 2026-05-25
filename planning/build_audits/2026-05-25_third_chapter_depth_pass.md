# 2026-05-25 Third-Chapter Depth Pass Audit

## Scope

- Added third compiled chapters for Volumes VI--XII:
  Yang--Baxter consistency, supersymmetric gauge theory, BF theory, line and
  surface defects, Schwinger--Keldysh real-time formalism, lattice reflection
  positivity, and trace anomalies.
- Tightened `planning/12_strict_writing_harness.md` with a section-level depth
  rule requiring primitive objects, symbol definitions, statement status, and
  an argument or construction in every reader-facing section.
- Moved the spinor and gamma-matrix convention material from the end of the
  monograph into the first spinor-field chapter as a local section, and
  updated active TeX cross-references to point to that section.

## Verification Plan

- Run `git diff --check`.
- Run `tools/audit_monograph_text.sh`.
- Run `tools/audit_chapter_dossiers.sh`.
- Run `rg -n '\\over([^A-Za-z]|$)' monograph/tex`.
- Run `tools/build_monograph.sh`.
- Inspect `pdfinfo monograph/tex/main.pdf`.
- Render representative pages from the moved spinor section and new third
  chapters after a clean build.

## Verification Results

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean after replacing a negative framing in
  the line/surface/domain-wall chapter by a positive definition statement.
- `tools/audit_chapter_dossiers.sh`: clean.
- `rg -n '\\over([^A-Za-z]|$)' monograph/tex`: no matches.
- `tools/build_monograph.sh`: clean; no unresolved references and no overfull
  boxes reported by the final log scan.
- `pdfinfo monograph/tex/main.pdf`: 952 pages, letter paper, PDF 1.5.
- Representative rendered pages inspected:
  `/tmp/qft_spinor_section_p542.png`, `/tmp/qft_yang_baxter_p892.png`,
  `/tmp/qft_susy_gauge_p905.png`, and `/tmp/qft_trace_anomaly_p950.png`.
  The spinor conventions now appear as Section 38.13 inside the spinor-field
  development, and the new Volume VI, VII, and XII chapters render with
  convention blocks, definitions, and displayed formulae intact.

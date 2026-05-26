# 2026-05-25 Issue 563: Quotedtheorem Attribution Rule

## Scope

Issue #563 asked the manuscript to distinguish locally proved theorems from
literature-quoted theorem boundaries by introducing a `quotedtheorem`
environment and requiring explicit source attribution.

## Edits

- Confirmed that `monograph/tex/preamble.tex` defines `quotedtheorem` as a
  numbered theorem-like environment labelled "Quoted Theorem".
- Tightened `planning/12_strict_writing_harness.md` so every
  `quotedtheorem` block must state its hypotheses and conclusion, state its
  local role, and name the external source or source lineage in the block or
  immediately following reader-facing paragraph.
- Added explicit source-lineage text near representative `quotedtheorem`
  uses: the \(P(\phi)_2\) cluster-output theorem, the
  Bisognano--Wichmann theorem, the framed cobordism hypothesis, and the
  stochastic-quantization/regularity-structures theorem boundaries.

## Targeted Verification

No calculation script was edited for this LaTeX/planning infrastructure pass.

## Repository Verification

- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

The monograph build and log scan completed cleanly after rephrasing the SPDE
attribution sentence to remove an overfull box.  The rebuilt PDF has 1290
pages.

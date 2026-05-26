# 2026-05-25 Issue 558: Dynamic Phi4_3 SPDE Theorem Package

## Scope

Issue #558 asked Volume XI Chapter 9 to display the theorem-level content of
the stochastic-quantization/regularity-structures construction: local
well-posedness, renormalized convergence, invariant measure, and
identification with constructive \(\Phi^4_3\) Euclidean data.

## Edits

- Expanded the quoted dynamic \(\Phi^4_3\) theorem package into four explicit
  clauses: smooth cutoff local well-posedness, BPHZ-renormalized convergence,
  invariant laws for the limiting Markov process, and equality with the
  constructive Euclidean \(\Phi^4_3\) Schwinger hierarchy after matching
  finite-volume regulator and local coordinates.
- Clarified that the four clauses are logically distinct and that invariant
  law construction is not the same as identifying the Euclidean QFT measure.
- Added a reference pointer to stochastic Yang--Mills as a gauge-theory SPDE
  laboratory, without treating it as a completed four-dimensional gauge-QFT
  construction.
- Updated the Volume XI Chapter 9 dossier to record the theorem package and
  the continuing self-contained proof obligation tracked separately by
  issue #582.

## Targeted Verification

No calculation script was edited for this text-only theorem-boundary pass.

## Repository Verification

- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

The monograph build and log scan completed cleanly.  The rebuilt PDF has
1290 pages.

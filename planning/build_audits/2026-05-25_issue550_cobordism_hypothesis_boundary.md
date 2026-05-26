# 2026-05-25 Issue 550: Cobordism Hypothesis Boundary Statement

## Scope

Issue #550 flagged that the framed fully extended cobordism hypothesis was
being treated too much like a locally proved theorem and that the
dualizability hypotheses were hidden behind a placeholder phrase.

## Edits

- Kept the statement in `quotedtheorem` form rather than as a locally proved
  theorem.
- Rewrote the theorem statement to spell out full \(D\)-dualizability:
  ordinary dualizability, adjoints for evaluation and coevaluation
  \(1\)-morphisms, and iterated adjointability through level \(D\).
- Added the \(D=1\) and \(D=2\) specializations to anchor the definition.
- Added reader-facing source-lineage text naming Baez--Dolan, Lurie, and
  modern low-dimensional/derived-geometric expositions such as
  Calaque--Scheimbauer.
- Updated the Volume VIII Chapter 2 dossier.

## Targeted Verification

No calculation script was edited for this theorem-boundary precision pass.

## Repository Verification

- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

The monograph build and log scan completed cleanly. The rebuilt PDF has
1290 pages.

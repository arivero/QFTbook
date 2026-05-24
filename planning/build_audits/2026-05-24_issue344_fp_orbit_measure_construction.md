# 2026-05-24 Issue #344 Faddeev--Popov Orbit Measure Audit

## Issue

GitHub issue #344 flagged that the gauge-fixing chapter introduced division by
the gauge-group volume and the Faddeev--Popov identity without displaying the
underlying orbit-measure construction.

## Edits

- Added `prop:fp-orbit-measure-construction` to the gauge-fixing, ghosts, and
  BRST chapter.
- The proposition works on a finite-regulator regular field-space chart, or a
  Sobolev local Hilbert-manifold chart with determinant regularization
  specified.
- It formulates \(q:U\to U/\mathcal G_\Lambda\) as a local principal-bundle
  quotient with a section \(F=0\).
- It defines the orbit measure as the pushforward of right Haar density along
  \(\xi\mapsto\phi^\xi\).
- It proves the orbit identity
  \(\int_{\mathcal O_\phi}\delta(F)|\det\mathcal M_F|=1\) under the
  one-intersection transversality hypothesis.
- It states the quotient-density representation
  \(\delta(F)|\det\mathcal M_F|\dd\mu_\Lambda\) tested on gauge-invariant
  functions.
- It separates the positive Euclidean density \(|\det\mathcal M_F|\) from the
  oriented determinant \(\det\mathcal M_F\) represented by ghosts in
  perturbation theory.
- Updated the chapter dossier with the orbit-measure construction and new
  symbols.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 753 pages.

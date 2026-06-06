# 2026-06-06 Issue #755 BCFT Coherence Sewing Ledger

## Scope

- Issue lane: #755 editorial quality and coherence drift.
- Secondary issue lane: #625/#697 BCFT sewing proof architecture.
- Manuscript target: Volume V, Chapter 14, immediately after the Liouville
  nonrational analytic sewing datum and before the rational
  Frobenius/module theorem boundary.

## Re-Audit

- Concern addressed: recent BCFT insertions had accumulated many local finite
  cells.  The chapter already had strong local material, but the transition
  from diagonal rational examples through Liouville nonrational data to the
  Frobenius/module construction could ask too much of the reader.
- Editorial decision: do not add another finite identity.  Add a compact
  sewing-move ledger that classifies existing cells by the elementary sewing
  move they test and by the still-missing global datum.
- TeX scope: prose/table only; no planning directive or issue-process
  language was inserted into the monograph.

## Manuscript Change

- Added a `Sewing-move map for the examples` paragraph and table.
- The map separates:
  - open/closed annulus checks from open Hilbert-space positivity and boundary
    field compatibility;
  - Ising/Cardy boundary OPE cells from common-domain and higher-move sewing
    requirements;
  - bulk-boundary/direct-sum normalization from metric, operator-map, and
    Chan--Paton trace data;
  - Liouville Plancherel/residue cells from nuclear test spaces, positive
    spectral measures, operator domains, and global contour prescriptions;
  - finite anomaly/move-defect models from generated move graphs and
    determinant-line trivialization.

## Verification Plan

- Focused Chapter 14 style/theorem/label/negative-scope audits.
- Dossier and monograph text audits.
- Full monograph build, because the table is TeX-visible.

## Verification Results

- `python3 tools/audit_theorem_form.py
  monograph/tex/volumes/volume_v/chapter14_boundary_conformal_field_theory.tex`
  passed.
- `python3 tools/audit_unnumbered_display_labels.py
  monograph/tex/volumes/volume_v/chapter14_boundary_conformal_field_theory.tex`
  passed.
- `tools/audit_negative_scope_prose.py --fail
  monograph/tex/volumes/volume_v/chapter14_boundary_conformal_field_theory.tex`
  passed.
- `tools/audit_style_density.py --root monograph/tex/volumes/volume_v
  --window 120 --stride 60 --fail --limit 20` passed after the TeX paragraph
  was tightened from "ledger/datum" wording to "map/input" wording.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/audit_monograph_text.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed; the rebuilt PDF is
  `monograph/tex/main.pdf` at 3410 pages with a clean log scan.

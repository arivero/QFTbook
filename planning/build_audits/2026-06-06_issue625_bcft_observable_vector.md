# 2026-06-06 Issue 625 BCFT Observable-Vector Audit

## Scope

- Targeted Volume V, Chapter 14, the BCFT Cardy--Lewellen sewing lane.
- Added a boundary-observable vector architecture after the annulus-shadow
  nonreconstruction diagnostic.
- The edit organizes annulus, disk, bulk-boundary, boundary-OPE, two-point,
  defect-endpoint, and closed-loop sewing outputs as projections of one
  boundary datum, with separate chiral, open-sector, local-coordinate,
  pairing, generated-move, and anomaly-line residuals.

## Quality Audit

- This is architecture work, not another isolated finite BCFT identity.
- It addresses the coherence risk that annulus, stabilizer, Liouville, and
  move-budget cells could read as cumulative proof of full BCFT sewing.
- The TeX states a physics-facing construction dependency; issue/process
  bookkeeping remains in planning files.
- The new companion evidence strengthens the existing dependency-separation
  check into an assembled boundary-observable vector with residual transport.

## Verification

- `python3 -m py_compile calculation-checks/bcft_cardy_checks.py`
- `python3 calculation-checks/bcft_cardy_checks.py`
- `tools/run_calculation_checks.sh --python-only --only bcft_cardy`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_v/chapter14_boundary_conformal_field_theory.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_v/chapter14_boundary_conformal_field_theory.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_v/chapter14_boundary_conformal_field_theory.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_v/chapter14_boundary_conformal_field_theory.tex --window 120 --stride 60 --fail --limit 20`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`

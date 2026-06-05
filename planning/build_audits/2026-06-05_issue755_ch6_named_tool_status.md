# 2026-06-05 Issue #755 Chapter 6 Named-Tool Status Audit

## Scope

- Target: Volume II Chapter 6, especially the heavily developed analyticity,
  Cutkosky, generalized-unitarity, Steinmann, and Landau spine.
- Objective: address the #755 named-physics-theorem sub-pass by making point
  of use status visible for named tools instead of allowing conventional names
  to imply proof strength.
- Boundary: no new amplitude cell, no new theorem claim, and no process
  directive inserted into monograph TeX.

## Changed Artifacts

- `monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`
- `planning/chapter_dossiers/volume_ii/chapter06_analyticity_crossing_landau.md`

## Re-Audit Notes

- Added `rem:chapter06-named-tool-status-ledger` near the chapter entrance.
- Tightened the generalized-unitarity opening so Cutkosky is used as a
  perturbative physical-cut theorem with explicit regulator/state/sheet data,
  while generalized cuts remain algebraic reconstruction probes.
- This pass is a coherence/status repair for a dense chapter rather than
  additional lemma accumulation.

## Verification

- `python3 -m py_compile calculation-checks/generalized_unitarity_reduction_checks.py`
- `python3 calculation-checks/generalized_unitarity_reduction_checks.py`
- `tools/run_calculation_checks.sh --python-only --only generalized_unitarity_reduction_checks`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
- Date: 2026-06-05.

# 2026-06-07 Issue #844 Hori--Vafa Branch-Status Repair

## Scope

- Target issue: #844, with local relevance to #847.
- Monograph target:
  `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`.
- Audit target: `tools/audit_theorem_form.py`.

## Substance

- Reclassified the Coulomb one-loop branch/monodromy block from
  `controlledapproximation` to a `remark`.
- Renamed the current label to `rem:glsm-coulomb-one-loop-branch-monodromy`.
- The content is retained: component determinant response fixes the local
  logarithm sign; logarithm-sheet shifts are transported by integral periods of
  the compact logarithmic FI coordinate \(T\); \(\exp(T)\) remains the physical
  gauge-flux fugacity; compact periodicity is not a sign oracle.
- Extended the theorem-form audit so a `controlledapproximation` title
  containing `ledger` must carry visible approximation controls and a component
  estimate, just like `gate`, `map`, `diagnostic`, and `laboratory`.

## Quality Audit

- This is a status-surface repair, not a demotion of the physics.  The branch
  bookkeeping remains useful convention control before any Hori--Vafa formula
  is used, but it no longer receives the visual status of a controlled
  continuum approximation.
- The repair reinforces the #847 scrutiny rule: compact flux periodicity tests
  \(2\pi\) normalization and branch transport, while the determinant sign must
  come from the component determinant/Fujikawa calculation.
- Process language remains in this planning note, not in the TeX.

## Verification

- `python3 -m py_compile tools/audit_theorem_form.py`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail --limit 40`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- `bash tools/audit_monograph_text.sh monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 -m json.tool calculation-checks/evidence_contracts.json >/dev/null`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

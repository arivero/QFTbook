# 2026-06-07 Issue #597 Spectral Local-Green Matching Evidence

## Scope

- Target issue: #597, instantons as physical amplitudes.
- Monograph target:
  `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- Added `ca:instanton-spectral-local-green-matching-test`.

## Quality Audit

- This pass addresses the prior weakness that the local Green-function
  companion was too close to a subtraction template.  The new text chooses a
  concrete zero-mode-deleted spectral regulator and separates two source
  classes before any subtraction is made.
- Smooth external sources are represented by a spectral pairing whose tail is
  controlled by source decay.  Local/coincident source coordinates are
  represented by a diagonal shell expansion with explicit `A0 N`, `A1 H_N`,
  finite counterterm, and summable remainder data.
- The physics boundary is explicit: the calculation tests source-class and
  local-matching architecture for a normal-mode regulator.  It does not claim
  the continuum Pauli-Villars determinant constant, a complete instanton
  measure, or a phenomenological instanton regime.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  passed.
- `PYTHONPATH=calculation-checks python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  passed.
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
  passed.
- Metadata audits passed:
  `python3 -m json.tool calculation-checks/evidence_contracts.json >/dev/null`;
  `python3 tools/audit_calculation_check_inventory.py`;
  `python3 tools/audit_calculation_evidence_contracts.py`;
  `tools/audit_chapter_dossiers.sh`.
- Focused Chapter 20D audits passed:
  `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`;
  `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`;
  `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`;
  `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --window 120 --stride 60 --fail --limit 20`;
  `tools/audit_monograph_text.sh monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- TeX process-language scan passed:
  `rg -n "claude|review|directive|monitor|issue #|GitHub|planning/build_audits" monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
  returned no matches.
- Global calculation suite passed:
  `tools/run_calculation_checks.sh --python-only`.
- Global build passed:
  `tools/build_monograph.sh`, producing
  `monograph/tex/main.pdf`.

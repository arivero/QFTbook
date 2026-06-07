# 2026-06-07 Issue #597 Normal-Green Source-Class Repair

## Scope

- Target issue: #597, instantons as physical amplitudes.
- Monograph target:
  `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- Repaired `ca:instanton-subtracted-normal-green-matching`.

## Quality Audit

- This is a physics-scope correction, not new moduli-space infrastructure.
  The previous normal-Green block treated subtraction as if it were required
  for any source bilinear.  The repaired text first declares the
  source/operator class: smooth smeared sources, local/composite source
  coordinates, and background-minus-vacuum differences are different
  observables.
- The local subtraction formula is retained, but only for declared
  local/composite or background-subtracted coordinates.  Smooth smeared
  source pairings keep ordinary primed propagation and are not subjected to a
  default free-propagator subtraction.
- The residual budget now includes the Green/resolvent norm multiplying the
  projector error, rather than treating projector uncertainty as an
  untyped scalar.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  passed.
- `PYTHONPATH=calculation-checks python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  passed.
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
  passed.
- Focused Chapter 20D audits passed:
  `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`;
  `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`;
  `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`;
  `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --window 120 --stride 60 --fail --limit 20`;
  `tools/audit_monograph_text.sh monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- TeX process-language scan passed:
  `rg -n "claude|review|directive|monitor|issue #|GitHub|planning/build_audits" monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
  returned no matches.
- Metadata audits passed:
  `python3 -m json.tool calculation-checks/evidence_contracts.json >/dev/null`;
  `python3 tools/audit_calculation_check_inventory.py`;
  `tools/audit_chapter_dossiers.sh`;
  `python3 tools/audit_calculation_evidence_contracts.py`.
- Global calculation suite passed:
  `tools/run_calculation_checks.sh --python-only`.
- Global build passed:
  `tools/build_monograph.sh`, producing
  `monograph/tex/main.pdf`.

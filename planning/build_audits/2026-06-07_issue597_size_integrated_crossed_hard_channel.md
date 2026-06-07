# 2026-06-07 Issue 597 Size-Integrated Crossed Hard Channel Audit

## Scope

- Targeted Volume II, Chapter 20D, the instantons-as-physical-amplitudes
  chapter.
- Added `ca:instanton-size-integrated-crossed-hard-channel` after the
  hard-window tail-subtraction block.
- The pass turns the scalar coefficient entering the crossed \(RR\to LL\)
  channel into a retained-window, common-regulator amplitude coordinate:
  source determinants, Haar projection, nonzero-mode source quotient,
  amputation, crossing, running collective factor, two endpoint tails, and
  helicity residual propagation are kept in one calculation.

## Quality Audit

- This is an amplitude-assembly pass, not another moduli-space or ADHM
  expansion.
- The size integral is not treated as a formal density integral: the core,
  leading endpoint tail, subleading endpoint tail, and residual are separate
  physical coefficient data.
- The scalar retained coefficient is still separated from the fixed-helicity
  external-state amplitude and from spin-summed rates.
- The TeX contains only the physics calculation and its residual obligations.
  Issue/review/directive language remains in planning files.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --window 120 --stride 60 --fail --limit 20`
- `rg -n "directive|claude_review|GitHub|issue #|monitor|planning/build_audits" monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex` (zero matches)
- `bash tools/audit_monograph_text.sh monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

# 2026-06-07 Issue 597 Crossed Chiral Channel Audit

## Scope

- Targeted Volume II, Chapter 20D, the instantons-as-physical-amplitudes
  chapter.
- Added `ca:instanton-thooft-crossed-chiral-channel` after the amputated
  four-point assembly.
- The pass extracts a massless \(RR\to LL\) scattering channel from the
  all-outgoing two-flavor 't Hooft source kernel by selecting the anomalous
  \(Q=1\) source monomial first, then crossing the barred slots with LSZ
  residues.

## Quality Audit

- This is a physics-amplitude extraction pass, not another ADHM or
  moduli-space expansion.
- The anti-instanton sector is kept as the conjugate \(LL\to RR\) channel
  rather than inserted into the same massless \(RR\to LL\) amplitude.
- The text distinguishes the theta-charged one-instanton amplitude coordinate
  from a positive rate: a rate is a quadratic neutral projection, while a
  theta-linear observable needs an explicit chirality-breaking reference,
  mass insertion, or CP-paired comparison.
- Issue/review/directive language remains in planning files; the TeX only
  states the physical calculation and residual obligations.

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

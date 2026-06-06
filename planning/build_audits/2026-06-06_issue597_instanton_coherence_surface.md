# 2026-06-06 Issue 597 Instanton Coherence Surface Audit

## Scope

- Targeted Volume II, Chapter 20D, after several rapid instanton-amplitude
  insertions.
- Repaired reader-facing surface language so the chapter presents a physical
  amplitude route: source functional, gauge-sliced zero-mode Jacobian,
  chirality-source selection, and observable maps.
- Kept stable labels and cross-references unchanged; equations and companion
  finite checks are unchanged in substance.

## Quality Audit

- This pass addresses chapter coherence after dense local insertions.
- It does not add a new instanton cell, ADHM/moduli-space material, or
  tangential mathematics.
- The visible monograph text now avoids process-facing gate/ledger/discipline
  titles in the edited instanton chapter, while planning and evidence files
  record the audit history.
- No planning directives, GitHub issue text, monitoring language, or
  review-thread instructions were inserted into monograph TeX.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --window 120 --stride 60 --fail --limit 20`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`

# 2026-06-06 Issue #844 Integrable Observable-Map Audit

## Scope

- Reframed the Volume VI Chapter 1 end-to-end route block as an observable
  reconstruction map.
- Clarified that route residuals are named slots until estimates in a common
  observable norm or topology are supplied.
- Updated the Chapter 1 dossier and calculation-check inventory.
- Extended `calculation-checks/factorized_scattering_algebra_checks.py` with a
  negative control against treating nonzero physical-projection residuals as
  irrelevant.

## Quality Intent

This pass addresses the architecture risk that exact integrable data can sound
like direct evidence for physical local observables.  The reader-facing chapter
now separates exact scattering, TBA, and dressing coordinates from the
Hilbert-space, local-algebra, form-factor/domain, thermodynamic-limit,
microscopic-current, Kubo, and physical-projection checkpoints needed by the
observable being claimed.  The residual inequality is now explicitly a budget
only after the residual terms have been turned into comparable estimates.

## Verification

- `python3 -m py_compile calculation-checks/factorized_scattering_algebra_checks.py`
- `python3 calculation-checks/factorized_scattering_algebra_checks.py`
- `tools/run_calculation_checks.sh --python-only --only factorized_scattering_algebra`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `python3 tools/audit_negative_scope_prose.py`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vi/chapter01_factorized_scattering_and_integrability.tex --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `git diff --check`
- `tools/build_monograph.sh`

All commands passed.  The full monograph build completed cleanly and produced
`monograph/tex/main.pdf` at 3402 pages.

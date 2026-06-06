# 2026-06-06 Issue #597 Dynamical Theta-Source Audit

## Scope

- Added `ca:dynamical-theta-source-axion-curvature` to
  `monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`.
- Extended `calculation-checks/qcd_theta_witten_veneziano_checks.py` with
  `check_dynamical_theta_source_curvature()`.
- Updated the calculation-check inventory prose and the Ch20 dossier.

## Quality Intent

This pass addresses the instanton-depth concern by moving from moduli-space
infrastructure to a physical source-curvature handoff.  The manuscript now
states that a dynamical pseudoscalar coupled through the renormalized theta
coordinate inherits curvature from a selected branch susceptibility only after
kinetic normalization, branch/contact convention, mixing, and instanton-activity
budgets are controlled.  A dilute instanton cosine is recorded as a conditional
specialization, not as a substitute for the QCD branch susceptibility.

## Verification

- `python3 -m py_compile calculation-checks/qcd_theta_witten_veneziano_checks.py`
- `python3 calculation-checks/qcd_theta_witten_veneziano_checks.py`
- `tools/run_calculation_checks.sh --python-only --only qcd_theta_witten_veneziano_checks`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --fail`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `git diff --check`
- `tools/build_monograph.sh`

All commands passed.  The full monograph build completed cleanly and produced
`monograph/tex/main.pdf` at 3401 pages.

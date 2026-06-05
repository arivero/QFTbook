# 2026-06-05 Issue #597 Instanton/Witten--Veneziano Comparison Audit

## Scope

- Target: Volume II Chapter 21, the theta/singlet channel adjacent to the
  instanton chiral-spurion bridge.
- Physics objective: keep instanton calculus tied to physical QFT observables
  by separating source-saturated instanton amplitudes, conditional instanton
  theta curvature, pure-YM Witten--Veneziano curvature, full massless-QCD theta
  screening, and \(\eta'\) or \(\eta,\eta'\) spectral observables.
- Quality guard: this pass adds a comparison window and exact checks, not more
  moduli-space infrastructure and not a directive embedded in TeX.

## Changed Artifacts

- `monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex`
- `calculation-checks/qcd_theta_witten_veneziano_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_ii/chapter21_global_anomalies_ssb_pions.md`

## Re-Audit Notes

- The new TeX block is a controlled approximation, with equations that state
  the extra hypotheses needed before replacing \(\chi_{\rm YM}\) by a dilute
  instanton activity.
- The exact check script now verifies the comparison mass gap, the trace
  budget, the instanton-branch Schur cancellation, and finite negative
  controls against both under-budgeting and confusing the full massless-QCD
  susceptibility with the pure-glue WV input.
- The paired dossier records the scope and the distinction between source
  kernels and physical pseudoscalar observables.

## Verification

- `python3 -m py_compile calculation-checks/qcd_theta_witten_veneziano_checks.py`
- `python3 calculation-checks/qcd_theta_witten_veneziano_checks.py`
- `tools/run_calculation_checks.sh --python-only --only qcd_theta_witten_veneziano_checks`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
- `git diff --check`

All checks passed on 2026-06-05.

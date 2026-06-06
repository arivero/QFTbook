# 2026-06-06 Issue #630 Euclidean-To-Retarded Transport Audit

## Scope

- Addressed the QCD transport-depth gap in Volume X Chapter 12 by adding a
  Euclidean-to-retarded extraction gate between the real-time hydrodynamic
  response window and the channel-specific shear, bulk/sound, and charge
  spectral windows.
- Kept directives and issue process notes out of the monograph TeX.  The
  monograph text states only the physics datum: thermal kernel, contact and
  zero-mode subtraction, UV-tail/OPE input, low-frequency spectral class,
  inverse map, and residual budget.

## Substance Audit

- The pass is physics-depth rather than extra lemma density: it blocks the
  common shortcut from finite Euclidean correlator data to viscosity or
  conductivity without a spectral inverse problem and stability estimate.
- It sharpens the QCD transport architecture by requiring analytic
  continuation, finite-volume, continuum, contact, tail, and ansatz residuals
  before Euclidean/lattice data enter the real-time spectral gates.
- The companion check constructs Euclidean moments from independent spectral,
  contact, and UV-tail data, then rejects raw midpoint, one-sample,
  missing-contact, missing-tail, and missing-continuation shortcuts.

## Verification

- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`
- `python3 calculation-checks/qcd_phase_checks.py`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex --window 120 --stride 60 --fail --limit 20`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only --only qcd_phase`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

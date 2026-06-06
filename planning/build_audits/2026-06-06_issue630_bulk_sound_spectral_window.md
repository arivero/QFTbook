# 2026-06-06 Issue #630 Bulk/Sound Spectral-Window Pass

## Scope

- Volume X Chapter 12, QCD phase structure and plasma response.
- Target: deepen the hydrodynamic response layer by treating bulk viscosity as
  a scalar response-extraction problem, not as a raw trace-correlator slogan.

## Substance

- Added `ca:qcd-finite-bulk-sound-spectral-window` after the finite shear
  spectral-window block.
- The new monograph block defines the subtracted bulk-pressure source
  `mathcal B=delta P_tr-c_s^2 delta T00`, records the pressure-energy slope
  subtraction, and relates the sound-pole attenuation to
  `zeta=w Gamma_s-2(d-1) eta/d`.
- The error budget now keeps sound width, enthalpy, shear subtraction,
  finite-`k` dispersion, regular background, continuum/contact subtraction,
  thermodynamic derivative uncertainty, and critical scalar contamination as
  separate data.
- The companion finite check independently reconstructs `zeta` from the
  subtracted scalar slope and from the sound pole, and rejects raw trace-slope,
  width-only, missing-shear, and hidden-critical shortcuts.

## Quality Audit

- Physics-first scope: the pass addresses a real QCD transport extraction
  subtlety in the scalar/longitudinal channel, where critical fluctuations and
  contact subtractions matter.
- Architecture: the insertion is paired with the existing shear spectral
  window, making the hydrodynamic-response section a sequence of extraction
  gates rather than an accumulation of unrelated finite identities.
- Boundary: the text does not claim a microscopic derivation of the QCD sound
  pole; it states the finite response-window data needed before a bulk
  viscosity extraction is meaningful.

## Verification

- `python3 calculation-checks/qcd_phase_checks.py`
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`
- `tools/run_calculation_checks.sh --python-only --only qcd_phase`
- `tools/run_calculation_checks.sh --python-only`
- `git diff --check`
- Process-language scan on the touched monograph/check files
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py && python3 tools/audit_calculation_evidence_contracts.py`
- `tools/build_monograph.sh`

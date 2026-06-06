# 2026-06-06 Issue 527 Ray--Velocity Matching Audit

## Scope

- Targeted Volume IV, Chapter 05 charged Haag--Ruelle / dressed LSZ material.
- Added a controlled approximation requiring the asymptotic Wilson-line ray or
  Coulomb tail of a massive charged external packet to match its velocity cell,
  up to finite Hilbert soft reparametrization.
- Added finite exact companion checks for wrong-ray logarithmic growth, wrong
  Dollard coefficient, wrong soft-factor division, charge-only shortcuts, and
  compact same-ray summability.

## Quality Audit

- This is physics-facing amplitude/external-state architecture: it ties the
  Wilson-line ray to soft factors, Dollard phases, angular flux sectors, and
  hard-coefficient extraction.
- It deliberately does not add more abstract Wilson-line path geometry or
  moduli-space-style infrastructure.
- The monograph text contains no planning directives, review references,
  monitoring language, or GitHub issue bookkeeping.
- The controlled approximation does not claim the full nonperturbative
  charged Haag--Ruelle theorem; it records the finite-cutoff obstruction that
  any such theorem must respect.

## Verification

- `python3 -m py_compile calculation-checks/charged_flux_dressing_checks.py`
- `python3 calculation-checks/charged_flux_dressing_checks.py`
- `tools/run_calculation_checks.sh --python-only --only charged_flux_dressing`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex --window 120 --stride 60 --fail --limit 20`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

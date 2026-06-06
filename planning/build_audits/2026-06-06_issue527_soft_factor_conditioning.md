# Issue #527 charged soft-factor conditioning repair

Date: 2026-06-06

## Scope

Addressed the fresh #527 review about the soft-subtracted charged
boundary-value estimator.  The previous fixed-threshold estimate divided by
the amplitude soft factor but did not state the extra order/uniformity needed
when that factor tends to zero as the detector threshold is removed.

This is a physical extraction-condition repair for charged LSZ data, not a new
Wilson-line geometry or finite-cell expansion.

## Changes

- Updated Vol IV Ch5 to state that
  `eq:dressed-boundary-value-hard-estimator-bound` is a fixed-soft-window
  estimate unless a relative uniformity condition is supplied.
- Added the fixed-threshold order of operations:
  remove the Dollard phase and finite soft factor at fixed detector
  resolution/infrared regulator, then take the shell, endpoint/contact,
  threshold-window, and same-flux schedule limits.
- Added the simultaneous-threshold hypothesis
  `R_pre(eta) <= omega(eta) |S_amp(lambda_eta,E_T_eta)|`,
  `omega(eta)->0`.
- Added the negative control that absolute residual convergence before
  division is not enough when `S_amp -> 0`.
- Extended `charged_flux_dressing_checks.py` with a rational
  vanishing-soft-factor family:
  - `o(S_amp)` residuals give shrinking hard-coefficient error;
  - `O(S_amp)` residuals shrink absolutely but leave a fixed divided error.
- Updated the calculation-check README and Vol IV Ch5 dossier.

## Verification

- `python3 -m py_compile calculation-checks/charged_flux_dressing_checks.py`
- `python3 calculation-checks/charged_flux_dressing_checks.py`
- `tools/run_calculation_checks.sh --python-only --only charged_flux_dressing`
- `git diff --check`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

The full Python calculation suite passed.  The full monograph build completed
with clean log scan at 3473 pages.

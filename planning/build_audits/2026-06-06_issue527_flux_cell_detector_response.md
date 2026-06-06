# 2026-06-06 Issue #527 Flux-Cell Detector Response Audit

## Scope

- Target: Volume IV, Chapter 5, charged Haag--Ruelle/LSZ.
- Issue: #527, detector-facing extraction of charged LSZ data in
  nonconfining gauge sectors.
- Local focus: the finite-resolution step after the flux-resolved
  detector-inclusive probability bridge.
- Calculation companion: `calculation-checks/charged_flux_dressing_checks.py`.

## Substance Added

- Added the controlled approximation `Flux-cell detector response and charged
  hard coefficients`.
- The new text models measured detector rates as a calibrated stochastic
  response matrix on sharp flux probabilities, plus backgrounds and a declared
  residual.
- A calibrated left inverse reconstructs sharp flux probabilities with an
  explicit residual-propagation bound.
- The hard coefficient is extracted only after dividing by the resolved soft
  factor and the finite detector normalization.
- Degenerate response columns are identified as genuine detector information
  loss.  They do not license coherent amplitude summation across sharp
  angular-flux sectors.

## Quality Audit

- This pass is physics-facing: it addresses how a charged LSZ coefficient is
  read from finite-resolution detector rates, rather than adding tangential
  mathematical infrastructure.
- It keeps the theorem boundary intact.  The full nonperturbative charged
  Haag--Ruelle theorem and the Wilson-line/Dollard large-time estimates remain
  open.
- The companion check uses exact rational finite models and negative controls:
  uncalibrated detector response, singular response columns, omitted soft
  factors, and coherent amplitude summation.
- No directive, monitoring, planning, or issue-process language was inserted
  into monograph TeX.

## Verification

- `python3 -m py_compile calculation-checks/charged_flux_dressing_checks.py`
  passed.
- `python3 calculation-checks/charged_flux_dressing_checks.py` passed.
- `python3 calculation-checks/check_utils_checks.py` passed after the
  residual-budget comparison was routed through the shared finite upper-bound
  assertion with exact rational tolerance.
- `tools/run_calculation_checks.sh --python-only --only
  charged_flux_dressing` passed.
- Focused Ch5 theorem-form, unnumbered-display-label, negative-scope, and
  style-density audits passed.
- Process-language scan of the touched TeX and calculation-check surfaces
  found no matches.
- `git diff --check` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/audit_monograph_text.sh` passed.
- `python3 tools/audit_calculation_check_inventory.py` passed.
- `python3 tools/audit_calculation_evidence_contracts.py` passed.
- `tools/build_monograph.sh` passed; `monograph/tex/main.pdf` rebuilt and
  log-scanned clean at 3450 pages.
- `tools/run_calculation_checks.sh --python-only` passed; Wolfram checks were
  not selected.

## Re-Audit Note

The first full Python sweep caught a raw residual-budget inequality through
`check_utils_checks.py`.  The comparison was rewritten to use the shared
finite `assert_leq` helper with `Fraction(0)` tolerance, preserving exact
rational arithmetic and satisfying the NaN-guard audit.

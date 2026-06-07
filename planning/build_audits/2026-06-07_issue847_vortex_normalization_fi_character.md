# Issue #847 Vortex-Normalization FI-Character Audit

## Scope

- Added a Chapter 09 proposition making the branch change of
  vortex-normalization constants an FI-character shift on the declared compact
  flux lattice.
- Extended the GLSM companion with a rank-two quotient-lattice finite model:
  allowed charges pair integrally with fractional quotient fluxes, while a
  cover-charge-one shortcut passes on the covering lattice but fails on the
  actual compact flux lattice.
- Updated the calculation README, evidence contract, and Chapter 09 dossier.

## Quality Audit

- This is a Hori--Vafa normalization repair in the monograph's own compact
  flux conventions, not an imported formula check.
- The physics point is topological-sector visibility: finite determinant
  normalizations are scheme data only after their branch shifts act trivially
  on all allowed gauge bundles.
- The pass does not prove the continuum vortex regulator limit, the full
  Hori--Vafa operator map, or a complete mirror-QFT equivalence theorem.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- Focused Chapter 09 theorem/display/negative-scope/style/text audits.
- Chapter 09 TeX scan for review/directive/planning language.
- JSON, evidence-contract, inventory, dossier, whitespace, full Python
  calculation-check, and full monograph-build audits.

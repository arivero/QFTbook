# Issue #630 measured DIS test-functional pass

## Scope

- Targeted Volume II Chapter 19, compact-\(x\) DIS/PDF/DGLAP.
- Added `ca:qcd-dis-measured-test-functional`, making a physical compact-DIS
  prediction a tested color-singlet structure-function scalar rather than a
  PDF-only evolution statement.
- The new block requires the same measured weight, coefficient row, light-ray
  PDF coordinate, finite-regulator subtraction balance, endpoint exclusion, and
  regulator residual to be assembled together.
- Updated `qcd_dglap_checks.py` with exact negative controls for using a row
  from a different measured weight, omitting the endpoint boundary residual,
  and omitting either final-state soft inclusivity or incoming-collinear PDF
  subtraction.
- Refreshed the factorization textual-candidate review anchors after the Ch19
  insertion shifted source-derived line keys.
- Restored the Ch19b non-global reference-map boundary saying that
  super-leading or hadron-hadron Glauber questions are separate coordinates
  from the finite BMS non-global model.

## Re-audit

This pass is physics-facing factorization architecture, not a new finite-cell
annex.  The finite companion checks only the observable-assembly algebra and
guardrail failures; it does not prove all-order DIS factorization,
nonperturbative PDF existence, threshold resummation, or small-\(x\)
factorization.  The monograph TeX carries only the physics statement; issue and
quality-control bookkeeping remains in planning files.

## Follow-up Re-audit

Issue #844 review correctly identified that the residual display was a
proof-obligation decomposition, not a controlled approximation.  The monograph
block was therefore demoted to `rem:qcd-dis-measured-test-functional-map`.
The companion target was likewise narrowed: it checks the finite row/PDF dual
transport, measured-row negative control, endpoint-support boundary
obligation, and finite-regulator soft/collinear balance, but it does not assign
or certify the physical higher-twist, perturbative, boundary, or continuum
residual estimates.

## Verification

- `python3 -m py_compile calculation-checks/qcd_dglap_checks.py`
- `python3 calculation-checks/qcd_dglap_checks.py`
- `tools/run_calculation_checks.sh --python-only --only qcd_dglap`
- focused Ch19 style-density, theorem-form, unnumbered-display-label,
  negative-scope, and process-language scans
- focused Ch19b style-density, theorem-form, unnumbered-display-label,
  negative-scope, and process-language scans
- `python3 calculation-checks/scet_factorization_checks.py`
- `tools/run_calculation_checks.sh --python-only --only scet_factorization`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- full `tools/run_calculation_checks.sh --python-only`
- full `tools/build_monograph.sh`, clean at 3478 pages

# Issue #725 warning-clean Wilson-overlap audit

## Scope

This pass addresses the #725 critique that the `susy_2d_lg_glsm_checks.py`
magnetic-torus Wilson-overlap index cell used a raw NumPy matrix product in
the Hermitian kernel construction.  A passing index assertion after
divide/overflow/invalid runtime warnings would be unacceptable evidence for
the Fujikawa sign convention.

The warning was not reproducible on the current local runtime with
`PYTHONWARNINGS=error`, but the raw product was still a weak evidence
contract.  The companion now proves finite inputs, routes the kernel product
through `finite_matmul()`, proves finite output, and includes an explicit
RuntimeWarning-as-error construction regression.

## Runtime Assumption

The finite Wilson kernel is small and dense in this companion.  Its matrix
product is required to be finite-entry arithmetic; if the platform BLAS emits
a runtime warning, `finite_matmul()` converts that warning to a guarded
reference multiplication rather than letting the evidence cell pass silently.
If both optimized and reference products fail finite arithmetic, the check
raises an assertion.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `PYTHONWARNINGS=error PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- `python3 -m json.tool calculation-checks/evidence_contracts.json >/dev/null`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`

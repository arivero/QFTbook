# Issue #769 event-shape cumulant pass

Date: 2026-06-07

Scope:
- Added `ca:one-loop-event-shape-cumulant-cell` to Volume II Chapter 6 after the paired-measurement cell.
- Computed the local soft-collinear one-emission cumulant integral for `tau = alpha beta` and `tau < tau_0`.
- Made the finite observable datum explicit: after the double pole cancels, the local singular chart contributes `-1/2 log^2(1/tau_0)`.

Evidence:
- Added `check_one_emission_event_shape_cumulant_cell()` to `calculation-checks/generalized_unitarity_reduction_checks.py`.
- The companion uses exact symbolic-log coefficients for `eps^-2`, `eps^-1`, `L/eps`, finite, finite `L`, and finite `L^2` terms.
- Negative controls reject frozen locally inclusive measurements, factorized endpoint vetoes that leave a logarithmic pole, and one-coordinate endpoint shortcuts that miss the double logarithm.

Quality audit:
- The TeX block states the limitation: it is a local one-emission soft-collinear cell, not a complete event-shape factorization theorem.
- No planning or directive language was added to monograph TeX.
- The pass answers the physics-depth concern by moving from abstract measurement bookkeeping to a concrete differential Sudakov logarithm.

Verification:
- `python3 calculation-checks/generalized_unitarity_reduction_checks.py`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `bash tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `bash tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_negative_scope_prose.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

Non-blocking note:
- `python3 tools/audit_calculation_evidence_contracts.py --fail-on-risk-report` still reports pre-existing nonmanifest risky companions outside this pass. The manifest evidence-contract audit is clean.

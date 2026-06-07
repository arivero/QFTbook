# 2026-06-06 Issue #725 NLSM Weyl-Anomaly Evidence Contract

## Scope

- Target issue: #725, independent evidence contracts and adversarial tests for
  high-risk calculation companions.
- Companion promoted: `calculation-checks/nlsm_weyl_anomaly_checks.py`.
- Chapter supported: Volume V, Chapter 11, NLSM Weyl-anomaly and
  target-space beta-function representatives.
- Planning companion:
  `planning/chapter_dossiers/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.md`.

## Substance Audit

- Physics target: the local Weyl-anomaly package used to decide perturbative
  worldsheet conformality in a background \((G,B,\Phi)\).
- The check now carries an extended evidence contract with target claims,
  independent construction, imported assumptions, negative controls, scope
  boundary, convention dependencies, domain assumptions, and remaining
  conditional content.
- The new adversarial finite package guards the central overread:
  coordinate beta components are not themselves the invariant conformality
  test.  Hatted tensor representatives require target-diffeomorphism and
  \(B\)-gauge pieces, and the scalar Weyl anomaly remains a separate
  condition.
- This is not a new sigma-model derivation in the monograph.  It strengthens
  the verification boundary for an existing physics claim and reduces the
  strict #725 high-risk backlog.

## Exact Checks Added

- A finite metric representative with nonzero coordinate beta components whose
  hatted metric representative vanishes after the redundant vector piece is
  supplied.
- A finite antisymmetric representative whose hatted \(B\)-beta vanishes only
  after the exact \(B\)-gauge piece is included.
- A scalar-anomaly negative control showing that vanishing tensor
  representatives do not imply full Weyl-anomaly cancellation.

## Verification Plan

- Run the focused NLSM Weyl-anomaly companion and py_compile.
- Run the focused calculation harness selection.
- Run JSON/evidence-contract audits, including the strict backlog check to
  confirm the backlog decreases by one.
- Run dossier, text, inventory, diff, full calculation, and full build gates.

## Verification Results

- `python3 -m py_compile calculation-checks/nlsm_weyl_anomaly_checks.py`
  passed.
- `python3 calculation-checks/nlsm_weyl_anomaly_checks.py` passed.
- `tools/run_calculation_checks.sh --python-only --only nlsm_weyl_anomaly`
  passed.
- `python3 -m json.tool calculation-checks/evidence_contracts.json` passed.
- `python3 tools/audit_calculation_evidence_contracts.py` passed with the
  standing non-blocking risk report.
- `python3 tools/audit_calculation_evidence_contracts.py --fail-on-risk-report`
  failed as expected on the remaining manifestless high-risk backlog; the
  backlog count is now 34 and no longer includes
  `nlsm_weyl_anomaly_checks.py`.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/audit_monograph_text.sh` passed.
- `python3 tools/audit_calculation_check_inventory.py` passed.
- Process-language scan on the edited check/README/manifest surfaces found no
  issue, directive, review, or monitor language.
- `git diff --check` passed.
- Full `tools/run_calculation_checks.sh --python-only` passed.
- `tools/build_monograph.sh` passed; the PDF was already up to date at 3483
  pages.

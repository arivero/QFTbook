# 2026-06-06 Issue #519 Measured EEC Response/Covariance Audit

## Scope

- Added `ca:measured-eec-response-covariance-contract` to
  `monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex`.
- Extended `calculation-checks/energy_correlator_track_checks.py` with exact
  rational event-ensemble checks for endpoint covariance repair, linear
  detector-response covariance transport, and detector-noise budgeting.
- Updated the Chapter 19b dossier, calculation-check inventory, and
  factorization textual-candidate review ledger.

## Quality Intent

This pass extends the measured EEC material from endpoint moment closure to
the observable contract used by finite detector-bin measurements.  The new
block treats endpoint atoms as eventwise coordinates before forming ensemble
covariances, then transports the resulting mean and covariance through a
declared detector response and noise coordinate.  This is physics-facing
architecture rather than an additional local identity: it specifies what a
light-ray/endpoints/nonperturbative prediction must provide before it can be
compared to correlated binned EEC data.

## Verification

- `git diff --check`
- `python3 -m py_compile calculation-checks/energy_correlator_track_checks.py`
- `python3 calculation-checks/energy_correlator_track_checks.py`
- `tools/run_calculation_checks.sh --python-only --only energy_correlator_track`
- `python3 calculation-checks/scet_factorization_checks.py`
- `tools/run_calculation_checks.sh --python-only --only scet_factorization`
- `tools/run_calculation_checks.sh --python-only`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`

All commands passed after registering the new semantic factorization candidate
under the measured EEC prediction budget and rephrasing one prose-audit trip
point.  The full monograph build completed cleanly and produced
`monograph/tex/main.pdf` at 3409 pages.

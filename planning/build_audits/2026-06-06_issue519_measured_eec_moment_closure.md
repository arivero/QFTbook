# 2026-06-06 Issue #519 Measured EEC Moment Closure Audit

## Scope

- Targeted issue #519, energy-correlator/light-ray observable depth.
- Added `ca:measured-eec-global-moment-closure` to Vol II Ch 19b after the
  measured small-angle endpoint chart.
- Added exact rational checks in `energy_correlator_track_checks.py` for the
  endpoint-only correction that repairs measured zeroth and first EEC moments.
- Repaired the factorization occurrence/textual ledgers exposed by the full
  Python suite: the DIS threshold factorized coordinate now has a source-derived
  manifest disposition, and stale textual review anchors were refreshed.

## Substance Audit

- This is physics-depth work, not lemma-density work.  The new text asks when
  small-angle, back-to-back, and separated-angle endpoint charts assemble into a
  single measured detector distribution.
- The closure uses measured selected-energy data
  \(A_\omega=(\sum_r\omega_r z_r)^2\) and
  \(B_\omega=|\sum_r\omega_r z_r\mathbf n_r|^2\), rather than silently imposing
  full-calorimeter center-of-momentum moments.
- The endpoint atoms \(K_+^\omega,K_-^\omega\) are solved from the two measured
  moment equations, and a finite detector-test bound records the cost of
  repairing residual defects.
- Negative controls reject the two tempting shortcuts: using full-calorimeter
  atoms for a selected observable and repairing only the zeroth moment.

## Verification

- `python3 -m py_compile calculation-checks/energy_correlator_track_checks.py`
- `python3 calculation-checks/energy_correlator_track_checks.py`
- `tools/run_calculation_checks.sh --python-only --only energy_correlator_track_checks`
- `python3 calculation-checks/scet_factorization_checks.py`
- `tools/run_calculation_checks.sh --python-only`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`

## Re-Audit

The added monograph text is not a directive and does not mention process policy.
It is a measured-observable assembly constraint: local endpoint resummations do
not become a physical EEC prediction until their endpoint atoms glue to the same
global detector moments.  The calculation companion is adversarial enough to
catch common wrong closures, and the full build plus full Python suite passed
after the occurrence-ledger repair.

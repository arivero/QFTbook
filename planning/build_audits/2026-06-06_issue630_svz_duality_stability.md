# 2026-06-06 Issue #630 SVZ Duality/Stability Audit

## Scope

- Target issue: #630, QCD rigor/depth backlog.
- Chapter touched: Volume II, Chapter 19, current-sum-rule section.
- Companion check: `calculation-checks/qcd_sum_rule_checks.py`.

## Substance Audit

- Physics target: QCD sum-rule extraction quality, not additional
  mathematics adjacent to the chapter.  The pass treats the hard part of SVZ
  use: when a Borel plateau plus pole-continuum ansatz is evidence for a
  spectral parameter rather than a threshold-tuning artifact.
- New controlled approximation:
  `ca:qcd-svz-duality-stability-gate`.
- Main controls now required in one window:
  OPE-tail control after Borel transform, continuum-duality remainder,
  positivity/truncation status, threshold sensitivity, plateau variance, and
  finite pole-remainder error.
- Re-audit result: the insertion builds on the existing current-correlator,
  OPE, and Borel-window exposition rather than opening a tangential topic.
  It raises the argument architecture from "one more identity" to a workflow
  for deciding whether a quoted SVZ mass extraction is controlled.

## Exact Checks Added

- Plateau diagnostic:
  \(-\partial_\tau(\mathcal L_1/\mathcal L_0)\) equals the retained spectral
  variance when the retained spectral measure is positive.
- Continuum threshold:
  \(\partial_{s_0}m_{\rm eff}^2\) contains the boundary weight times
  \(s_0-m_{\rm eff}^2\), so a shortcut that only keeps the boundary weight is
  rejected.
- Pole remainder:
  the mass-estimator deviation is bounded by the finite \(R_0,R_1\) remainder
  formula, and dropping \(R_0\) is caught by a negative control.

## Verification Plan

- Run the focused QCD sum-rule checks.
- Run chapter text audits and dossier audits.
- Run calculation inventory/evidence audits.
- Run the full calculation suite and full monograph build after repairing any
  line-anchor ledgers shifted by the chapter insertion.

## Verification Results

- `python3 calculation-checks/qcd_sum_rule_checks.py`: passed.
- `tools/run_calculation_checks.sh --python-only --only qcd_sum_rule_checks`:
  passed.
- Chapter theorem-form, unnumbered-display-label, negative-scope, and
  style-density audits: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `python3 tools/audit_calculation_check_inventory.py`: passed.
- `python3 tools/audit_calculation_evidence_contracts.py`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `python3 calculation-checks/scet_factorization_checks.py`: passed after
  refreshing Ch. 19 textual factorization line anchors shifted by the
  insertion.
- `tools/run_calculation_checks.sh --python-only`: passed.
- `tools/build_monograph.sh`: passed.

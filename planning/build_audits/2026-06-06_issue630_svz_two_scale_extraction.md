# 2026-06-06 Issue #630 SVZ Two-Scale Extraction Audit

## Scope

- Target issue: #630, QCD rigor/depth backlog.
- Chapter touched: Volume II, Chapter 19, current-sum-rule/SVZ section.
- Companion check: `calculation-checks/qcd_sum_rule_checks.py`.

## Substance Audit

- Physics target: the credibility of a QCD sum-rule mass extraction, not a
  tangential mathematical identity.  The pass strengthens the existing SVZ
  gate by requiring the quoted mass to survive a two-scale window test in
  \(\tau\) and \(s_0\).
- New controlled approximation:
  `ca:qcd-svz-two-scale-extraction-window`.
- Main architectural addition: aggregate OPE, perturbative, duality,
  regulator, and positivity residuals are propagated through the logarithmic
  mass quotient.  The zeroth-moment residual is load-bearing because it moves
  the denominator.
- Negative-control target: a flat curve produced by choosing a moving
  \(s_0(\tau)\) is a cancellation between \(\partial_\tau m_{\rm eff}^2\) and
  \(s_0'\partial_{s_0}m_{\rm eff}^2\), not independent spectral evidence.

## Exact Checks Added

- Aggregate window residual:
  \[
    |(\widehat L_1/\widehat L_0)-(L_1/L_0)|
  \]
  obeys the finite quotient bound with both \(\Delta L_1\) and
  \(\Delta L_0\), and the check fails the shortcut that drops \(\Delta L_0\).
- Retuned-threshold plateau:
  the finite ledger verifies that a nonzero threshold velocity can cancel a
  nonzero \(\tau\)-slope when threshold sensitivity is nonzero.

## Verification Results

- `python3 -m py_compile calculation-checks/qcd_sum_rule_checks.py`: passed.
- `python3 calculation-checks/qcd_sum_rule_checks.py`: passed.
- `tools/run_calculation_checks.sh --python-only --only qcd_sum_rule`: passed.
- Chapter negative-scope, theorem-form, unnumbered-display-label, and
  style-density audits: passed.
- `python3 tools/audit_calculation_evidence_contracts.py`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `python3 tools/audit_calculation_check_inventory.py`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed; generated
  `monograph/tex/main.pdf` at 3400 pages.

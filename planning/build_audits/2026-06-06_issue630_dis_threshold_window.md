# Issue #630 DIS threshold plus-distribution window pass

Date: 2026-06-06.

Scope:

- Chapter: Volume II, Chapter 19, QCD renormalization, asymptotic freedom, and
  DIS.
- New monograph label: `ca:qcd-dis-threshold-plus-distribution-window`.
- Companion check: `check_threshold_test_function_window()` in
  `calculation-checks/qcd_dglap_checks.py`.

Substance audit:

- This is an endpoint-physics repair, not a new mathematical annex.  The pass
  makes the distributional cusp kernel act on measured test functions and
  shows explicitly that the plus prescription subtracts the endpoint value.
- The terminal-cell bounds for \(D_0\) and \(D_1\) record why compact-\(x\)
  DIS factorization is not uniform as the measurement support approaches
  \(x=1\).
- The large-\(N\) harmonic-number identity is kept as a moving-test-function
  cusp probe, not as a substitute for physical threshold factorization.
- A real DIS threshold approximation is required to carry hard-current
  matching, final-state jet, soft Wilson-line, evolution, Mellin-contour or
  prescription, and power-remainder data.

Negative controls:

- Replacing \(D_0\) by the ordinary pole \(1/(1-x)\) leaves an endpoint-value
  logarithm on a constant test function.
- The fixed terminal-cell test is not the same datum as the large-\(N\)
  moving Mellin family \(x^{N-1}\).
- The cusp plus-distribution alone is rejected as a complete threshold theorem
  when hard, jet, soft, contour, and power entries are omitted.

Expected verification:

- Run the focused QCD DGLAP check.
- Run the calculation evidence/inventory audits.
- Run Chapter 19 prose/form-label audits and the full monograph build.

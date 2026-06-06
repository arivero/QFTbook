# 2026-06-06 Issue #769 Loop Jacobi Repair Re-Audit

## Scope

- Target: Volume II Chapter 06, generalized unitarity and loop-amplitude
  reconstruction, specifically the color--kinematics/double-copy surface.
- Related issue: #769 perturbative amplitudes.
- Companion: `calculation-checks/generalized_unitarity_reduction_checks.py`.

## Substance Audit

- The existing chapter already warned that cut-equivalent or gauge-null
  one-loop numerator shifts need not be valid double-copy shifts.
- This pass adds the positive local repair criterion: in one routed Jacobi
  triplet, if the numerator Jacobi defect lies in an allowed common
  contact/IBP/evanescent surface direction, subtracting one third of that
  defect from each numerator restores the kinematic Jacobi identity while
  remaining color-null before integration.
- The same repair is double-copy null only when the second numerator copy is
  Jacobi-satisfying, or when a separate gravity-null surface proof is supplied.

## Negative Controls Added

- A defective second numerator copy makes the common repair visible in the
  candidate gravity integrand.
- A graph-dependent color-null shift can leave the gauge amplitude unchanged
  while changing the double-copy pairing.
- Jacobi vanishing on sampled cuts does not prove the full routed numerator
  defect vanishes.

## Scope Boundary

- This is a local numerator-representative criterion for loop-level
  color--kinematics bookkeeping.  It does not prove the existence of
  loop-level color--kinematics representations for general theories, does not
  construct a full gravity integrand, and does not close the broader #769
  amplitude program.

## Verification Results

- `python3 -m py_compile calculation-checks/generalized_unitarity_reduction_checks.py`
  passed.
- `python3 calculation-checks/generalized_unitarity_reduction_checks.py`
  passed.
- `tools/run_calculation_checks.sh --python-only --only generalized_unitarity_reduction`
  passed.
- Focused Chapter 06 audits passed: theorem form, unnumbered display labels,
  negative-scope prose, and style density.
- Repository audits passed: `tools/audit_chapter_dossiers.sh`,
  `tools/audit_monograph_text.sh`,
  `tools/audit_calculation_check_inventory.py`, and
  `tools/audit_calculation_evidence_contracts.py`.
- Full `tools/run_calculation_checks.sh --python-only` passed.
- Full `tools/build_monograph.sh` passed; `main.pdf` built cleanly at
  3405 pages.
- `git diff --check` passed after this audit note was finalized.

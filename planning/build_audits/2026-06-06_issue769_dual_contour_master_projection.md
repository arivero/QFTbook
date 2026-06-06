# 2026-06-06 Issue #769 Dual-Contour Master Projection Audit

## Scope

- Target issue: #769, generalized unitarity and loop-amplitude bridge.
- Chapter touched: Volume II, Chapter 6, generalized-unitarity/master-integral
  section.
- New monograph label:
  `ca:dual-contour-master-coefficient-extraction`.
- Companion check:
  `check_dual_contour_master_coefficient_extraction()` in
  `calculation-checks/generalized_unitarity_reduction_checks.py`.

## Substance Audit

- Physics target: the bridge from algebraic generalized cuts to physical
  loop-amplitude master coefficients.  The pass is not a new isolated finite
  identity; it inserts the missing coefficient-extraction architecture between
  sector projection and master-transport/differential-equation data.
- The new gate makes the slogan "the cut fixes the coefficient" conditional on
  an invertible contour/master pairing
  \(P_{ij}=\mathcal C_i[M_j]\).
- It requires a declared subtraction vector for contact, surface,
  lower-sector, and regulator residues before raw cut values are interpreted
  as coefficients.
- It records an inverse-pairing error majorant, so numerical or approximate
  reconstruction is judged by conditioning and residual budgets rather than by
  leading-singularity matching alone.

## Negative Controls

- Raw contour values need not equal master coefficients.
- Omitting a lower-sector/contact subtraction shifts the extracted
  coefficients.
- Surface-polluted contours propagate exactly through \(P^{-1}\) into a
  coefficient shift.
- A rank-one contour pairing cannot distinguish two retained masters.

## Verification Results

- `python3 -m py_compile calculation-checks/generalized_unitarity_reduction_checks.py`:
  passed.
- `python3 calculation-checks/generalized_unitarity_reduction_checks.py`:
  passed.
- `tools/run_calculation_checks.sh --python-only --only generalized_unitarity_reduction`:
  passed.
- Chapter negative-scope, theorem-form, unnumbered-display-label, and
  style-density audits: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `python3 tools/audit_calculation_check_inventory.py`: passed.
- `python3 tools/audit_calculation_evidence_contracts.py`: passed with only
  the standing non-blocking risk-class report.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed; generated
  `monograph/tex/main.pdf` at 3400 pages.

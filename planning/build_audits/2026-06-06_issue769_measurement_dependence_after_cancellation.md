# 2026-06-06 Issue #769 Measurement Dependence After Cancellation Audit

## Scope

- Targeted GitHub issue #769, with #844 coherence in mind.
- Extended Volume II, Chapter 6 after the unresolved one-emission measurement
  cell.
- Goal: keep the loop-amplitude development physics-facing by showing that a
  reconstructed finite virtual amplitude and pole cancellation still do not
  determine an observable unless the real-emission measurement map is supplied.

## Substance Added

- Added `ca:one-loop-measurement-dependence-after-cancellation`.
- The new cell compares two infrared-safe measurements \(W_A\) and \(W_B\)
  with the same reduced-event limit \(W_0\).
- It proves at the local-cell level that they share the same virtual pole and
  counterevent but differ by the finite unresolved contribution
  \[
    \int d\zeta\,S_0(\zeta)\int_0^1 dx\,
      \frac{W_A(x,\zeta)-W_B(x,\zeta)}{x}.
  \]
- The companion check adds exact rational paired-measurement polynomials,
  verifies pole cancellation for both observables, computes the finite
  difference, and rejects locally inclusive and finite-remainder-only
  shortcuts.

## Quality Audit

- This is not a new tangential mathematical identity: it sharpens the
  physical endpoint of the generalized-unitarity section.
- It separates the virtual hard remainder from observable construction, which
  is one of #769's explicit acceptance criteria.
- The check is finite and self-contained, but its negative controls are aimed
  at physics overreads: treating pole cancellation or the finite virtual
  remainder as enough to predict a measured quantity.
- No planning directives or issue-management language were inserted into the
  monograph TeX.

## Verification

- `python3 calculation-checks/generalized_unitarity_reduction_checks.py`
- `python3 -m py_compile calculation-checks/generalized_unitarity_reduction_checks.py`
- `tools/run_calculation_checks.sh --python-only --only generalized_unitarity_reduction`
- `tools/run_calculation_checks.sh --python-only`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `python3 tools/audit_negative_scope_prose.py`
- `python3 tools/audit_style_density.py --fail --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex --limit 20`
- `git diff --check`
- `tools/build_monograph.sh`

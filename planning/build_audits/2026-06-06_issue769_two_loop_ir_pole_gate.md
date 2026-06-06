# 2026-06-06 Issue #769 Two-Loop IR-Pole Gate Audit

## Scope

- Target issue: #769, perturbative loop-amplitude development.
- Chapter touched: Volume II, Chapter 6, generalized-unitarity section.
- Companion check: `calculation-checks/generalized_unitarity_reduction_checks.py`.

## Substance Audit

- Physics target: two-loop amplitudes as ingredients in finite observables.
  The new block does not add another cut coefficient or isolated integral cell;
  it connects reconstructed two-loop virtual amplitudes to universal
  soft/collinear pole structure and NNLO observable assembly.
- New controlled approximation:
  `ca:two-loop-ir-pole-consistency-gate`.
- Main mechanism:
  \[
    F^{(2)} = A^{(2)} - I^{(1)} A^{(1)} - I^{(2)} A^{(0)}.
  \]
  This forces the lower-loop amplitude and one-loop finite remainder into the
  two-loop evidence ledger before any finite hard object is quoted.
- Re-audit result: aligned with the monograph standard.  It deepens the
  physics of loop-amplitude reconstruction by separating cut equality, pole
  consistency, finite hard remainders, real-radiation subtraction, and measured
  observables.  It is not tangential mathematics and does not place directives
  in TeX.

## Exact Checks Added

- Two-loop recursive Laurent extraction:
  `A2 - I1 A1 - I2 A0` is finite and equals `F2`.
- Expanded pole ledger:
  `A2 = (I1^2 + I2) A0 + I1 F1 + F2`.
- Negative controls:
  dropping `I1 A1`, using only `I1 F1`, and omitting the `F1^2` hard term in
  the NNLO observable are all rejected.
- NNLO observable budget:
  virtual poles cancel only after paired unresolved real/factorization
  subtractions, and the residual budget must include lower-loop and
  IR real-radiation sectors.

## Verification Plan

- Focused syntax and generalized-unitarity checks.
- Focused Chapter 6 text audits.
- Calculation inventory/evidence audits.
- Dossier and monograph text audits.
- Full Python calculation suite and full monograph build after any fallout is
  repaired.

## Verification Results

- `python3 -m py_compile calculation-checks/generalized_unitarity_reduction_checks.py`
- `python3 calculation-checks/generalized_unitarity_reduction_checks.py`
- `tools/run_calculation_checks.sh --python-only --only generalized_unitarity_reduction_checks`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_monograph_text.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

All listed checks passed.  The full monograph build completed cleanly at
`monograph/tex/main.pdf`.

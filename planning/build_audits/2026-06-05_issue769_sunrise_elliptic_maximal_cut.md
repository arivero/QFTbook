# Issue #769 Sunrise Elliptic Maximal-Cut Pass

## Scope

- Volume II, Chapter 6:
  `ca:two-loop-sunrise-elliptic-maximal-cut`.
- Companion evidence:
  `calculation-checks/generalized_unitarity_reduction_checks.py`.
- Inventory/source updates: calculation-check README, Chapter 6 dossier, and
  foundational bibliography.

## Substance

- Added a physical two-loop master-family diagnostic rather than another local
  one-loop coefficient identity.
- The new block identifies the equal-mass sunrise Symanzik polynomial, affine
  maximal-cut curve, eliminated quartic, discriminant
  \(256r^2(r-1)^3(r-9)\), physical positive-parameter threshold at \(r=9\),
  and pseudo-threshold at \(r=1\).
- The text explains why the maximal cut is an elliptic period for generic
  \(r\), so master-integral evaluation needs a period basis, lower sectors,
  Euclidean boundary constants, and analytic-continuation path/sheet data.

## Verification

Completed on 2026-06-05:

- `python3 -m py_compile calculation-checks/generalized_unitarity_reduction_checks.py`
- `python3 calculation-checks/generalized_unitarity_reduction_checks.py`
- `tools/run_calculation_checks.sh --python-only --only generalized_unitarity_reduction_checks`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex --fail --limit 20`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- metadata-leak scan on touched monograph/check files
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

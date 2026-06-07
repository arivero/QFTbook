# 2026-06-07 Issue #847 Quotient Global-Form Lattice Gate

## Scope

- Target issue: #847, Hori--Vafa signs and normalization from compact flux
  conventions.
- Monograph target:
  `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`.
- Added `ca:glsm-global-form-flux-lattice-gate`.

## Quality Audit

- This pass addresses the remaining global-form propagation gap, not a new
  Hori--Vafa formula.  The chapter now gives the lattice data required before
  ordinary covering-torus mirror constraints can be interpreted for
  `U(1)^s/Gamma`.
- The new block separates the cocharacter/flux lattice `Lambda_G`, the dual
  electric character lattice `Lambda_G^vee`, the logarithmic FI-theta period
  lattice, allowed dual exponentials, and residual mirror orbifold data.
- The rank-one `U(1)/Z_n` example is a physical topological-sector test:
  cover-charge-one matter is not a quotient representation, the minimal flux
  is fractional in the cover coordinate, and the ordinary `2 pi i` FI period
  is not single-valued on that flux.

## Verification

- Focused companion:
  `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`;
  `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`;
  `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`.
- Focused chapter audits:
  `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`;
  `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`;
  `tools/audit_monograph_text.sh monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`;
  `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`;
  `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --window 120 --stride 60 --fail --limit 20`.
- Planning/metadata audits:
  `python3 -m json.tool calculation-checks/evidence_contracts.json`;
  `python3 tools/audit_calculation_check_inventory.py`;
  `python3 tools/audit_calculation_evidence_contracts.py`;
  `tools/audit_chapter_dossiers.sh`;
  TeX leakage scan for review/directive/planning strings.
- Global verification:
  `tools/run_calculation_checks.sh --python-only`;
  `tools/build_monograph.sh`;
  `git diff --check`.

# Issue #844/#847 Projective-Instanton Status Re-Audit

## Scope

- Re-audited the Volume VII Chapter 09 `P^{N-1}` instanton/Hori--Vafa
  comparison surface after the compact-flux and full-QFT repair passes.
- Demoted four projective-instanton comparison blocks from
  `controlledapproximation` to remarks:
  - degree-one A-model zero-mode measure bridge;
  - finite measure-scheme covariance;
  - Hori--Vafa residue/direct-instanton cross-check;
  - degree-`d` projective instanton iteration.
- Tightened `tools/audit_theorem_form.py` so future controlled-approximation
  blocks cannot carry explicit comparison/proof-obligation titles.

## Quality Audit

- The demoted blocks retain useful equations: residual telescopes, finite
  incidence orientation, measure-transport covariance, and degree-`d` gluing
  budgets.
- They do not supply independent determinant-line, zero-mode, compactification,
  operator-map, or continuum estimates in one regulator, so the stronger
  controlled-approximation status was not warranted.
- This pass improves coherence and status honesty without adding planning or
  directive language to the monograph TeX.

## Verification

- `python3 -m py_compile tools/audit_theorem_form.py`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail --limit 40`
- `python3 tools/audit_theorem_form.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- `tools/run_calculation_checks.sh --python-only`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 -m json.tool calculation-checks/evidence_contracts.json`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `git diff --check`
- `tools/build_monograph.sh`

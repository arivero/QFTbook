# 2026-06-07 Issue #847 Hori--Vafa Spectral/Fujikawa Re-Audit

## Scope

- Target issue: #847, Vol VII Ch09 Hori--Vafa determinant sign and
  superspace/component normalization chain.
- Evidence-quality shadow issue: #725, self-confirming Hori--Vafa component
  response companion.
- Monograph target:
  `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`.
- Companion target: `calculation-checks/susy_2d_lg_glsm_checks.py`.

## Quality Audit

- The earlier determinant-sign re-audit correctly removed compact periodicity
  as a sign oracle, but its companion still assigned the real response
  coefficient and the mass-phase Jacobian.  This pass replaces that
  assignment ledger with a finite spectral/Fujikawa laboratory.
- The monograph now displays the two-dimensional gamma matrices,
  `gamma_*`, and `gamma^{12}=i gamma_*`; differentiates a finite
  complex-scalar determinant with reference subtraction to get the real
  `D` response; and computes the theta partner from the regulated chiral trace
  `Tr_reg gamma_* = Q k`.
- The companion constructs the same data independently: gamma matrices,
  complex-scalar determinant powers, finite spectral traces, paired nonzero
  fermion chiralities, and a finite index/Jacobian calculation.  Negative
  controls reject the wrong bosonic determinant power, a real-scalar-only
  shortcut, unpaired fermion spin traces, one-sided measure factors, wrong
  chirality orientation, and absolute-value-only determinants.
- This remains a local Coulomb-chart determinant calculation.  It does not
  close the larger Hori--Vafa issue items concerning the common-flux
  `exp(-Y_i)` operator map, the common physical coefficient versus products of
  projected normalizations, or quotient global-form propagation.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- `python3 tools/audit_theorem_form.py monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_unnumbered_display_labels.py monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --window 120 --stride 60 --fail --limit 20`
- `rg -n "directive|claude_review|monitor|open issue|GitHub issue|depth-pass|unprecedented|planning doc|agent|review" monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
  returned no matches.
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

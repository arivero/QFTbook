# 2026-06-07 Issue #847 Hori--Vafa Determinant-Sign Re-Audit

## Scope

- Target issue: #847, Vol VII Ch09 Hori--Vafa signs and normalization from
  compact flux conventions.
- Monograph target:
  `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`.
- Re-audited `ca:glsm-coulomb-one-loop-branch-monodromy` and the preceding
  local determinant derivation.

## Quality Audit

- The pass removes the invalid claim that the opposite determinant-log sign
  contradicts compact flux normalization.  Both signs transport logarithm
  branches by integral periods of `T`; compact periodicity checks the
  `2 pi` normalization, not the determinant sign.
- The monograph now traces the chapter's sign to the component linear response
  of a massive charged chiral multiplet in a constant `sigma,D,F_12`
  background and to the mass-phase Jacobian in the same theta convention.
- The finite companion rejects two different shortcuts: using branch
  periodicity as a sign oracle, and using `log |M|` without the mass-phase
  Jacobian.  It keeps the old `exp(tau)` fugacity rejection.
- This is a scrutiny/repair pass on the Hori--Vafa normalization chain.  It
  does not claim full GLSM mirror equivalence, a continuum vortex
  compactness theorem, or a construction of the common-flux disorder operator.

## Re-Audit Note

- Superseded in the later 2026-06-07 spectral/Fujikawa re-audit on the
  evidence-strength point: the previous companion separated response factors
  but still assigned the `-1/2` scalar response and `Q alpha` Jacobian.  The
  later pass computes those data in a finite gamma-matrix, determinant-trace,
  paired-fermion, and index-Jacobian model.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `python3 tools/audit_theorem_form.py monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_unnumbered_display_labels.py monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --window 120 --stride 60 --fail --limit 20`
- `rg -n "directive|claude_review|monitor|open issue|GitHub issue|depth-pass|unprecedented|planning doc|agent|review" monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
  returned no matches.
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

# 2026-06-07 Issue #847 Hori-Vafa One-Loop Branch Monodromy Pass

## Scope

- Target issue: #847, Vol VII Ch09 Hori--Vafa signs and normalization from
  compact flux conventions.
- Monograph target:
  `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`.
- Added `ca:glsm-coulomb-one-loop-branch-monodromy` in the abelian GLSM
  Coulomb one-loop section, before the Coulomb critical equation and before
  the Hori--Vafa mirror constraints are used.

## Quality Audit

- This pass does not import a Hori--Vafa sign convention.  It derives the
  branch ledger from the chapter's own compact `T=2 pi i tau` coordinate and
  local one-loop determinant derivative.
- The pass separates the real proper-time subtraction from the holomorphic
  branch data: the proper-time integral supplies the real logarithm, while the
  axial anomaly and compact theta period supply the monodromy.
- The new finite companion rejects three shortcuts: transporting the branch
  with the wrong sign, replacing the holomorphic logarithm by an absolute
  value, and using the period-one `tau` exponential instead of `exp(T)`.
- The addition is local to the Coulomb protected coordinate chart.  It does
  not assert full GLSM mirror equivalence, continuum existence, or vortex
  compactness.

## Re-Audit Note

- Superseded in the later 2026-06-07 determinant-sign re-audit: compact
  `T` periodicity checks integral branch transport for either determinant
  sign and therefore cannot choose the sign.  The sign must be fixed by the
  component determinant response and mass-phase Jacobian.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
  passed.
- `python3 calculation-checks/susy_2d_lg_glsm_checks.py` passed.
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
  passed.
- Focused chapter-09 theorem-form, display-label, negative-scope,
  style-density, and monograph-text audits passed.
- `python3 tools/audit_calculation_evidence_contracts.py` passed.
- `python3 tools/audit_calculation_check_inventory.py` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed before staging.
- `tools/run_calculation_checks.sh --python-only` passed.
- `tools/build_monograph.sh` passed; the generated PDF/log scan was clean.

# 2026-06-07 Issue #847 Common-Flux Operator-Map Diagnostic

## Scope

- Target issue: #847, Hori--Vafa sign, normalization, and common-flux
  operator-map scrutiny in Volume VII Chapter 9.
- Chapter touched:
  `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`.
- Companion touched: `calculation-checks/susy_2d_lg_glsm_checks.py`.
- Dossier touched:
  `planning/chapter_dossiers/volume_vii/chapter09_two_dimensional_supersymmetric_models.md`.
- Calculation manifest and README were updated for the new diagnostic tag.

## Substance Audit

The pass addresses the remaining #847 risk that primitive mirror coefficients
`c_i` extracted from one common gauge-flux sector can be mistaken for a
complete original-sector physical amplitude.  The chapter now inserts a
finite-regulator residual diagnostic after the source-projection paragraph.
It requires an original source space, a charge-one functional, original and
dual source rows, an operator transport map, row-wise matrix-element
comparison for the `exp(-Y_i)` representatives, equal-charge flavor covariance,
an observable assembly row, and an explicit span residual.

This is deliberately not presented as a continuum Hori--Vafa derivation.  The
controlled statement marks the proof obligation: compact flux periodicity,
the Coulomb logarithmic saddle term, and primitive coefficient extraction do
not by themselves supply the observable operator map.  A product such as
`prod_i c_i^{Q_i^a}` is a mirror/FI coordinate until source assembly and span
control identify it with the tested observable.

## Companion Evidence

`check_common_flux_operator_map_diagnostic()` builds an exact finite source
model with:

- common source functional and primitive mirror rows;
- identity source transport and row-wise operator-map equality;
- equal-charge flavor swap covariance;
- a retained primitive-row null direction invisible to the primitive
  coefficients;
- an observable row that sees that null direction;
- a one-point assembly fit that fails on a shifted common functional with the
  same primitive coefficients;
- a residual telescope whose budget fails when the span term is omitted.

This is an adversarial finite diagnostic for the operator-map boundary, not a
proof of the continuum GLSM mirror theorem.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `python3 -m json.tool calculation-checks/evidence_contracts.json`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- `python3 tools/audit_theorem_form.py monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_unnumbered_display_labels.py monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_negative_scope_prose.py monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail --limit 20`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

All targeted and repository-wide checks passed before landing.  The live
monitor check found `claude_review.md` unchanged, both hourly monitoring
automations paused as requested, and no newer #847 update before this pass was
prepared for landing.

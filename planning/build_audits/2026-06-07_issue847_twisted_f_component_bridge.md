# 2026-06-07 Issue #847 Twisted-F Component Bridge

## Scope

- Target issue: #847, Vol VII Ch09 Hori--Vafa signs and normalization from
  compact flux conventions.
- Related issues: #848 full mirror-QFT data and #725 evidence independence.
- Monograph target:
  `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`.
- Companion target: `calculation-checks/susy_2d_lg_glsm_checks.py`.

## Quality Audit

- The previous determinant repair computed the Hermitian Dirac square and the
  local density `Q/(4 pi) log(|M|^2/mu^2)`, but the final conversion to a
  normalized twisted superpotential still appeared where it was used.
- This pass moves that conversion into the chapter's convention layer:
  derivative algebra, ordered twisted Berezin measure, Wess--Zumino vector
  representative, `Sigma=bar D_+ D_- V`, and the top component
  `D+i F_12` are now displayed before the Hori--Vafa lane uses them.
- The FI term and the `-Q Sigma Y` term are expanded at the same component
  normalization.  This ties the local determinant density to the compact
  theta weight and to the `Y -> Y + 2 pi i` period test before the Coulomb
  one-loop calculation is invoked.
- The determinant passage now identifies the two different sources of factors:
  `1/(4 pi)` comes from the two-dimensional momentum density, while
  `1/(2 pi)` comes from the normalized twisted-`F` top-component projection.
- The companion rejects repeated `1/(4 pi)` twisted-`F` normalization,
  doubled-log holomorphic coefficients, and half-density `Sigma Y`
  compact-period shortcuts.
- Boundary retained: this is a convention-closure and local determinant pass.
  It does not prove the common-flux-to-`exp(-Y_i)` operator map, construct the
  full mirror QFT datum, or close the cigar/Liouville full-action issues.

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
- `tools/build_monograph.sh` (clean, 3502 pages)

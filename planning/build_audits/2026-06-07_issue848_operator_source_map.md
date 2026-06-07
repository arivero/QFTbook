# 2026-06-07 Issue #848 Operator/Source Map Evidence

## Scope

- Target issue: #848, full mirror-QFT data beyond Hori--Vafa protected
  superpotentials.
- Monograph target:
  `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`.
- Companion target:
  `calculation-checks/susy_2d_lg_glsm_checks.py`.

## Substance

- Added `rem:glsm-mirror-operator-source-data` after the admissible mirror
  datum definition.
- The new remark records a finite-volume source spectral formula:
  \(G_O(\beta)=\sum_n |\langle e_n,Oe_0\rangle|^2 e^{-\beta(E_n-E_0)}\).
  This makes operator/source matrix elements part of the full mirror datum,
  not a consequence of the Hamiltonian spectrum or protected ring alone.
- Added `check_full_mirror_operator_source_obstruction()` to the GLSM
  companion.  It constructs two finite candidate endpoints with the same
  spectrum and protected multiplication data but different Euclidean source
  two-point coefficients.
- Updated the calculation README, evidence contract, and Ch09 dossier with
  the operator/source matrix-element comparison tag.

## Quality Audit

- This is not another protected Hori--Vafa residue identity.  It targets the
  operator/state-completeness debt left open by #848.
- The edit stays inside the QFT comparison layer: it asks what source
  derivatives of the regulated generating functional require after the
  spectral-domain data have been named.
- The TeX contains no process language, review directives, GitHub references,
  or planning-document text.

## Verification

- Focused GLSM checks passed:
  `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`;
  `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`;
  `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`.
- Focused Ch09 audits passed:
  `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`;
  `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`;
  `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`;
  `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --window 120 --stride 60 --fail --limit 20`;
  `tools/audit_monograph_text.sh monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`.
- TeX process-language scan passed:
  `rg -n "claude|review|directive|monitor|issue #|GitHub|planning/build_audits" monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
  returned no matches.
- Metadata and dossier audits passed:
  `python3 -m json.tool calculation-checks/evidence_contracts.json >/dev/null`;
  `python3 tools/audit_calculation_check_inventory.py`;
  `python3 tools/audit_calculation_evidence_contracts.py`;
  `tools/audit_chapter_dossiers.sh`.
- Global checks passed:
  `tools/run_calculation_checks.sh --python-only`;
  `tools/build_monograph.sh`;
  `git diff --check`.

## Freshness

- `claude_review.md` was unchanged since 2026-06-03 07:48:35 PDT.
- Saved monitor automations remained `PAUSED`.
- Open issues were refreshed before this note.  #848 had no newer comment
  after `a0268a37` (`Define admissible mirror spectral domains`) at
  2026-06-07T12:12:10Z.

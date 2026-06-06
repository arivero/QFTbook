# 2026-06-06 Issue #844 Rigorous-RG Observable-Map Audit

## Scope

- Audited the Volume XI Chapter 7 rigorous-RG hotspot under the canonical
  claim-architecture rule.
- Reframed the model-by-model synthesis as an observable-output map rather
  than a status classifier.
- Cleaned local reader-facing "ledger" headings where the text was only using
  ordinary identity, proof-order, or reconstruction-analysis language.
- Updated the Chapter 7 dossier and calculation-check inventory.
- Extended `calculation-checks/rg_projection_checks.py` with an ordered
  observable-output stage check.

## Quality Intent

The pass addresses the #844 risk that formal RG objects can look like physical
predictions before source windows, reconstruction topology, and target
identification have been supplied.  The reader-facing synthesis now orders the
physical target, RG map, fixed point or trajectory, source-window control,
observable reconstruction, target identification, and verification boundary.
Auxiliary hierarchical systems, tensor maps, functional-RG ansatz flows, and
long-range fermionic constructions are therefore compared by the observable
claim they actually support, not by shared fixed-point vocabulary.

## Companion Evidence

`check_rg_claim_observable_output_stage_map()` models the ordered stage prefix
with exact finite data.  It accepts a complete ordinary short-range
observable package, but rejects:

- an auxiliary hierarchical fixed point promoted to a short-range observable
  without target identification;
- a projected functional-RG beta zero promoted before a full fixed-point lift;
- a skipped reconstruction layer hidden by later target labels.

This is a category-boundary check, not a proof of an RG theorem.

## Verification

- `python3 -m py_compile calculation-checks/rg_projection_checks.py`
- `python3 calculation-checks/rg_projection_checks.py`
- `tools/run_calculation_checks.sh --python-only --only rg_projection`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_xi/chapter07_rigorous_renormalization_group.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_xi/chapter07_rigorous_renormalization_group.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_xi/chapter07_rigorous_renormalization_group.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_xi/chapter07_rigorous_renormalization_group.tex --fail --limit 20`
- `git diff --check`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh` (clean; `main.pdf`, 3404 pages)

All targeted and repository-wide checks passed before landing.

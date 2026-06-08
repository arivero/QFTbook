# Issue #844 Semantic-Status Follow-Up

## Scope

- Re-audited overpromoted `controlledapproximation` blocks named in the
  issue #844 follow-up comments: status summaries, a literal hypothesis,
  theorem-boundary checklists, exact finite constructions, and one exact
  continuity identity.
- Kept stable labels where downstream references already point to the block,
  but updated cross-reference prose to cite the actual semantic environment.

## Manuscript Changes

- Demoted status/checklist blocks to remarks:
  Gribov--Zwanziger status, Eguchi--Kawai status, small-\(x\) resummation
  status, projective scattering status, supercoset status, sausage bootstrap
  matching, subgroup algorithm status, the integrated Drell--Yan theorem
  boundary, and the finite Glauber calculation boundary.
- Reclassified the nested string input as a hypothesis.
- Reclassified the two-state spectroscopy mixing coordinate as a definition.
- Reclassified the compact-QED noninvertible chiral-defect block as a
  construction.
- Reclassified the produced-stress continuity block as a proposition, because
  it is an exact finite-window identity inside the stated diagonal particle
  ansatz; the subsequent backreaction use remains the controlled
  approximation.

## Guardrail Added

- `tools/audit_theorem_form.py` now rejects `controlledapproximation` titles
  of the form `Status of ...`, `... hypothesis`, `... theorem boundary`, and
  `What ... proves`, in addition to the earlier proof-obligation/data-package
  vocabulary.
- `planning/12_strict_writing_harness.md` records the same rule in planning
  prose, keeping the directive out of the monograph TeX.

## Verification

- `python3 tools/audit_theorem_form.py`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `python3 tools/audit_negative_scope_prose.py`: clean.
- `python3 tools/audit_unnumbered_display_labels.py`: clean.
- Focused `python3 tools/audit_style_density.py --root ... --fail` on every
  touched chapter: clean.
- Full `python3 tools/audit_style_density.py --fail --limit 40`: pre-existing
  unrelated clusters remain in Volume VII/VIII/X chapters; none is in this
  edit set.
- `tools/run_calculation_checks.sh --python-only`: clean.
- `python3 calculation-checks/scet_factorization_checks.py`: clean, including
  the factorization occurrence ledgers updated in this pass.
- `tools/build_monograph.sh`: clean after shortening two remark headings that
  initially produced local overfull boxes.

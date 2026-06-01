# Interval Subgroup-Boundary Wrapper Demotion

## Scope

Issue #691 proof-substance continuation in
`volume_viii/chapter11_finite_gauge_theory_state_sum_tqft.tex`.

## Audit Finding

The former proposition `Interval sectors for subgroup boundaries` was a useful
finite example but not a theorem-family result.  Its proof consisted of the
direct action groupoid identification, orbit classification, stabilizer
calculation, and a reference to the already-established finite
action-groupoid cardinality formula.

## Edit

The material is now a worked paragraph labelled
`par:finite-subgroup-boundary-double-cosets`.  The action groupoid
`G//(H_0 x H_1)`, double-coset sector set `H_0\G/H_1`, stabilizer
`H_0 cap g H_1 g^{-1}`, and groupoid cardinality
`|G|/(|H_0||H_1|)` are unchanged.  The theorem-form audit now rejects the old
wrapper title if it is reintroduced.

## Verification

Passed:

- `python3 -m py_compile tools/audit_theorem_form.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` gives `Pages: 2798`

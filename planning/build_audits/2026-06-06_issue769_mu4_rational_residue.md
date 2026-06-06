# Issue #769 mu4 rational residue

Date: 2026-06-06

## Scope

This pass strengthens the loop-level generalized-unitarity section of
Volume II, Chapter 6 by replacing a qualitative rational-term warning with
the local residue mechanism needed for a physical gauge-theory amplitude.
The new controlled approximation is
`ca:dimension-shifted-all-plus-rational-residue`.

The insertion derives, in the declared scalar-box normalization, the
dimension-shift relation
\[
I_4^{[\mu^4]}=-\epsilon(1-\epsilon)I_4^{(8-2\epsilon)}
\]
and the shifted-box simplex pole
\[
I_4^{(8-2\epsilon)}=\frac{1}{6\epsilon}+O(1),
\]
so the evanescent numerator leaves the finite rational residue \(-1/6\).
The text then identifies the massive-four-dimensional unitarity operation:
keep the cut scalar mass \(m_\mu^2\), extract the \(m_\mu^4\) coefficient of
the cut-tree product, and only then apply the dimension-shift residue.

## Quality And Scope Re-Audit

- Physics depth: this is not a new spinor or integral identity for its own
  sake.  It explains why the pure-Yang--Mills all-plus amplitude is absent
  from strict four-dimensional cuts and how the missing regulator data enter
  the reconstructed amplitude.
- Architecture: the block sits between the four-point all-plus warning and
  the five-point all-plus template, so the reader sees the mechanism before
  the higher-multiplicity recurrence of the same blind spot.
- Boundary: the coefficient of a physical color-ordered amplitude is still
  left convention dependent until loop measure, color, and particle content
  are declared.  The pass derives the universal local \(\mu_\perp^4\) box
  residue in the chosen normalization, not a full all-plus Feynman-graph
  calculation.

## Evidence Companion

`calculation-checks/generalized_unitarity_reduction_checks.py` now includes
`check_mu4_dimension_shift_rational_residue()`.  The check verifies:

- the three-simplex pole coefficient \(1/6\);
- the finite dimension-shift residue \(-1/6\);
- independence of the residue from the finite part of the shifted box at
  this order;
- extraction of a sample massive-scalar \(m_\mu^4\) coefficient;
- strict four-dimensional cut blindness to the same nonzero rational residue;
- wrong-sign and no-dimension-shift negative controls.

## Verification

- `python3 -m py_compile calculation-checks/generalized_unitarity_reduction_checks.py`
- `python3 calculation-checks/generalized_unitarity_reduction_checks.py`
- `tools/run_calculation_checks.sh --python-only --only generalized_unitarity`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex --window 120 --stride 60 --fail --limit 20`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

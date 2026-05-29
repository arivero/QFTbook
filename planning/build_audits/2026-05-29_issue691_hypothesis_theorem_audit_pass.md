# 2026-05-29 Issue #691 Hypothesis/Theorem-Form Audit Pass

## Scope

This pass tightened the theorem-form harness so that a nearby theorem-family
statement after either an `assumption` or a `hypothesis` is audited.  Reviewed
exceptions are now explicit in `tools/audit_theorem_form.py`.

## Demotions

- Recast the Carlson interpolation uniqueness corollary as a paragraph
  applying the quoted Carlson theorem.
- Recast the free Reggeon heat kernel and the two-Reggeon Gaussian
  convolution as calculations rather than propositions.
- Retitled the higher-dimensional Froissart counting result as conditional.
- Recast the SQCD Higgs-patch collective-coordinate count, Yukawa-lifting
  Berezin determinant, and electric-magnetic anomaly arithmetic as explicit
  calculations rather than propositions.
- Recast the soft-drop IRC classification and the hypersurface GLSM classical
  chamber analysis as local analyses rather than propositions.

## Harness

`tools/audit_theorem_form.py` now rejects reintroduction of those demoted
calculation wrappers as theorem/proposition/lemma/corollary titles.

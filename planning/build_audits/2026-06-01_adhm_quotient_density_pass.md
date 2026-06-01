# ADHM Quotient Density Pass

Date: 2026-06-01

Issue lane: #597.

## Scope

This pass continues the instanton-measure development after the general
ADHM quotient datum was added.  The previous pass supplied the variables,
moment maps, stability, and dimension count.  The remaining local gap was
that the "moduli-space measure" still appeared as a named object rather than
as a finite-dimensional quotient density with an explicit coarea formula.

## Manuscript Changes

- Added Definition `def:adhm-quotient-density` in Volume II, Chapter 20.
- Equipped the ADHM affine space with the flat Hermitian metric and defined
  the regular level set, vertical orbit tangent space, horizontal
  orthogonal complement, and quotient Riemannian density.
- Added Proposition `prop:adhm-quotient-density-coarea`, deriving the
  level-set coarea formula
  \[
    \int_{\mathcal M}F\,d\nu
    =
    \operatorname{Vol}(U(K))^{-1}
    \int_Z F(X)\,(\det M(X))^{-1/2}\,d\operatorname{vol}_Z
  \]
  from the horizontal/vertical metric splitting.
- Added the equivalent ambient delta-function expression with the
  moment-map coarea Jacobian \(J_\mu=\det(D\mu D\mu^\ast)^{1/2}\).
- Added a remark separating the classical zero-mode density from the
  nonzero-mode determinant, operator renormalization, and analytic
  small-instanton boundary estimates.

## Calculation Check

Extended `calculation-checks/bpst_instanton_normalization_checks.py` with
finite checks for:

- the \(U(1)\) polar quotient toy model, where dividing the circle density
  by \(\operatorname{Vol}(U(1))\sqrt{M}\) leaves the radial quotient density
  \(dr\);
- the homogeneous scaling of the centered ADHM quotient-density coarea
  expression: ambient density \(V\), quadratic constraints \(C\), coarea
  Jacobian \(C\), and orbit Gram factor \(G\) combine to the quotient
  dimension \(V-C-G=4kN_c-4\);
- the associated cone shell power \(4kN_c-5\).

The calculation-check README and Volume II Chapter 20 dossier were updated.

## Verification

Targeted verification should include:

```bash
python3 calculation-checks/bpst_instanton_normalization_checks.py
python3 -m py_compile calculation-checks/bpst_instanton_normalization_checks.py
git diff --check
python3 tools/audit_theorem_form.py
python3 tools/audit_unnumbered_display_labels.py
tools/audit_negative_scope_prose.py
tools/audit_monograph_text.sh
tools/audit_chapter_dossiers.sh
tools/build_monograph.sh
```

This pass still does not close #597.  It supplies the finite-dimensional
classical zero-mode quotient-density construction.  Determinant
normalizations, continuum scheme dependence, boundary estimates, and the
full multi-instanton semiclassical measure remain open.

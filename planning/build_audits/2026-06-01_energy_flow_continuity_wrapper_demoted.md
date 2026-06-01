# 2026-06-01 Energy-Flow Continuity Wrapper Demotion

## Scope

This pass continues the anti-wrapper audit for theorem-family statements whose
proofs are finite algebra rather than theorem-level QFT arguments.  The
smeared energy-flow soft/collinear continuity estimate in Volume II Chapter 19
is physically important, but its proof is the direct action of a finite
positive calorimetric measure on a \(C^1(S^2)\) test function plus a Lipschitz
bound.

## Manuscript Changes

- Demoted `Soft and collinear continuity of smeared energy flow` from
  lemma/proof form to paragraph-level worked estimate.
- Preserved the soft bound
  \(|\Delta\widehat{\mathcal E}_X(f)|\leq\varepsilon\|f\|_\infty\).
- Preserved the collinear recombination bound in terms of
  \((E_a+E_b)\operatorname{Lip}(f)\) and the support diameter.
- Reworded the energy-correlation-function paragraph so IRC safety refers to
  the worked estimate rather than a theorem-family label.

## Harness

- Added the old title to `tools/audit_theorem_form.py` so it cannot reappear
  as theorem/proposition/lemma/corollary content.

## Verification

Clean in this pass:

- `python3 -m py_compile tools/audit_theorem_form.py`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

The rebuilt manuscript is `monograph/tex/main.pdf`, 2796 pages.

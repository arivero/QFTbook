# Cohomological Localization Theorem Boundary Pass

Date: 2026-05-30

## Scope

- Reviewed `claude_review.md` and the live GitHub proof-debt backlog, with the
  TQFT/RG-mechanism cluster in issue #698 as the active target.
- Focused on Volume VIII, Chapter 5, where the compact finite-dimensional
  localization theorem still had a theorem-boundary defect: the action \(S\)
  appeared in the conclusion without being part of the theorem datum, and the
  inverse Euler factor was named before the normal super-Gaussian had been
  constructed.

## Manuscript Changes

- Made \(S\), \(X\), and \(V\) part of the finite-dimensional localization
  datum and stated \(QS=0\), \(QX=0\), and \(Q^2\)-invariance explicitly.
- Replaced the undefined "normal quadratic complex" phrase by a displayed
  local normal model
  \[
    (QV)_2=\frac12 u^iA_{ij}u^j+\frac12\eta^\alpha C_{\alpha\beta}\eta^\beta
  \]
  and defined \(e_{Q^2}(N_F)^{-1}\) through the corresponding
  determinant/Pfaffian super-Gaussian.
- Added the Berezinian-degree balance condition needed for the simple
  fixed-locus formula, rather than hiding this point in the word
  "nondegenerate."
- Expanded the proof so the Stokes/Ward step, exponential suppression away
  from \(F\), normal rescaling, Gaussian domination, and gluing of local
  Euler factors are separate steps.

## Calculation Check

- Extended `calculation-checks/cohomological_field_theory_checks.py` with an
  exact rational check of the squared inverse-Euler factor
  \(\operatorname{Pf}(C)^2/\det(A)\) in a two-even/two-odd local model.

## Verification

- `python3 calculation-checks/cohomological_field_theory_checks.py`
- `python3 -m py_compile calculation-checks/cohomological_field_theory_checks.py`
- `tools/audit_theorem_form.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_unnumbered_display_labels.py`

The full monograph build is run after this audit note in the commit workflow.

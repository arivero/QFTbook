# Eleventh Cross-Volume Wrapper Pass

Date: 2026-05-29

Scope: continued issue #691 after the tenth anti-wrapper checkpoint.  This pass
used the semantic scan for substitution, convention, and finite-calculation
proofs, then read the flagged statements in context before editing.

## Demotions

Demoted six theorem-family wrappers to worked prose:

- `Majorana conjugation is Lorentz covariant`.
- `Quarkonium fine and hyperfine spin algebra`.
- `Linear elastic pole coordinate near a narrow vector resonance`.
- `Massless free QCD pressure`.
- `Infrared loop integral by Schwinger parameter`.
- `Scalar four-point prefactor covariance`.

The calculations remain in the monograph because they are useful convention,
spectroscopy, thermodynamic, hydrodynamic, and conformal-frame checks.  Their
former theorem-family status was the problem: each proof was finite algebra,
a direct coordinate linearization, or an elementary regulated integral, not a
domain theorem about QFT.

## Retained Statements

No retained proof was expanded in this pass.  The immediate compact-proof queue
contains four items that had already been read as genuine infrastructure:
Fredholm canonical coefficients, causal-propagator kernel identification,
unitary implementation in the GNS setting, and Chern--Weil transgression.

## Guardrails

`tools/audit_theorem_form.py` now rejects recurrence of the six demoted titles
as theorem-family wrappers.

## Verification

Commands run before the full build:

- stale-label scan for all removed labels.
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_unnumbered_display_labels.py`

Final checkpoint verification completed:

- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` (`Pages: 2582`)

The full build and final log scan are clean.

## Remaining Queue

The `<=115`-word immediate-proof heuristic queue remains four items:

- `Fredholm expansion and canonical coefficients`.
- `Kernel of the causal propagator`.
- `Unitary implementation of an invariant state`.
- `Chern--Weil transgression`.

The broader semantic queue remains the next useful target.  The current
estimate is roughly ten to twenty likely demotions, plus a comparable number of
status rewrites where theorem/proposition language is too strong because the
substance is carried by hypotheses.

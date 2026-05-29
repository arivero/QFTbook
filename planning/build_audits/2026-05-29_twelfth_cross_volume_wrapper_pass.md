# Twelfth Cross-Volume Wrapper Pass

Date: 2026-05-29

Scope: continued issue #691 after the eleventh anti-wrapper checkpoint.  This
pass combined the semantic scan for definition/substitution proofs with the
short-proof queue above the already-reviewed `<=115` band.  Each edited item was
read in local context before demotion.

## Demotions

Demoted twelve theorem-family wrappers to worked prose:

- `Wigner cocycle and change of helicity frame`.
- `External-pole stability`.
- `Exact low-source identity for a plateau split`.
- `Mirror TBA variational equation`.
- `Longitudinal HTL response and Landau cut`.
- `Explicit \(SU(3)\) Wilson-score gradient`.
- `One-screening Dotsenko--Fateev beta integral`.
- `Null factorization and mostly-plus spinor invariant`.
- `On-shell degrees of freedom of a chiral two-form`.
- `Finite redefinitions and beta-vector fields`.
- `\(\mathcal N=(2,2)\) one-loop K\"ahler beta tensor`.
- `Uhlenbeck boundary as BV boundary data`.

The text keeps the formulas and calculations.  The change is the status label:
these are frame algebras, residue-coordinate bookkeeping, finite-regulator
identity bookkeeping, repeated variational calculations, elementary integrals,
degree-of-freedom counts, chain-rule transformations, specializations of
earlier beta-function calculations, or applications of a previously stated BV
boundary principle.

## Guardrails

`tools/audit_theorem_form.py` now rejects recurrence of the twelve demoted
titles as theorem/proposition/lemma/corollary wrappers.

## Verification

Commands run before the full build:

- stale-label scan for all removed labels.
- `python3 tools/audit_theorem_form.py`

Current proof-environment count after this pass: `674`.  The `<=115`-word
queue remains four compact infrastructure items; the `<=130` queue is down to
thirty-eight items.

Final checkpoint verification completed:

- `git diff --check`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` (`Pages: 2582`)

The full build and final log scan are clean.

## Remaining Queue

The remaining likely-demotion count is now lower but not exhausted.  A
conservative estimate is roughly eight to fifteen likely demotions plus another
ten or so status rewrites where the theorem-family wrapper is not obviously
trivial by length, but the substance is hidden in hypotheses or prior
definitions.

# 2026-05-29 Volume I Chapter 8 Wrapper Pass

## Scope

This pass reviewed the first short-proof candidates in the scalar
path-integral and Green-function chapter.

## Decisions

- The finite-dimensional Schrödinger-regulator criterion was initially retained
  as a proposition because it precisely records when the finite-dimensional
  Trotter--Kato and Feynman--Kac theorems may be used.  A later proof-status
  pass demoted it to framework prose because the theorem-level work is the
  Chapter 4 theorem, not the matching of hypotheses in this chapter.
- The zeta determinant scale-dependence formula was demoted to a worked
  paragraph.  The calculation is useful and remains fully displayed, but its
  proof is the Mellin-transform bookkeeping following from the determinant
  definition and heat-kernel expansion.
- The free Feynman boundary-value pole-placement formula was demoted to a
  worked paragraph.  It remains the local derivation of the \(i\epsilon\)
  denominator from Wick rotation, but it is not a theorem-level claim.
- The theorem-form audit now rejects reintroducing these two calculation
  titles as theorem-family wrappers.

## Verification

This note is paired with the full verification run for the commit: strict text
audit, negative-scope prose audit, theorem-form audit, display-label audit,
`git diff --check`, and a full monograph build.

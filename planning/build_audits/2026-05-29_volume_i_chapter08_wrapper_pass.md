# 2026-05-29 Volume I Chapter 8 Wrapper Pass

## Scope

This pass reviewed the first short-proof candidates in the scalar
path-integral and Green-function chapter.

## Decisions

- `prop:scalar-regulator-trotter-status` remains a proposition because it is a
  precise conditional import of the finite-dimensional Trotter--Kato and
  Feynman--Kac theorems.  Its title was changed to the positive formulation
  "Finite-dimensional Schrödinger regulators inherit Trotter--Kato".
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

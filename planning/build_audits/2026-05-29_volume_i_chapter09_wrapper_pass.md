# 2026-05-29 Volume I Chapter 9 Wrapper Pass

## Scope

This pass reviewed the first short-proof candidates in the Kallen--Lehmann
chapter.

## Decisions

- The spacelike parity of \(\Delta_+(x;\mu^2)\) was demoted from a proposition
  to a worked calculation.  The frame choice \(x\mapsto(0,\vec r)\) and
  \(\vec p\mapsto-\vec p\) argument remains in full because it is useful for
  seeing how locality is encoded in the positive-frequency kernel.
- The Euclidean Kallen--Lehmann and subtracted Stieltjes statements remain
  propositions: they organize spectral positivity into Euclidean analytic
  data and contact-term ambiguity.
- The scalar-field matrix element on an isolated shell remains a proposition,
  but its hypotheses were sharpened.  The statement now works in a selected
  spin-zero isolated channel, and the proof explains the distributional point
  notation, the zero-overlap case, phase fixing, and the multiplicity-space
  variant.
- The theorem-form audit now rejects reintroducing the spacelike parity
  calculation as a theorem-family wrapper.

## Verification

This note is paired with the full verification run for the commit: strict text
audit, negative-scope prose audit, theorem-form audit, display-label audit,
`git diff --check`, and a full monograph build.

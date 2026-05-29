# 2026-05-29 Volume I Chapter 11 Anti-Wrapper Pass

## Scope

Read the theorem-family statements in
`monograph/tex/volumes/volume_i/chapter11_lorentzian_green_functions_and_analytic_continuation.tex`
whose proofs were short or calculation-heavy.

## Decisions

- Kept proposition-level status for compatibility of time-ordered Wightman
  pieces, contact-term freedom, forward-tube analyticity, loop-rotation pinch
  obstruction, and spectral thresholds.  These statements depend on
  distributional extension, spectrum-condition support, edge-of-the-wedge or
  Landau-support reasoning, not on a mere substitution.
- Demoted `Free scalar Feynman boundary value` to a worked paragraph.  The
  content is an important pole-placement derivation, but the proof is a
  contour evaluation of the two time orderings.
- Demoted `Source sign under Wick rotation` to a worked paragraph.  The
  content is a convention-fixing calculation of `i dz^0` on the two Wick
  contours.
- Demoted `Lorentzian--Euclidean graph factor under simultaneous rotation` to
  a worked paragraph.  The mathematical substance is the stated contour-pinch
  hypothesis; the phase is graph bookkeeping once that hypothesis is imposed.
- Demoted `Tadpole contour rotation and self-energy matching` to a worked
  paragraph.  The residual automorphism factor and contour rotation are needed
  in the text, but the proof is the displayed one-loop calculation.

## Recurrence Guard

`tools/audit_theorem_form.py` now rejects these four titles if they reappear in
theorem-family environments.

## Verification

Run the theorem-form audit, text audits, diff check, and full monograph build
after the edit.

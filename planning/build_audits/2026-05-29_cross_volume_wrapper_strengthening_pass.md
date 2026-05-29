# 2026-05-29 Cross-Volume Wrapper Strengthening Pass

## Scope

Read the highest-scoring remaining theorem/proof candidates from the broad
anti-wrapper heuristic.  Decisions were made from the local mathematical
content, not from the heuristic score alone.

## Demoted To Worked Paragraphs

- `Two-magnon matching for the one-loop chain`: kept the finite-difference
  contact calculation because it fixes the ordered-chamber convention, but
  removed theorem-family status.
- `Normalization and first moment of track-function evolution`: kept the
  paired finite-kernel moment derivation, but demoted it because the proof is
  moment algebra once the nonperturbative track-function datum has been
  defined.

## Strengthened As Substantive Claims

- `Mathai--Quillen localization for a transverse section`: expanded the proof
  through deformation by \(t^{1/2}s\), exponential suppression away from the
  zero locus, tubular normal coordinates, Gaussian/Berezin determinant
  cancellation, and the induced orientation of \(Z(s)\).
- `Local uniform convergence and Barnes representation of \(H\)`: replaced
  the thin convention proof with a Weierstrass-product convergence argument,
  termwise logarithmic differentiation, and the explicit Barnes \(G\)-product
  comparison.
- `Retarded stress-tensor response at separated points`: expanded the proof
  with the metric-source sign convention, retarded support, microcausality,
  and the separation of diagonal contact terms.
- `McKean--Singer identity`: expanded the proof to state the elliptic spectral
  input, trace-class heat kernel, nonzero spectral pairing, and zero-mode
  contribution.
- `Feshbach--Schur reduction at finite cutoff`: added the finite resolvent
  distance estimate controlling the eliminated \(Q\)-component.
- `Scalar lattice reflection positivity`: expanded the proof by half-lattice
  factorization and the nonnegative crossing-kernel expansion into absolute
  squares.

## Recurrence Guard

`tools/audit_theorem_form.py` now rejects the demoted titles and the old weak
titles replaced by stronger statements.

## Verification

The theorem-form/text/prose/display-label audits, `git diff --check`, and
the full monograph build were clean.  The rebuilt PDF has 2579 pages.  The
cross-volume short-proof heuristic count decreased from 82 before this pass
to 74 after the pass.

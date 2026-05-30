# 2026-05-30 Frobenius Cylinder Wrapper Pass

## Scope

Anti-wrapper audit pass on Volume VIII, Chapter 2,
`chapter02_bordism_functoriality_extended_tqft.tex`.

The former lemma `Cylinder and Frobenius identities` contained useful
relations, but its proof was a direct dual-basis verification.  The equations
are needed in the proof of the \(2D\) oriented TQFT/Frobenius-algebra
classification theorem, while the standalone lemma wrapper overstated the
substance of this algebraic check.

## Changes

- Removed the lemma/proof environment around the cylinder and neck identities.
- Kept the labelled equations
  `eq:frobenius-cylinder-identity` and `eq:frobenius-neck-identity`, because
  the later classification proof refers to them.
- Recast the verification as a paragraph explaining its geometric meaning:
  cap/cup gluing gives the cylinder identity, and critical-level interchange
  gives the neck-exchange relation.
- Left the classification theorem itself unchanged, since that is the
  substantive statement where these identities belong.

## Status

This is a demotion pass for issue #691: a trivial theorem-family wrapper was
removed while preserving the useful algebra and its role in the deeper
classification theorem.

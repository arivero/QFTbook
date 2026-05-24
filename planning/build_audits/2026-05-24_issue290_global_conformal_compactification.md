# Issue #290 Global Conformal Compactification Pass

## Scope

- Addressed GitHub issue #290:
  `[Vol V Ch 2] Global conformal compactification not described`.
- Target chapter:
  `monograph/tex/volumes/volume_iii/chapter02_conformal_killing_vectors_and_the_conformal_group.tex`.

## Content Added

- Added Section `sec:euclidean-compactification-radial-cylinder`.
- Constructed the Euclidean compactification
  \(\widehat{\mathbb R^D}\simeq S^D\) by stereographic coordinates and showed
  explicitly that the round metric is Weyl equivalent to the flat metric.
- Explained that denominator singularities in flat Mobius formulae are chart
  singularities on \(S^D\), not failures of the global conformal map.
- Connected the radial cylinder
  \(\mathbb R_\tau\times S^{D-1}\) to the compactification as the Weyl frame
  on \(\mathbb R^D\setminus\{0\}\), with origin and infinity becoming the two
  cylinder ends and inversion acting by \(\tau\mapsto-\tau\).
- Extended the Lorentzian construction with Einstein-cylinder coordinates:
  \(u=\tan((T-\chi)/2)\), \(v=\tan((T+\chi)/2)\), the Weyl factor, and the
  universal cylinder cover \(\mathbb R_T\times S^{D-1}\).
- Created GitHub issue #521 for a later full mathematical treatment of
  Euclidean and Lorentzian conformal-group representation theory.

## Verification Targets

- Chapter 2 must no longer introduce finite conformal maps only as local
  rational formulae on \(\mathbb R^D\); their global compactified action must
  be explicit.
- The radial cylinder in Chapter 4 must be connected to the conformal
  compactification, not left as an independent construction.
- The compactification pass must not pretend to complete the separate
  rigorous representation-theory development.

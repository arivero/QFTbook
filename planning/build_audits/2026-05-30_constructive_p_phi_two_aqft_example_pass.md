# 2026-05-30 Constructive P(phi)2 AQFT Example Pass

## Scope

This pass addresses the substantial-example component of issue #695.  Volume
IV, Chapter 3 already contained the conditional Wightman-to-net theorem; the
new text adds an interacting model checkpoint showing how the hypotheses of
that theorem are verified or separated in a constructive scalar model.

## Manuscript Change

- Added a paragraph-level constructive `P(phi)_2` checkpoint after the
  Wightman-to-net status remark.
- Defined the bounded local field net by spectral projections of the
  self-adjoint closures of real smeared reconstructed fields.
- Listed the model-specific analytic inputs required before the formula is a
  Haag-Kastler net: essential self-adjointness, strong commutation of
  spacelike separated closures, and covariance/time-slice compatibility of
  the limiting bounded functions.
- Distinguished the local field net from the fixed-point observable net when
  the constructive model has a finite internal symmetry group.
- Recorded how kink sectors, mass gap, nuclearity, split inclusions, Haag
  duality, and DHR reconstruction become concrete model questions rather than
  abstract axiomatic assumptions.

## Issue Alignment

- #695: adds an interacting constructive AQFT object rather than only theorem
  boundaries for abstract local nets.
- #691: avoids presenting the model checklist as a proposition; it is
  construction prose because the theorem-level content lies in the
  model-specific estimates.

## Remaining Proof Debt

This pass does not close #695.  The constructive example must eventually be
expanded with explicit model estimates for nuclearity/split/duality wherever
the monograph uses those properties, and other interacting examples remain
needed.

# Forty-Eighth Cross-Volume Wrapper Pass

Date: 2026-05-29

Purpose: continue issue #691 after the forty-seventh pass by reading the next
high-risk proposition/theorem candidates.  This pass focused on useful
support facts whose proofs are finite algebra, finite-dimensional projection,
or direct covariance/monodromy consequences.  The mathematical content is
retained, but proposition status is removed.

## Demoted To Lemmas

- Volume I, Chapter 13:
  `External pole as one-particle spectral projection`.  This is the support
  lemma identifying the LSZ pole residue with the isolated one-particle
  spectral projection.
- Volume I, Chapter 16:
  `Finite Berezin Gaussian and contractions`.  The determinant/source identity
  and contraction convention are essential for later fermionic path integrals,
  but the proof is finite exterior algebra with the declared Berezin ordering.
- Volume II, Chapter 10:
  references to the BPST data item now point to its lemma form.
- Volume II, Chapter 19:
  `Polynomiality of GPD moments`.  The proof is the local twist-two expansion
  plus Lorentz-covariant tensor decomposition; it is a structural support lemma
  for GPDs, not an independent proposition.
- Volume II, Chapter 19:
  `Zero-recoil normalization`.  The proof uses the leading-HQET heavy-flavor
  charge normalization to fix the Isgur-Wise value at \(w=1\); it supports the
  heavy-quark expansion.
- Volume II, Chapter 20:
  `BPST one-instanton data`.  The instanton curvature, charge, and action
  normalization remain explicit, but this is a convention-sensitive data lemma.
- Volume II, Chapter 20b:
  `Exact bosonized local gauge sector`.  The result follows from the preceding
  current-sector bosonization theorem and local elimination of the electric
  field branch.
- Volume VII, Chapter 6:
  `Maximal-rank meson invariant for the ADS patch`.  This is a holomorphic
  invariant-function lemma on the maximal-rank meson locus.
- Volume VII, Chapter 7:
  `Rank-one hypermultiplet monodromy`.  The Picard-Lefschetz monodromy formula
  is retained as a reusable special-geometry lemma.
- Volume X, Chapter 4:
  `Finite-volume Mazur projection`.  The proof is the finite-dimensional
  Hilbert-space projection onto conserved charges and the resulting
  zero-frequency lower bound.
- Volume X, Chapter 12:
  `Finite-regulator Roberge-Weiss periodicity`.  The exact finite-regulator
  periodicity is a center-twisted gauge-transformation lemma.
- Volume XI, Chapter 6:
  `Pairwise detailed balance for compact SU(2) link Metropolis`.  This is a
  finite Markov-kernel detailed-balance lemma under the inversion-symmetric
  proposal hypothesis.

## Retained After Reading

The following high-score candidates were read and retained in their current
status:

- local conformal-current Ward identity: a source-chart contact-distribution
  statement combining translation, trace, and conformal-current Ward data;
- mid-link/free/staggered/lattice reflection-positivity statements: finite
  reflection-positive mechanisms, not merely sign checks;
- finite-codimension critical surface: an application of the stable graph and
  submersion/implicit-function theorem;
- isolated spectral atom and LSZ bound-state pole statements: foundational
  spectral-to-pole machinery;
- finite-dimensional BV Stokes and BV pushforward/QME statements: genuine BV
  integration machinery, even in finite Darboux charts;
- RTT and transfer-matrix commutativity: core integrability algebra rather
  than disposable algebraic arithmetic.

## Inventory After This Pass

- theorem: 87
- proposition: 267
- lemma: 114
- corollary: 10
- theorem-family total: 478
- proof: 473
- remark: 313
- example: 75

The theorem-family total is unchanged from the previous pass because these
edits demote proposition status to lemma status.  This is still meaningful:
the proof burden is now presented as local support infrastructure instead of
as proposition-level structure.

Remaining work for #691: the obvious calculation wrappers are mostly exhausted.
The next passes should read semantic clusters where proposition status may be
supported by nontrivial hypotheses, especially local-net construction,
contact-term source identities, finite-dimensional BV/cohomological machinery,
and conditional RG/constructive statements.

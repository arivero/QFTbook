# Forty-Sixth Cross-Volume Wrapper Pass

Date: 2026-05-29.

Purpose: continue issue #691 by reading another cluster of short
theorem/proposition proofs as statement-hypothesis-proof units.  The goal of
this pass was not to make every short proof disappear: compact proofs of real
machinery are acceptable.  The target was the narrower failure mode in which a
calculation, convention conversion, or direct substitution was packaged as a
proposition with a proof environment.

## Demoted or Reframed

- Volume XI, chapter 9: `Mixed-covariance criterion for common Wick limits`
  was lowered from proposition to lemma.  It is a useful covariance-to-Wick
  convergence tool, but its proof is the Wick covariance identity plus
  continuity of polynomial Gaussian moments in a fixed covariance norm.
- Volume XI, chapter 9: `Global compact-continuity criterion for DPD solution
  maps` was lowered from proposition to lemma.  The result organizes a
  blow-up-alternative/compactness argument; the analytic substance remains in
  the rough energy and Besov fixed-point estimates.
- Volume XI, chapter 9: `Sobolev compactness criterion for cutoff-field
  tightness` was lowered from proposition to lemma.  The proof is the compact
  embedding plus Markov inequality.
- Volume XI, chapter 9: `Bounded-cylinder comparison from a common density
  limit` was lowered from proposition to lemma.  It is the measure-theoretic
  \(L^1\)-density comparison used by the regulator discussion.
- Volume XI, chapter 9: `Dyadic Cauchy criterion for random models` was
  lowered from proposition to lemma.  The statement is an abstract convergence
  lemma; the deep work is the BPHZ random-model construction and the tree
  estimates that verify its hypotheses.
- Volume I, chapter 7: `Noether identity for a variational symmetry` was moved
  out of proposition/proof form and written as a paragraph-level off-shell jet
  identity, with the local identity now referenced by equation number.
- Volume I, chapter 16: `Odd second-class constraints and Dirac brackets` was
  moved out of proposition/proof form.  The finite odd-mechanics computation is
  still present, including the Dirac bracket and the two-state \(N=2\)
  quantization, but it is no longer presented as a proposition.
- Volume II, chapter 17: `Connection, curvature, and Bianchi identities` was
  moved out of proposition/proof form.  The convention, component curvature,
  covariance, and Bianchi derivation remain in the main flow.
- Volume XI, chapter 9: `Finite-cutoff nonlinear coordinate decomposition` was
  moved out of proposition/proof form.  The finite-cutoff Wick decomposition
  for \(XY\) and \(X^2Y\), including the exact local subtraction term, remains
  as derivation prose.

## Read and Retained in This Pass

- The pAQFT change of Hadamard function was retained as a proposition.  The
  proof is short because the second-order contraction operator gives a compact
  coproduct identity, but the statement is a genuine algebra-isomorphism
  result.
- The scattering-chamber consistency statement in factorized scattering was
  retained as a proposition.  It identifies the groupoid presentation of
  rapidity-chamber changes with unitarity and the Yang-Baxter relation.
- The Kotecky--Preiss/Brydges--Kennedy convergence criterion was retained as a
  theorem.  Its proof contains the rooted-tree recursion and the uniform
  polymer-cluster convergence bound; it is not just a restatement of a
  smallness hypothesis.
- The Osterwalder-Seiler character criterion was retained as a theorem.  It is
  a finite-volume reflection-positivity theorem using Peter-Weyl decomposition
  of crossing plaquettes into sums of squares.
- The finite Grassmann reflection-positivity criterion was retained as a
  proposition.  The proof performs the finite Berezin ordering and positivity
  reduction required for lattice fermions.
- The McKean--Singer identity was retained as a proposition.  The statement is
  the heat-trace index bridge; the proof uses elliptic spectral pairing and
  trace-class heat-kernel convergence.
- The OS semigroup contraction and one-gap continuation propositions were
  retained.  They are basic, but they carry the corrected OS-II reconstruction
  logic: polynomial growth gives contraction, and the spectral theorem gives
  the controlled one-gap boundary value.

## Harness Update

`tools/audit_theorem_form.py` now rejects reintroduction of these
calculation-only theorem-family titles:

- `Finite-cutoff nonlinear coordinate decomposition`
- `Finite-cutoff Wick decomposition for nonlinear negative coordinates`
- `Connection, curvature, and Bianchi identities`
- `Noether identity for a variational symmetry`
- `Odd second-class constraints and Dirac brackets`

## Inventory After Edits

- theorem: 87
- proposition: 291
- lemma: 92
- corollary: 10
- theorem-family total: 480
- theorem/proposition total: 378
- proof environments: 475
- controlled approximations: 70
- examples: 75
- remarks: 312

The remaining risk is increasingly semantic rather than lexical.  The highest
priority tail is the pattern where a proposition is a consequence of a strong
assumption whose real mathematical content has not been justified nearby.  A
separate reading pass is still required for those assumption/proposition
pairs; #691 remains open.

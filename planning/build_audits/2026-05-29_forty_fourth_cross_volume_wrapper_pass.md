# Forty-Fourth Cross-Volume Anti-Wrapper Pass

Date: 2026-05-29

Scope: Continued Issue #691 audit of theorem/proposition/corollary packaging,
with emphasis on statements whose proofs are coefficient extractions,
finite-dimensional algebra, or direct consequences of a stronger hypothesis.

## Demoted Formal Statements

- Vol I ch19: `Tree-level Ward identity for the Compton hard kernel`
  from theorem to lemma.  The cancellation is important for the representative
  independence of the displayed Born kernel, but its proof is a tree-level
  diagrammatic Ward calculation.
- Vol I ch20: `One-loop QED vacuum polarization in explicit-coupling
  coordinates` from proposition to lemma.  The derivation remains fully
  displayed; the formal role is a convention-sensitive one-loop coefficient.
- Vol II ch06: `Auxiliary pushforward and the p=0 momentum trace` from
  proposition to lemma, with references updated.  It is a functional-analytic
  support lemma for the Dyson lift.
- Vol II ch08: `Power-counting finite-list criterion` and `One-loop local
  poles in six-dimensional cubic theory` from propositions to lemmas.
- Vol II ch14: `One-loop quartic vector field` from proposition to lemma.
- Vol II ch19: `Antisymmetric Casimir ratio in trace-delta convention`,
  `Free transverse determinant and the Luscher term`, `Coupled-channel
  K-matrix determinant and sheet continuation`, and `Tree-level collinear
  coefficient for the separated EEC` from propositions to lemmas.
- Vol II ch19c: `One-loop gauge beta coefficients` from proposition to lemma.
- Vol II ch20c: `Endpoint exponents` from corollary to lemma.
- Vol II ch23: `1PI source equation and inverse two-point kernel` from
  proposition to lemma.
- Vol III ch02: `Euclidean conformal charge algebra` from proposition to lemma.
- Vol V ch11: `One-loop metric divergence`, `One-loop string-frame
  functional`, `Local one-loop origin of the H-coefficients`,
  `Torsionful one-loop package`, and `Modular behavior of the lattice trace`
  from propositions to lemmas.
- Vol V ch13: `Screening computation of the degenerate OPE coefficient` and
  `Dual screening computation` from propositions to lemmas.
- Vol V ch15: `Mode algebra from the N=1 OPEs` from proposition to lemma.
- Vol VI ch09: `Sugawara tensor at the WZW endpoint` from proposition to lemma.
- Vol VII ch02: `Gauge kinetic coefficient in Wess-Zumino gauge` from
  proposition to lemma.
- Vol VII ch08: `Algebra of the SU(2), N_f=2 quantum deformation` from
  proposition to lemma, with an explicit sentence added that the dynamical
  content is the Wilsonian quantum-deformation input and the lemma records only
  algebraic consequences.
- Vol X ch07: `One-loop origin and coefficient of the Debye mass term` from
  proposition to lemma.
- Vol XI ch02: `Two-loop local mass coordinate in the chapter's normalization`
  from proposition to lemma.
- Vol XI ch09: `Spatial Fourier cutoff two-loop coordinate` from proposition
  to lemma.
- Vol XI ch10: `Rayleigh-Ritz bound at fixed Hamiltonian` from proposition to
  lemma.
- Vol XII ch02: `First logarithmic Hadamard coefficient` from proposition to
  lemma.

## Retained After Reading

- `Analytic Fredholm Bethe-Salpeter pole criterion`: retained as theorem.  The
  statement is a genuine analytic-Fredholm pole criterion, not a coefficient
  check.
- `Axis trace nonuniqueness`: retained as proposition.  It constructs a
  counterexample to a tempting Dyson-axis inference.
- `Finite-dimensional thimble decomposition`: retained as theorem.  The
  assumptions are explicit properness/no-escape/Morse data, and the statement
  is the finite-dimensional relative-homology decomposition needed before any
  QFT thimble analogy.
- `Argument criterion for allowability`: retained as theorem.  It proves the
  Kontsevich-Segal linear allowability criterion from the pointwise positivity
  conditions.
- `Finite-dimensional BV Stokes theorem`: retained as theorem.  This is the
  finite-dimensional BV integration theorem used by later localization
  arguments.
- `Smooth Fourier multiplier covariance convergence` and
  `Mixed-covariance criterion for common Wick limits`: retained as
  propositions.  These are analytic estimates with dyadic bounds and explicit
  convergence hypotheses, not merely substitutions.

## Counts After This Pass

The theorem-family distribution after the edits is:

- theorem: 90
- proposition: 305
- corollary: 10
- lemma: 82
- hypothesis: 49
- assumption: 15

The title-keyword screen for theorem/proposition/corollary candidates is down
to 30 survivors.  The screen is intentionally over-inclusive; the remaining
items require continued semantic reading rather than mechanical demotion.

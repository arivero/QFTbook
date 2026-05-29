# Thirty-Fourth Cross-Volume Wrapper Pass

Date: 2026-05-29

Scope: continued Issue #691 proof-substance audit, concentrating on the
short-proof queue after commit `4aeeedfa`.

Changes made:

- Demoted the aligned Cartan Abelian-string BPS bound from a proposition/proof
  to a derivation paragraph.  The displayed bound is the rank-one
  square-completion plus a triangle inequality inside a deliberately
  Abelianized chart; the hypotheses and scope remain explicit.
- Demoted the first hydrodynamic pole formulas from a proposition/proof to a
  calculation paragraph.  The formulas follow by solving the linearized
  first-order constitutive equations after the derivative expansion and
  retarded-correlator assumptions have been made.
- Demoted the massless Schwinger-model screened static potential from a
  proposition/proof to an inline static-probe calculation, and updated the
  figure caption so it no longer points to a theorem-family wrapper.
- Demoted the flat trace equation from a proposition/proof to a source-chart
  derivation paragraph.  The nontrivial input is the existence of the local
  source functional and local RG vector field; the displayed identity is the
  separated-point consequence.
- Demoted the finite-regulator Polyakov-loop character-coordinate selection
  rule from a proposition/proof to a Peter--Weyl/center-charge derivation
  paragraph, and updated the later reference accordingly.
- Expanded the causal-propagator kernel lemma in the locally covariant free
  scalar chapter to spell out smoothness, equality of retarded and advanced
  representatives, \(P_Mu=f\), compactness of the causal diamond by global
  hyperbolicity, and compact support of \(u\).

Retained after reading:

- Fredholm expansion and canonical coefficients: a genuine trace-class
  Fredholm-minor identity, short because it invokes finite-rank approximation
  and exterior-power trace-norm bounds.
- Exact center symmetry of pure thermal lattice Yang--Mills: elementary but
  exact finite-regulator symmetry statement, not merely notation.
- Anomaly-induced massive electric field and exact bosonized local gauge
  sector in the Schwinger model: exact operator/current-sector consequences
  central to the example, not just decorative computations.
- Perturbative interacting local net: a structural pAQFT consequence of
  causal factorization, time-slice quotient, and relative \(S\)-matrices.
- Functoriality of the locally covariant free scalar: kept as proposition
  because it constructs the covariant functor and is used by the time-slice
  argument.

Current count after edits:

- theorem: 95
- proposition: 369
- lemma: 29
- corollary: 10
- proof: 498
- theorem-family total: 503

Issue #691 remains open.  The remaining short-proof queue is now dominated by
actual structural lemmas/propositions, but it still requires line-by-line
reading because shortness alone is not enough evidence either way.

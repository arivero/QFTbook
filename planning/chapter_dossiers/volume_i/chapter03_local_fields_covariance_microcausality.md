# Volume I, Chapter 3 Dossier: Local Fields, Covariance, And Microcausality

## Status

Current status: included in the compiled manuscript and cross-checked against
handwritten 253a pp. 5--9 in the 2026-05-22 source pass.

## Logical Role

This chapter gives the first proper definition-level treatment of local fields
as operator-valued distributions, states their covariance and locality
conditions, and relates field coordinates to local observable assignments.

## Framework

Working framework:

- Minkowski spacetime \(\mathbb M^D\);
- test-function space such as \(C_c^\infty(\mathbb M^D)\) or Schwartz space,
  chosen explicitly;
- dense invariant domain \(\mathcal D\subset\Hilb\) for unbounded smeared
  fields when needed;
- operator-valued distributions \(\widehat\Phi_A\);
- finite-dimensional Lorentz representation on field indices \(A\);
- strongly continuous unitary Poincare representation on \(\Hilb\);
- local algebra assignment from Chapter 1.

## Primary Source Anchors

- `transcription/tex/253a/foundations.tex`, lines around the first field
  operator discussion, Poincare covariance, microcausality, and the
  interacting-theory postulates.
- `references/253a lectures 2022.pdf`, pp. 5--9: spacetime point labels for
  field operators, Poincare transformation of local fields, microcausality,
  and the interacting-theory postulates.
- `references/sound_references/fewster_rejzner_aqft_intro_1904.04051.pdf`,
  Section 4.1 for local-algebra requirements and field-coordinate comparison.
- `references/sound_references/buchholz_dybalski_scattering_2023.pdf`,
  opening discussion for Wightman fields as operator-valued distributions and
  their relation to bounded local algebras.

## External Reference Needs

- Wightman axioms for operator-valued distributions: still needs a classical
  reference candidate in the source-control layer.
- AQFT local algebra comparison: Fewster--Rejzner currently used.
- Scattering-oriented Wightman/AQFT comparison: Buchholz--Dybalski currently
  used.

## Notation Inventory

| Symbol | Type | Framework |
| --- | --- | --- |
| \(C_c^\infty(\mathbb M^D)\) | test-function space | distributions |
| \(\mathcal D\) | dense invariant domain in \(\Hilb\) | unbounded operators |
| \(\widehat\Phi_A\) | operator-valued distribution | field coordinate |
| \(x\in\mathbb M^D\) | spacetime label, not a Hilbert-space operator | localization |
| \(f\) | test function | smearing |
| \(f_g\) | pullback-transformed test function \(f_g(y)=f(g^{-1}y)\) | covariance |
| \(\widehat\Phi_A(f)\) | operator on \(\mathcal D\) or affiliated local operator | smeared field |
| \(S(\Lambda)\) | finite-dimensional representation on field indices | covariance |
| \(\operatorname{supp} f\) | closed support of \(f\) | localization |
| \(|A|\) | fermion parity of a homogeneous field component | graded locality |

## Definition Ledger

- operator-valued distribution;
- spacetime label versus Hilbert-space operator;
- smeared field;
- local support of a smeared field;
- common invariant field domain;
- distributional matrix elements of finite products;
- Poincare pullback on test functions and its composition order;
- Poincare-covariant field;
- infinitesimal translation covariance for scalar fields;
- Poincare invariance of spacelike support separation;
- microcausality for smeared fields;
- graded locality for fermionic fields;
- local polynomial field algebra on a common domain;
- Wightman distribution of a field multiplet.

## Claim Ledger

- Point-field notation is shorthand for distributional smearing.
  Status: definition/framework statement. Certification: Wightman-style
  definition.
- The spacetime argument \(x\) in \(\widehat\Phi_A(x)\) is a localization
  label and becomes an operator only after smearing.
  Status: source-certified convention. Certification: handwritten p. 5.
- Covariance acts simultaneously on spacetime arguments and field indices.
  Status: definition. Certification: chapter definition.
- Distributional product matrix elements extend from smeared products to
  distributions on \((\mathbb M^D)^n\).
  Status: proven in chapter. Certification:
  `prop:distributional-matrix-elements`.
- The pullback convention satisfies \((f_g)_h=f_{hg}\).
  Status: definition plus finite check. Certification:
  `def:poincare-pullback-test-functions` and
  `calculation-checks/local_field_covariance_checks.py`.
- Scalar infinitesimal translations obey
  \([P_\mu,\Phi(f)]=-i\Phi(\partial_\mu f)\).
  Status: infinitesimal form of the covariance definition, derived in chapter
  prose by differentiating the finite transformation law.
- Covariant field transformations send fields localized in \(\mathcal O\)
  to fields localized in \(g\mathcal O\).
  Status: direct support check in chapter prose. Certification:
  covariance-of-localization paragraph after the infinitesimal-translation
  proposition.
- Poincare covariance of fields and vacuum invariance imply covariance of all
  Wightman distributions.
  Status: derived in chapter prose. Certification:
  paragraph "Covariance of Wightman distributions."
- Spacelike support separation is Poincare invariant.
  Status: direct support check in chapter prose. Certification:
  paragraph "Poincare invariance of spacelike support separation."
- Microcausality is a support condition on smeared commutators.
  Status: definition. Certification: chapter definition.
- Adjacent spacelike-separated insertions in a Wightman distribution can be
  exchanged with the Koszul sign.
  Status: direct consequence of the microcausality definition and common-domain
  hypothesis, now recorded as a paragraph calculation rather than a separate
  proposition.
- Local polynomial field algebras obey isotony and graded locality on the
  common domain.
  Status: direct support and microcausality consequence in chapter prose.
  Certification: paragraph "Isotony and graded locality for polynomial field
  algebras."
- Wightman distributions inherit field covariance and locality by smearing.
  Status: consequence recorded in chapter prose. Certification:
  paragraph "Field axioms inherited by Wightman distributions."
- Local fields can coordinate local observable data but need not be the only
  primitive.
  Status: framework comparison. Certification: AQFT comparison.

## Drafted Chapter Sections

- Field multiplets as operator-valued distributions.
- Poincare covariance of fields.
- Spacelike separation of supports.
- Microcausality.
- Field coordinates and local algebras.
- Wightman functions.
- Position in the construction.

## Drafting Constraints

- Do not use pointwise commutators as the primary definition without also
  stating their distributional meaning.
- Do not treat Wightman or AQFT as the universal foundation.
- Do not use local field notation before defining test functions and smearing.
- Define every representation, domain, support condition, and index set.
- 2026-05-24 issue #424 pass: restated field-covariance translations using
  \(U(a)=\exp(i a_\mu P^\mu)=\exp(i a^\mu P_\mu)\), matching Chapters 1--2.
- 2026-05-27 issue #615 pass: promoted the domain and covariance material
  into explicit definitions/propositions and added companion checks for the
  pullback order, Lorentz sign, component tensor factors, and graded exchange.
- 2026-05-27 issue #615 follow-up: formalized the field-multiplet datum,
  localization, distributional matrix-element proof, Poincare pullback,
  infinitesimal translation law, localization covariance, spacelike support
  invariance, graded commutator, polynomial field algebra, and Wightman
  distribution inheritance statements.

## Figure Ledger

Included figure:

- spacelike separated supports of test functions and associated local regions.

The figure must label spacetime axes, light cones, supports, and the condition
that every point in one support is spacelike separated from every point in the
other.

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
| \(x\in\mathbb M^D\) | spacetime label for point-field notation, not a Hilbert-space operator | localization |
| \(f\) | test function | smearing |
| \(\widehat\Phi_A(f)\) | operator on \(\mathcal D\) or affiliated local operator | smeared field |
| \(S(\Lambda)\) | finite-dimensional representation on field indices | covariance |
| \(\operatorname{supp} f\) | closed support of \(f\) | localization |

## Definition Ledger

- operator-valued distribution;
- spacetime label versus Hilbert-space operator;
- smeared field;
- local support of a smeared field;
- Poincare-covariant field;
- microcausality for smeared fields;
- graded locality for fermionic fields.

## Claim Ledger

| Claim | Status | Certification |
| --- | --- | --- |
| Point-field notation is shorthand for distributional smearing. | Definition/framework statement | Wightman-style definition |
| The spacetime argument \(x\) in \(\widehat\Phi_A(x)\) is a localization label and becomes an operator only after smearing. | Source-certified convention | Added from handwritten p. 5 |
| Covariance acts simultaneously on spacetime arguments and field indices. | Definition | Chapter definition |
| Microcausality is a support condition on smeared commutators. | Definition | Chapter definition |
| Local fields can coordinate local observable data but need not be the only primitive. | Framework comparison | AQFT comparison, stated carefully |

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

## Figure Ledger

Included figure:

- spacelike separated supports of test functions and associated local regions.

The figure must label spacetime axes, light cones, supports, and the condition
that every point in one support is spacelike separated from every point in the
other.

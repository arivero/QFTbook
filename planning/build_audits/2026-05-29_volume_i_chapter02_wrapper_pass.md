# 2026-05-29 Volume I Chapter 2 Wrapper Pass

## Scope

This pass continues the issue #691 audit in the opening structural chapter.
The guiding distinction was whether a theorem-family statement carried genuine
QFT or operator-theoretic content, or merely displayed algebra following from
a convention.

## Decisions

- `prop:joint-translation-spectrum` remains a proposition.  It is the chapter's
  precise passage from a strongly continuous translation representation to a
  joint projection-valued measure, and it records the important distinction
  between strong commutativity and formal commutation of unbounded generators.
  Its proof was expanded to spell out uniqueness, coordinate-generator
  domains, and the support meaning of the spectrum condition.
- The bosonic Fock inner-product permutation sum was demoted from a proposition
  to a worked normalization formula.  The equation label was kept because the
  formula is useful later, but the proof wrapper was removed.
- `prop:free-scalar-microcausality-chapter-two` remains a proposition.  It is
  the explicit construction of locality for the first free field.  Its proof
  was strengthened to state the common Fock domain, smeared commutator, and
  support argument for the Pauli--Jordan distribution on the spacelike region.
- The theorem-form audit now rejects reintroducing the Fock inner-product
  calculation as a theorem-family wrapper.

## Verification

This note is paired with a full verification run before commit: strict text
audit, negative-scope prose audit, theorem-form audit, display-label audit,
`git diff --check`, and full monograph build because TeX source changed.

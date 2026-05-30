# Modular Finite Examples Anti-Wrapper Pass

## Scope

- Continued the semantic theorem/proof audit for issue #691.
- Targeted Volume IV, Chapter 4, where finite type-I modular calculations
  were useful but over-ranked as propositions.

## Finding

The finite Hilbert-Schmidt standard-form calculation and the finite Connes
cocycle calculation are exact and valuable.  They fix conventions, signs, and
the order of noncommuting density matrices.  They are not theorem-level QFT
claims: the operator-algebraic substance remains the Tomita--Takesaki and
Connes quoted theorem boundaries, while the finite blocks are normalization
models.

## Change

- Demoted `Finite standard form of a faithful matrix state` from proposition
  to example.
- Demoted `Finite standard-form Connes cocycle` from proposition to example.
- Replaced both `proof` environments by verification paragraphs.
- Preserved the finite formulas:
  \(S(X)=\rho^{-1/2}X^*\rho^{1/2}\),
  \(J(X)=X^*\), \(\Delta(X)=\rho X\rho^{-1}\), and
  \(u_t=\rho_\psi^{it}\rho_\omega^{-it}\).
- Updated the chapter dossier and added theorem-form audit guards against
  reintroducing these titles as theorem/proposition/lemma/corollary wrappers.

## Verification

- `python3 calculation-checks/tomita_standard_form_checks.py`
- `python3 -m py_compile calculation-checks/tomita_standard_form_checks.py`

## Status

This pass reduces #691 presentation debt.  It does not close #691 because
the global semantic audit of theorem-family environments and quoted-theorem
boundaries remains active.

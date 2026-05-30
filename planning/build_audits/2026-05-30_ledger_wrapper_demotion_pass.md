# Ledger Wrapper Demotion Pass

## Scope

- Continued the #691 semantic audit of theorem/proposition/lemma environments.
- Targeted theorem-family statements whose own titles or surrounding prose
  identified them as ledgers rather than theorem-level results.

## Changes

- In Volume V, Chapter 11, the symmetric-product primitive-joining
  Schwarzian/OPE-power block is now derivational prose.  The local inverse
  branch Schwarzian, twist weight, OPE exponent, and warning that the analytic
  coefficient is not fixed by the ledger are preserved.
- In Volume VI, Chapter 9, the `SU(N)` nested root-count ledger is now
  derivational prose.  The inverse-Cartan singlet condition and the
  \(N\)-ality integrality obstruction remain as the representation-theoretic
  input for nested TBA source vectors.
- `tools/audit_theorem_form.py` now rejects those two titles if they are
  reintroduced as theorem, proposition, lemma, or corollary environments.

## Status

This pass removes two theorem-family shells without weakening the mathematics.
It does not claim that the global #691 proof-substance audit is complete.

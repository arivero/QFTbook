# 2026-05-29 Volume I Calculation-Wrapper Pass

## Scope

This pass continues the anti-wrapper audit requested in GitHub issue #691.  It
targets early Volume I statements whose proof environments contained only
finite-dimensional Wick bookkeeping or direct oscillator algebra.  The
mathematics was preserved as worked derivations, but the theorem-family
wrappers were removed so that propositions remain reserved for structural
claims.

## Edits

- Chapter 5 now treats cancellation of vacuum components in normalized
  two-point functions as finite-cutoff graph bookkeeping in prose, not as a
  proposition.
- Chapter 5 now treats the derivative-interaction one-loop self-energy and
  local counterterm choice as an explicit worked cutoff calculation, not as a
  proposition.  The nearby finite-gap paragraph no longer cross-references a
  proposition wrapper.
- Chapter 6 now treats the equal-time oscillator algebra, Bogoliubov
  reparametrization, and free-Hamiltonian diagonalization as worked canonical
  derivations.  The later covariance and microcausality result remains a
  proposition because it identifies the constructed Fock field as a covariant,
  local operator-valued distribution.
- The theorem-form audit script now rejects the demoted titles if they
  reappear as theorem-family environments.

## Verification

Verification commands are recorded in the final commit message and terminal
history for this pass.  The expected gates are the theorem-form audit, the
display-label audit, the negative-scope prose audit, the monograph text audit,
`git diff --check`, and a full LaTeX build because TeX source was edited.

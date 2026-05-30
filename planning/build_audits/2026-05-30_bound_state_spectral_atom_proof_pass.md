# 2026-05-30 Bound-State Spectral Atom Proof Pass

## Scope

Anti-wrapper audit pass on Volume II, Chapter 3,
`chapter03_bound_states_from_exchange_amplitudes.tex`.

The compact proof of Theorem
`thm:bound-state-spectral-atom-first-sheet-pole` was a genuine theorem, not
a demotion candidate, but it compressed the load-bearing argument into a few
sentences.  This pass keeps the theorem and expands the proof to the level
needed for the monograph.

## Changes

- Made explicit that the finite-rank residue is canonically defined on the
  isolated positive-energy mass shell.
- Added the needed regularity hypothesis that the finite-rank product of
  matrix elements admits a holomorphic local off-shell extension when the
  pole is written as a meromorphic first-sheet function.
- Inserted the joint translation spectral measure
  \(\bra{\vac}A(0)E(\dd q)B(0)\ket{\vac}\) and separated the isolated
  projection \(\Pi_B\) from the remaining support.
- Derived the mostly-plus scalar Feynman denominator from the \(P^0\)-contour
  identity, including the pole locations.
- Explained why different holomorphic off-shell extensions of the on-shell
  residue differ by \((P^2+M_B^2)\) times a holomorphic function and hence
  change only the analytic remainder.
- Replaced the old one-sentence continuum argument with the spectral-gap
  argument: after removing the isolated shell, the remaining support is
  separated from the chosen first-sheet point, so local finiteness permits
  differentiation under the spectral integral and gives a holomorphic
  remainder.

## Status

This pass does not close the global anti-wrapper issue.  It records one
theorem that survived the audit and now has a substantive proof rather than a
compressed assertion.

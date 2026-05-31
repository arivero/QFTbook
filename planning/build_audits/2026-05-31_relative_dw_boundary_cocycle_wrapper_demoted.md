# Relative Dijkgraaf-Witten boundary cocycle wrapper demoted

Date: 2026-05-31

Related issue: GitHub #691, theorem/proof substance and anti-wrapper audit.

## Scope

This pass audited the relative Dijkgraaf-Witten boundary cocycle block in
`volume_viii/chapter11_finite_gauge_theory_state_sum_tqft.tex`.  The
cancellation is an important finite state-sum identity, but after the relative
datum `delta beta=i^* omega` and the boundary weight convention have been
specified, the local proof is the finite cochain ratio calculation for a
boundary Pachner move.

## Change

- Replaced the proposition/proof shell titled "Boundary cocycle cancellation"
  by paragraph-level construction prose.
- Preserved the invariant weight statement, the interior
  `delta omega=1` step, the boundary ratio
  `omega^epsilon (delta beta)^(-epsilon)=1`, and the resulting obstruction
  class `i^*[omega]`.
- Added a theorem-form audit guard against reintroducing the old title as a
  theorem/proposition/lemma/corollary wrapper.
- Updated the Volume VIII Chapter 11 dossier.

## Status

This is another concrete #691 demotion.  The exact finite arithmetic companion
`finite_gauge_subgroup_boundary_checks.py` continues to verify the relative
cochain cancellation in explicit finite examples.

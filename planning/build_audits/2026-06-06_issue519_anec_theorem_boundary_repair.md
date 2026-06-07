# 2026-06-06 Issue #519 ANEC Theorem-Boundary Repair

## Trigger

- Addressed fresh #519 review on the Vol III Ch10 ANEC/conformal-collider
  section.
- The review identified two load-bearing problems: the ANEC statement was
  stronger than the cited FLPW/HKT theorem boundaries, and the modular sketch
  used sharp-region reduced-density-matrix/local-entropy language inconsistent
  with the monograph's AQFT type-III discipline.

## Primary Source Check

- Rechecked Faulkner--Leigh--Parrikar--Wang, arXiv:1605.08072: modular
  relative-entropy route with regulator and continuum/domain caveats.
- Rechecked Hartman--Kundu--Tajdini, arXiv:1610.05308: causality/light-cone
  OPE route with interacting/no-higher-spin, convergence/asymptotic, order of
  limits, and infrared assumptions.
- Rechecked Casini--Teste--Torroba, arXiv:1703.10656: null-plane modular
  Hamiltonian and half-sided modular-inclusion theorem boundary for the exact
  null-cut formula and sign convention.

## Changes

- Replaced the overstrong ANEC theorem with a route-scoped theorem boundary.
- Replaced sharp-region density-matrix and local-entropy notation by local
  von Neumann algebras, Tomita modular generators, and Araki relative entropy.
- Added the Casini--Teste--Torroba null-cut modular-flow theorem boundary.
- Recast the sign calculation in terms of the full modular generator and
  half-sided-inclusion positivity.
- Demoted the finite-factor entropy squeeze to a regulated mnemonic requiring
  explicit regulator independence, collar removal, common-domain, and entropy
  first-variation assumptions.
- Updated `conformal_collider_checks.py` to reject one-sided null-cut and
  unregulated sharp-density-matrix shortcuts.

## Scope

- This is a theorem-boundary repair for the detector-positivity chain in #519.
- It does not claim a new proof of ANEC, a construction of CFT light-ray
  operators, or a full endpoint-matched EEC theorem.

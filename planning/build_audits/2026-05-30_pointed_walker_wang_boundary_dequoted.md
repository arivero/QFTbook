# Pointed Walker-Wang Boundary Mechanism Pass

Date: 2026-05-30

Issue context:

- Advances #698, the TQFT/generalized-symmetry quoted-theorem proof-debt
  cluster.

Scope:

- `monograph/tex/volumes/volume_viii/chapter09_boundaries_defects_and_categories.tex`
- `planning/chapter_dossiers/volume_viii/chapter09_boundaries_defects_and_categories.md`
- `calculation-checks/walker_wang_boundary_checks.py`
- `calculation-checks/README.md`

Substantive changes:

- Replaced the Crane--Yetter / Walker--Wang `quotedtheorem` with a local
  finite construction for the pointed finite abelian mechanism.
- Defined the finite pointed input `(A,q)`, its polarized braiding form `b`,
  and the radical `Rad(A,b)`.
- Verified that pointed Walker--Wang bulk deconfined line labels are precisely
  `Rad(A,b)`, and that nondegenerate pointed input leaves no nontrivial
  deconfined bulk line while retaining the braided pointed category on the
  boundary.  The verification is a finite plaquette-crossing criterion, not a
  theorem about a continuum QFT.
- Added the toric-code example as an explicit modular boundary order with
  trivial bulk radical.
- Preserved the honest status boundary for the fully general
  Crane--Yetter/Walker--Wang categorical theorem package.

Verification plan:

- Run the new pointed Walker--Wang calculation check.
- Run the standard TeX/prose/theorem/dossier audits and rebuild the monograph.

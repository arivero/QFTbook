# BRST Hermitian Ghost Convention Pass

## Scope

- Tightened `monograph/tex/volumes/volume_ii/chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex`.
- Updated `planning/chapter_dossiers/volume_ii/chapter18_gauge_fixing_ghosts_brst.md`.
- Updated `planning/04_master_architecture.md`,
  `planning/13_development_dependency_map.md`, and
  `planning/source_inventory/stringbook_crosswalk.md` to record BV as a core
  later gauge-theory framework.

## Manuscript Changes

- Made explicit that the gauge field, infinitesimal parameter, and ghost use
  the Hermitian coordinate space
  \(\mathfrak g=i\,\mathfrak g_{\mathrm{ah}}\), with
  \([X,Y]_{\mathrm H}=-i[X,Y]\).
- Added the matrix and component forms of \(D_\mu(A)\zeta\) in the gauge-orbit
  discussion.
- Aligned the Faddeev--Popov Grassmann determinant with the later
  gauge-fixing fermion convention by using the Minkowski exponent
  \(-i\int\bar c\,\mathcal M c\), with the field-independent phase caveat
  stated explicitly.
- Defined the ghost as an odd field valued in the same Hermitian coordinate
  space as the infinitesimal gauge parameter and spelled out
  \([c,c]_{\mathrm H}^a=f^a{}_{bc}c^b c^c\).
- Replaced the terse nilpotency assertion by explicit checks of \(s^2=0\) on
  the ghost, gauge field, and matter field, using the graded derivation rule,
  Jacobi identity, and representation identity.
- Added a bridge from Slavnov--Taylor sources to BV antifields, recording BV as
  the later framework for gauge-theory 1PI and Wilsonian effective actions.
- Updated architecture/dependency planning to make BV a required gauge-theory
  development rather than an optional appendix.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`
- Rendered and inspected affected PDF pages, including page 291 for the
  expanded nilpotency derivation and page 295 for the Slavnov--Taylor/BV
  bridge.

## Remaining Boundary

- The chapter still treats global Gribov issues and full BV/antifield
  cohomology as later developments.  This pass was limited to local
  perturbative BRST conventions, their algebraic consistency, and the planning
  bridge to the later BV framework.

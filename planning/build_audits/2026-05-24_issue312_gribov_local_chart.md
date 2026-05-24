# Issue #312 Gribov Local-Chart Audit

## Issue

GitHub issue #312 noted that the nonabelian gauge-fixed path integral was
hedged as local but did not precisely characterize the Gribov-free coordinate
regime or the relation between first Gribov region, Singer obstruction, and
fundamental modular domain.

## Resolution

- Added Proposition `prop:coulomb-slice-atlas`, a Sobolev-completed local
  Coulomb-slice theorem for irreducible connections.  The proposition states
  the field space, gauge group, stabilizer removal, elliptic
  Faddeev--Popov operator \(d_A^*d_A\), and the Hilbert-manifold inverse
  function theorem argument producing a genuine local gauge-orbit chart.
- Added a paragraph explaining that the elementary Faddeev--Popov formulae are
  coordinate formulae in such charts and are not a global nonperturbative
  gauge-fixed continuum measure.
- Added Proposition `prop:landau-gribov-free-regime`, deriving the Landau
  norm-functional first variation and Hessian and identifying the interior of
  the first Gribov region as the infinitesimal Gribov-free regime.
- Added Figure `fig:gribov-region-fundamental-domain`, showing the Landau
  surface, first Gribov region, Gribov horizon, fundamental modular domain,
  and boundary gauge identifications.
- Added a Maxwell-chapter contrast sentence making clear that the abelian
  field-independent determinant is a special linear-gauge simplification and
  not the template for a global nonabelian gauge fixing.

## Verification

- Working-tree verification before commit:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`

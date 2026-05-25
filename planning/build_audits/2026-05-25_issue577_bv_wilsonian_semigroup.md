# Build Audit: Issue 577 BV Wilsonian Semigroup

Date: 2026-05-25

## Scope

Addressed GitHub issue #577 in
`monograph/tex/volumes/volume_vii/chapter04_supersymmetric_wilsonian_schemes.tex`.

## Mathematical Changes

- Replaced the previous semigroup argument, which assumed the load-bearing
  Fubini and boundary facts, by a finite-cutoff BV formulation.
- Introduced admissible BV Wilsonian steps: split odd symplectic exact
  sequence, Lagrangian integration cycle, convergence or oscillatory
  prescription, BV boundary condition, and supersymmetry compatibility.
- Made the Wilsonian map a pushforward of BV half-densities rather than a
  primitive map of actions; actions arise after choosing a reference
  half-density and logarithm coordinate.
- Added a finite-cutoff Darboux-coordinate proof of BV Stokes, making the
  no-boundary condition an explicit ordinary Stokes boundary term rather
  than an unanalyzed phrase.
- Proved preservation of the quantum master equation by the split BV
  Laplacian and BV Stokes.
- Introduced composable BV Wilsonian towers and proved the semigroup property
  using the product Lagrangian cycle and the declared Fubini theorem.
- Added the gauge-theory warning that scale-dependent gauge fixing or
  supersymmetric regulators are harmless only when represented by admissible
  BV isotopies; otherwise the boundary defect is a Ward-identity anomaly.

## Verification

- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 1259 pages.

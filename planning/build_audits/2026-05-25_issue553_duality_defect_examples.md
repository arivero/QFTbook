# 2026-05-25 Issue 553: Vol IX Duality-Defect Examples

## Scope

Issue #553 flagged that Volume IX promised Kramers-Wannier defects, duality
walls, noninvertible defects from gauging, and line-lattice examples without
delivering them in the volume.

## Edits

- Rephrased the end of Volume IX Chapter 9 so it no longer promises examples
  without a home; it now points to Chapter 10 for the finite normal-subgroup
  gauging and electric-magnetic line-lattice examples while preserving the
  interacting-continuum construction as the open problem.
- Added a proposition in Chapter 10 proving that an anomaly-free finite
  subgroup gauging interface becomes a noninvertible defect at a self-dual
  point, with
  `D_H^dagger D_H = direct sum_{h in H} D_h`.
- Added a finite normal-subgroup gauging example and identified critical
  Ising Kramers-Wannier as the `H = Z_2` case.
- Added the four-dimensional abelian electric-magnetic line lattice example
  with explicit `S` and `T` wall actions.
- Proved that the `S` and `T` transformations preserve the Dirac pairing.
- Updated the Chapter 9 and Chapter 10 dossiers.

## Verification

- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

The first build pass caught an overfull box in the new self-dual-gauging
proposition text; the sentence was reflowed and the subsequent monograph build
and log scan completed cleanly.  The rebuilt PDF has 1297 pages.

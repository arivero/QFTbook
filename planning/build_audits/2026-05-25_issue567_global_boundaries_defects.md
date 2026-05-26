# 2026-05-25 Issue 567: Global Boundaries and Defects

## Scope

Issue #567 flagged Volume IX Chapter 8 as an abstract framework chapter with
no labeled environments, no worked boundary examples, no defect-fusion
examples, and no anomaly-inflow bookkeeping at the defect level.

## Edits

- Rewrote the chapter with labeled definitions for boundary QFT data,
  boundary operator expansion, interfaces/domain walls, renormalized defect
  fusion, and anomaly lines.
- Added a free scalar half-space example distinguishing Neumann and Dirichlet
  leading boundary operators by the method of images.
- Added the Chern-Simons boundary WZW current as a concrete boundary operator
  algebra, with cross-reference to Volume VIII.
- Added critical Ising topological defect fusion and proved that the
  Kramers-Wannier defect is noninvertible with Frobenius-Perron dimension
  `sqrt(2)`.
- Added a three-dimensional `Z_N` BF electric-magnetic duality surface and
  its action on line labels.
- Added a proposition formulating anomaly inflow as canonical
  trivialization of the tensor product of defect anomaly and bulk inflow
  lines.
- Added an open Wilson-line endpoint calculation showing the boundary charge
  condition for gauge invariance.
- Updated the Volume IX Chapter 8 dossier.

## Verification

- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

The monograph build and log scan completed cleanly after the usual
cross-reference rerun.  The rebuilt PDF has 1296 pages.

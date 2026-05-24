# 2026-05-24 Issue #339 Ising Universality Chain Audit

## Issue

GitHub issue #339 asked for an end-to-end theorem tying the logical chain
from lattice Ising data through Wilsonian coordinates and scaling limits to
CFT data, rather than leaving the links in separate paragraphs.

## Edits

- Added `thm:conditional-ising-universality-lattice-to-cft-data` to
  Volume II, Chapter 15.
- The theorem assumes thermodynamic limits, uniform finite-coordinate
  Wilsonian convergence, source-dependent scaling-limit convergence,
  convergence of reflection-positive OS quadratic forms, OS/radial
  reconstruction, the stress-tensor hypotheses for a CFT, and radial OPE
  convergence.
- The conclusion states that normalized long-distance lattice correlators
  converge to universal separated-point scaling functions independent of the
  microscopic representative.  At the critical endpoint these are determined
  by the Ising CFT data; away from criticality they require the constructed
  relevant deformation by \(\sigma\) and/or \(\varepsilon\).
- Updated the statistical Ising chapter dossier.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 747 pages.

# 2026-05-24 Issue #338 Scattering Limit Topology Audit

## Issue

GitHub issue #338 asked for the Haag--Ruelle chapters to separate the topology
of individual scattering-state vector limits from the topology in which the
wave operators exist as maps.

## Edits

- Added a topology paragraph to Volume I, Chapter 12, defining
  \(\Omega_{{\rm out},t}^{\rm HR}\) on a dense algebraic
  velocity-separated Fock domain and displaying the Hilbert-norm convergence
  \(\|\Omega_{{\rm out},t}^{\rm HR}F-\Omega_{\rm out}F\|_{\Hilb}\to0\).
- Stated that the packaged map convergence is strong convergence on each fixed
  Fock vector, that weak matrix-element convergence follows from it, and that
  Haag--Ruelle does not assert operator-norm convergence.
- Added the same distinction to Volume IV, Chapter 5 in the mathematical
  scattering presentation.
- Updated the Volume I Chapter 12 dossier.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean; rebuilt
  `monograph/tex/main.pdf` at 746 pages.

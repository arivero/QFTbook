# 2026-05-30 Issue #700 Mirror TBA Datum Pass

## Target

- GitHub issue: #700.
- Local target:
  `monograph/tex/volumes/volume_vi/chapter07_mirror_channel_tba_finite_size_wrapping.tex`.
- Problem: mirror-channel finite-size TBA used torus decompositions, mirror
  kernels, density equations, analytic strips, and wrapping-contour data before
  aggregating the framework as a named datum.

## Edit

- Added `Hypothesis~\ref{hyp:mirror-finite-size-tba-datum}` at the chapter
  opening.
- The datum now fixes the regulated torus partition functional, direct and
  mirror Hamiltonian decompositions, mirror species and diagonal scattering
  phases, TBA kernels, mirror density/entropy convention, bulk vacuum-energy
  coordinate, and analytic strip/pole ledger for excited-state and operator
  wrapping formulae.
- Rewrote the first section to assume the named datum.
- Removed out-of-scope wording from the planar-wrapping bridge.
- Updated the Volume VI Chapter 7 dossier.

## Verification

- `git diff --check` clean.
- `python3 tools/audit_theorem_form.py` clean.
- `python3 tools/audit_unnumbered_display_labels.py` clean.
- `tools/audit_negative_scope_prose.py` clean.
- `tools/audit_monograph_text.sh` clean.
- `tools/audit_chapter_dossiers.sh` clean.
- `tools/build_monograph.sh` clean.
- `pdfinfo monograph/tex/main.pdf`: 2684 pages.

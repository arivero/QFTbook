# 2026-05-30 Issue #700 Hydrodynamic Datum Pass

## Target

- GitHub issue: #700.
- Local target:
  `monograph/tex/volumes/volume_x/chapter05_hydrodynamics_from_ward_identities.tex`.
- Problem: the chapter had a hydrodynamic scaling-family definition, but the
  first-order hydrodynamic effective-theory data were distributed across source
  Ward identities, local variables, frame choice, constitutive relations, and
  entropy-production sections.

## Edit

- Added `Definition~\ref{def:first-order-hydrodynamic-datum}` before the
  conserved-density and constitutive derivations.
- The datum now aggregates the regulated Schwinger-Keldysh source functional,
  exact stress/current Ward identities, equilibrium thermodynamic manifold,
  local variables, Landau frame, ideal and first-gradient constitutive maps,
  and entropy-current positivity data.
- Rewrote the hydrodynamic-scaling transition to state positively how the datum
  is used as a microscopic QFT approximation.
- Updated the Volume X Chapter 5 dossier.

## Verification

- `git diff --check` clean.
- `python3 tools/audit_theorem_form.py` clean.
- `python3 tools/audit_unnumbered_display_labels.py` clean.
- `tools/audit_negative_scope_prose.py` clean.
- `tools/audit_monograph_text.sh` clean.
- `tools/audit_chapter_dossiers.sh` clean.
- `tools/build_monograph.sh` clean.
- `pdfinfo monograph/tex/main.pdf`: 2685 pages.

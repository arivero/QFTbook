# Volume I Chapter 12 Haag--Ruelle Formalization Follow-Up

Date: 2026-05-27.

Files:

- `monograph/tex/volumes/volume_i/chapter12_haag_ruelle_scattering_theory.tex`
- `planning/chapter_dossiers/volume_i/chapter12_haag_ruelle_scattering_theory.md`

Scope:

- Added labels and theorem-style structure around the massive one-particle
  sector, filtered local creators, point-field isolated-shell projection,
  scalar asymptotic Fock space, Haag--Ruelle wave operators on the separated
  algebraic domain, isometric wave-operator extension, scattering operator,
  and range/completeness distinctions.
- Kept this chapter's status as the point-field and estimate layer.  The full
  algebraic theorem remains the Volume IV Haag--Ruelle theorem; this pass
  clarifies the logical objects used before LSZ rather than duplicating that
  theorem.
- Did not rerun the existing `haag_ruelle_velocity_checks.py`, since this pass
  did not change that calculation-check script.  The full monograph build
  still verifies all TeX labels and cross-references introduced here.

Verification:

- targeted long-line scan on the edited chapter/dossier/audit
- targeted weak-language scan on the edited chapter/dossier/audit
- `git diff --check` on edited files
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`

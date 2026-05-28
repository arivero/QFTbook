# Volume I Chapter 13 LSZ Formalization Follow-Up

Date: 2026-05-27.

Files:

- `monograph/tex/volumes/volume_i/chapter13_lsz_reduction_and_the_s_matrix.tex`
- `planning/chapter_dossiers/volume_i/chapter13_lsz_reduction.md`

Scope:

- Formalized the massive scalar LSZ datum, relativistic external-state
  normalization, wave-packet scattering matrix element, interpolating-field
  pole datum, connected Lorentzian source convention, LSZ external amputation
  map, invariant scalar amplitude convention, connected-kernel partition
  formula, tree-level \(\phi^4\) post-reduction example, and scalar-LSZ scope
  boundary.
- Kept the logic order explicit: Haag--Ruelle defines \(S\) first; LSZ
  relates its already-defined matrix elements to time-ordered Green-function
  pole data; perturbative Feynman graphs enter only after the reduction
  theorem.
- Did not rerun `calculation-checks/lsz_residue_checks.py`, since this pass
  did not edit that already-verified script.  The full monograph build checks
  the new TeX labels and cross-references.

Verification:

- targeted long-line scan on the edited chapter/dossier/audit
- targeted weak-language scan on the edited chapter/dossier/audit
- `git diff --check` on edited files
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`

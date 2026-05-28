# Volume I Chapter 1 Opening Framework Formalization Follow-Up

Date: 2026-05-27.

Files:

- Chapter 1 TeX source.
- Chapter 1 dossier.

Scope:

- Added labels to the continuum-QFT, EFT-presentation, Wightman,
  local-net, Euclidean-correlation, regulated-theory, continuum-correlation,
  and Hilbert/algebraic-completion definitions.
- Promoted the vacuum projection and translation-sign convention to a
  proposition with proof.
- Proved that local finite source-coordinate changes alter source derivatives
  only by distributions supported on collision diagonals.
- Formalized the first derived objects whose hypotheses enter later:
  stable one-particle sectors, S-matrix, LSZ, and path-integral
  presentations.

Verification:

- targeted ASCII scan on the edited chapter/dossier/audit
- targeted weak-language scan on the edited chapter/dossier/audit
- targeted long-line scan on the edited chapter/dossier/audit
- `git diff --check` on edited files
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`

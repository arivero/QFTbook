# Local Counterterm 1PI Coordinate Pass

Date: 2026-05-22

Scope:

- `monograph/tex/volumes/volume_ii/chapter08_renormalizability_and_local_counterterms.tex`
- `planning/chapter_dossiers/volume_ii/chapter10_renormalizability_local_counterterms.md`

Substantive changes:

- Recast perturbative renormalizability as a finite-dimensional family of
  regulator-dependent bare-coordinate maps \(b_\Lambda,b_\varepsilon\).
- Separated full distributional Green-function and 1PI-kernel finiteness from
  the narrower local Taylor-coefficient criterion used for counterterm
  classification.
- Added explicit vacuum-energy and tadpole bookkeeping to the four-dimensional
  scalar counterterm census.
- Replaced the generic \(\phi^6\) panel by a one-loop eight-point diagram that
  correctly represents generation of the \(\phi^8\) counterterm.
- Added the \(\mu^{\varepsilon/2}\) factor for \(D=6-\varepsilon\) cubic
  theory and wrote the higher-order self-energy pole as
  \(A_\varepsilon k^2+B_\varepsilon m_R^2\).

Verification:

- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- Visual inspection of rendered Chapter 30 pages, especially Figures 30.1--30.4.

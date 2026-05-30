# Specialized-Method Exposure Pass: QCD And Pure Yang--Mills

Date: 2026-05-30.

Purpose: enforce the monograph rule that a specialized physics chapter should
not teach general method machinery unless that chapter uses the machinery to
extract a concrete model-specific result.

Files audited and edited:

- `monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`
- `monograph/tex/volumes/volume_ii/chapter17b_lattice_yang_mills_nonperturbative_definition.tex`
- `planning/chapter_dossiers/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_dis.md`

QCD spectroscopy cleanup:

- Removed the remaining local discussion of GEVP basis covariance and the
  finite-rank source-basis algebra from the QCD spectroscopy section.
- Rephrased the hadron spectral extraction setup so the QCD chapter declares
  the invariant physics output: finite-volume color-singlet energies, stable
  masses, scattering amplitudes, and sheet-labeled pole data.
- Rephrased light-meson, baryon-resonance, hybrid, and glueball extraction
  paragraphs so they no longer present a general finite-volume method as QCD
  substance.  They now specify only the QCD source families and the
  finite-volume-to-infinite-volume reconstruction data.

Pure Yang--Mills cleanup:

- Removed the exposed reference to GEVP algebra, basis covariance, and residual
  criteria from the pure-glue lattice definition chapter.
- Kept the pure-Yang--Mills content: Wilson-loop source spaces, cubic-group
  channel assignments, reflection positivity, transfer-matrix spectral
  representation, and continuum/infinite-volume limit.

Audit result:

- A repository-wide search for `GEVP method`, `generalized eigenvalue problem`,
  `basis covariance`, and related phrases now leaves such machinery only in
  `volume_xi/chapter05_wilson_lattice_gauge_theory.tex`, the finite-volume
  methodology chapter where it is substantively developed.
- Specialized chapters may cite finite-volume energies or source-family
  correlators as QCD/Yang--Mills data, but should not reproduce the numerical
  spectral-analysis method unless a concrete physics quantity is actually
  extracted in that chapter.

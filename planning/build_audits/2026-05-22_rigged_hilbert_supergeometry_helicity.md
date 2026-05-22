# Rigged-Hilbert, Supergeometry, and Massless-Helicity Audit

Date: 2026-05-22

## Scope

- Added a mathematical excursion on rigged Hilbert spaces and continuous
  spectra to
  `monograph/tex/volumes/volume_i/chapter02_quantum_mechanics_relativity_and_locality.tex`.
- Propagated the generalized-state convention to the Haag--Ruelle, LSZ,
  cross-section, massive-spin, and massless-helicity chapters.
- Added a rigorous supergeometric account of odd path-integral variables to
  `monograph/tex/volumes/volume_i/chapter16_spinor_fields_fermionic_statistics_and_grassmann_path_integrals.tex`.
- Tightened the massless little-group and photon-intertwiner derivation in
  `monograph/tex/volumes/volume_i/chapter17_massless_particles_helicity_and_gauge_redundancy.tex`.

## Content Added Or Tightened

- Defined a rigged Hilbert space \(\Phi\subset\Hilb\subset\Phi^\times\),
  including the Schwartz/tempered-distribution model, spectral-measure
  distinction between Hilbert eigenvalues and generalized eigenvectors,
  direct-integral notation, mass-shell test spaces, and the weak meaning of
  delta-normalized plane-wave identities.
- Clarified that sharp-momentum one-particle states and plane-wave
  scattering kernels are distributional vectors or kernels, while wave
  packets give the primary Hilbert-space statements.
- Distinguished fermionic operator fields from Grassmann path-integral
  variables: the former are conventional operators on a graded Hilbert space,
  while the latter are odd coordinates on finite-dimensional configuration
  superspaces.
- Defined the purely odd affine superspace
  \(\Pi V=(\{\ast\},\Lambda(V^\vee))\), its functor of points, the local
  model \((B,\mathcal O_B\otimes\Lambda(E^\vee))\), and the algebraic
  Berezin integral on Berezinian densities.
- Stated explicitly that Berezin integration is not a positive or countably
  additive Borel measure and that continuum fermionic path integrals are
  shorthand for regulated finite-dimensional Berezin integrals.
- Wrote the massless little-group matrices \(R_3(\theta)\),
  \(T(\alpha,\beta)\), and their generators \(A,B\), including the
  \(ISO(2)\) commutators.
- Made the continuous-spin alternative explicit as nonzero joint spectrum of
  the null-translation generators, with helicity sectors characterized by
  the trivial action of those translations.
- Re-derived the photon vector intertwiner and its null-translation shift by
  a multiple of the reference momentum, then separated physical
  field-strength operators from gauge-fixed vector-potential variables.

## Source and Rendering Checks

- Handwritten-source comparison for the massless-helicity block used
  `monograph/tex/build/source_visual_trace/253a_trace-189.png` through
  `253a_trace-196.png`, together with
  `transcription/tex/253a/foundations.tex`, roughly lines 8011--8365.
- Rendered manuscript pages checked visually:
  - rigged-Hilbert section:
    `monograph/tex/build/visual_audit_rigged_hilbert_20260522/rigged-041.png`
    through `rigged-043.png`;
  - massless-helicity matrices and photon intertwiners:
    `monograph/tex/build/visual_audit_ch17_helicity_20260522b/ch17-151.png`
    through `ch17-156.png`, followed after the final phase-convention patch
    by `monograph/tex/build/visual_audit_ch17_helicity_20260522c/ch17-154.png`
    through `ch17-156.png`;
  - odd configuration superspaces:
    `monograph/tex/build/visual_audit_ch16_supergeometry_20260522b/ch16-296.png`.
- The displayed matrices, direct-integral formulas, mass-shell kernel,
  superspace definitions, and photon-intertwiner formulas fit in the text
  block without overrun in the rendered PDF.

## Verification

- `tools/build_monograph.sh`

The build completed cleanly and produced
`monograph/tex/main.pdf`. The strict monograph text audit run by the build
script was clean.

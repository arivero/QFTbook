# Core Depth Pass 7

Date: 2026-05-21

Scope: a focused core pass strengthening mathematical steps in scattering,
Wilsonian RG, anomaly structure, conformal representation theory, and
Wightman reconstruction.  Deferred topics remained outside the active
manuscript.

## Content Added

- Added a Haag--Ruelle velocity-support separation estimate.  The new section
  makes the spacelike tube separation and stationary-phase decay explicit,
  preparing the commutator estimate used in the scattering-state limit.
- Added redundant directions and field-coordinate changes to the Wilsonian
  chapter.  The new section identifies equation-of-motion plus Jacobian
  directions as coordinate changes on theory space and explains the quotient
  used in classifying physical RG directions.
- Added topological charge sectors and theta periodicity to the anomaly
  chapter, including the fixed-charge decomposition and its relation to the
  anomaly-invariant parameter `\bar\theta`.
- Added conformal blocks as primary-multiplet contributions in the OPE
  chapter, including the quadratic Casimir eigenvalue and the separation
  between kinematic blocks and dynamical OPE data.
- Added Wightman clustering and the vacuum sector, expressing factorization
  at large spacelike separation through the translation spectral resolution
  and the uniqueness of the zero-momentum vacuum projection.

## Verification

- `tools/build_monograph.sh`
  - Passed.
  - Built `monograph/tex/main.pdf`.
  - Log scan reported clean.
- `pdfinfo monograph/tex/main.pdf`
  - 322 pages.
- `git diff --check`
  - Passed after this audit note was added.
- `tools/audit_monograph_text.sh`
  - Passed after this audit note was added.
- Deferred-topic scan over active volume TeX files
  - Passed after this audit note was added.

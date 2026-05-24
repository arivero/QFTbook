# Build Audit: Issue #301 Lorentzian Oscillatory Path Integral

Date: 2026-05-24

Scope:

- `monograph/tex/volumes/volume_i/chapter06_relativistic_scalar_fields_and_canonical_quantization.tex`
- `monograph/tex/volumes/volume_i/chapter04_hamiltonian_evolution_and_time_sliced_path_integrals.tex`
- `monograph/tex/volumes/volume_i/chapter08_scalar_path_integrals_and_euclidean_green_functions.tex`
- `planning/chapter_dossiers/volume_i/chapter04_lagrangian_and_path_integral_data.md`
- `planning/chapter_dossiers/volume_i/chapter06_relativistic_scalar_fields_canonical.md`
- `planning/chapter_dossiers/volume_i/chapter08_scalar_path_integrals_green_functions.md`
- `tools/audit_monograph_text.sh`

Issue addressed:

- GitHub #301 asked that the Lorentzian symbol
  \(\int[D\phi]\exp(iS[\phi])\) be classified as an oscillatory
  pseudo-integral rather than left as generic regulated shorthand.

Mathematical changes:

- Chapter 6 now states that a finite-regulator Lorentzian Lagrangian
  expression is an oscillatory integral or oscillatory distribution; quadratic
  actions are Fresnel integrals with determinant magnitude and signature
  phase.
- Chapter 8 now includes Definition
  `def:lorentzian-oscillatory-path-integral`, which defines the finite
  regulator object by Abel boundary values or Fourier oscillatory-integral
  definitions, gives the nondegenerate Gaussian Fresnel formula including
  the signature phase, records the Maslov-index role in families, and
  identifies perturbation theory with finite-regulator stationary phase around
  chosen critical configurations.
- The continuum Lorentzian notation is explicitly classified as an
  oscillatory pseudo-integral: compatible finite-regulator oscillatory
  distributions, their boundary values, or their asymptotic expansions.
- The Glimm--Jaffe functional-integral reference is scoped to the
  positive-measure scalar sector, preserving the broader path-integral
  framework needed for fermions, gauge theories, theta terms, BV, lattice and
  holonomy constructions, and formal perturbation theory.
- Chapter 4's Feynman--Kac discussion now states the positive-measure
  construction affirmatively as one entry in a broader typed path-integral
  taxonomy.
- The strict text harness now rejects reader-facing claims that identify the
  path integral with a Borel-measure recipe.

Verification:

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean full XeLaTeX build and log scan;
  generated `/Users/xiyin/QFT/monograph/tex/main.pdf`.

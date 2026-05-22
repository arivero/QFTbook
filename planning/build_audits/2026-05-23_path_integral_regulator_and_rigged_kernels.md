# 2026-05-23 Path-Integral Regulator And Rigged-Kernel Pass

## Scope

- `monograph/tex/volumes/volume_i/chapter01_what_is_qft.tex`
- `monograph/tex/volumes/volume_i/chapter04_lagrangian_formalism_and_quantum_mechanical_path_integrals.tex`
- `monograph/tex/volumes/volume_i/chapter06_relativistic_scalar_fields_and_canonical_quantization.tex`
- `planning/chapter_dossiers/volume_i/chapter04_lagrangian_and_path_integral_data.md`
- `planning/chapter_dossiers/volume_i/chapter06_relativistic_scalar_fields_canonical.md`

## Manuscript Changes

- Replaced an imprecise kernel phrase in the opening Wightman-presentation
  definition by "distribution kernels," so the point-field notation is tied to
  the previously declared distributional smearing convention.
- Strengthened the quantum-mechanical path-integral chapter by declaring the
  common Schwartz test domain for \(\widehat q^a\) and \(\widehat p_a\), the
  Gelfand triple
  \[
    \mathcal S(\mathbb R^d)
    \subset
    L^2(\mathbb R^d,\dd^dq)
    \subset
    \mathcal S'(\mathbb R^d),
  \]
  and the \(\hbar\)-dependent Fourier normalization used by \(\ket q\) and
  \(\ket p\).
- Recast the continuum expression
  \[
    \int [Dq]\exp(\ii S[q]/\hbar)
  \]
  as a compact notation for the finite time-sliced construction with specified
  regulator, limit, operator symbol, and boundary conditions.
- Rewrote the scalar canonical chapter's comparison with the Lagrangian field
  path integral using explicit regulator data
  \((R,\mathcal C_R,\dd\mu_R,S_R)\), so the field path-integral symbol denotes
  a limit or asymptotic expansion of regulated objects.

## Verification

- Ran `tools/build_monograph.sh`; the strict text audit, LaTeX build, and log
  scan were clean.
- Rendered the touched regions:
  - physical PDF page 23, printed page 5, Wightman-presentation definition;
  - physical PDF pages 59--60, printed pages 41--42, canonical
    quantum-mechanical data and path-integral notation;
  - physical PDF page 85, printed page 67, scalar canonical/path-integral
    separation.
- Visual inspection found no overlapping text, equation crowding, or malformed
  displayed formulas in the touched regions.

## Remaining Development Direction

The same convention should continue to be propagated into every later use of
sharp momentum kernels, field-space path integrals, and source-dependent
generating functionals.  The current pass covers the first dependency layer.

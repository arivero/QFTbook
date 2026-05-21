# Volume III protected data, localization, and defects checkpoint

Date: 2026-05-21

## Scope

Extended Volume III after the Witten-diagram and Mellin-amplitude chapter with
four new reader-facing chapters:

- `chapter24_protected_sectors_and_superconformal_indices.tex`
- `chapter25_supersymmetric_localization_and_exact_observables.tex`
- `chapter26_integrated_correlators_and_bootstrap_on_conformal_manifolds.tex`
- `chapter27_defects_boundaries_and_extended_symmetry_data.tex`

These chapters continue the CFT volume through protected supersymmetric data,
exact observables, integrated correlator constraints, and extended conformal
data carried by defects and higher-form symmetry operators.

## Content Checks

- Defined \(Q\)-cohomology on the radial-quantization Hilbert space, the
  positive operator \(\mathcal B=\{Q,Q^\dagger\}\), and the identification of
  protected states with harmonic representatives under stated domain
  assumptions.
- Introduced short multiplets, recombination, and the superconformal index as a
  graded trace whose non-BPS contributions cancel in \(Q\)-pairs.
- Described protected OPE algebras and the protected two-dimensional chiral
  algebra construction as cohomological subsectors of the parent theory.
- Stated the localization principle from \(Q^2\) as a bosonic symmetry,
  \(Q\)-exact deformations, the BPS locus, one-loop determinants, and
  observable insertions.
- Added exact-observable examples: sphere partition functions, coupling
  derivatives, and supersymmetric Wilson-loop matrix-model integrals.
- Developed integrated correlators as linear functionals of ordinary CFT
  correlators and related them to derivatives of exact observables on conformal
  manifolds.
- Connected differentiated crossing equations, duality covariance, and large
  \(N\) Mellin data to global bootstrap constraints.
- Added conformal defects, bulk-to-defect OPE data, defect crossing, boundary
  CFT, displacement operators, topological symmetry defects, higher-form
  symmetry operators, and line-operator duality.

## Figure Audit

Added and inspected the following figures in the rendered PDF:

- Figure 24.1: \(Q\)-cohomology and harmonic protected representatives.
- Figure 24.2: cancellation of paired non-BPS states in the index.
- Figure 24.3: protected chiral algebra as a cohomological image.
- Figure 25.1: localization flow to the BPS locus.
- Figure 25.2: sphere partition-function data and coupling derivatives.
- Figure 25.3: Wilson-loop matrix-model observable.
- Figure 26.1: integrated correlator as a linear functional.
- Figure 26.2: differentiated crossing constraint.
- Figure 26.3: global bootstrap on a conformal manifold.
- Figure 27.1: bulk-to-defect operator product expansion.
- Figure 27.2: defect crossing in a two-point function.
- Figure 27.3: linking of a higher-form symmetry operator with a charged
  extended operator.

Rendered pages 336-352 of `monograph/tex/main.pdf` to
`/tmp/qft_cft_protected_localization_visual_audit`.  After visual inspection,
patched Figure 24.1 label spacing, Figure 26.3 arrow routing, and Figure 27.3
to depict the linking relation more explicitly.  Re-rendered the affected
pages, including a final check of page 338.

## Verification

Passed:

- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`
- `git diff --check`

The final build log scan reported:

`Monograph build and log scan clean: /Users/xiyin/QFT/monograph/tex/main.pdf`

`pdfinfo monograph/tex/main.pdf` reports 352 pages.

## Next Target

The next natural continuation is to develop the bridge from conformal defects
and protected observables toward the later volumes on generalized symmetries,
anomalies, topological sectors, and holographic effective field theory.

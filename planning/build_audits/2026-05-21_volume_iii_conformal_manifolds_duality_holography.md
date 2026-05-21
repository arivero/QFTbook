# Volume III conformal manifolds, duality, and holography checkpoint

Date: 2026-05-21

## Scope

Extended Volume III after the planar spin-chain chapter with four new
reader-facing chapters:

- `chapter20_conformal_manifolds_and_exactly_marginal_deformations.tex`
- `chapter21_duality_and_global_structure_of_conformal_data.tex`
- `chapter22_large_n_conformal_data_and_holographic_fields.tex`
- `chapter23_witten_diagrams_and_mellin_amplitudes.tex`

These chapters continue the CFT volume beyond the available source spine while
preserving the established logical order:

1. conformal data and deformations of conformal data,
2. global identifications of conformal data by duality,
3. large-\(N\) conformal data and the emergence of AdS fields,
4. Witten diagrams and Mellin amplitudes as correlator technology.

## Content Checks

- Defined conformal manifolds as smooth families of complete conformal data,
  with tangent vectors represented by integrated dimension-\(D\) scalar
  primaries modulo redundant directions.
- Explained beta-function obstructions from marginal-operator OPE data,
  including the second-order logarithmic obstruction.
- Defined duality as an isomorphism of complete QFT data, including Hilbert
  spaces, local operator algebras, extended operators, and background fields.
- Treated the global conformal manifold as a quotient by a duality group, with
  the \(\mathcal N=4\) \(\tau_{\rm YM}\) upper-half-plane coordinate used as
  the concrete running example.
- Introduced holographic large \(N\) CFTs through \(C_T\), factorization,
  sparse low-dimension single-trace spectra, and local AdS effective
  interactions.
- Added the scalar AdS mass-dimension relation, boundary-to-bulk propagator,
  generating functional, current/gauge-field dictionary, and stress-tensor
  metric dictionary.
- Introduced tree-level Witten diagrams for scalar correlators and Mellin
  amplitudes with their constraints, contact polynomial behavior, and exchange
  pole families.

## Figure Audit

Added and inspected the following figures in the rendered PDF:

- Figure 20.1: conformal-manifold tangent vector and beta-function vector
  field.
- Figure 20.2: obstruction flow from marginal operators to beta functions and
  conformal locus.
- Figure 21.1: quotient of a coordinate cover by duality.
- Figure 21.2: operator bundle monodromy around a special locus.
- Figure 22.1: boundary source and bulk field in Euclidean AdS.
- Figure 22.2: holographic field dictionary for scalars, currents, and the
  stress tensor.
- Figure 23.1: three-point contact Witten diagram.
- Figure 23.2: four-point exchange Witten diagram.
- Figure 23.3: Mellin contact polynomial and exchange pole schematic.

Rendered pages 318-335 of `monograph/tex/main.pdf` to
`/tmp/qft_cft_frontier_visual_audit`.  After visual inspection, patched the
Figure 20.1 explanatory label, the Figure 22.1 duality wording, the Figure 23.1
label/arrow spacing, and the Figure 21.1 real/imaginary axis labels.

## Verification

Passed:

- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`
- `git diff --check`

The final build log scan reported:

`Monograph build and log scan clean: /Users/xiyin/QFT/monograph/tex/main.pdf`

`pdfinfo monograph/tex/main.pdf` reports 335 pages.

## Next Target

The next natural continuation is to expand the post-holographic part of Volume
III into protected CFT data, supersymmetric localization interfaces, bootstrap
constraints on exactly marginal families, and then prepare the bridge toward
the later volumes on generalized symmetries, defects, anomalies, and
holographic effective field theory.

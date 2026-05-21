# Volume IV framework opening checkpoint

Date: 2026-05-21

## Scope

Opened Volume IV, `Mathematical Frameworks and Nonperturbative Construction`,
with four reader-facing chapters:

- `chapter01_wightman_fields_and_reconstruction.tex`
- `chapter02_osterwalder_schrader_reconstruction.tex`
- `chapter03_algebraic_qft_local_nets_and_states.tex`
- `chapter04_superselection_sectors_and_locality_properties.tex`

The main manuscript now inputs `volumes/volume_iv/volume_iv_current.tex` after
Volume III.  This block begins the framework-comparison volume after the CFT
sequence without treating any existing framework as the single foundation of
the monograph.

## Source Checks

Local source checks used:

- `references/sound_references/schmidt_euclidean_reconstruction_math-ph_9811002.txt`
  for Wightman-to-Schwinger analyticity, Euclidean reconstruction, and growth
  hypotheses.
- `/tmp/fewster_rejzner_aqft_intro_1904.04051.txt`, extracted from the local
  PDF in `references/sound_references`, for local nets, GNS representations,
  spectrum condition, Reeh--Schlieder, split property, and superselection
  terminology.
- `/tmp/fredenhagen_rejzner_paqft_1208.1428.txt`, extracted from the local PDF,
  for the algebraic formulation, local covariance, and perturbative AQFT
  interface.
- `/tmp/buchholz_dybalski_scattering_2023.txt`, extracted from the local PDF,
  for the algebraic scattering interface and Haag--Ruelle context.

## Content Checks

- Defined Wightman data as Hilbert-space, vacuum, Poincare representation,
  common domain, and operator-valued tempered distributions.
- Stated covariance, spectral support, locality after smearing, cyclicity, and
  positivity with explicit symbols.
- Added Wightman functions, the reconstruction theorem, the reconstruction
  quotient construction, and tube analyticity from spectral positivity.
- Defined Euclidean Schwinger data, time reflection, reflection positivity,
  the positive-time quotient, the reconstructed Hamiltonian, and the OS
  theorem with explicit growth/regularity status.
- Introduced local nets, isotony, Einstein causality, covariance, time-slice,
  additivity, quasilocal algebras, states, the GNS representation, vacuum
  representations, represented von Neumann nets, and local covariance.
- Added Reeh--Schlieder as a theorem-level locality/spectrum consequence.
- Developed sector representations, the DHR localization criterion,
  transportable localized endomorphisms, fusion, intertwiners, field algebra
  reconstruction, the split property, modular data, and the algebraic
  Haag--Ruelle scattering interface.

## Figure Audit

Added and inspected the following figures in the rendered PDF:

- Figure 1.1: Wightman framework data.
- Figure 1.2: Wightman reconstruction from a positive correlation hierarchy.
- Figure 1.3: tube analyticity from spectral positivity.
- Figure 2.1: OS reflection positivity.
- Figure 2.2: OS reconstruction flow.
- Figure 2.3: Euclidean measure to OS-positive Schwinger data.
- Figure 3.1: AQFT local net, isotony, and spacelike commutativity.
- Figure 3.2: GNS construction and represented local algebras.
- Figure 3.3: Reeh--Schlieder local cyclicity.
- Figure 4.1: DHR localized sector.
- Figure 4.2: sector fusion and intertwiners.
- Figure 4.3: split property.
- Figure 4.4: modular wedge flow.

Rendered pages 354-371 of `monograph/tex/main.pdf` to
`/tmp/qft_volume_iv_framework_visual_audit`.  After visual inspection, patched
Figure 1.1 arrow routing, Figure 3.1 label placement and commutativity layout,
and Figure 4.2 sector-fusion arrows.  Re-rendered the affected pages at higher
resolution.

## Verification

Passed:

- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`
- `git diff --check`

The final build log scan reported:

`Monograph build and log scan clean: /Users/xiyin/QFT/monograph/tex/main.pdf`

`pdfinfo monograph/tex/main.pdf` reports 371 pages.

## Next Target

The next natural continuation is to extend Volume IV with Haag--Ruelle in the
framework-comparison setting, constructive QFT and lattice continuum limits,
reflection-positive Euclidean measures, perturbative AQFT, and BV/BRST as a
homological construction.

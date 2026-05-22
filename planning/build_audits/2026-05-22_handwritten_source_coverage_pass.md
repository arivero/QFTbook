# 2026-05-22 Handwritten Source Coverage Pass

## Scope

This pass reviewed the local source spine for:

- 253a, `references/253a lectures 2022.pdf`, 244 pages;
- 253b, `references/253b lecture notes 2023.pdf`, 257 pages;
- selected 253c, `references/253c 2023.pdf`, 185 pages.

The operational comparison used `transcription/tex/253a/foundations.tex`,
`transcription/tex/253b/scattering_rg_qcd.tex`, and
`transcription/tex/253c/conformal_field_theory.tex`, with Ben Lou's
transcriptions used only as non-authoritative page-index aids.

## Register Update

The source coverage register was expanded into a 253a/253b/selected-253c
matrix:

- `planning/source_inventory/253a_253b_no_skip_coverage_register.md`

The register distinguishes `mapped` from `certified`: most topics have a clear
compiled monograph home, but only a small number have been checked at
derivation and figure level against the handwritten pages.

## Immediate Gaps Patched

Two source blocks were found to have substantive omissions in compiled TeX:

1. 253b pages 202--210: the Banks--Zaks fixed-point alternative, Wilson-line
   flux-tube operators, Wilson-loop static potential, and confinement
   diagnostic.
2. 253b pages 249--257: explicit \(N_f=2\) pion scattering from the nonlinear
   sigma model, the \(A(s,t,u)=4s/F_{\rm st}^2\) leading amplitude, and the
   one-loop chiral-log plus four-derivative counterterm structure.

These were patched in:

- `monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`;
- `monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex`.

The relevant chapter dossiers were updated to make these blocks explicit
coverage requirements.

## Remaining High-Priority Partial Rows

- 253a pages 43--51: derivative interactions, measure, regulator dependence,
  and counterterms.
- 253b pages 71--80: generating functionals and the 1PI effective action.
- 253b pages 97--110: 1PI renormalization group.
- 253b pages 147--156: Wilsonian effective actions and Polchinski flow.
- 253b pages 182--201: ordinary Lorenz-gauge Yang--Mills Feynman-rule figures
  remain to be audited, although the background-field beta-function
  derivation was certified in the previous pass.

## 253c Boundary

The compiled CFT volume currently covers the selected core material through
OPE/crossing.  Projective lightcone/bootstrap, two-dimensional CFT, modular
material, supersymmetric QFT, and large-\(N\)/spin-chain material remain source
obligations for later special volumes, not omissions from the present core
volumes.

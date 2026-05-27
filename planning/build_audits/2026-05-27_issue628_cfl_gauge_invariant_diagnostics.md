# Issue #628 CFL Gauge-Invariant Diagnostics Pass

Date: 2026-05-27

## Scope

This pass develops the gauge-invariant interpretation of the
color-flavor-locked dense-QCD phase in
`monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`.
It is written to avoid treating a gauge-covariant diquark one-point function
as a physical local order parameter.

## Content Added

- Defined the antisymmetric spin-zero diquark composites
  \(\varphi_L,\varphi_R\in \overline{\square}_{\rm color}\otimes
  \overline{\square}_{L,R}\) with baryon charge \(2/3\).
- Constructed local gauge-invariant composites
  \[
    \mathcal B_L=\det \varphi_L,\qquad
    \mathcal B_R=\det \varphi_R,\qquad
    \Sigma=\varphi_L^\dagger\varphi_R.
  \]
- Recorded their transformation content:
  \(\mathcal B_L,\mathcal B_R\) are color and flavor singlets with baryon
  charge \(2\), while \(\Sigma\) is color invariant, baryon neutral, and
  transforms as \(g_L\Sigma g_R^{-1}\).
- Added a Wilson-line completed diquark two-point function as a
  gauge-invariant but path-dependent diagnostic of the long-distance order
  encoded by a gauge-covariant diquark field.
- Proved by Haar averaging in finite volume that a local operator in a
  nontrivial irreducible color representation has zero expectation value
  in a gauge-invariant regularized theory, so \(\langle\varphi_L\rangle\)
  is not a physical local order parameter.
- Added exact rational checks of the CFL composite baryon charges.

## Verification

- `python3 calculation-checks/qcd_phase_checks.py`
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`
- `git diff --check -- calculation-checks/README.md calculation-checks/qcd_phase_checks.py monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md planning/build_audits/2026-05-27_issue628_cfl_gauge_invariant_diagnostics.md`
- `rg --pcre2 -n '\\over(?!line)' calculation-checks/README.md calculation-checks/qcd_phase_checks.py monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md planning/build_audits/2026-05-27_issue628_cfl_gauge_invariant_diagnostics.md`
  returned no matches.
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reports 2209 pages.

## Remaining Work

This closes only the basic gauge-invariant diagnostic layer.  The dense-QCD
chapter still needs systematic treatment of Meissner screening and collective
modes, neutrality constraints, crystalline phases, anomaly matching across
CFL, and non-Fermi-liquid corrections.

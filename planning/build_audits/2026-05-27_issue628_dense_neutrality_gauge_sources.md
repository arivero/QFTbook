# Issue #628 Dense Neutrality And Gauge Sources Pass

Date: 2026-05-27

## Scope

This pass extends the high-density and CFL part of
`monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`
by separating physical global chemical potentials from gauge-constraint
variables.  The goal is to remove the common but misleading language in
which color neutrality is treated as if it came from an ordinary
grand-canonical color chemical potential.

## Content Added

- Defined the finite-regulator global-charge ensemble with the physical
  gauge-invariant projector
  \[
    \Pi_{\rm phys}=\int_{\mathcal G_\Lambda}d\eta\,U(\eta).
  \]
- Proved that infinitesimal Gauss-law generators annihilate the physical
  projector and therefore have zero expectation value in every such
  finite-regulator state.
- Explained temporal color backgrounds \(A_0^a\), and the symbols often
  denoted \(\mu_3,\mu_8\), as gauge-fixed coordinates whose saddle equations
  impose Gauss-law/color-neutrality stationarity rather than independent
  thermodynamic sources.
- Defined the neutrality problem for gauge-invariant external charges by
  pressure derivatives after all charged species in the physical setup have
  been included.
- Proved ideal CFL electric neutrality at zero electric source using
  diagonal \(SU(3)_V\) invariance and the traceless charge matrix
  \[
    Q_{\rm em}=\operatorname{diag}(2/3,-1/3,-1/3).
  \]
- Identified the unbroken rotated electromagnetic \(U(1)\) in the same
  color-flavor transformation convention used for the CFL orientation field.
- Added exact calculation checks for traceless flavor charge neutrality,
  the rotated \(U(1)\) invariance condition, and Gauss-law projected color
  charge.

## Verification

Recorded before commit:

- `python3 calculation-checks/qcd_phase_checks.py`: passed with
  `All QCD phase-structure checks passed.`
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`: passed.
- `git diff --check -- calculation-checks/README.md
  calculation-checks/qcd_phase_checks.py
  monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex
  planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md
  planning/build_audits/2026-05-27_issue628_dense_neutrality_gauge_sources.md`:
  passed.
- Targeted primitive-fraction scan on the touched TeX, check, dossier, and
  audit files: no matches.
- `tools/build_monograph.sh`: passed; monograph build and log scan clean.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2214`.

## Remaining Work

The dense-QCD chapter still needs the microscopic weak-coupling computation
of CFL low-energy constants, neutrality beyond ideal CFL with quark masses
and beta equilibrium, crystalline phases, anomaly matching across CFL, and
non-Fermi-liquid corrections.

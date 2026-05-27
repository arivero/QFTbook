# Issue #628 Dense Fermi-Surface Stress Pass

Date: 2026-05-27

## Scope

This pass extends the dense-QCD part of
`monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`
by deriving the leading mass and chemical-potential stresses that deform the
ideal CFL Fermi-surface geometry.

## Content Added

- Defined the residual energies \(\xi_a(p)=\sqrt{p^2+m_a^2}-\mu_a\), the
  average residual energy, and the pairwise effective half-mismatch
  \(\delta_{ij}^{\rm eff}\).
- Derived the mass-shifted Fermi momentum
  \[
    p_{F,a}=\mu_a-\frac{m_a^2}{2\mu_a}+O(m_a^4/\mu_a^3).
  \]
- Derived the leading pairwise mismatch
  \[
    \delta_{ij}^{\rm eff}
    =
    -\frac{\mu_i-\mu_j}{2}
    +
    \frac{m_i^2-m_j^2}{4\bar\mu}
    +\cdots .
  \]
- Distinguished the strange-light Fermi-momentum splitting
  \(m_s^2/(2\mu_q)\) from the pairwise half-mismatch \(m_s^2/(4\mu_q)\).
- Added a controlled two-species BCS comparison and derived the Clogston
  scale \(\delta_C=\Delta_0/\sqrt2\) from the explicit grand-potential
  balance
  \[
    \Omega_{\rm pair}-\Omega_{\rm normal}
    =
    -\frac12N(0)\Delta_0^2+N(0)\delta^2+\cdots .
  \]
- Added exact arithmetic checks for the mass-shift coefficient, the
  strange-light stress coefficients, and the squared Clogston ratio.

## Verification

Recorded before commit:

- `python3 calculation-checks/qcd_phase_checks.py`: passed with
  `All QCD phase-structure checks passed.`
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`: passed.
- `git diff --check -- calculation-checks/README.md
  calculation-checks/qcd_phase_checks.py
  monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex
  planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md
  planning/build_audits/2026-05-27_issue628_dense_fermi_surface_stress.md`:
  passed.
- Targeted primitive-fraction scan on the touched TeX, check, dossier, and
  audit files: no matches.
- `tools/build_monograph.sh`: passed; monograph build and log scan clean.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2218`.

## Remaining Work

The dense-QCD chapter still needs a full neutrality-plus-gap variational
analysis beyond ideal CFL, crystalline phases, non-Fermi-liquid corrections,
and microscopic weak-coupling values of CFL low-energy constants.

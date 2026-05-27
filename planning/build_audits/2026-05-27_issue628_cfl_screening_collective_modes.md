# Issue #628 CFL Screening And Collective Modes Pass

Date: 2026-05-27

## Scope

This pass extends the dense-QCD/CFL development in
`monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`
from gauge-invariant CFL order diagnostics to screening and physical
collective modes.

## Content Added

- Defined gauge-invariant static electric and magnetic screening correlators
  using field-strength insertions connected by a fundamental Wilson line.
- Defined the associated large-distance screening exponents \(m_E,m_M\), with
  explicit path-family dependence stated rather than hidden.
- Added the CFL Higgs-screening effective action for a gauge-covariant
  color-flavor orientation coordinate \(U(x)\), with trace-delta convention
  stated inside the definition.
- Derived the screening mass matrices
  \[
    (m_E^2)^{ab}=g^2F_H^2\delta^{ab},\qquad
    (m_M^2)^{ab}=g^2F_H^2v_H^2\delta^{ab}.
  \]
- Defined the ideal CFL collective fields \(\Sigma\in SU(3)\) and
  \(e^{i\phi_B}\in U(1)_B\), and wrote the leading dense-medium effective
  action with independent velocities.
- Derived the chiral-octet and baryon-phonon dispersions
  \[
    \omega^2=v_\pi^2\mathbf k^2,\qquad
    \omega^2=v_B^2\mathbf k^2.
  \]
- Added calculation checks for the eight screened color sectors, the
  \(8+1=9\) physical ideal-CFL gapless modes, and the trace-delta screening
  prefactor bookkeeping.

## Verification

Recorded before commit:

- `python3 calculation-checks/qcd_phase_checks.py`: passed with
  `All QCD phase-structure checks passed.`
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`: passed.
- `git diff --check -- calculation-checks/README.md
  calculation-checks/qcd_phase_checks.py
  monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex
  planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md
  planning/build_audits/2026-05-27_issue628_cfl_screening_collective_modes.md`:
  passed.
- `tools/build_monograph.sh`: passed; monograph build and log scan clean.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2212`.

## Remaining Work

The dense-QCD chapter still needs the microscopic weak-coupling computation
of CFL low-energy constants, neutrality constraints, crystalline phases,
anomaly matching across CFL, and non-Fermi-liquid corrections.

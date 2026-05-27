# 2026-05-27 Issue #628 QCD Phase Static HTL Debye-Mass Pass

## Scope

- Continued the #628 QCD phase-structure depth pass in Volume X,
  Chapter 12.
- Added a static HTL polarization proposition after the HTL regime definition
  and before the Linde-scale discussion.
- Defined the trace convention used in the calculation:
  `tr_R(T_R^a T_R^b)=T_R delta^{ab}` and
  `f^{acd} f^{bcd}=C_A delta^{ab}`.
- Derived the Debye mass from the hard-particle color susceptibility rather
  than quoting it as a standard thermal-field-theory formula.
- Evaluated the Bose and Fermi susceptibility integrals
  `I_B=T^2/6` and `I_F=T^2/12`, including the degeneracy factors `2 C_A`
  for gluons and `4 T_R` for each Dirac fermion.
- Specialized the result to the monograph's `SU(N_c)` trace-delta convention:
  `C_A=2N_c`, `T_fund=1`, hence
  `m_D^2=g^2 T^2(2N_c/3+N_f/3)`.
- Stated the screened static longitudinal propagator as a static HTL
  electric response, not as a gauge-invariant particle pole.
- Extended `calculation-checks/qcd_phase_checks.py` with exact rational
  checks for the Bose/Fermi integral coefficients, degeneracy factors, and
  the `SU(3), N_f=3` coefficient.

## Checks

- `python3 calculation-checks/qcd_phase_checks.py`: passed.
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`: passed.
- `git diff --check -- monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex calculation-checks/qcd_phase_checks.py calculation-checks/README.md planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md planning/build_audits/2026-05-27_issue628_qcd_phase_static_htl_debye.md`: passed.
- `tools/build_monograph.sh`: passed; strict text audit and final log scan
  clean.
- `pdfinfo monograph/tex/main.pdf`: reports 2193 pages.

## Status

This strengthens the HTL part of the QCD phase chapter.  It does not close
#628: remaining work includes full nonstatic HTL tensor/effective-action
derivations, interacting Polyakov-loop effective theories,
lattice-continuum status ledgers, quantitative QGP observables, high-density
EFT, and controlled dense-phase examples.

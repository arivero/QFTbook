# 2026-05-27 Issue #628 QCD Phase Low-Temperature Chiral EFT Pass

## Scope

- Continued the #628 QCD phase-structure depth pass in Volume X,
  Chapter 12.
- Added a low-temperature chiral effective theory subsection immediately
  after the finite-temperature Ward/GMOR material.
- Defined the leading chiral effective datum with
  `U: R^3 x S^1_beta -> SU(N_f)`, constants `F` and `B`, the Euclidean
  leading action, and the trace-delta pion-field parameterization.
- Stated explicitly that `F` is the half-trace-normalized decay constant,
  while the trace-delta decay constant used earlier is `sqrt(2) F`.
- Proved the tree-level source normalization `Sigma=F^2 B` and
  `M_pi^2=2Bm`, including the conversion to the trace-delta GMOR form.
- Derived the one-loop pion-gas correction
  `Sigma(T)/Sigma(0)=1-(N_f^2-1)T^2/(12N_f F^2)+O(T^4/F^4)` from the
  thermal pion pressure and the mass derivative of the Bose integral.
- Stated the formula as a controlled low-temperature asymptotic result inside
  the broken phase, not as a proof of a chiral restoration temperature.
- Extended `calculation-checks/qcd_phase_checks.py` with exact rational
  checks for the tree-level chiral EFT source normalization, trace-delta
  GMOR conversion, low-temperature coefficient for several `N_f`, and the
  pressure-derivative chain rule.

## Checks

- `python3 calculation-checks/qcd_phase_checks.py`: passed.
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`: passed.
- `git diff --check -- monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex calculation-checks/qcd_phase_checks.py calculation-checks/README.md planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md planning/build_audits/2026-05-27_issue628_qcd_phase_low_temperature_chiral_eft.md`: passed.
- `tools/build_monograph.sh`: passed; strict text audit and final log scan
  clean.
- `pdfinfo monograph/tex/main.pdf`: reports 2192 pages.

## Status

This strengthens the finite-temperature chiral sector of the QCD phase
chapter.  It does not close #628: remaining work includes interacting
Polyakov-loop effective theories, lattice-continuum status ledgers,
quantitative QGP observables, high-density EFT, controlled dense-phase
examples, and further finite-temperature chiral effective theory beyond the
leading pion-gas correction.

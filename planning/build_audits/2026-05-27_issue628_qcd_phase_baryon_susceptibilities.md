# 2026-05-27 Issue #628 QCD Phase Baryon-Susceptibility Pass

## Scope

- Continued the #628 QCD phase-structure depth pass in Volume X,
  Chapter 12.
- Added a baryon-susceptibility and critical-point-diagnostic section after
  the finite-density sign-problem discussion.
- Defined the dimensionless baryon source \(x=\mu_B/T\), finite-regulator
  partition function \(Z_{a,V}(x)\), baryon cumulants
  \(\kappa_{n,a,V}^B\), and susceptibilities \(\chi_{n,a,V}^B\).
- Proved the first, second, and fourth cumulant formulas in terms of
  finite-volume baryon-number moments.
- Proved the vanishing of odd cumulants at \(\mu_B=0\) under exact charge
  conjugation.
- Defined the Taylor expansion of \(p(T,\mu_B)/T^4\) and its
  Cauchy--Hadamard radius.
- Stated precisely what the susceptibility radius establishes: analyticity
  inside the convergence disk, and identification of a real critical endpoint
  only with independent input locating the nearest limiting singularity on
  the positive real axis.
- Added the even-ratio estimator with explicit positivity and single-scale
  hypotheses.
- Extended `calculation-checks/qcd_phase_checks.py` with exact rational
  checks for baryon cumulants, charge-conjugation odd-cumulant vanishing,
  susceptibilities, and the radius-estimator formula.

## Checks

- `python3 calculation-checks/qcd_phase_checks.py`: passed.
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`: passed.
- `git diff --check -- monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex calculation-checks/qcd_phase_checks.py calculation-checks/README.md planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md planning/build_audits/2026-05-27_issue628_qcd_phase_baryon_susceptibilities.md`: passed.
- `tools/build_monograph.sh`: passed; strict text audit and final log scan
  clean.
- `pdfinfo monograph/tex/main.pdf`: reports 2188 pages.

## Status

This strengthens the finite-density diagnostic layer of the QCD phase
chapter.  It does not close #628: remaining work includes interacting
Polyakov-loop effective theories, lattice-continuum status ledgers,
quantitative QGP observables, high-density EFT, and controlled dense-phase
examples.

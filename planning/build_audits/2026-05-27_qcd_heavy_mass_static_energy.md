# 2026-05-27 QCD Heavy-Mass Static-Energy Pass

## Scope

- Added a heavy-quark mass-coordinate and static-energy section to Volume II,
  Chapter 19 after the NRQCD/pNRQCD foundation.
- Defined the renormalized static energy from rectangular Wilson loops with a
  stated line-renormalization prescription.
- Separated gauge-invariant static energies and hadron masses from formal
  gauge-fixed perturbative quark mass coordinates.
- Proved the finite mass/potential scheme transformation
  \(m'\!=m+\delta m\), \(V'\!=V-2\delta m\), including the corresponding
  quarkonium eigenvalue shift.
- Defined the potential-subtracted mass coordinate and derived the leading
  subtraction
  \(\delta m_{\rm PS}^{(0)}(\mu_f)=g^2C_F\mu_f/(4\pi^2)\) in the monograph
  trace-delta convention.
- Stated the heavy-quark renormalon issue as a statement about specified
  perturbative expansions and summation prescriptions, not as a
  nonperturbative definition of a colored-particle mass.

## Checks

- `python3 calculation-checks/qcd_heavy_mass_static_energy_checks.py`
- `python3 -m py_compile calculation-checks/qcd_heavy_mass_static_energy_checks.py`
- `git diff --check -- ...` on the changed manuscript, calculation-check,
  README, dossier, and audit files.
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`: 2165 pages, 8775325 bytes, PDF 1.5.

## Status

This pass supplies the mass-scheme and static-energy anchor needed for later
quarkonium precision development.  It does not yet compute loop corrections to
the static potential, threshold mass conversions beyond the leading PS
subtraction, ultrasoft logarithms, spin-dependent potentials, or inclusive
quarkonium production/decay factorization.

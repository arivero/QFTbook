# 2026-05-27 Issue #628 QCD Phase Roberge--Weiss Pass

## Scope

- Continued the #628 QCD phase-structure depth pass in Volume X,
  Chapter 12.
- Added an imaginary-chemical-potential subsection after the real-density
  sign-problem proof and before baryon susceptibilities.
- Defined the quark and baryon imaginary-chemical-potential angles
  `mu_q=iT theta_q`, `mu_B=iT theta_B`, with `theta_B=N_c theta_q`, and the
  equivalent twisted thermal boundary condition
  `q(beta,x)=-exp(i theta_q) q(0,x)`.
- Stated the finite-regulator assumptions explicitly: compact `SU(N_c)`
  links, center-twisted temporal gauge transformations, and a gauge-covariant
  Dirac operator whose imaginary chemical potential is a boundary twist.
- Proved finite-regulator Roberge--Weiss periodicity
  `Z(theta_q+2*pi*k/N_c)=Z(theta_q)` by a center-twisted gauge
  transformation.
- Converted this to baryon-angle periodicity
  `Z(theta_B+2*pi*k)=Z(theta_B)`.
- Proved positivity for vectorlike pairs at real `theta_q` via
  `gamma_5`-Hermiticity at imaginary chemical potential.
- Added a status remark on Roberge--Weiss lines:
  `theta_q=(2r+1)pi/N_c` may become a thermodynamic-limit sector-exchange
  singularity, but finite-volume partition functions remain analytic and this
  does not locate a real-`mu_B` critical endpoint.
- Extended `calculation-checks/qcd_phase_checks.py` with exact rational
  checks for quark-angle shifts, baryon-angle periodicity, canonical integer
  baryon-charge periodicity, and the high-temperature Roberge--Weiss loci.

## Checks

- `python3 calculation-checks/qcd_phase_checks.py`: passed.
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`: passed.
- `git diff --check -- calculation-checks/README.md calculation-checks/qcd_phase_checks.py monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md planning/build_audits/2026-05-27_issue628_qcd_phase_roberge_weiss.md`: passed.
- `tools/build_monograph.sh`: passed; strict text audit and final log scan were clean.
- `pdfinfo monograph/tex/main.pdf`: reports 2195 pages.

## Status

This sharpens the finite-density part of the chapter by separating real
chemical potential, imaginary chemical potential, and Taylor/cumulant
diagnostics.  It does not close #628: remaining work includes nonstatic HTL
tensor/effective-action derivations, interacting Polyakov-loop effective
theories, lattice-continuum status ledgers, high-density EFT, and controlled
dense phase examples.

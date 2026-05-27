# 2026-05-27 Issue #628 QCD Phase Chiral-Ward Pass

## Scope

- Continued the #628 QCD phase-structure depth pass in Volume X,
  Chapter 12.
- Fixed the chiral condensate convention in the Banks--Casher subsection:
  `Sigma_m(T)` is now the positive per-flavor mass-source response, while
  the flavor-summed scalar expectation is `-N_f Sigma_m(T)`.
- Distinguished spatial volume `V_3` from Euclidean thermal four-volume
  `mathcal V_4=beta V_3` in the Dirac spectral-density normalization.
- Rewrote the Banks--Casher definition so the displayed sign agrees with the
  proof and with the positive density formula `Sigma(T)=pi rho(0)`.
- Added a finite-temperature nonsinglet axial Ward-identity subsection with
  trace-delta flavor-generator normalization.
- Defined the Euclidean pseudoscalar density, axial current, and
  pseudoscalar susceptibility with explicit sign conventions.
- Proved the integrated Ward identity
  `2m chi_pi^{ab}=-<bar q {tau^a,tau^b} q>` and the flavor-symmetric
  consequence `m chi_pi^{ab}=delta^{ab} Sigma_m`.
- Derived the finite-temperature GMOR relation only under an explicit
  isolated-pion-pole and pole-saturation hypothesis, with the conversion
  between trace-delta and half-trace flavor-generator conventions.
- Extended `calculation-checks/qcd_phase_checks.py` with exact rational
  checks for the chiral Ward identity and GMOR normalization factors.

## Checks

- `python3 calculation-checks/qcd_phase_checks.py`: passed.
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`: passed.
- `git diff --check -- monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex calculation-checks/qcd_phase_checks.py calculation-checks/README.md planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md planning/build_audits/2026-05-27_issue628_qcd_phase_chiral_ward_identity.md`: passed.
- `tools/build_monograph.sh`: passed; strict text audit and final log scan
  clean.
- `pdfinfo monograph/tex/main.pdf`: reports 2190 pages.

## Status

This strengthens the chiral-restoration layer of the QCD phase chapter and
fixes a sign/convention inconsistency in the earlier Banks--Casher statement.
It does not close #628: remaining work includes interacting Polyakov-loop
effective theories, lattice-continuum status ledgers, quantitative QGP
observables, high-density EFT, controlled dense-phase examples, and more
detailed chiral effective theory at finite temperature.

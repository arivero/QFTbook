# 2026-05-27 Issue #628 QCD Phase Retarded HTL Pass

## Scope

- Continued the #628 QCD phase-structure depth pass in Volume X,
  Chapter 12.
- Added a retarded hard-thermal-loop subsection after the static Debye-mass
  derivation and before the Linde obstruction.
- Defined the induced-current kernel `mathcal K_R^{mu nu,ab}` in the
  monograph mostly-plus convention by
  `j^mu_a=mathcal K_R^{mu nu,ab} A_nu^b`.
- Normalized the retarded kernel so that its static `00` component agrees
  with the previously derived Debye mass.
- Introduced the adjoint auxiliary field `W_a(x,v)` and the gauge-covariant
  kinetic equations `(v.D)W=v^i F_{i0}` and
  `j^mu=m_D^2 int_v v^mu W`.
- Proved covariant current conservation before choosing a component frame.
- Derived the linearized retarded angular kernel from the auxiliary
  equation, including the `+i0` prescription.
- Proved transversality with `K_mu=(-omega,k)` in the mostly-plus convention.
- Evaluated the longitudinal angular integral and identified the Landau cut
  as the retarded response singularity from velocities satisfying
  `omega=v.k`.
- Extended `calculation-checks/qcd_phase_checks.py` with exact rational
  angular-moment and transversality bookkeeping checks.

## Checks

- `python3 calculation-checks/qcd_phase_checks.py`: passed.
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`: passed.
- `git diff --check -- calculation-checks/README.md calculation-checks/qcd_phase_checks.py monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md`: passed.
- `rg --pcre2 -n '\\over(?!line)' monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex calculation-checks/qcd_phase_checks.py planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md`: no matches.
- `tools/build_monograph.sh`: passed; strict text audit and final log scan were clean.
- `pdfinfo monograph/tex/main.pdf`: reports 2197 pages.

## Status

This closes a local gap between the static Debye-mass projection and the full
nonstatic HTL response.  It does not close #628: remaining work includes
interacting Polyakov-loop effective theories, lattice-continuum status
ledgers, high-density EFT, controlled dense phase examples, and a deeper
comparison between kinetic, Schwinger--Keldysh, and Euclidean formulations of
thermal QCD response.

# 2026-05-27 Issue #628 QCD Phase Thermodynamic-Observable Pass

## Scope

- Continued the #628 QCD phase-structure depth pass in Volume X,
  Chapter 12.
- Expanded the free-plasma and QGP-observable bridge from a list of
  quantities into a proposition deriving the pressure-derivative identities.
- Defined entropy density `s`, baryon density `n_B`, energy density
  `epsilon`, interaction measure `Delta=epsilon-3p`, and the `mu_B=0`
  sound speed `c_s^2` from a twice continuously differentiable limiting
  pressure.
- Proved the thermodynamic identities
  `dp=s dT+n_B dmu_B`, `d epsilon=T ds+mu_B dn_B`, and
  `Delta=T partial_T p + mu_B partial_mu p - 4p`.
- Proved the fixed-`x=mu_B/T` relation
  `Delta/T^4 = T partial_T[p(T,xT)/T^4]_x`, which is the precise form used
  when comparing thermal QCD calculations of the interaction measure.
- Derived the `mu_B=0` sound-speed formula
  `c_s^2=(partial_T p)/(T partial_T^2 p)` under charge conjugation and
  positive heat-capacity hypotheses.
- Added a conformal Stefan--Boltzmann benchmark showing that a homogeneous
  degree-four pressure has `Delta=0` and `c_s^2=1/3`.
- Extended `calculation-checks/qcd_phase_checks.py` with exact rational
  checks for the homogeneous pressure identity, fixed-`mu_B/T` reduced
  pressure, and conformal sound speed.

## Checks

- `python3 calculation-checks/qcd_phase_checks.py`: passed.
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`: passed.
- `git diff --check -- monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex calculation-checks/qcd_phase_checks.py calculation-checks/README.md planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md planning/build_audits/2026-05-27_issue628_qcd_phase_thermodynamic_observables.md`: passed.
- `tools/build_monograph.sh`: passed; strict text audit and final log scan
  clean.
- `pdfinfo monograph/tex/main.pdf`: reports 2194 pages.

## Status

This strengthens the quantitative QGP-observable layer of the chapter.  It
does not close #628: remaining work includes nonstatic HTL tensor/effective
action derivations, interacting Polyakov-loop effective theories,
lattice-continuum status ledgers, high-density EFT, and controlled dense
phase examples.

# 2026-05-27 Issue #628 QCD Phase Polyakov Effective Measure Pass

## Scope

- Continued the #628 QCD phase-structure depth pass in Volume X,
  Chapter 12.
- Added a finite-regulator Polyakov-loop effective-measure subsection under
  the center-symmetry discussion.
- Defined the exact finite-regulator Polyakov-loop effective object as the
  pushforward of the lattice path-integral weight to temporal Wilson lines.
- Distinguished positive probability measures from normalized complex linear
  functionals at real chemical potential or other complex-weight regulators.
- Proved the Peter--Weyl character-coordinate expansion for an `L^2` density
  and the pure-gauge total-`N`-ality selection rule.
- Stated a controlled-approximation criterion for local Polyakov-loop
  actions: omitted coefficients must be bounded by a convergent cluster or
  hopping expansion, or by a stated numerical error estimate.
- Derived the leading pure-gauge strong-coupling nearest-neighbor tube
  interaction with coefficient `J_1=u_square^{N_tau}+O(u_square^{N_tau+2})`.
- Derived the leading Wilson heavy-quark hopping term, including the
  antiperiodic thermal-winding sign and the coefficient
  `h=2 N_f (2 kappa)^{N_tau}` in the standard Wilson hopping normalization.
- Extended `calculation-checks/qcd_phase_checks.py` with exact center-charge
  and winding-exponent bookkeeping checks.

## Checks

- `python3 calculation-checks/qcd_phase_checks.py`: passed.
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`: passed.
- `git diff --check -- calculation-checks/README.md calculation-checks/qcd_phase_checks.py monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md`: passed.
- `rg --pcre2 -n '\\over(?!line)' monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex calculation-checks/qcd_phase_checks.py planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md`: no matches.
- `tools/build_monograph.sh`: passed after making the Polyakov effective
  measure material a subsection to avoid a theorem-number overfull in the
  table of contents; strict text audit and final log scan were clean.
- `pdfinfo monograph/tex/main.pdf`: reports 2200 pages.

## Status

This gives the chapter a finite-regulator foundation for Polyakov-loop
effective theories and separates exact marginalization from controlled local
truncations.  It does not close #628: remaining work includes
lattice-continuum status ledgers, high-density EFT, controlled dense phase
examples, and a deeper comparison between kinetic, Schwinger--Keldysh, and
Euclidean formulations of thermal QCD response.

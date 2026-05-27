# 2026-05-27 Issue #628 QCD Phase Finite-Regulator Pass

## Scope

- Reviewed the live #628 QCD-phase backlog and the existing Volume X QCD
  phase-structure chapter.
- Added a finite-lattice thermal gauge datum with compact link integration,
  unrooted integer-flavor determinants, masses, couplings, and fugacity.
- Proved finite-regulator analyticity: finite lattice partition functions are
  entire in finite couplings and masses and Laurent-polynomial in fugacity;
  finite pressures are holomorphic away from finite-regulator zeros.
- Defined thermodynamic phase transitions by limiting pressure
  nonanalyticity or nonunique source-selected Gibbs/KMS states.
- Added the Lee--Yang zero-free-neighborhood criterion: uniform convergence
  of zero-free finite pressures excludes pressure singularities.
- Proved the source-curvature susceptibility identity, tying divergent
  susceptibilities to integrated connected correlators.
- Extended `calculation-checks/qcd_phase_checks.py` with exact checks for the
  fugacity Laurent-polynomial shift and source-curvature identity.
- Updated the Volume X chapter dossier and calculation-check index.

## Checks

- `python3 calculation-checks/qcd_phase_checks.py` passed.
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py` passed.
- `git diff --check -- monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex calculation-checks/qcd_phase_checks.py calculation-checks/README.md planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md planning/build_audits/2026-05-27_issue628_qcd_phase_finite_regulator.md` passed.
- `tools/build_monograph.sh` passed with strict text audit and final log scan
  clean.
- `pdfinfo monograph/tex/main.pdf` reports 2184 pages.

## Status

This strengthens the analytic and limiting-procedure foundation of the QCD
phase-structure chapter.  It does not close #628: substantial work remains on
Polyakov-loop effective potentials, lattice-continuum status ledgers,
quantitative QGP observables, high-density EFT, and concrete phase-structure
examples with controlled hypotheses.

# Issue #628 QCD Phase Development: High-Density EFT Pass

## Scope

- Added a high-density effective-theory section to Volume X, Chapter 12 before
  the CFL order-parameter discussion.
- Defined the HDET scale hierarchy, patch fields, residual momentum
  decomposition, and the regulated meaning of the patch sum.
- Derived the Fermi-surface measure and density of states, including the
  two-spin Dirac factor.
- Derived the tree-level patch inverse propagator and transverse-curvature
  term.
- Derived the zero-temperature dense-quark HDL Debye coefficient in the
  monograph trace convention
  `tr_fund(T^a T^b)=delta^{ab}`.
- Derived the BCS logarithm as a Fermi-surface instability of a specified
  attractive channel while separating it from the QCD-specific gap prefactor.

## Verification

- `python3 calculation-checks/qcd_phase_checks.py`
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`
- `git diff --check -- calculation-checks/README.md calculation-checks/qcd_phase_checks.py monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md`
- `rg --pcre2 -n '\\over(?!line)' monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex calculation-checks/qcd_phase_checks.py planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`

The monograph build and log scan were clean.  The generated PDF has 2204 pages.

## Issue Status

This pass deepens #628 but does not close it.  Remaining work includes more
quantitative dense-QCD examples, weak-coupling QCD gap prefactors with
screened magnetic gluon exchange, and a stronger bridge between finite-density
effective theory, lattice limitations, and controlled nonperturbative
observables.

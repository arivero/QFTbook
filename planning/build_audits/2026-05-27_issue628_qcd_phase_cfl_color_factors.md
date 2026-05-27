# Issue #628 QCD Phase Development: CFL Color-Factor Pass

## Scope

- Expanded the color-superconductivity section of Volume X, Chapter 12.
- Added the trace-delta one-gluon exchange color-factor derivation for
  `square tensor square = Sym^2 square plus wedge^2 square`.
- Proved that the two-index antisymmetric quark-quark channel is attractive
  and the symmetric channel is repulsive in the stated Born-kernel convention.
- Proved the spin-zero \(s\)-wave exchange-symmetry statement that pairs
  color antisymmetry with flavor antisymmetry.
- Recast the CFL Goldstone count as a proposition with a proof separating
  Higgsed color directions from physical global Goldstone modes.
- Added exact arithmetic checks for the dense pairing color factors in the
  monograph trace convention.

## Verification

- `python3 calculation-checks/qcd_phase_checks.py`
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`
- `git diff --check -- calculation-checks/README.md calculation-checks/qcd_phase_checks.py monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md`
- `rg --pcre2 -n '\\over(?!line)' monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex calculation-checks/qcd_phase_checks.py planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`

The monograph build and log scan were clean.  The generated PDF has 2205 pages.

## Issue Status

This pass deepens #628 but does not close it.  The weak-coupling QCD gap
prefactor, screened magnetic gluon kernel, and quantitative dense-matter
examples remain for later passes.

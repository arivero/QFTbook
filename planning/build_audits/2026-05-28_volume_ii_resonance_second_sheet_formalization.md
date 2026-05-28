# Volume II Resonance Second-Sheet Formalization Audit

## Scope

- Strengthened `monograph/tex/volumes/volume_ii/chapter04_unstable_particles_self_energies_and_resonances.tex`.
- Formalized the distinction among cut, line-shape, complex-energy pole, and
  \(s\)-plane width coordinates.
- Added explicit proofs for:
  - physical-axis unitarity excluding a resonance pole on the physical boundary,
  - the threshold discontinuity sign of the one-loop self-energy,
  - elastic unitarity of the Breit--Wigner factor,
  - absence of the scalar resonance zero on either half of the first sheet,
  - the adjacent-sheet narrow-pole location by a contraction/Newton argument.
- Added `calculation-checks/resonance_second_sheet_checks.py` for finite
  algebra and sign checks behind the chapter formulas.

## Verification

Run on 2026-05-28:

```sh
python3 calculation-checks/resonance_second_sheet_checks.py
python3 -m py_compile calculation-checks/resonance_second_sheet_checks.py
git diff --check -- monograph/tex/volumes/volume_ii/chapter04_unstable_particles_self_energies_and_resonances.tex calculation-checks/resonance_second_sheet_checks.py calculation-checks/README.md planning/chapter_dossiers/volume_ii/chapter04_resonances_dressed_propagators.md planning/build_audits/2026-05-28_volume_ii_resonance_second_sheet_formalization.md
tools/build_monograph.sh
pdfinfo monograph/tex/main.pdf | rg '^Pages:'
```

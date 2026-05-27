# Build Audit: Pure SYM Local Index Oscillator

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`.
- Issues: #562 and #606.
- Main TeX target:
  `monograph/tex/volumes/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.tex`.
- Companion files:
  - `calculation-checks/susy_n1_pure_sym_checks.py`.
  - `calculation-checks/README.md`.
  - `planning/chapter_dossiers/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.md`.

## Source Leads

- Internal monograph source: the finite-volume Witten-index identity and
  small-circle affine-Toda pure-SYM chamber in Volume VII Chapter 06.
- Stringbook comparison: the stringbook Witten-index appendix emphasizes the
  spectral caveat for gapless systems and the local oscillator/Morse
  computation.  This pass translates only the intrinsic QFT index logic; no
  string compactification or holographic input is used.

## Substantive Changes

- Removed an implicit local-index shortcut from the small-circle input.
- Added a finite-dimensional holomorphic chiral-oscillator proposition:
  near an isolated nondegenerate chiral critical point, Takagi normal form
  reduces the Hessian to independent complex oscillators, each with a unique
  even Gaussian ground state and local supertrace `+1`.
- Distinguished the holomorphic chiral local index from the real Morse sign
  of `Re W`, preventing a common convention error in the Witten-index count.
- Updated the pure-SYM index/condensate ledger to use the new local-index
  proposition rather than assuming the contribution.
- Extended the pure-SYM calculation check with the local oscillator rank,
  parity, and convention ledger.

## Verification

- `python3 calculation-checks/susy_n1_pure_sym_checks.py` passed.
- `python3 -m py_compile calculation-checks/susy_n1_pure_sym_checks.py`
  passed.
- `tools/run_calculation_checks.sh` passed, including the pure-SYM checks.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed.  The resulting
  `monograph/tex/main.pdf` has 1817 pages and file size 7244950 bytes.

## Status

This pass further decomposes the pure `SU(N_c)` Witten-index computation into
explicit assumptions and finite-dimensional calculations.  It does not claim
a constructive proof of confinement, the four-dimensional mass gap, or the
spectral-continuation hypothesis.

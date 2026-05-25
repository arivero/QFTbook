# Volume VIII Chern-Simons Modular-Data Pass

## Trigger

- `claude_review.md` flagged the Chern--Simons chapter as framework-only:
  Wilson lines were defined, but no Jones/Verlinde/Reshetikhin--Turaev type
  calculation or modular data were displayed.

## Manuscript Edits

- Expanded
  `monograph/tex/volumes/volume_viii/chapter04_chern_simons_theory.tex`
  with explicit \(SU(2)_k\) modular data.
- Added the finite sine-transform modular \(S\)-matrix, with an orthogonality
  proof.
- Added normalized \(S^3\) unknot and Hopf-link expectation values
  \(S_{0a}/S_{00}\) and \(S_{ab}/S_{00}\).
- Added \(SU(2)_1\) and \(SU(2)_2\) examples, including the non-invertible
  spin-\(\frac12\) line at level \(2\).
- Added the Verlinde formula, the truncated \(SU(2)\) fusion rule, and the
  closed genus-\(g\) state-space dimension formula.
- Updated the Volume VIII Chapter 4 dossier.

## Calculation Check

- Added `calculation-checks/chern_simons_su2_modular_checks.py`.
- `python3 calculation-checks/chern_simons_su2_modular_checks.py` passed.

## Build Verification

- `git diff --check` passed.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` passed in
  `monograph/tex`.
- `main.pdf` now builds to 1197 pages, with no undefined references in
  `main.log`.

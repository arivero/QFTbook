# Volume VI Sine-Gordon And Bootstrap Depth Pass

## Trigger

- `claude_review.md` flagged Volume VI as too survey-like in the exact
  integrable-model chapters, with key bootstrap steps asserted rather than
  derived.
- The sine-Gordon lightest-breather amplitude needed a more careful treatment
  of direct versus crossed physical-strip poles.

## Manuscript Edits

- Expanded
  `monograph/tex/volumes/volume_vi/chapter02_two_dimensional_scattering_analyticity_bootstrap.tex`
  with explicit horizontal-strip growth hypotheses, the rapidity derivation
  of the bound-state mass formula, a residue derivation of the fusion
  identity, and the elementary scalar block pole/zero algebra.
- Expanded
  `monograph/tex/volumes/volume_vi/chapter08_sine_gordon_massive_thirring_affine_toda.tex`
  with the neutral scalar block \(F_a(\theta)\), residue-sign computation,
  correction of the lightest-breather crossed-pole discussion, the minimal
  breather-breather amplitude, and the direct fusion-pole mass derivation.
- Updated the corresponding Volume VI chapter dossiers.

## Calculation Check

- `python3 calculation-checks/sine_gordon_smatrix_checks.py` passed.
- The check now verifies the crossed pole, neutral-block residue signs,
  breather-breather unitarity and crossing, and the direct fusion mass
  formula in addition to the previous soliton-matrix tests.

## Build Verification

- `git diff --check` passed.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` passed in
  `monograph/tex`.
- `main.pdf` now builds to 1193 pages, with no undefined references in
  `main.log`.

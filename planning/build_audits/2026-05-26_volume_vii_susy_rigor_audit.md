# Build Audit: Volume VII SUSY Rigor/QFT-Foundation Pass

Date: 2026-05-26

Branch: `codex/susy-gauge-dynamics-localization`

## Scope

This pass reviewed the Volume VII supersymmetric field-theory chapters for
rigor, self-contained derivations, convention consistency, and accidental
string-theory-as-foundation language.  The guiding standard was that external
string-theoretic material can motivate examples or convention checks, but the
monograph's arguments must be QFT arguments with explicit hypotheses.

## Substantive Edits

- Chapter 06: replaced residual Klebanov-Witten/Klebanov-Strassler
  "regular-brane" and "one-brane" vocabulary by intrinsic rank/common-rank
  gauge-theory language, and made the dossier state that the stringbook source
  is convention/example guidance only.
- Chapter 08: added an explicit affine chiral quotient and symplectic vacuum
  quotient datum, a proposition comparing them under stated Kempf-Ness
  hypotheses, and a worked rank-one abelian quotient example
  `C[x,y]^{C^*}=C[xy]`.
- Chapter 10: renamed the ABJM "one-brane quotient" proposition to the
  rank-one abelian quotient and described it as an intrinsic gauge-theory
  calculation.
- Chapter 11: rewrote the `(2,0)` anomaly-polynomial status boundary so the
  quoted theorem is protected QFT data, not a construction imported from
  string theory or geometry.
- Chapter 15: changed the cusp/Konishi strong-coupling language so
  semiclassical string comparisons are historical checks rather than inputs.
- Chapter dossiers 08, 10, 11, 13, 14, and 15 now record the QFT-foundation
  scope boundary and the new quotient checks.
- Added `calculation-checks/susy_moduli_space_checks.py` and documented it in
  `calculation-checks/README.md`.

## Review Findings

- Chapters 04--07 remain the deepest four-dimensional SUSY gauge-dynamics
  stack: Wilsonian schemes, holomorphy, SQCD, pure SYM, instantons, and the
  current nonperturbative ledgers are developed with explicit assumptions.
- Chapter 08 was the largest local rigor gap because it used the quotient
  slogan too quickly.  The new quotient proposition fixes the immediate
  foundation, though future passes should still add singular local models and
  derived/scheme-theoretic branch data.
- Chapters 10--11 are honest about non-Lagrangian or monopole-sector inputs,
  but need future expansion of parity-anomaly/global-form data and self-dual
  tensor/anomaly descent.
- Chapters 12--15 contain extensive integrability calculations.  Their main
  remaining obligation is to keep every all-coupling or strong-coupling claim
  separated from external string-theoretic motivation unless the QFT-side
  derivation is displayed.
- Chapter 16 has a useful localization datum and finite-dimensional theorem,
  but future work should expand determinant, contour, compactification, and
  instanton-measure derivations.

## Verification

- `python3 calculation-checks/susy_moduli_space_checks.py`: passed.
- `python3 -m py_compile calculation-checks/susy_moduli_space_checks.py`:
  passed.
- `tools/run_calculation_checks.sh`: passed, including the new moduli-space
  quotient checks and existing Wolfram gamma-trace checks.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: passed; generated
  `monograph/tex/main.pdf` with 1850 pages and file size 7375170 bytes.

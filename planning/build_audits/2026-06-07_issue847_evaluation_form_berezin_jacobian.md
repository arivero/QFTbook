# Issue #847 Evaluation-Form Berezin Jacobian

## Target

- GitHub issue: #847, Hori--Vafa signs, normalizations, and direct
  instanton/amplitude scrutiny.
- Chapter target:
  `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`.
- Companion target: `calculation-checks/susy_2d_lg_glsm_checks.py`.
- Planning target:
  `planning/chapter_dossiers/volume_vii/chapter09_two_dimensional_supersymmetric_models.md`.

## Substance

- Added `ex:cpn-degree-one-evaluation-berezin-jacobian` after the Euler
  determinant-line calculation for the degree-one `P^{N-1}` A-model sector.
- The new example computes the pulled-back evaluation forms for two point
  insertions and one hyperplane insertion on the affine degree-one chart.
  Their top wedge has determinant `+1` against the Euler-oriented fermion
  zero-mode measure.
- The block separates the insertion/Berezin Jacobian from the mirror root sum
  and from the stable-map line count.  Rescaled hyperplane representatives,
  duplicated/contact forms, and orientation swaps change or kill the coefficient.
- Added `check_degree_one_cpn_evaluation_form_berezin_jacobian()` with exact
  rational determinant/rank checks for `N=2,...,8`.
- Updated the calculation README, evidence-contract tag, and Ch09 dossier.

## Re-Audit Notes

- This is physics-facing instanton-measure work: it checks how A-twisted local
  insertions saturate fermion zero modes in the retained degree-one sector.
- It avoids promoting Hori--Vafa residue agreement or a stable-map line count
  to a physical amplitude by itself.
- It does not prove the continuum vortex-regulator limit, the full
  Hori--Vafa operator/source comparison theorem, or uniform determinant and
  compactification residual estimates.
- The monograph TeX contains no directive, review, monitor, or issue-management
  language.

## Verification

- Passed focused GLSM py_compile, standalone check, and harness entry.
- Passed Ch09 theorem/display/prose/style/text audits and process-language
  leakage scan.
- Passed evidence-contract, calculation-inventory, chapter-dossier, JSON, and
  diff checks.
- Passed full `tools/run_calculation_checks.sh --python-only`.
- Passed full `tools/build_monograph.sh`.

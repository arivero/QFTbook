# Issue #848 Matrix Spectral-Measure Gate

## Target

- GitHub issue: #848, full GLSM/Hori--Vafa and cigar/Liouville mirror-QFT data.
- Chapter target:
  `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`.
- Companion target: `calculation-checks/susy_2d_lg_glsm_checks.py`.
- Planning target:
  `planning/chapter_dossiers/volume_vii/chapter09_two_dimensional_supersymmetric_models.md`.

## Substance

- Added `constr:cigar-liouville-matrix-spectral-measure` immediately after
  the source spectral-resolution construction.  The new block upgrades the
  noncompact spectral comparison from a scalar phase-density/source-row
  observable to the matrix-valued spectral measure for a family of local
  sources.
- Defined `d\mu_{IJ,\alpha}` and `G^{f,\mathcal I}_{IJ,\alpha}` so
  Plancherel weights, source rows, pole norming constants, positivity, and
  contact terms are compared in a single operator/source scheme.
- Included a finite three-bin model in the TeX: two candidates share the
  first source and mixed entry; the second source differs.  A local contact
  patch matches one heat-kernel test, but a second Euclidean test leaves a
  residual discrepancy.
- Added `check_cigar_liouville_matrix_spectral_measure_gate()` to the GLSM
  companion with exact rational arithmetic for the same obstruction.
- Updated the calculation README, evidence-contract tags, and Ch09 dossier.

## Re-Audit Notes

- The pass targets a physical full-QFT datum: source-normalized noncompact
  spectral measures and their positivity/Gram-kernel structure.  It avoids a
  new protected superpotential cell.
- The construction is still a finite interface check.  It does not derive the
  Liouville reflection formula, the full Plancherel measure, all pole
  residues, finite-field Kahler uniqueness, or the full cigar/Liouville mirror
  equivalence.
- The monograph TeX contains no directive, review, monitor, or issue-management
  language.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
  passed.
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`
  passed.
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
  passed.
- Ch09 theorem/display/prose/style/text audits and process-language leakage
  scan passed.
- Evidence-contract, calculation-inventory, chapter-dossier, JSON, and diff
  checks passed.
- Full `tools/run_calculation_checks.sh --python-only` passed.
- Full `tools/build_monograph.sh` passed.

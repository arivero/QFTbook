# Build Audit: Issue #603 LG/GLSM Intrinsic-QFT Pass

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`
- Issue: #603
- Files:
  - `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
  - `planning/chapter_dossiers/volume_vii/chapter09_two_dimensional_supersymmetric_models.md`
  - `calculation-checks/susy_2d_lg_glsm_checks.py`
  - `calculation-checks/README.md`

## Mathematical Content Added

- Defined polynomial two-dimensional `N=(2,2)` Landau-Ginzburg data as
  field-variable data, including component fields, Kahler metric, and
  holomorphic superpotential.
- Derived the auxiliary-field potential and the classical critical-locus
  vacuum equations.
- Defined quasihomogeneous isolated Landau-Ginzburg data and the Jacobi
  algebra.
- Proved the Jacobian quotient from a stated `B`-type local differential
  `Q_B phi^i = 0`, `Q_B eta_i = partial_i W`.
- Proved the quasihomogeneous charge ledger, Fermat Jacobi basis, Fermat
  Jacobi dimension, and protected central-charge consistency test.
- Defined abelian GLSM data with integer charges, invariant superpotential,
  FI-theta coordinate, gauge coupling, and regulator.
- Proved the classical chamber analysis for charges `(1,...,1,-d)` and
  superpotential `P G_d(X)`, including the `r>0` hypersurface quotient, the
  `r<0` residual finite gauge group `mu_d` and LG chamber, and the singular
  status of `r=0`.
- Kept the presentation intrinsic to two-dimensional QFT: no mirror-duality,
  superstring, D-brane, or string-compactification argument is used.

## Calculation Checks

- Added `calculation-checks/susy_2d_lg_glsm_checks.py` for:
  - `A_k` quasihomogeneous charges and central charges;
  - Fermat monomial charge and derivative charge ledgers;
  - Fermat Jacobi dimensions;
  - quintic LG central charge and Jacobi dimension;
  - hypersurface GLSM gauge-invariance, axial-anomaly, chamber-dimension,
    and residual finite-group arithmetic.

## Verification

- `python3 calculation-checks/susy_2d_lg_glsm_checks.py`: passed.
- `python3 calculation-checks/superconformal_algebra_checks.py`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/run_calculation_checks.sh`: passed, including the Wolfram Language
  gamma-trace backend.
- `tools/build_monograph.sh`: passed with clean final log scan.
- `pdfinfo monograph/tex/main.pdf`: 1766 pages, 7031397 bytes, PDF 1.5.
- No `references/` files were modified, added, or staged in this pass.

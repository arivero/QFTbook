# Build Audit: Issue #603 Abelian GLSM Coulomb Pass

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`
- Issue: #603
- Files:
  - `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
  - `planning/chapter_dossiers/volume_vii/chapter09_two_dimensional_supersymmetric_models.md`
  - `calculation-checks/susy_2d_lg_glsm_checks.py`
  - `calculation-checks/README.md`
  - `planning/build_audits/2026-05-26_issue603_coulomb_glsm.md`

## Mathematical Content Added

- Added an intrinsic abelian GLSM Coulomb-branch one-loop ledger between the
  GLSM datum and the classical chamber analysis.
- Stated the local determinant hypotheses explicitly: nonzero chiral masses,
  logarithm branch, supersymmetric Wilsonian regulator, scale choice, and
  exclusion of boundary, vortex, and singular-locus contributions from the
  local one-loop calculation.
- Derived the effective twisted-superpotential critical equation
  \[
    \prod_i (Q_i\sigma/\mu)^{Q_i}=\exp(t)
  \]
  from the displayed one-loop \(\widetilde W_{\rm eff}\).
- Proved that all-positive charges give \(\sum_i Q_i\) simple local Coulomb
  roots and worked out the \(\mathbb P^{N-1}\) charge-one count.
- Recorded the hypersurface charge-vector consequence: the Coulomb
  \(\sigma\)-exponent is \(N-d\), equal to the axial anomaly coefficient, so
  the anomaly-free case gives a FI-theta singular-locus condition rather than
  isolated Coulomb roots.

## Calculation Checks

- Extended `calculation-checks/susy_2d_lg_glsm_checks.py` with exact integer
  checks for:
  - positive-charge Coulomb vacuum counts;
  - \(\sigma\)- and \(\mu\)-exponents in the one-loop critical equation;
  - hypersurface charge-vector Coulomb exponent equals the axial anomaly;
  - quintic hypersurface exponent zero.

## Verification

- `python3 calculation-checks/susy_2d_lg_glsm_checks.py` passed.
- `tools/run_calculation_checks.sh` passed, including the Wolfram
  gamma-trace/anomaly-normalization check.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed before staging.
- `tools/build_monograph.sh` passed after rebasing onto `origin/main` and
  produced `monograph/tex/main.pdf` with 1778 pages.
- A final log scan found no unresolved-reference LaTeX warnings in
  `monograph/tex/main.log`.
- A reference/prohibited-path guard found no staged, modified, or untracked
  `references/`, `.claude/`, or `claude_review.md` files in this pass.

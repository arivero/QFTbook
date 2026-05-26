# Build Audit: Issue #594 N=4 Exact Marginality Pass

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`
- Issue: #594, partial `N=4` Yang-Mills conformal-manifold component
- Files:
  - `monograph/tex/volumes/volume_vii/chapter12_planar_n4_spectral_problem_spin_chains.tex`
  - `planning/chapter_dossiers/volume_vii/chapter12_planar_n4_spectral_problem_spin_chains.md`
  - `calculation-checks/susy_n4_scft_checks.py`
  - `calculation-checks/README.md`
  - `planning/build_audits/2026-05-26_issue594_n4_exact_marginality.md`

## Mathematical Content Added

- Replaced the previous `N=4` exact-marginality quote with an explicit
  finite-conformal-family hypothesis: regulator, gauge and supersymmetry Ward
  identities, stress-tensor multiplet placement of the coupling operator,
  fixed source/contact-term normalization, absence of current-moment-map
  obstructions, and zero beta function for the complex coupling.
- Defined the upper-half-plane coupling chart
  `tau=theta/(2 pi)+4 pi i/g_YM^2` and the field-theoretic theta-periodicity
  input from integer instanton number.
- Proved, under the finite-family hypothesis, that the local `N=4`
  conformal family is one complex dimensional before global duality
  identifications.
- Separated electric-magnetic duality into its own QFT status boundary:
  a subgroup `Gamma <= PSL(2,Z)` depends on the chosen global form and
  line-operator lattice, and only conditionally produces the quotient
  `H/Gamma`.

## Calculation Checks

- Extended `calculation-checks/susy_n4_scft_checks.py` with exact checks for:
  - the `1-0=1` local exact-marginal source-chart dimension count;
  - theta-periodicity for integer instanton number;
  - `SL(2,Z)` generator determinants and relations `S^2=(ST)^3=-I`;
  - preservation of the upper half-plane by `S` and `T`;
  - invariance of the weak-coupling `q=exp(2 pi i tau)` coordinate under
    `T`.

## Verification

- `python3 calculation-checks/susy_n4_scft_checks.py` passed, including the
  new exact-marginal coupling-chart and modular-generator checks.
- `tools/run_calculation_checks.sh` passed, including the Wolfram gamma-trace
  backend.
- `tools/audit_monograph_text.sh` initially flagged one reader-facing
  phrasing issue in the new scope-boundary paragraph; the wording was revised
  and the audit then passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed with a clean log scan and produced
  `monograph/tex/main.pdf` with `1790` pages before rebasing.
- After rebasing the branch on the latest `origin/main`, the targeted N=4
  check, full calculation-check harness, text audit, chapter-dossier audit,
  `git diff --check`, and `tools/build_monograph.sh` were rerun.  The
  rebuilt PDF passed the log scan and contains `1795` pages.
- No `.claude/`, `claude_review.md`, or `references/` files were edited or
  staged for this pass.

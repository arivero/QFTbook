# Build Audit: Issue 588 Seiberg-Witten Rigor Pass

- Date: 2026-05-26
- Branch: `codex/susy-gauge-dynamics-localization`
- Worktree: `/Users/xiyin/QFT_susy_gauge_dynamics_localization`
- Issue: GitHub #588, Seiberg-Witten derivation-rigor slice only.
- Scope boundary: pure QFT. No superstring compactification, Calabi-Yau engineering, or holographic assumptions are used as monograph input.

## Source Review

- Handoff contract and lane file were reviewed before work: `00_common_agent_contract.md`, `README.md`, and `03_susy_gauge_dynamics_localization.md`.
- `claude_review.md` and open GitHub issue #588 were reviewed; #590 was previously corrected/closed as out of scope for the QFT monograph.
- Local source payload for this pass: `references/susy_gauge_dynamics_localization/issue588_sw_rigor/`.
- Source leads used for comparison only: Seiberg-Witten 1994 pure `N=2` papers, Argyres-Douglas singularity papers, and local prior references. The monograph text gives self-contained derivations for the statements added in this pass.

## Files Changed

- `monograph/tex/volumes/volume_vii/chapter07_four_dimensional_n2_seiberg_witten.tex`
- `calculation-checks/sw_su2_periods.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_vii/chapter07_four_dimensional_n2_seiberg_witten.md`
- `references/susy_gauge_dynamics_localization/issue588_sw_rigor/`

## Mathematical Content Added

- Added an argument-type ledger for the pure `su(2)` Seiberg-Witten construction, separating QFT hypotheses, symmetry-derived statements, holomorphy-derived statements, special-geometry theorems, constraint-derived steps, consistency checks, and heuristic/status-boundary statements.
- Fixed rank-one charge and monodromy conventions by defining the charge lattice, Dirac pairing, period vector, and central charge before the monodromy calculation.
- Proved the Picard-Lefschetz hypermultiplet monodromy matrix from the pairing convention and checked symplecticity and unipotence.
- Added a minimal-ansatz derivation of the pure `su(2)` curve `y^2=(x^2-\Lambda^4)(x-u)`, including the discriminant calculation and the explicit assumptions under which the uniqueness statement is valid.
- Added a local Argyres-Douglas cusp-scaling subsection with assumptions stated, the local model `y^2=x^3+v x+u`, the differential convention, and the scaling-dimension derivation. The text marks this as local special geometry rather than a full constructive QFT theorem.

## Calculation Checks

- Extended `calculation-checks/sw_su2_periods.py` to verify:
  - Picard-Lefschetz central-charge action for representative light charges.
  - Symplecticity and unipotence of the resulting monodromy matrices.
  - The minimal-curve discriminant for the three branch points.
  - The Argyres-Douglas cusp scaling equations and resulting dimensions.

## Verification

- `python3 calculation-checks/sw_su2_periods.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- TeX log scan for reference/citation warnings, errors, overfull/underfull boxes, and foreign-command markers.
- `pdfinfo monograph/tex/main.pdf` reported 1538 pages.

## Remaining Work

- Do not close #588 from this pass. It still asks for additional `N=4` SCFT/operator-spectrum development and broader Seiberg-Witten development beyond the pure-rank-one rigor slice addressed here.

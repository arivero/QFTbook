# 2026-05-28 Issue #634: Standard Model RG Depth Pass

## Scope

Second focused development pass on GitHub issue #634 for
`monograph/tex/volumes/volume_ii/chapter19c_standard_model_hybrid_definition.tex`.

This pass adds the perturbative running part of the Standard Model hybrid
datum as source-chart statements rather than as ultraviolet-completion
claims.  The hypercharge convention is the chapter convention
`Q = T^3 + Y`; the GUT-rescaled coupling is treated only as a coordinate
change.

## Manuscript Changes

- Added Section `One-Loop Running in a Minimal Source Chart`.
- Added Proposition `prop:sm-one-loop-gauge-beta`, deriving
  `(4 pi)^2 beta_g1 = (41/6) g1^3`,
  `(4 pi)^2 beta_g2 = -(19/6) g2^3`, and
  `(4 pi)^2 beta_g3 = -7 g3^3` from the Standard Model representation sums.
- Added a hypercharge-normalization remark converting to
  `b_1^GUT = 41/10`.
- Added Proposition `prop:sm-one-loop-top-higgs-subsystem`, stating the
  one-loop minimal-subtraction top-Yukawa and Higgs-quartic subsystem on the
  invariant source subspace where only `y_t` is nonzero among Yukawa singular
  values.
- The proof text keeps the RG equations explicitly perturbative and avoids
  claims about selecting ultraviolet boundary data.

## Calculation Check

- Extended `calculation-checks/standard_model_anomaly_checks.py`.
- New checks cover the one-loop gauge beta coefficients, hypercharge
  GUT-rescaling, the top-Yukawa group-factor coefficients, and the compact
  versus expanded Higgs-quartic gauge polynomial.

## Verification

Passed before checkpoint:

- `python3 calculation-checks/standard_model_anomaly_checks.py`
- `python3 -m py_compile calculation-checks/standard_model_anomaly_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh` (`main.pdf`, 2338 pages)

## Remaining Issue #634 Work

This pass does not close #634.  Remaining large items include precision
electroweak `S,T,U`, the full muon `g-2` hybrid calculation, a more explicit
dimension-six operator-basis ledger, and the chiral-lattice construction
connection.  Higgs vacuum-stability discussion should be added only as a
controlled RG/source-chart statement, not as a claim that the RG selects
ultraviolet boundary data.

# 2026-06-06 Issue #597 Proper-Time Determinant Channel Audit

## Scope

- File touched: `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- Companion evidence: `calculation-checks/instanton_physical_amplitude_architecture_checks.py`.
- Planning inventory: Ch20D dossier and calculation-check README.
- Target: improve the dedicated instanton physical-amplitude chapter by opening
  the zero-mode-deleted determinant logarithm which feeds the channel density.

## Substance

- Added `ca:instanton-proper-time-determinant-channel` between density
  normalization and channel packaging.
- The new block derives the source-channel determinant logarithm from
  zero-mode-deleted boson, ghost, fermion/Pfaffian, and counterterm pieces.
- It records the local coefficient identity
  `-1/2 h_B + h_gh + h_F + h_ct = b0`, with the SU(3), `N_f=2` split
  `7/3 + 22/3 = 29/3`.
- It turns leftover determinant-log errors into an absolute source-window
  bound, so signed heat-kernel cancellations cannot be used as amplitude
  control.
- It explicitly distinguishes a nonzero determinant density from a nonzero
  source/projection amplitude.

## Quality And Scope Judgment

- This is physics-amplitude depth, not ADHM or moduli-space expansion.
- The pass strengthens the fluctuation-measure step the user flagged as harder
  and more important than moduli-space analysis.
- The monograph TeX contains no GitHub, directive, monitoring, or planning
  language.
- The calculation check includes adversarial controls for wrong determinant
  signs, omitted ghost determinant, signed residual cancellation, and
  rank-killed source channels.

## Verification

- Passed: focused Ch20D theorem/display/negative/style/process scans.
- Passed: `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`.
- Passed: `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`.
- Passed: `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`.
- Passed: calculation inventory and evidence-contract audits.
- Passed: chapter dossier and monograph text audits.
- Passed: full Python calculation suite; Wolfram checks were not selected.
- Passed: `tools/build_monograph.sh` at 3451 pages after replacing local
  `\Tr`/`\Pf` notation by explicit `\operatorname{Tr}`/`\operatorname{Pf}`.

# Build Audit: ADS Radial Higgs Cutoff

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`.
- Issues: #562, #597, and #606.
- Main TeX target:
  `monograph/tex/volumes/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.tex`.
- Companion files:
  - `calculation-checks/susy_instanton_nekr_checks.py`.
  - `calculation-checks/README.md`.
  - `planning/chapter_dossiers/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.md`.

## Source Leads

- Internal monograph source: Volume II BPST instanton normalization and the
  existing Volume VII Chapter 06 ADS one-instanton derivation.
- Stringbook convention floor:
  `/Users/xiyin/PhysicsLogic/references/stringbook/string notes.tex` around
  the 4D N=1 Wilsonian and ADS discussion, especially the caution that the
  nonzero ADS coefficient is an instanton-calculus input.
- The pass is intrinsic supersymmetric QFT. No superstring,
  compactification, brane, or holographic argument is used.

## Substantive Changes

- Added the radial Higgs-cutoff calculation, a finite radial-integral check
  for the instanton-size coordinate in the `N_f=N_c-1` ADS Higgs patch.
- The calculation defines
  `H(v, tilde v)=sum_i(|v_i|^2+|tilde v_i|^2)` and proves
  `int_0^infty rho^(2p-1) exp(-c H rho^2) d rho
  = (p-1)!/(2(cH)^p)` for `p > 0`, `c > 0`, and `H > 0`.
- The text records exactly what the Higgs expectation values prove:
  exponential large-size convergence and real homogeneous scaling of the
  radial factor.
- The proposition also states the status boundary explicitly: this real
  cutoff estimate does not determine the holomorphic `1/det M` denominator
  and does not extend the maximal-rank instanton calculation across
  `det M=0`, where the Yukawa lifting rank changes.
- Extended `susy_instanton_nekr_checks.py` with an exact rational check of
  the radial-integral recurrence, real scaling under `H -> |t|^2 H`, and the
  exponent relation between `rho^(2p-1)` and `(cH)^(-p)`.

## Verification

- `python3 calculation-checks/susy_instanton_nekr_checks.py` passed.
- `python3 -m py_compile calculation-checks/susy_instanton_nekr_checks.py`
  passed.
- `tools/run_calculation_checks.sh` passed, including the Wolfram gamma-trace
  check.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed.
- Output PDF metadata after the build: 1849 pages, 7370368 bytes.

## Status

This pass turns the phrase "the Higgs vev cuts off the instanton size
integral" into a proved finite calculation with hypotheses. It does not
complete the full ADS measure theorem: the angular/orientation measure,
nonzero-mode determinant, small-size endpoint, holomorphic regulator, and
nonzero coefficient remain the analytic instanton-calculus input recorded in
the chapter.

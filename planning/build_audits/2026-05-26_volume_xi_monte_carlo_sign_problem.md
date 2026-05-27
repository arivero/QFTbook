# 2026-05-26 Volume XI Monte Carlo Sign-Problem Audit

## Scope

- Deepened Volume XI, Chapter 6 from an algorithmic overview into a
  finite-regulator theorem-level treatment.
- Added a self-contained finite-state ergodic theorem using primitive powers
  and an explicit \(\ell^1\) contraction.
- Proved the exact finite-\(N\) autocorrelation variance identity and derived
  the integrated-autocorrelation asymptotic under absolute summability.
- Defined the average phase as \(Z/Z_R\), defined the finite-volume
  phase-quenched free-energy difference, and proved the sample-size lower
  bound behind exponential phase-reweighting degradation.
- Clarified the determinant-positivity logic: \(\gamma_5\)-Hermiticity gives
  determinant reality; positivity requires an even degenerate determinant
  power or a conjugate-pair construction.

## Calculation Checks

- Added `calculation-checks/monte_carlo_sign_problem_checks.py`, which checks:
  - the finite-\(N\) autocorrelation variance identity in a two-state chain;
  - the finite reweighting identity and average-phase relative variance;
  - the determinant reality/positivity distinction in a finite
    \(\Gamma D\Gamma=D^\dagger\) model.

## Verification

- `python3 calculation-checks/monte_carlo_sign_problem_checks.py`
- `python3 -m py_compile calculation-checks/monte_carlo_sign_problem_checks.py`
- `python3 calculation-checks/ising_metropolis_finite_checks.py`
- `python3 calculation-checks/z2_gauge_metropolis_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

## Residual Work

The full monograph build and log scan were clean.  `pdfinfo` reports
`Pages: 1842` for `monograph/tex/main.pdf`.

- This pass treats finite-state Markov-chain and finite-volume sign-problem
  algebra.  Later numerical-method chapters should still develop TCSA, DLCQ,
  Hamiltonian truncation, HMC, error analysis for continuum extrapolations,
  and finite-size scaling workflows.

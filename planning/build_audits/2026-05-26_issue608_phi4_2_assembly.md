# 2026-05-26 Issue #608 Phi4_2 Assembly Pass

## Scope

Addressed the first concrete weakness flagged in `claude_review.md` and
GitHub issue #608: the \(\Phi^4_2\) stochastic-quantization chapter had
proved or isolated the finite-dimensional Langevin identity, Wick powers,
Sobolev DPD local fixed point, smooth energy estimate, and invariant-law
passage, but did not assemble them into a single logically checkable theorem.

## Manuscript Changes

- Added Theorem `thm:phi-four-two-spde-main-theorem` in Volume XI, Chapter 9.
- The theorem states the finite-cutoff Wick-ordered Gibbs measures
  \(\mu_N\), their Markov semigroups \(P_t^{(N)}\), and the limiting field
  topology \(H^{-\kappa}\).
- The theorem lists the four analytic inputs needed for full
  two-dimensional stochastic-quantization closure:
  1. path-space convergence of the enhanced OU fields
     \((X_N,:X_N^2:,:X_N^3:)\);
  2. global compact-continuity of the DPD solution map;
  3. tightness of stationary cutoff laws and support on the DPD
     decomposition;
  4. closure of reflection positivity under the weak limit for cylinder
     observables.
- The proof derives invariance from the finite-dimensional Langevin identity
  and Proposition `prop:spde-invariant-measure-limit`, then records the
  Schwinger-function and OS-positivity consequences.
- Added Proposition `prop:spde-sobolev-dpd-three-dimensional-obstruction`.
  This proves that the Sobolev DPD closure used for \(\Phi^4_2\) cannot be
  transported to dynamic \(\Phi^4_3\): the minimal multiplier condition
  \(\beta>1/2+\kappa\) already forces the heat-smoothing exponent above
  \(1\), while Duhamel integrability requires \(\theta<1\).

## Calculation Check

Extended `calculation-checks/constructive_scalar_spde_checks.py` with
`check_phi4_three_sobolev_dpd_obstruction_arithmetic()`, verifying:

- the sample minimal multiplier threshold gives
  \(\theta=1+\frac52\kappa>1\);
- the stronger Sobolev-algebra threshold gives
  \(\theta=\frac32+2\kappa>1\).

## Issue Status

#608 remains open.  This pass closes the first assembly/framing gap but does
not yet prove the sharp Besov/Hölder global estimates, the concrete
\(\Phi^4_3\) modelled-distribution Schauder/product estimates, or the
SPDE-to-Wightman closure.

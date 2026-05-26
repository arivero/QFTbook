# 2026-05-26 Issue #582 One-Loop Relative-Scale Gap

## Scope

- Volume XI, Chapter 9 now includes a concrete one-loop relative-scale
  estimate for a local subtraction.
- This is the first step from the abstract sector summability infrastructure
  toward tree-by-tree BPHZ estimates for dynamic \(\Phi^4_3\).

## Mathematical Content

- Two dyadic kernels \(K_i\) and \(L_j\) of orders \(a\) and \(b\) are
  compared in the two sectors \(j\leq i\) and \(j>i\).
- In the \(j\leq i\) sector the local term \(L_j(0)\) is subtracted.  A
  Holder-scale estimate for \(L_j(h)-L_j(0)\) gives the relative gap
  \(a+\theta\).
- In the \(j>i\) sector no local subtraction is needed for this prototype;
  the smaller support of \(L_j\) gives the relative gap \(b\).
- For dynamic \(\Phi^4_3\), \(Q=5\) and \(a=b=2\).  The remaining base
  factor \(2^{(Q-a-b)k}=2^k\) is the local mass-coordinate divergence, while
  the relative scales are summable.

## Calculation Check

- `calculation-checks/constructive_scalar_spde_checks.py` now verifies the
  exact arithmetic for \(Q=5\), \(a=b=2\), \(\theta=1\):
  the local-sector exponent at \(i=7,j=4\), the off-sector exponent at
  \(i=4,j=7\), and the geometric sums for the local and off-diagonal gaps.

## Remaining Issue #582 Obligations

- Extend the one-loop prototype to the actual negative-tree coordinates of
  the BPHZ model.
- Prove the two-loop nested and non-nested sector decompositions, including
  overlapping local subtractions.
- Verify the corresponding \(\Pi\)- and \(\Gamma\)-coordinate charts so that
  the coordinate-to-model convergence theorem can be applied.

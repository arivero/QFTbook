# 2026-05-27 Volume XI Finite-Size Scaling Pass

## Scope

This pass deepens Volume XI, Chapter 4 by replacing informal finite-size
scaling language with an RG-coordinate theorem and by defining finite-volume
step scaling as a continuum coordinate.

## Substantive Additions

- Added a finite-volume limit discussion that separates the ultraviolet
  cutoff \(a\), physical box size \(L=Na\), and physical correlation length.
- Defined a finite-size scaling datum for \(N=b^n\) lattice tori: relevant
  endpoint coordinate, irrelevant-coordinate estimate, operator dimensions,
  and uniform separated-point control.
- Proved finite-size scaling from the datum:
  \[
    N^{\sum_i\Delta_{I_i}}G_N^{I_1\ldots I_k}
    =
    F^{I_1\ldots I_k}(tN^{y_t})+O(N^{-\omega}).
  \]
- Derived the physical finite-volume scaling variable
  \(t(a)N^{y_t}\to (ML)^{y_t}\) under the continuum mass tuning
  \(t(a)=(aM)^{y_t}+O(a^{y_t+\epsilon})\).
- Defined step scaling through a finite-volume observable coordinate and a
  continuum \(a/L\to0\) limit at fixed \(g_L=u\), including the required
  Symanzik extrapolation structure and remainder statement.
- Extended the continuum-scaling calculation check with finite-size endpoint
  variables, irrelevant corrections, and physical finite-volume scaling.

## Verification

- Passed: `python3 calculation-checks/continuum_scaling_window_checks.py`
- Passed: `python3 -m py_compile calculation-checks/continuum_scaling_window_checks.py`
- Passed: primitive-fraction scan on touched files.
- Passed: `git diff --check` on touched files.
- Passed: `tools/build_monograph.sh`
- Built PDF: `/Users/xiyin/QFT/monograph/tex/main.pdf`, 2227 pages.

## Remaining Work

- Chapter 4 still needs a nontrivial interacting finite-size example with
  actual estimates, and Chapter 5 should connect the finite-volume
  step-scaling definition to gradient-flow and Wilson-loop gauge-theory
  coordinates.

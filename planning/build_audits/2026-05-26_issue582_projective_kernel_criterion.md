# Issue #582 Projective Kernel Criterion Checkpoint

## Manuscript Change

- Added Proposition `prop:spde-projective-kernel-dual-norm-criterion` to
  Volume XI, Chapter 9.
- The proposition proves that an \(E'\)-valued chaos kernel represented as a
  Bochner integral
  \[
    \int_S f(s)\otimes \ell(s)\,\mathrm d\mu(s)
  \]
  has projective tensor norm bounded by
  \[
    \int_S \|f(s)\|_{H^{\otimes q}}\|\ell(s)\|_{E'}\,\mathrm d\mu(s).
  \]
- The edge estimate splits parameter increments into the variation of the
  Hilbert kernel \(f_x-f_y\) and the variation of the dual test-functional
  \(\ell_x-\ell_y\).
- The application to \(E_r=C^r\) test functions records that point
  evaluations have bounded dual norm and that evaluation differences have
  Holder control in \(E_r'\).

## Calculation Check

- Extended `calculation-checks/constructive_scalar_spde_checks.py` with exact
  finite arithmetic for the projective base bound, the two edge-variation
  terms, and a sample evaluation-difference contribution.

## Remaining Issue #582 Obligations

- Use this criterion to prove the concrete projective tensor bounds for the
  BPHZ kernels of \(\Xi,X,X^2,X^3,XY,X^2Y\).
- Prove the scalar \(c_n\) coordinate kernel estimates.
- Extend the strict negative-sector estimates to the full solution sector.
- Complete the invariant-law and OS-reconstruction comparison.

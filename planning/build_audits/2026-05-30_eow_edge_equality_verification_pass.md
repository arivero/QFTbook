# 2026-05-30 EOW Edge-Equality Verification Pass

## Scope

This pass strengthens the distributional edge-of-the-wedge component of
issue #695 in Volume I, Chapter 11.  The several-complex-variables
edge-of-the-wedge theorem remains quoted analytic infrastructure, but the
QFT-specific verification of its real-edge equality hypothesis is now written
explicitly.

## Manuscript Change

- Expanded the paragraph following `thm:distributional-edge-of-the-wedge` so
  it records the analytic proof mechanism at the correct status level:
  polynomial tube bounds give distributional boundary values, equality on the
  real edge removes the boundary-value cocycle, and the holomorphic
  representative is obtained through edge-of-the-wedge exactness/envelope of
  holomorphy.
- Added a dedicated Wightman verification paragraph for adjacent labels
  `a,b`, defining the spacelike real open edge `O_ab`.
- Displayed the distributional equality
  `<W_{...ab...}-W_{...ba...},f>=0` for `f` supported in `O_ab`, derived by
  partitioning into product neighborhoods and applying scalar
  microcausality to the two spacelike separated smearings.
- Recorded the graded/Koszul variant without forcing the scalar chapter to
  change conventions.

## Issue Alignment

- #695: strengthens the OS/Wightman boundary-value component by proving the
  local QFT edge-equality input rather than leaving it as a compressed
  sentence.
- #691: avoids creating a new theorem/proposition wrapper for a local
  verification step; the result is integrated as proof infrastructure around
  the quoted analytic theorem.

## Remaining Proof Debt

This pass does not close #695.  The analytic edge-of-the-wedge theorem is
still quoted pure mathematics, and the issue also includes substantial
interacting AQFT examples and other foundational structural inputs.

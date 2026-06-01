# 2026-06-01 Anomaly Abelianized Descent-Coordinate Pass

Related issue: GitHub #696, anomaly proof debt in monograph conventions.

## Target

The previous #696 descent/WZW pass made clear that Bardeen counterterms move
representatives but leave the symmetric anomaly-polynomial coordinate fixed.
This continuation fills in the local calculation behind the coefficient
comparison used by the QCD Wess--Zumino--Witten level argument.

## Manuscript changes

- Volume II Chapter 20 now contains an explicit Abelianized descent coordinate:
  for commuting flavor backgrounds,
  \[
    I_5^{(0)}=C_{abc}A^aF^bF^c,\qquad
    \delta_\lambda I_5^{(0)}
      =d(C_{abc}\lambda^aF^bF^c).
  \]
- The same paragraph records the cubic polarization identity showing how the
  homogeneous cubic polynomial on commuting backgrounds recovers the symmetric
  trilinear anomaly coefficient.
- Volume II Chapter 21 now cross-links the WZW level comparison to this local
  descent coordinate, so the \(\operatorname{Tr}(\alpha\,dA\,dA)\) comparison
  is not presented as a low-order approximation or an arbitrary current
  convention.

## Calculation check

`calculation-checks/anomaly_matching_wzw_checks.py` now verifies, with exact
rational arithmetic, that the symmetric cubic coefficient is recovered by the
polarization identity used in the text.  The existing Bardeen-counterterm
symmetrization and WZW level checks remain unchanged.

## Scope boundary

This pass narrows the local descent/WZW matching part of #696.  It does not
prove the full APS, Bismut--Freed, Dai--Freed, or mod-two-index analytic
theorems, and it does not close #696.

# Quillen Spectral-Cut Determinant-Line Pass

Date: 2026-05-31

GitHub issue: #696, anomaly proof debt.

## Scope

Volume XII, Chapter 7 used the Quillen determinant line and the
Bismut--Freed connection in the global-anomaly discussion.  The surrounding
text had explained the holonomy boundary, but the spectral-cut construction of
the line bundle still compressed the finite transition map between local
charts.

## Change

Expanded the determinant-line transport section with the explicit spectral-cut
chart:

- for a cut \(a\notin\operatorname{Spec}(D_b^-D_b^+)\), define the low-mode
  spaces \(E_{<a}^\pm(b)\) and the local line
  \(L_a(b)=\det E_{<a}^+(b)\otimes\det E_{<a}^-(b)^*\);
- for two cuts \(a<c\), define the finite window \(E_{[a,c)}^\pm(b)\);
- show that \(D_b^+\) restricts to an isomorphism on that window and that
  \(\det D_{[a,c)}^+(b)\) is the transition element between determinant-line
  charts;
- state the refinement cocycle
  \(\det D_{[a,d)}^+=\det D_{[c,d)}^+\det D_{[a,c)}^+\).

This is the finite-dimensional algebra behind the Quillen gluing.  The
zeta-regularized high-mode determinant and heat-kernel counterterm remain the
infinite-dimensional analytic part attached to the Bismut--Freed theorem
boundary.

## Calculation Check

Extended `calculation-checks/eta_global_anomaly_checks.py` with an exact
rational finite-window determinant check verifying the spectral-cut transition
cocycle for several cuts and singular values.

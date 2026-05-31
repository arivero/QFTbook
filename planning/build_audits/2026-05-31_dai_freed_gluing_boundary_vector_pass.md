# 2026-05-31 Dai--Freed Gluing Boundary-Vector Pass

## Scope

This pass continues GitHub issue #696, the anomaly proof-debt lane.  The target
was Volume XII, Chapter 7, in the Dai--Freed inflow section.  Earlier passes
had defined determinant/Pfaffian lines, eta phases, groupoid descent, Quillen
spectral-cut charts, and a finite Pfaffian-orientation model.  The remaining
local gap in this section was that the sentence "changing the filling changes
the trivialization by the closed-manifold phase" was correct but compressed:
the reader needed to see the boundary vector and gluing mechanism explicitly.

## Edits

- Added a bounding-manifold normalization paragraph showing how APS gives
  \[
    \exp(2\pi i\,\xi(B_Y))
    =
    \exp\!\left(2\pi i\int_X \widehat A(TX)\operatorname{ch}(\widetilde E)\right)
  \]
  modulo the integer APS index whenever the closed odd-dimensional datum
  bounds.
- Added a boundary-vector paragraph: for an odd manifold \(Y\) with boundary
  \(M\), \(Z_{\rm DF}(Y)\) is a vector in the inverse boundary anomaly line
  \(L_M^{-1}\), not a number.
- Added the gluing identity
  \[
    \langle Z_{\rm DF}(Y_0),Z_{\rm DF}(Y_1)\rangle
    =
    Z_{\rm DF}(Y_0\cup_M(-Y_1)).
  \]
  The text explains that the right side is numerical because the boundary
  anomaly lines cancel under gluing.
- Extended `calculation-checks/eta_global_anomaly_checks.py` with finite
  \(U(1)\)-phase checks for gluing associativity and for the APS integer
  ambiguity in replacing the eta phase by a bounding local-index integral.
- Updated the Volume XII, Chapter 7 dossier.

## Boundary

This pass does not prove the analytic Dai--Freed theorem.  It narrows the QFT
logical gap by exposing the finite determinant-line algebra and the exact
place where the quoted APS/Bismut--Freed/Dai--Freed global-analysis
infrastructure enters.

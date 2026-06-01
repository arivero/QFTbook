# Anomaly Local Clifford Index-Coefficient Pass

## Scope

- GitHub issue context: #696, anomaly proof-debt in monograph conventions.
- Edited chapter:
  `monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`.

## Change

- Expanded the closed spin Dirac index theorem boundary with the local
  heat-kernel coefficient that the anomaly calculation actually uses.
- In normal coordinates and a local bundle trivialization, the gauge-curvature
  endomorphism is
  \[
    \mathcal E_F=\frac12\Gamma^{\mu\nu}F_{\mu\nu}.
  \]
- The first \(\Gamma_5\)-supertrace contribution in the diagonal heat
  parametrix is
  \[
    (4\pi t)^{-2}\frac{t^2}{2}
    \operatorname{tr}_{\rm spin,R}(\Gamma_5\mathcal E_F^2),
  \]
  and the Clifford trace
  \[
    \operatorname{tr}_{\rm spin}
    (\Gamma_5\Gamma^{\mu\nu}\Gamma^{\rho\sigma})
    =4\epsilon^{\mu\nu\rho\sigma}
  \]
  gives the displayed \(1/(32\pi^2)\) coefficient.
- The text still keeps the full Atiyah--Singer theorem as global-analysis
  input; this pass supplies the convention-sensitive local coefficient rather
  than pretending to prove the full index theorem.

## Calculation Check

- Extended `calculation-checks/anomaly_polynomial_descent_checks.py` with the
  exact rational identity
  \[
    (4\pi)^{-2}\cdot\frac12\cdot\left(\frac12\right)^2\cdot4
    =\frac1{32\pi^2}
  \]
  at the level of the coefficient multiplying
  \(\epsilon^{\mu\nu\rho\sigma}\operatorname{tr}_R(F_{\mu\nu}F_{\rho\sigma})\).

## Status

This narrows the local anomaly/index normalization boundary.  It does not
claim to prove the full closed Atiyah--Singer theorem, the APS theorem, or
the Bismut--Freed/mod-two-index global-analysis infrastructure.

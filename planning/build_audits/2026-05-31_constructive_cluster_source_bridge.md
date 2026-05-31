# 2026-05-31 Constructive Cluster Source Bridge

Scope: GitHub issue #703, constructive cluster-expansion absorption lane.

Changes:

- Expanded Volume XI, Chapter 2 at the transition from the abstract hard-core
  polymer gas to QFT Schwinger functions.
- Added the finite source deformation
  `K_lambda(X)=K(X) exp(sum_alpha lambda_alpha b_alpha(X))` and the connected
  source coefficient as a derivative of `log Z_Lambda(lambda)`.
- Wrote the explicit connected-cluster/source-assignment formula showing that
  nonzero connected source coefficients require a connected incompatibility
  graph meeting all source neighbourhoods.
- Explained finite-volume factorization when no incompatibility path connects
  source regions, and exponential decay when a connecting path has size
  proportional to cell distance.
- Extended `calculation-checks/constructive_scalar_spde_checks.py` with a
  finite hard-core polymer gas: disconnected source regions give zero mixed
  cumulant; inserting a bridge polymer gives the exact nonzero cumulant
  `385/312481`; removing the bridge restores zero.
- Updated the Volume XI Chapter 2 dossier, the calculation-check README, and
  the statmech crosswalk.

The pass deliberately avoids adding a new theorem-family wrapper.  The
load-bearing theorem remains the Kotecky--Preiss/Brydges--Kennedy convergence
criterion; this pass clarifies how its connected clusters become connected
Schwinger coefficients.

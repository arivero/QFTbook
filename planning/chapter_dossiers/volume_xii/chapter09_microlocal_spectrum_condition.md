# Chapter 09: Microlocal Spectrum Condition And Hadamard Geometry

## Source Position

Volume XII now inserts the microlocal analytic machinery underlying Hadamard
states, point splitting, time-ordered products, and locally covariant
renormalization.

## Notation Inventory

- `WF(u)`: wavefront set of a distribution.
- `P`: Klein-Gordon operator on a curved spacetime.
- `omega_2`: two-point function of a quasifree state.
- `sigma`, `sigma_epsilon`: half squared geodesic distance and its
  boundary-value prescription.
- `U`, `V`: Hadamard parametrix coefficients.
- `H_epsilon`: local Hadamard singular distribution.
- `p(x,k)`: principal symbol governing propagation of singularities.
- `Gamma_n(M)`: graph-defined microlocal spectrum cone for \(n\)-point
  distributions.
- `k^\sharp`: metric dual vector of a covector \(k\).

## Claim Ledger

- Defines wavefront set with the chart-level rapid-decay condition and proves
  the product criterion for distributions by the Fourier-convolution
  obstruction mechanism.
- States the microlocal Hadamard two-point condition with null-geodesic
  cotangent relation, including the mostly-plus future-covector convention
  and the sign of the second covector.
- Adds the higher microlocal spectrum cone \(\Gamma_n(M)\) and the
  all-\(n\)-point microlocal spectrum condition; records why quasifree
  Hadamard states satisfy it by Wick's theorem and the product criterion.
- Defines the local Hadamard parametrix and its geometric coefficients.
- Derives explicitly that the Hamiltonian flow of the Klein-Gordon principal
  symbol projects to affinely parametrized null geodesics and parallel
  transports the covector.
- Defines Wick products by point splitting and relates time-ordered products
  to local extensions across diagonals.

## Calculation Checks

- `calculation-checks/microlocal_spectrum_checks.py`: verifies the
  mostly-plus future-covector convention, the Klein-Gordon Hamilton flow sign,
  the two-point graph covector pattern \((p,-p)\), and the opposite-cone
  product obstruction.

## Figure Ledger

No figure is included in this pass.  Future figures should include
wavefront-set cones, null-geodesic cotangent transport, and configuration
space diagonals for time-ordered extensions.

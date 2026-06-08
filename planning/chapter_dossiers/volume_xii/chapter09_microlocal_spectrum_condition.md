# Chapter 09: Microlocal Spectrum Condition And Hadamard Geometry
Source-File: monograph/tex/volumes/volume_xii/chapter09_microlocal_spectrum_condition.tex

## Source Position

Volume XII now opens its printed order with the microlocal analytic machinery
underlying Hadamard states, point splitting, time-ordered products, and
locally covariant renormalization.  The following chapters consume named
results from this chapter: the product criterion, the microlocal Hadamard
two-point condition, the Hadamard parametrix recursion, and the diagonal
extension problem for Wick and time-ordered products.

## Notation Inventory

- `WF(u)`: wavefront set of a distribution.
- `P`: Klein-Gordon operator on a curved spacetime.
- `omega_2`: two-point function of a quasifree state.
- `sigma`, `sigma_epsilon`: half squared geodesic distance and its
  boundary-value prescription.
- `Delta`: van Vleck determinant.
- `U=Delta^{1/2}`: leading Hadamard coefficient.
- `V`, `v_j`: logarithmic Hadamard coefficient and its transport-recursion
  coefficients.
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
- Defines the local Hadamard parametrix and derives its geometric
  coefficients: the transport equation for `U=Delta^{1/2}`, the complete
  recursion for `v_j`, the coincidence value of `v_0`, and the diagonal
  recursion denominator `1/[2(j+1)(j+2)]`.
- Separates the metric characteristic Hamiltonian from the principal symbol of
  the chapter's Klein-Gordon operator `P_M=-nabla^mu nabla_mu+m^2+xi R`.
- Derives explicitly that the Hamiltonian flow of the Klein-Gordon principal
  symbol projects to affinely parametrized null geodesics and parallel
  transports the covector.
- Defines Wick products by point splitting and relates time-ordered products
  to local extensions across diagonals.
- Separates a generic smooth Hadamard-coordinate change \(H\mapsto H+w\),
  whose Wick-square shift is the smooth diagonal \(w(x,x)\), from the
  stricter local covariant finite Wick-prescription freedom
  \(c_1R+c_2m^2\) imposed only after covariance, scaling, and field-equation
  conditions are chosen.

## Calculation Checks

- `calculation-checks/microlocal_spectrum_checks.py`: verifies the
  mostly-plus future-covector convention, the Klein-Gordon Hamilton flow sign,
  the two-point graph covector pattern \((p,-p)\), the opposite-cone product
  obstruction, the diagonal coefficients in the four-dimensional Hadamard
  recursion, and the Wick-square distinction between a generic smooth
  Hadamard-coordinate diagonal and local covariant finite-renormalization
  freedom.

## Figure Ledger

No figure is included in this pass.  Future figures should include
wavefront-set cones, null-geodesic cotangent transport, and configuration
space diagonals for time-ordered extensions.

## Anti-Wrapper Audit

- 2026-06-08 issue #729 printed-order pass: moved this source file to the
  front of the printed Volume XII sequence so the microlocal product
  criterion, Hadamard wavefront condition, local parametrix recursion, and
  diagonal-extension problem are established before the chapters that consume
  them.  This is a dependency repair, not a new nonperturbative
  curved-spacetime QFT theorem.
- 2026-06-08 issue #855 regression pass: corrected the Wick-products section
  so it no longer identifies an arbitrary smooth Hadamard-coordinate diagonal
  with the local covariant \(c_1R+c_2m^2\) Wick-square freedom.  The canonical
  point-splitting and pAQFT chapters remain the detailed destinations for
  prescription changes and interacting Wick-polynomial transport.

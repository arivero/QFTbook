# Volume XI, Chapter 2 Dossier: Constructive Scalar Models And OS Data

## Logical Role

- Role in the monograph: begin detailed constructive examples with the scalar
  models that provide interacting OS/Wightman constructions.
- Immediate predecessor: constructive status catalog and construction routes.
- Immediate successor: lattice reflection positivity, stochastic
  quantization, and numerical methods.

## Definitions And Results

- Gaussian reference field with covariance \((-\Delta+m^2)^{-1}\).
- Wick powers as limits of smoothed Gaussian fields.
- Hermite-polynomial derivation of Wick coefficients.
- \(P(\phi)_2\) finite-volume Schwinger functions and finite-volume UV
  theorem.
- Negative Sobolev control norm for the \(P(\phi)_2\) stability estimate.
- Quoted Nelson--Glimm--Jaffe--Spencer/Guerra--Rosen--Simon stability theorem:
  \(V_{\varepsilon,\Lambda}\ge
  -A_\Lambda-B_\Lambda\|\phi\|_{H^{-s}}^\alpha\) with \(\alpha<2\), plus
  uniform exponential integrability of the finite-volume density.
- Polymer activity norm, hard-core Ursell coefficients, Penrose tree-graph
  inequality, Kotecky--Preiss/Brydges--Kennedy rooted-tree convergence
  criterion, and exponential clustering estimate.
- Hamiltonian number-operator bound role in the original \(\phi^4_2\)
  construction.
- \(\phi^4_d\) superficial-degree formula and explicit tadpole cutoff
  asymptotics.
- \(\Phi^4_3\) regulated action with local mass and vacuum-energy
  renormalizations.
- OS data output from constructive theorems.
- Comparison problem for cluster, stochastic, and rigorous-RG constructions.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(C\) | massive Euclidean covariance |
| \(\phi(f)\) | Gaussian generalized field smeared by \(f\) |
| \(C_\varepsilon(0)\) | regularized coincident covariance |
| \(V_\Lambda\) | finite-volume interaction |
| \(S_{\varepsilon,\Lambda}\) | regulated finite-volume action |
| \(\|\phi\|_{H^{-s}(\Lambda_1)}\) | negative Sobolev control norm used in the stability estimate |
| \(\alpha\) | subquadratic exponent in the \(P(\phi)_2\) stability bound |
| \(a_\varepsilon,b_\varepsilon\) | regulator-dependent local coefficients |
| \(K(X,\phi)\) | polymer activity on the polymer \(X\) |
| \(\kappa(X)\) | numerical majorant for the polymer activity after large-field weighting |
| \(\|K\|_{a,b}\) | schematic cluster norm with large-field weight |
| \(\varphi_{\mathrm c}(X_1,\ldots,X_n)\) | hard-core Ursell coefficient for the incompatibility graph |
| \(B_{R_0}\) | finite-range cell-neighbourhood constant for incompatible polymers |
| \(\omega_d\) | superficial degree of divergence |
| \(S_n\) | limiting Schwinger hierarchy |

## Claim Ledger

1. Wick powers are Gaussian \(L^p\) limits after smearing, and their
   coefficients are Hermite coefficients.
2. \(P(\phi)_2\) finite-volume UV limits follow from local integrability of
   logarithmic covariance powers, hypercontractivity, and the quoted
   stability theorem.  The proof now displays how the subquadratic Sobolev
   bound combines with Fernique and Holder estimates to give uniform
   integrability and convergence of normalized Schwinger functions.
3. Cluster expansion convergence follows from a polymer smallness criterion:
   the proof now displays the Penrose tree-graph inequality, the rooted-tree
   recursion \(F_{N+1}(X)\le\exp(\sum_{Y\nsim X}\kappa(Y)F_N(Y))\), and the
   leftover exponential-weight argument producing clustering.
4. Hamiltonian \(\phi^4_2\) construction rests on number-operator and
   relative-bound estimates, not on a formal interaction.
5. \(\Phi^4_3\) needs regulator-dependent local terms as part of the
   regulated action; the allowed terms follow from power counting.
6. Constructive \(\Phi^4_3\) theorems produce Schwinger functions satisfying
   the OS
   properties in the constructed regimes.
7. Constructive route comparison requires equality of Schwinger functions in
   a common topology, not merely matching labels.

## Figures

- Regulator-to-OS hierarchy construction diagram.
- Wick-ordering contraction diagram.
- Comparison triangle among cluster expansion, SPDE, and rigorous RG.

## Audit Notes

- 2026-05-25 issue #571 pass: the finite-volume \(P(\phi)_2\) ultraviolet
  theorem no longer hides the Glimm--Jaffe stability estimate inside one
  sentence.  The chapter now defines the negative Sobolev control norm, states
  the Nelson--Glimm--Jaffe--Spencer/Guerra--Rosen--Simon stability theorem as
  a `quotedtheorem`, explains why pointwise boundedness of \(P\) is not the
  proof, and displays the Fernique/Young/Holder argument that turns the
  stability bound into \(L^p\)-convergence of the finite-volume density and
  Schwinger functions.
- 2026-05-25 issue #572 pass: the Kotecky--Preiss cluster theorem no longer
  cites the tree-graph estimate as a black box.  The chapter defines the
  incompatibility majorants, states and proves the Penrose tree-graph bound,
  proves the rooted-tree recursion under an explicit
  \(B_{R_0}\epsilon\le a'\) smallness condition, and derives exponential
  clustering from the unused \(a-a'\) weight along paths connecting the two
  observable supports.

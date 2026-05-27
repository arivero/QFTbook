# Chapter 09: Anomalous and Topological Transport

## Source Position

Volume X now develops the nondissipative transport layer controlled by
anomalies, source protocols, equilibrium generating functionals, and Kubo
limits.

## Notation Inventory

- `W[g,A]`: equilibrium generating functional.
- `A_V`, `A_A`, `F_V`: vector and axial background sources and vector
  field strength.
- `T`, `u^mu`, `mu`: hydrodynamic temperature, velocity, and chemical
  potential.
- `mu_V`, `mu_A`, `mu_R`, `mu_L`: vector, axial, right-handed, and
  left-handed chemical potentials.
- `J^mu`, `T^mu nu`: current and stress tensor.
- `C`: anomaly coefficient in the displayed current convention.
- `Q=eq`: physical electromagnetic source charge, used when translating
  source-normalized response to electromagnetic response.
- `B^mu`, `omega^mu`: rest-frame magnetic field and vorticity.
- `xi_B`, `xi_omega`: chiral magnetic and vortical transport coefficients.
- `G^R_AB`: retarded correlator.
- `J_cons`, `J_cov`, `J_BZ`: consistent variational current, covariant
  current, and Bardeen--Zumino local current polynomial.
- `B_A^i`, `B_a^i`: spatial curls of the hydrostatic gauge source and
  Kaluza--Klein one-form in the three-dimensional equilibrium functional.

## Claim Ledger

- Defines anomalous transport through source variation and retarded
  correlators.
- States the four-dimensional `U(1)^3` anomaly equation in a declared
  convention.
- Defines the hydrostatic anomalous-source datum, separating chemical
  potentials for exactly conserved charges from background source parameters
  for anomalous currents.
- Defines consistent and covariant currents in the sign convention used for
  anomalous source variations, including the Bardeen--Zumino shift and its
  contact-term meaning.
- Gives a Kubo definition of the chiral magnetic coefficient with order of
  limits fixed.
- Derives parity-odd equilibrium response from Chern-Simons-type source terms.
- Proves the spatial variation formula for a general hydrostatic
  Chern--Simons functional
  `c_AA A dA + c_Aa A da + c_aa a da`, including the source and
  Kaluza--Klein curls.
- Derives the source-normalized chiral magnetic coefficient
  `J_V^i = mu_A B_V^i/(2 pi^2)` from the thermal reduction of the
  vector-vector-axial inflow term, and translates it to the physical
  electromagnetic current `J_em^i = e^2 q^2 mu_A B_em^i/(2 pi^2)`.
- Re-derives the same CME coefficient by lowest-Landau-level counting.
- Displays the Dirac chiral vortical coefficients
  `J_V|_omega = mu_V mu_A omega/pi^2` and
  `J_A|_omega = ((mu_V^2+mu_A^2)/(2 pi^2)+T^2/6) omega`, including the
  cancellation of the vector-current `T^2` term.
- Derives the entropy-current constraint and records the contact-term
  dependence of transport definitions.

## Calculation Checks

- `calculation-checks/anomalous_transport_checks.py` verifies the right/left
  Weyl sums for the CME and CVE coefficients, the equilibrium Chern-Simons
  variation coefficient, the general hydrostatic Chern-Simons variation
  algebra, and the physical electromagnetic charge factor.

## Figure Ledger

No figure is included in this pass.  Future figures should include source
variation diagrams, Kubo limit order, and equilibrium stationary-background
decomposition.

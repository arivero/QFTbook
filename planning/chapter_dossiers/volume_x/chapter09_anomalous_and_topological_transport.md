# Chapter 09: Anomalous and Topological Transport
Source-File: monograph/tex/volumes/volume_x/chapter09_anomalous_and_topological_transport.tex

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
  left-handed occupation parameters in Weyl-sum formulas.
- `a_0^5`: constant axial background source / thermal holonomy.
- `mu_5^occ`: prepared axial occupation imbalance `(mu_R - mu_L)/2`.
- `J^mu`, `T^mu nu`: current and stress tensor.
- `C`: anomaly coefficient in the displayed current convention.
- `Q=eq`: physical electromagnetic source charge, used when translating
  source-normalized response to electromagnetic response.
- `B^mu`, `omega^mu`: rest-frame magnetic field and vorticity.
- `xi_B`, `xi_omega`: chiral magnetic and vortical transport coefficients.
- `G^R_AB`: retarded correlator.
- `Gamma^ij`, `K_loc^ij`: response kernel and local
  Bardeen--Zumino/magnetization contact kernel used in the CME Kubo
  convention ledger.
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
- Gives a Kubo definition of the chiral magnetic coefficient with source
  action, Hamiltonian sign, response-kernel sign, local contact terms, and
  order of limits fixed.
- Derives parity-odd equilibrium response from Chern-Simons-type source terms.
- Proves the spatial variation formula for a general hydrostatic
  Chern--Simons functional
  `c_AA A dA + c_Aa A da + c_aa a da`, including the source and
  Kaluza--Klein curls.
- Chooses the prepared, slowly relaxing chiral imbalance as the primary CME
  protocol and defines the density matrix containing `mu_5^occ`.
- Separates the axial-source hydrostatic ledger from the occupation ledger:
  thermal reduction of the vector-vector-axial inflow term gives
  `W_3 = - beta a_0^5 A_V dA_V/(4 pi^2)`, hence the vector-preserving
  consistent source current `J_cons,V = -a_0^5 B_V/(2 pi^2)`.
- Derives the Bardeen--Zumino vector polynomial in the chapter convention,
  with `J_BZ,V = +a_0^5 B_V/(2 pi^2)` for the static source, so the
  source-only covariant vector current vanishes.
- Derives the prepared-imbalance local CME current by lowest-Landau-level
  counting:
  `J_occ,V^i = mu_5^occ B_V^i/(2 pi^2)`, with the combined convention ledger
  `J_cons,V = (mu_5^occ - a_0^5) B_V/(2 pi^2)` and
  `J_cov,V = mu_5^occ B_V/(2 pi^2)`.
- Translates the prepared-imbalance current to the physical electromagnetic
  current `J_em,occ^i = e^2 q^2 mu_5^occ B_em^i/(2 pi^2)`.
- Adds a compact protocol table comparing axial source, prepared imbalance,
  modified axial charge, and transport extraction, including source/gauge
  datum, density-matrix charge, current representative/Ward identity, and
  state status.
- Displays the Dirac chiral vortical coefficients
  `J_V|_omega = mu_V mu_A omega/pi^2` and
  `J_A|_omega = ((mu_V^2+mu_A^2)/(2 pi^2)+T^2/6) omega`, including the
  cancellation of the vector-current `T^2` term.
- Derives the entropy-current constraint and records the contact-term
  dependence of transport definitions.

## Calculation Checks

- `calculation-checks/anomalous_transport_checks.py` verifies the right/left
  Weyl sums for the CME and CVE coefficients, the equilibrium
  Chern-Simons variation coefficient with the thermal-circle normalization,
  the consistent/Bardeen--Zumino/covariant CME ledger for simultaneous
  occupation and axial-source data, the Kubo sign following from
  `H = H_0 - int A_i J^i`, the periodic cancellation of magnetization curls,
  the general hydrostatic Chern-Simons variation algebra, and the physical
  electromagnetic charge factor.

## Figure Ledger

No figure is included in this pass.  Future figures should include source
variation diagrams, Kubo limit order, and equilibrium stationary-background
decomposition.

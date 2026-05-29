# Chapter 07: Phases Of Gauge Theories

## Source Position

Volume IX has developed global forms, higher-form symmetries, line and
surface operators, confinement, screening, discrete theta terms, and anomaly
inflow.  This chapter synthesizes those structures into a precise
infinite-volume definition of gauge-theory phase data and explains how local
analyticity, static potentials, higher-form symmetry, screening, condensates,
and topological sectors fit together.

## Notation Inventory

- `A_Lambda`: finite-region gauge-invariant observable algebra.
- `A_obs`: declared quasi-local observable system.
- `omega`: thermodynamic-limit state on `A_obs`.
- `P`: parameter domain of couplings and topological terms.
- `W_R(C)`, `C_{T,L}`, `V_R(L)`: Wilson loop, rectangular contour, and static
  potential.
- `rho_{R,L}`: spectral measure for a static-source transfer-matrix sector.
- `sigma_gamma`, `mu_gamma`, `kappa_R`: area-law string tension, perimeter
  coefficient, and Coulomb coefficient.
- `A`, `Ahat`: finite one-form symmetry and its Pontryagin dual.
- `C`: finite center-sensitive dyonic charge group.
- `B`: finite Dirac pairing on `C`.
- `S`, `S_perp`: subgroup screened by dynamical finite-energy excitations and
  its finite-braiding orthogonal complement.
- `C_ext`, `C_top`: external-probe quotient `C/S` and residual topological
  charge group `S_perp/S` when the screened subgroup is isotropic.
- `K`, `K_perp`: condensed isotropic charge subgroup and its orthogonal
  complement.
- `G_R(gamma_xy)`, `rho_R(gamma)`: open gauge-invariant transporter
  correlator and Fredenhagen--Marcu type ratio.
- `Phi_IR`: map from microscopic topological extended operators to the
  long-distance topological sector.

## Claim Ledger

- Defines a phase only after specifying regulator class, parameter domain,
  observable system, limit prescription, and comparison topology.
- Defines phases as connected regions over which thermodynamic-limit states,
  local spectra, correlators, extended operators, symmetry realization, and
  topological sectors extend continuously.
- Derives finite-volume gauge averaging: gauge-variant local fields have zero
  expectation with gauge-invariant finite-volume boundary conditions.
- Defines static potentials from renormalized rectangular Wilson loops.
- Derives large-time extraction of the bottom static-source spectral energy
  from a positive transfer-matrix spectral measure.
- Defines area, perimeter, and Coulomb responses as asymptotic laws of
  renormalized line operators.
- States the one-form symmetry action on charged lines by linking with
  topological symmetry surfaces.
- Distinguishes external-probe screening quotient from the residual
  finite-braiding topological charge group on which the pairing descends.
- Defines isotropic condensate subgroup and orthogonal complement of
  unconfined finite charges.
- Proves the finite condensate confinement criterion under its stated
  long-distance condensate hypothesis.
- Formulates electric, magnetic, and oblique confinement as applications of
  the finite Dirac pairing.
- States and proves the gauge-Higgs analytic-corridor proposition for local
  gauge-invariant observables from uniform cluster expansion.
- Defines Fredenhagen--Marcu type ratios and proves their leading exponential
  scaling under assumed open-line and closed-loop asymptotics.
- Defines topological order/deconfined gauge theory data as an IR TQFT plus
  the map from microscopic extended operators.

## Calculation Checks

- `calculation-checks/gauge_phase_diagnostics_checks.py` verifies finite
  condensate orthogonality, electric/magnetic/dyonic confinement by the
  \(\mathbb Z_N\) Dirac pairing, tropical static-energy extraction, and
  Fredenhagen--Marcu exponent bookkeeping.

## Figure Ledger

No figure is included in this pass.  A later diagram may show the observable
dependency of phase diagnostics: local correlators, line asymptotics,
screening quotient, condensate subgroup, and topological sector.

## Audit Notes

- 2026-05-29 anti-wrapper pass: demoted finite-volume gauge averaging from
  proposition form to prose.  The calculation is the finite-regulator Haar
  projection; continuum phase claims remain tied to the phase datum and
  thermodynamic-limit hypotheses.

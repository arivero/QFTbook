# Chapter 12: QCD Phase Structure, Plasma, and Dense Matter

## Source Position

Volume X now includes a dedicated chapter for QCD phases rather than treating
them as a side remark inside screening.  The chapter follows KMS, Euclidean
thermal path integrals, Schwinger--Keldysh response, hydrodynamics, and
thermal gauge screening, and supplies the phase-structure bridge requested in
GitHub issue #628.

## Notation Inventory

- `N_c`, `N_f`: number of colors and Dirac fundamental quark flavors.
- `beta=1/T`, `mu_B`, `mu_q=mu_B/N_c`: inverse temperature, baryon chemical
  potential, and quark chemical potential.
- `Z_{a,V}`, `p(T,mu_B,m)`: finite-regulator thermal partition function and
  thermodynamic pressure.
- `P_R(x)`, `ell(T)`: normalized Polyakov loop and center order parameter.
- `Sigma(T)`, `rho(lambda)`: chiral condensate and thermodynamic Dirac
  eigenvalue density.
- `p_SB`, `Delta=epsilon-3p`: Stefan--Boltzmann pressure and trace anomaly.
- `g_3^2=g^2T`, `m_D`: static magnetic coupling and Debye mass.
- `Delta_L`, `Delta_R`: CFL pairing amplitudes.

## Claim Ledger

- Defines a QCD phase datum requiring pressure, exact symmetries, order
  parameters, limit prescriptions, and status labels.
- Defines center deconfinement in pure Yang--Mills by the Polyakov-loop order
  parameter with the correct source/infinite-volume limiting order.
- Proves that nonzero-\(N\)-ality Polyakov loops vanish at finite volume and
  zero center-breaking source.
- Separates center deconfinement from the zero-temperature Wilson-loop area
  law and from the crossover use of Polyakov loops with dynamical fundamental
  quarks.
- Defines the chiral condensate as a mass-source derivative and proves the
  Banks--Casher relation under an explicit spectral-density hypothesis.
- Derives the massless free QCD pressure at zero and nonzero baryon chemical
  potential.
- Records the HTL domain as a controlled approximation and proves the
  magnetic \(g^6T^4\) Linde scale by dimensional analysis of the static
  magnetic theory.
- Defines transport coefficients through Kubo spectral limits rather than
  phenomenological language.
- Proves the origin of the finite-density sign problem from loss of
  \(\gamma_5\)-Hermiticity at real chemical potential.
- Defines the CFL condensate datum and performs the physical Goldstone count.
- Separates Wilson-loop, Polyakov-loop, 't Hooft-loop, center-vortex, and
  dual-superconductor criteria for confinement.

## Figure Requirements

- Future figures should show the \((T,\mu_B)\) plane with only status-labeled
  regions, and a separate operator diagram distinguishing Wilson loops,
  Polyakov loops, and disorder lines.  No figure is included in this pass.

## Calculation Checks

- `calculation-checks/qcd_phase_checks.py`: exact finite checks for the
  Stefan--Boltzmann coefficients, baryon-chemical-potential coefficients,
  Banks--Casher kernel normalization, Linde magnetic-scale power counting,
  and CFL Goldstone count.

## Open Issues

- The chapter is a first dedicated Vol X response to #628.  It does not close
  the issue because a full unprecedented-depth treatment still needs
  dedicated derivations of Polyakov-loop effective potentials, stronger
  lattice-continuum status ledgers, and substantially more quantitative QGP
  and dense-QCD examples.

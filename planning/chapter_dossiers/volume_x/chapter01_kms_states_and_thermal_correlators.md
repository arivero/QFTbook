# Volume X, Chapter 1 Dossier: KMS States And Thermal Correlators

## Logical Role

- Role in the monograph: begin the thermal and hydrodynamic volume from
  equilibrium states as algebraic real-time objects, not from a finite-volume
  trace formula.
- Immediate predecessor: spectral theory, scattering, stress-tensor
  normalization, and local current material from earlier volumes.
- Immediate successor: finite-temperature path integrals and real-time
  Schwinger--Keldysh theory.

## Definitions And Results

- \(C^\ast\)-dynamical system, analytic element, and analytic core.
- Gaussian-smearing lemma proving norm-dense entire analytic elements.
- KMS state as a bounded strip-analytic boundary condition.
- Finite Gibbs trace proof of the KMS condition by explicit energy-basis
  calculation.
- Chemical-potential warning: the automorphism defining equilibrium must be
  declared.
- Fourier convention for thermal correlators.
- Thermal greater/lesser functions and finite-volume spectral detailed
  balance.
- Spectral distribution \(\rho=G^>-G^<\), reconstruction of \(G^\gtrless\)
  away from zero-frequency singular sectors, and bosonic
  fluctuation--dissipation.
- Linear response from first-order interaction-picture evolution.
- Retarded correlator, causal support, and
  \(\rho=-2\operatorname{Im}G^R\) sign convention.
- Conserved densities, homogeneous thermal one-point functions, hydrodynamic
  state-family input, derivative expansion, and shear Kubo formula.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\Obs\) | observable \(C^\ast\)-algebra |
| \(\alpha_t\) | strongly continuous time-evolution automorphism |
| \(\Obs_{\rm an}\) | norm-dense analytic core |
| \(\omega\) | state on \(\Obs\) |
| \(\beta\) | inverse temperature |
| \(S_\beta\) | KMS strip \(0<\operatorname{Im}z<\beta\) |
| \(F_{A,B}\) | KMS strip function |
| \(G^>,G^<\) | thermal Wightman functions |
| \(\rho_{AB}\) | thermal spectral distribution |
| \(G^R\) | retarded correlator |
| \(T^{\mu\nu}\), \(J_A^\mu\) | conserved stress tensor and currents |
| \(u^\mu,T,\mu_A\) | velocity, temperature, and chemical potentials |
| \(\varepsilon,p,n_A\) | energy density, pressure, and charge density |
| \(\eta_{\rm sh}\) | shear viscosity |

## Claim Ledger

1. Thermal equilibrium is a condition on a state and a declared time
   evolution.
2. Entire analytic elements are norm dense by Gaussian smearing.
3. Finite-volume Gibbs traces satisfy KMS by a direct energy-basis proof.
4. Detailed balance follows from KMS and is verified explicitly by
   finite-volume spectral sums.
5. The spectral density reconstructs greater/lesser functions only after
   zero-frequency singular sectors are separated.
6. Bosonic fluctuation--dissipation is an algebraic consequence of detailed
   balance.
7. Retarded response follows from the first-order source expansion and is
   causal by construction.
8. Transport coefficients are QFT correlator limits only when the relevant
   zero-frequency limits exist.
9. Hydrodynamic fields arise from conserved-density state families and
   constitutive relations, not from new microscopic local operators.

## Figures

- Figure `fig:kms-strip`: KMS strip with lower and upper boundary correlators.
- Figure `fig:retarded-support`: retarded support on the real-time axis.
- Figure `fig:thermal-hydrodynamic-variables`: flow from KMS QFT one-point
  data to hydrodynamic fields and constitutive relations.

## Calculation Checks

- `calculation-checks/kms_foundation_checks.py` verifies the finite
  Gibbs-trace KMS boundary condition, detailed balance, spectral
  reconstruction, bosonic fluctuation--dissipation, and the retarded-sign
  convention in the shear Kubo formula.

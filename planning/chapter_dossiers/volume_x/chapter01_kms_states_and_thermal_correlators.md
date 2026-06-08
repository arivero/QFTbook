# Volume X, Chapter 1 Dossier: KMS States And Thermal Correlators
Source-File: monograph/tex/volumes/volume_x/chapter01_kms_states_and_thermal_correlators.tex

## Logical Role

- Role in the monograph: begin the thermal and hydrodynamic volume from
  equilibrium states as algebraic real-time objects, not from a finite-volume
  trace formula.
- Cross-volume role: front-load the statistical-mechanics-to-QFT absorption
  route, separating finite identities and numerical evidence from continuum
  QFT claims until the observable map, limiting topology, positivity/locality
  conditions, and reconstruction or comparison target are declared.
- Immediate predecessor: spectral theory, scattering, stress-tensor
  normalization, and local current material from earlier volumes.
- Immediate successor: finite-temperature path integrals and real-time
  Schwinger--Keldysh theory.

## Definitions And Results

- \(C^\ast\)-dynamical system, analytic element, and analytic core.
- Gaussian-smearing lemma proving norm-dense entire analytic elements.
- Statistical-mechanics absorption route map across equilibrium KMS,
  Kubo/hydrodynamic response, nonequilibrium stochastic/SK representations,
  finite-locality/topological laboratories, and constructive/numerical
  continuum evidence.
- KMS state as a bounded strip-analytic boundary condition.
- Finite Gibbs trace proof of the KMS condition by explicit energy-basis
  calculation.
- Chemical-potential warning: the automorphism defining equilibrium must be
  declared.
- Fourier convention for thermal correlators.
- Thermal greater/lesser functions and finite-volume spectral detailed
  balance, with unsigned fermionic unordered functions obeying the ordinary
  Boltzmann ratio and the signed lesser/Euclidean antiperiodic conventions
  separated explicitly.
- Spectral distribution \(\rho=G^>-G^<\), reconstruction of \(G^\gtrless\)
  away from zero-frequency singular sectors, and bosonic
  fluctuation--dissipation.
- Linear response from first-order interaction-picture evolution.
- Retarded commutator correlator, source-response kernel
  \(K^R=-G^{R,\mathrm{comm}}\) for \(H-fB\), causal support, and
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
| \(G^{<}_{F,\mathrm{sgn}}\) | signed fermionic lesser convention, \(-G^<\) relative to the unsigned unordered function |
| \(\rho_{AB}\) | thermal spectral distribution |
| \(G^{R,\mathrm{comm}}\), \(G^R\) | commutator-retarded correlator; the shorter \(G^R\) is used when no source-sign ambiguity is present |
| \(K^R_{AB}\) | physical source-response kernel for \(H_f=H-fB\), equal to \(-G^{R,\mathrm{comm}}_{AB}\) |
| \(T^{\mu\nu}\), \(J_A^\mu\) | conserved stress tensor and currents |
| \(u^\mu,T,\mu_A\) | velocity, temperature, and chemical potentials |
| \(\varepsilon,p,n_A\) | energy density, pressure, and charge density |
| \(\eta_{\rm sh}\) | shear viscosity |

## Claim Ledger

1. Thermal equilibrium is a condition on a state and a declared time
   evolution.
2. Statistical-mechanics inputs become QFT claims only after observables,
   regulators, limits, topology, positivity/locality conditions, and a
   reconstruction or comparison framework are specified.
3. Entire analytic elements are norm dense by Gaussian smearing.
4. Finite-volume Gibbs traces satisfy KMS by a direct energy-basis proof.
5. Detailed balance follows from KMS and is verified explicitly by
   finite-volume spectral sums; no extra minus appears in the unsigned
   unordered fermionic lesser function.
6. The spectral density reconstructs greater/lesser functions only after
   zero-frequency singular sectors are separated.
7. Bosonic fluctuation--dissipation is an algebraic consequence of detailed
   balance.
8. Retarded response follows from the first-order source expansion and is
   causal by construction; for \(H_f=H-fB\) the response kernel is
   \(K^R=-G^{R,\mathrm{comm}}\).
9. Transport coefficients are QFT correlator limits only when the relevant
   zero-frequency limits exist.
10. Hydrodynamic fields arise from conserved-density state families and
   constitutive relations, not from new microscopic local operators.

## Figures

- Figure `fig:kms-strip`: KMS strip with lower and upper boundary correlators.
- Figure `fig:retarded-support`: retarded support on the real-time axis.
- Figure `fig:thermal-hydrodynamic-variables`: flow from KMS QFT one-point
  data to hydrodynamic fields and constitutive relations.

## Calculation Checks

- `calculation-checks/kms_foundation_checks.py` verifies the finite
  Gibbs-trace KMS boundary condition, detailed balance, spectral
  reconstruction, bosonic fluctuation--dissipation, the one-mode fermionic
  unsigned/signed lesser distinction and Euclidean antiperiodicity, the
  two-level source-impulse sign \(K^R=-G^{R,\mathrm{comm}}\), and the
  retarded-sign convention in the shear Kubo formula.

## Recent Architectural Passes

- 2026-06-03 issue #703 pass: added the opening statistical-mechanics
  absorption route map.  The map coordinates Volume X equilibrium, transport,
  hydrodynamic, and nonequilibrium chapters with Volume XI constructive,
  scaling-window, rigorous-RG, stochastic-quantization, and numerical-evidence
  chapters, and records the theorem-boundary rule that finite cells or
  numerical evidence do not become continuum QFT claims without declared
  limits, topology, locality/positivity, and reconstruction/comparison data.
- 2026-06-08 issue #882 convention re-audit: corrected the \(H-fB\)
  source-response sign, separated unsigned fermionic KMS from the signed lesser
  and Euclidean antiperiodic conventions, and added exact finite regressions.
  This is convention infrastructure for later physics-output derivations, not
  a standalone depth-pass-B advance.

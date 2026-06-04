# Volume VI, Chapter 5 Dossier: Thermodynamic Bethe Ansatz

## Logical Role

- Role in the monograph: derive thermodynamic and finite-size data from exact
  factorized scattering in massive two-dimensional integrable QFT.
- Immediate predecessor: form-factor bootstrap and local operators.
- Immediate successor: nested TBA, Baxter relations, and separation variables.

## Definitions And Results

- Defines the diagonal massive TBA datum
  `def:diagonal-massive-tba-datum`: species set, masses, diagonal scattering
  amplitudes and phase branches, logarithmic derivative kernel,
  quantization-shift convention, thermodynamic root-density statement,
  exclusion-statistics entropy convention, and thermal/mirror normalization.
- Bethe--Yang quantization on a circle.
- Particle and hole rapidity densities.
- Scattering kernel from the derivative of the phase shift.
- Entropy functional and constrained free energy.
- TBA pseudoenergy equation from variational stationarity.
- Finite-size ground-state energy by mirror-channel interpretation.
- Free Majorana ultraviolet computation giving \(c=1/2\).
- Scaling Lee--Yang interacting one-particle TBA computation giving
  \(c_{\rm eff}=2/5\) from the kernel integral, golden-ratio plateau, and
  Rogers dilogarithm.
- Status checkpoint from scattering data to TBA: the kernel identity is
  separated from finite-volume Bethe--Yang control, root-density convergence,
  microscopic Bethe-cell entropy, free-energy minimizer control, and the
  mirror-channel identification of finite-size ground-state energy.
- Euler-scale generalized-hydrodynamics bridge from local TBA root densities:
  filling functions, dressing equation, effective velocity, conditional
  root-density continuity equation, charge-current conservation check, and a
  hard-rod calibration of collision-shift kinematics.
- Weak-integrability-breaking kinetic-cell layer: finite Markov collision
  datum with detailed balance, exact preserved charges, projected occupation
  collision functional, entropy production identity, and the controlled
  kinetic scaling ansatz for perturbing an integrable QFT by a local operator.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(L\) | spatial circle circumference |
| \(R\) | inverse temperature or mirror circumference |
| \(\mathsf A\) | species set in the diagonal TBA datum |
| \(S_{ab}\) | diagonal two-body scattering phase |
| \(\delta_{ab}\) | phase shift |
| \(\rho_a,\rho_a^h\) | particle and hole rapidity densities |
| \(\epsilon_a\) | pseudoenergy |
| \(\varphi_{ab}\) | scattering kernel |
| \(S_{\rm LY},\varphi_{\rm LY}\) | Lee--Yang scalar amplitude and TBA kernel |
| \(Y_0,\phi_{\rm g},L(x)\) | Lee--Yang plateau value, golden ratio, and Rogers dilogarithm |
| \(n_a,\rho_a^t,h^{\rm dr},v_a^{\rm eff}\) | GHD filling, total state density, dressed one-particle function, and effective velocity |
| \(\Omega,\pi_\omega,k_{\omega\omega'},P_\omega,C_i\) | finite collision-cell states, stationary weights, transition rates, cell probabilities, and projected collision functional |

## Claim Ledger

1. The TBA equations are consequences of the named diagonal massive TBA
   datum, including the root-density statement and entropy convention.
2. Bethe--Yang quantization follows from taking one particle around the
   circle through all other particles.
3. The density equation is the derivative of the quantization condition.
4. The TBA equation is the Euler--Lagrange equation of constrained free
   energy.
5. The finite-size ground-state energy uses mirror-channel interpretation and
   requires model-specific finite-volume control.
6. The free Majorana example computes its ultraviolet central charge directly
   from a dominated-convergence limit.
7. The scaling Lee--Yang example computes the interacting ultraviolet
   effective central charge from an explicit kernel integral and the
   Rogers-dilogarithm value \(L(\phi_{\rm g}^{-2})=\pi^2/15\).
8. The generalized-hydrodynamics section treats Euler-scale GHD as a
   conditional closure datum: local Bethe root densities obey a continuity
   equation with velocity \(v^{\rm eff}=(E')^{\rm dr}/(p')^{\rm dr}\), and
   charge currents \(j_h=\int h\rho v^{\rm eff}\) conserve every declared
   Bethe charge whenever the closure holds.
9. The hard-rod calibration solves the finite collision-shift equations
   exactly, showing how a state-dependent effective velocity arises before
   the quantum kernel is introduced.
10. The weak-breaking kinetic section separates finite collision-cell
    identities from the unproved local-QFT kinetic limit: detailed balance
    gives relative-entropy decay, exact charges are preserved by the
    transition graph, and higher Bethe charges decay precisely when the
    perturbation permits transitions that change them.
11. The TBA status checkpoint prevents the Lee--Yang and free-Majorana
    computations from being overclaimed: they verify specific TBA kernels,
    plateau equations, and ultraviolet asymptotics, but do not by themselves
    derive the finite-volume spectrum of an arbitrary local Hamiltonian with
    the same proposed scattering phase.

## Calculation Checks

- `calculation-checks/lee_yang_tba_checks.py` verifies the Lee--Yang scalar
  amplitude, kernel integral, plateau equation, and Rogers-dilogarithm value.
- `calculation-checks/generalized_hydrodynamics_checks.py` verifies the
  finite-grid dressing equation, the current identity behind
  \(j_h=\int h\rho v^{\rm eff}\), and the hard-rod effective-velocity
  solution.
- `calculation-checks/weak_breaking_collision_cell_checks.py` verifies the
  finite detailed-balance algebra, projected conservation of energy, decay of
  a higher Bethe-type charge, and the symmetrized entropy-production formula.

## Audit Notes

- 2026-05-29 eighth anti-wrapper pass: retained the variational TBA statement
  as substantive but expanded the proof to include the admissible density
  variations, the hole-density variation, the kernel-transpose convention,
  and the cancellation that converts the stationary free energy to the
  one-particle state-density integral.
- 2026-05-30 issue #700 defining-property pass: added the upfront diagonal
  massive TBA datum so the Bethe--Yang, density, entropy, pseudoenergy, and
  mirror-energy formulae are derived from named constituent data.
- 2026-06-01 statmech crosswalk/#703 GHD pass: added the Euler-scale
  generalized-hydrodynamics bridge from local TBA density data, with dressing,
  effective velocity, charge-current conservation, hard-rod calibration, and
  paired finite algebra checks.
- 2026-06-01 statmech crosswalk/#703 weak-breaking pass: added the finite
  collision-cell datum and weak-integrability-breaking kinetic scaling layer,
  so the exact conservation and entropy statements are separated from the
  open microscopic derivation of the kinetic limit.
- 2026-06-03 reconstruction-spine point-of-use pass: added the TBA status
  checkpoint separating the on-shell scattering kernel from the finite-volume,
  thermodynamic-limit, entropy, variational, and mirror-identification inputs
  needed for theorem-level TBA.

## Figures

- Circle/worldline Bethe--Yang diagram may be added later.

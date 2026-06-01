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
- Euler-scale generalized-hydrodynamics bridge from local TBA root densities:
  filling functions, dressing equation, effective velocity, conditional
  root-density continuity equation, charge-current conservation check, and a
  hard-rod calibration of collision-shift kinematics.

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

## Calculation Checks

- `calculation-checks/lee_yang_tba_checks.py` verifies the Lee--Yang scalar
  amplitude, kernel integral, plateau equation, and Rogers-dilogarithm value.
- `calculation-checks/generalized_hydrodynamics_checks.py` verifies the
  finite-grid dressing equation, the current identity behind
  \(j_h=\int h\rho v^{\rm eff}\), and the hard-rod effective-velocity
  solution.

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

## Figures

- Circle/worldline Bethe--Yang diagram may be added later.

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

## Audit Notes

- 2026-05-29 eighth anti-wrapper pass: retained the variational TBA statement
  as substantive but expanded the proof to include the admissible density
  variations, the hole-density variation, the kernel-transpose convention,
  and the cancellation that converts the stationary free energy to the
  one-particle state-density integral.
- 2026-05-30 issue #700 defining-property pass: added the upfront diagonal
  massive TBA datum so the Bethe--Yang, density, entropy, pseudoenergy, and
  mirror-energy formulae are derived from named constituent data.

## Figures

- Circle/worldline Bethe--Yang diagram may be added later.

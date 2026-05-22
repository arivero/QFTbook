# 2026-05-22 Derivative Interactions, Measure, and Counterterms Pass

## Scope

- Compared the operational transcription for the first-sequence
  derivative-interaction block against the current Volume I path-integral
  chapter.
- Primary manuscript file:
  `monograph/tex/volumes/volume_i/chapter05_correlation_functions_wick_rotation_and_gaussian_integrals.tex`.
- Follow-up handwritten-PDF visual certification was completed on 2026-05-22.
  Source images `253a_trace-043.png` through `253a_trace-051.png` were
  compared against the rendered manuscript pages containing Section 8.8
  (physical PDF pages 63--65, printed pages 47--49).

## Source Substance Required

- Derivative-coupled oscillator
  \[
    L=\frac12\dot q^2-\frac12 q^2-\frac{g}{8}q^2\dot q^2 .
  \]
- Canonical momentum, Hamiltonian, and operator-ordering ambiguity.
- Classical coordinate check
  \(y=q-\frac{g}{24}q^3+O(g^2)\), giving an ordinary anharmonic oscillator
  through order \(g\).
- Euclidean interaction written as
  \(-\frac{g}{8}q^2(q')^2\), or equivalently
  \(\frac{g}{24}q^3q''\) up to endpoint terms.
- Wick contractions with derivatives on propagators, including the
  high-frequency divergent loop-derivative term, finite terms, and the
  parity-odd vanishing term.
- Frequency cutoff in the measure and the one-loop regulated self-energy
  \[
    \Sigma_\Lambda(k)
    =
    \frac{\hbar g}{4}
    \left(
      \frac{\Lambda}{\pi}+\frac{k^2}{2}-\frac12+O(\Lambda^{-1})
    \right)
    +O(\hbar^2g^2).
  \]
- Local counterterm
  \(\Delta L_E=Cg\hbar q^2/2\), with
  \(C=\Lambda/(4\pi)+C_{\mathrm{fin}}\).
- Pole/energy-gap interpretation of the finite counterterm part:
  \[
    \omega_1
    =
    1+\hbar g
    \left(
      \frac{C_{\mathrm{fin}}}{2}+\frac18
    \right)
    +O(g^2).
  \]

## Patch Made

- Added the classical \(q\mapsto y\) coordinate check before the Euclidean
  calculation.
- Added the finite and parity-odd contraction terms so the calculation is not
  reduced to a single divergent integral.
- Replaced the one-panel contraction sketch with a three-panel figure showing
  the divergent loop-derivative term, the finite wavefunction term, and the
  vanishing odd-loop term.
- Added explicit \(k\) and \(k'\) labels to the divergent contraction panel
  and recorded in the caption that the loop momentum is restricted by
  \(|k'|<\Lambda\) after cutoff regularization.
- Added text emphasizing that the divergent expression is not a value of an
  already-defined continuum measure; the regulated measure and local
  counterterms are part of the definition.
- Added the two-point-function pole calculation and explained how the finite
  counterterm part selects the quantum Hamiltonian represented by the
  regulated Lagrangian path integral.
- Added the physical-input statement for fixing \(C_{\mathrm{fin}}\), including
  the comparison between quantum-mechanical ordering data and the stronger
  relativistic constraints from Poincare covariance, locality/microcausality,
  internal symmetries, and normalization conditions.

## Visual Certification

- Rendered manuscript pages were inspected after the TeX patch. The
  derivative-contraction figure is legible and preserves the source distinction
  among the linearly divergent loop-derivative term, the finite wavefunction
  term, and the parity-odd vanishing term.
- The cutoff self-energy, counterterm, choice
  \(C=\Lambda/(4\pi)+C_{\mathrm{fin}}\), and pole formula are correctly placed
  after the figure and match the handwritten calculation.
- No handwritten page image is included in the manuscript; the source diagrams
  are rewritten as TeX/TikZ figures.

## Register Update

- Promoted 253a pp. 43--51 from `mapped after 2026-05-22
  source-transcription audit` to `certified after 2026-05-22
  derivative-interaction source/figure audit`.

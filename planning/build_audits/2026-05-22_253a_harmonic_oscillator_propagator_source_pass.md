# 2026-05-22 253a Harmonic-Oscillator Propagator Source Pass

## Scope

- Source block: handwritten 253a pp. 19--23.
- Manuscript home:
  `monograph/tex/volumes/volume_i/chapter05_correlation_functions_wick_rotation_and_gaussian_integrals.tex`.
- Dossier:
  `planning/chapter_dossiers/volume_i/chapter05_euclidean_correlators_gaussian_perturbation.md`.
- Coverage register:
  `planning/source_inventory/253a_253b_no_skip_coverage_register.md`.

## Source Checks

- Restored the finite-interval harmonic-oscillator setup with
  \(q(-T)=q(T)=0\).
- Checked the sine basis
  \(f_n(\tau)=T^{-1/2}\sin(n\pi(\tau+T)/(2T))\), its orthonormality, and the
  eigenvalue \((n\pi/(2T))^2\).
- Checked the diagonal Euclidean action and normalized Gaussian coefficient
  covariance.
- Added the explicit \(k_n=n\pi/(2T)\), \(\Delta k=\pi/(2T)\) passage from
  the coefficient sum to the line integral, with an Abel regulator named as
  part of the limiting operation.
- Restored the exponential decomposition of the sine product, including the
  endpoint image contribution
  \(-\hbar(2\omega)^{-1}e^{-\omega(\tau_1+\tau_2+2T)}\).
- Checked the contour argument against the handwritten pole diagram and
  recorded the suppression condition
  \(|e^{ik\tau}|=e^{-(\operatorname{Im} k)\tau}\) for \(\tau>0\).

## Render Checks

- Built `monograph/tex/main.pdf` with `tools/build_monograph.sh`.
- Rendered physical PDF pages 67--69 to
  `/tmp/qft_253a_019_023_cert2-067.png` through
  `/tmp/qft_253a_019_023_cert2-069.png`.
- Inspected the harmonic-oscillator path figure, the long exponential
  decomposition formula, the complex-\(k\) contour, and the final boxed
  propagator.  No formula overflow or figure collision was observed.

## Verification Commands

- `tools/build_monograph.sh`
- `git diff --check`

## Result

The 253a pp. 19--23 harmonic-oscillator Euclidean propagator block is marked
certified in the source coverage register.

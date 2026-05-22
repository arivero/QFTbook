# 2026-05-22 253a Gaussian Integrals Source Pass

## Scope

- Source block: handwritten 253a pp. 24--29.
- Manuscript home:
  `monograph/tex/volumes/volume_i/chapter05_correlation_functions_wick_rotation_and_gaussian_integrals.tex`.
- Dossier:
  `planning/chapter_dossiers/volume_i/chapter05_euclidean_correlators_gaussian_perturbation.md`.
- Coverage register:
  `planning/source_inventory/253a_253b_no_skip_coverage_register.md`.

## Source Checks

- Checked the finite \(N\)-dimensional Gaussian normalization
  \(Z_A[J]=(2\pi)^{N/2}(\det A)^{-1/2}\exp(\frac12 J_i(A^{-1})_{ij}J_j)\).
- Restored the source-derivative evaluation of
  \(\langle q_i\rangle_A\), \(\langle q_iq_j\rangle_A\), and
  \(\langle q_iq_jq_kq_\ell\rangle_A\).
- Restored the \(4!\)-assignment explanation for the four-point function and
  the grouping into the three inequivalent Wick pairings.
- Checked the Wick-pairing figure and the contraction value
  \((q_iq_j)_{\mathrm{contr}}=(A^{-1})_{ij}\).
- Checked the functional Gaussian setup:
  \(A=-\partial_\tau^2+\omega^2\), \(A^{-1}\) as the Green kernel, and
  \((-\partial_\tau^2+\omega^2)G(\tau,\tau')=\delta(\tau-\tau')\).
- Restored the functional integration-by-parts derivation of
  \(\langle q(\tau_1)q(\tau_2)\rangle_0=G(\tau_1,\tau_2)\), including
  \(\delta q(\tau_2)/\delta q(\tau')=\delta(\tau'-\tau_2)\).
- Checked the Fourier-space diagonalization and covariance
  \[
    \langle\widetilde q(k_1)\widetilde q(k_2)\rangle_0
    =
    \frac{2\pi\delta(k_1+k_2)}{k_1^2+\omega^2}.
  \]

## Render Checks

- Built `monograph/tex/main.pdf` with `tools/build_monograph.sh`.
- Rendered physical PDF pages 69--73 to
  `/tmp/qft_253a_024_029_cert-069.png` through
  `/tmp/qft_253a_024_029_cert-073.png`.
- Inspected the finite Gaussian derivative displays, Wick-pairing diagram,
  functional integration-by-parts identities, Fourier-space covariance, and
  transition into the anharmonic oscillator section.  No formula overflow,
  figure collision, or lost source step was observed after reflowing the one
  overfull paragraph caught by the build log.

## Verification Commands

- `tools/build_monograph.sh`
- `git diff --check`

## Result

The 253a pp. 24--29 finite and functional Gaussian integral block is marked
certified in the source coverage register.

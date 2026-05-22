# 2026-05-22 Scalar Path Integrals and Green Functions Source/Figure Audit

## Scope

- Source block: `references/253a lectures 2022.pdf`, pp. 72--79.
- Monograph target:
  `monograph/tex/volumes/volume_i/chapter08_scalar_path_integrals_and_euclidean_green_functions.tex`.
- Rendered PDF: `monograph/tex/main.pdf`, physical pages 79--84, printed
  pages 63--68.

## Source Trace Reviewed

Rendered handwritten source images:

- `monograph/tex/build/source_visual_trace/253a_trace-072.png`
- `monograph/tex/build/source_visual_trace/253a_trace-073.png`
- `monograph/tex/build/source_visual_trace/253a_trace-074.png`
- `monograph/tex/build/source_visual_trace/253a_trace-075.png`
- `monograph/tex/build/source_visual_trace/253a_trace-076.png`
- `monograph/tex/build/source_visual_trace/253a_trace-077.png`
- `monograph/tex/build/source_visual_trace/253a_trace-078.png`
- `monograph/tex/build/source_visual_trace/253a_trace-079.png`

## Content Checks

- The formal scalar-field path integral and fixed-endpoint transition kernel
  are represented with an explicit spatial regulator.
- The field-configuration wave functional and the functional delta
  representation of \(\ket{\varphi_i;t_i}\) have been included.
- Vacuum \(n\)-point functions are introduced as operator-valued
  distributions, with analytic continuation assumptions stated.
- The complex-time contour and imaginary-time ordering are transcribed into a
  TeX figure and accompanying assumptions.
- Euclidean field-insertion notation and the Euclidean functional integral are
  stated with the \(x^0=-i\tau\) convention.
- The uniform Wick rotation maintains imaginary-time ordering and gives the
  Lorentzian time-ordered correlator.
- The free Euclidean two-point function is derived as the inverse of
  \(-\partial_E^2+m^2\).
- The continuation of the free propagator includes the momentum-contour
  rotation, the orientation factor \(-i e^{i\alpha}\), the nonvanishing
  denominator for \(0<\alpha\le\pi/2\), and the \(i\epsilon\) prescription.
- Wightman, time-ordered, and Euclidean/Schwinger Green functions are all
  defined before the transition to the Kallen-Lehmann chapter.

## Figure/Render Checks

- Rendered pages inspected:
  `/tmp/qft_ch11_scalar_path_audit-079.png` through
  `/tmp/qft_ch11_scalar_path_audit-084.png`.
- The complex-time contour figure preserves the source ordering data:
  \(-\operatorname{Im}z^0\) is vertical, \(\operatorname{Re}z^0\) is
  horizontal, and the insertions are vertically ordered.
- The uniform Wick-rotation figure shows simultaneous rotation of all
  insertions while preserving the ordering.
- The \(k^0\)-plane figure was improved to show the real \(k^0\) contour,
  pole motion from the Euclidean positions, and the final Feynman pole
  displacement \(-\omega_{\vec k}+i0\), \(+\omega_{\vec k}-i0\).

## Build

- `tools/build_monograph.sh` completed successfully after the chapter edits.
- The strict text audit and build log scan were clean, apart from the
  pre-existing hyperref warning in a later chapter.

# Build Audit: Issue #305 Complex-Time Contour Status

Issue:

- GitHub #305: `[Vol V Ch 4] Contour path-integral formula: no regulator,
  no classification`.

Files changed:

- `monograph/tex/volumes/volume_iii/chapter04_radial_quantization_and_state_operator_correspondence.tex`
- `planning/chapter_dossiers/volume_iii/chapter04_radial_quantization_state_operator.md`

Resolution:

- Replaced the raw contour formula
  `\int[D\Phi]\exp(iS_C[\Phi])\prod_i\mathcal O_i(x_i)` by
  `def:cft-contour-path-integral-status`.
- The new definition specifies a finite spatial regulator \(\Lambda\), a
  finite subdivision \(P\) of the complex-time contour, the finite regulator
  configuration space \(\mathcal C_{\Lambda,P}\), and the time-sliced contour
  action \(S_{C,\Lambda,P}\).
- The finite-regulator density is classified: ordinary finite-dimensional
  measure for even variables, Berezin density for odd variables, and
  gauge-fixed/BV data for gauge fields.
- Lorentzian contour segments are tied explicitly to
  `def:lorentzian-oscillatory-path-integral` in Volume I: oscillatory
  integral/distribution, Abel or Fourier boundary value, or stationary-phase
  asymptotic expansion.
- The continuum contour bracket is defined as a constructed distributional
  boundary value when available, and otherwise as the formal perturbative
  asymptotic expansion derived from the same regulator data.

Verification:

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean full XeLaTeX build and log scan;
  generated `/Users/xiyin/QFT/monograph/tex/main.pdf`.

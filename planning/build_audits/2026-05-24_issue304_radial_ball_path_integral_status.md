# Build Audit: Issue #304 Radial Ball Path-Integral Status

Issue:

- GitHub #304: `[Vol V Ch 4] Radial-quantization path integral on ball:
  regulator + measure unspecified`.

Files changed:

- `monograph/tex/volumes/volume_iii/chapter04_radial_quantization_and_state_operator_correspondence.tex`
- `planning/chapter_dossiers/volume_iii/chapter04_radial_quantization_state_operator.md`
- `tools/audit_monograph_text.sh`

Resolution:

- Replaced the raw continuum ball formula using `[D\Phi]_{B_R}` by the
  radial-reconstruction definition of the origin-created state through
  reflection-positive Schwinger-distribution pairings.
- Added `def:regulated-ball-preparation`, which declares the regulator used
  for the Lagrangian representative: a finite radial time slicing on
  \(B_R\setminus B_\rho\) after the Weyl map to the cylinder, a finite angular
  spectral cutoff on \(S^{D-1}\), and a renormalized inner-cap representative
  of the inserted local operator.
- Defined the finite boundary configuration space, trace map
  \(\operatorname{Tr}_{\varepsilon,R}\), boundary measure/density
  \(d\lambda_{\varepsilon,R}^{\partial}\), conditional interior integral, and
  gluing pairing.  The text distinguishes ordinary finite-dimensional bosonic
  measures from Berezin densities and gauge-fixed/BV densities.
- Stated the continuum limit topology: radial Hilbert norm, or a specified
  distribution topology before Hilbert completion.
- Tightened the monograph text harness so a future raw `[D\Phi]_{B_R}` ball
  measure cannot re-enter the manuscript unnoticed.

Verification:

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean full XeLaTeX build and log scan;
  generated `/Users/xiyin/QFT/monograph/tex/main.pdf`.

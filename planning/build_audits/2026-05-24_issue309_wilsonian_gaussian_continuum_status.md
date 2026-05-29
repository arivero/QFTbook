# Build Audit: Issue #309 Wilsonian Gaussian Continuum Status

Issue:

- GitHub #309: `[Vol III Ch 7] Wilsonian Gaussian measure: finite-dim theorem
  extended to continuum without naming the gap`.

Files changed:

- `monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex`
- `planning/chapter_dossiers/volume_ii/chapter17_wilsonian_effective_actions_polchinski_flow.md`

Resolution:

- Added the finite-regulator Gaussian pushforward calculation, a finite-regulator
  measure identity for Gaussian pushforward on finite-dimensional mode spaces.
- Verified the calculation by characteristic functions of independent Gaussian
  random variables with covariances \(C_{\Lambda'}\) and
  \(\widehat C_{\Lambda,\Lambda'}\).
- Added `hyp:wilsonian-pushforward-continuum-interpretation`, which separates
  the nonperturbative continuum interpretation into two additional convergence
  claims: convergence of the interacting source functionals and convergence of
  the Wilsonian pushforward or infinitesimal Wilson-Polchinski vector field in
  a specified topology.
- Updated the shell-integration paragraph so the finite-regulator equality is
  explicitly attributed to the theorem, while the continuum interpretation is
  explicitly attributed to the separate hypothesis.

Verification:

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean full XeLaTeX build and log scan;
  generated `/Users/xiyin/QFT/monograph/tex/main.pdf`.

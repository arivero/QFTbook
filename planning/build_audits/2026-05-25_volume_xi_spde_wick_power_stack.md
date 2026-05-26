# Volume XI Singular-SPDE Wick-Power Stack Audit

## Scope

This pass advances the self-contained proof-stack issue for Volume XI,
Chapter 9 by proving the first elementary stochastic-analysis components
inside the chapter: the stationary stochastic convolution, its covariance
normalization, two-dimensional Wick-power convergence, and heat-kernel
smoothing.

## Edits

- Updated
  `monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`.
- Added a Fourier-mode construction of the stationary linear SPDE on
  \(\mathbb T^2\), with noise covariance
  \(\mathbb E[\xi(\tau,x)\xi(\tau',y)]=2\delta(\tau-\tau')\delta(x-y)\).
- Proved that the stationary covariance is \((-\Delta+m^2)^{-1}\) and that
  the stochastic convolution belongs to \(H^{-s}\) for every \(s>0\) in two
  dimensions.
- Proved convergence of smeared Wick powers of the two-dimensional
  stochastic convolution, and an elementary
  \(L^2(\Omega;H^{-s})\), \(s>1\), convergence theorem.
- Added a Fourier heat-kernel smoothing estimate and connected it to the
  sharper Besov--Holder Schauder estimates used in the
  Da Prato--Debussche fixed point.
- Extended `calculation-checks/constructive_scalar_spde_checks.py` to verify
  the OU variance normalization, the two Sobolev threshold inequalities, and
  the heat-kernel optimization behind the smoothing estimate.
- Updated `calculation-checks/README.md` and the Volume XI Chapter 9 dossier.

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed; the generated
  `monograph/tex/main.pdf` has 1335 pages.

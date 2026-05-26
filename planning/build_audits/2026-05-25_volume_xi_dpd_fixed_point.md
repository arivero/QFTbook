# 2026-05-25 Volume XI DPD Fixed-Point Proof Pass

## Scope

This pass develops the deterministic local fixed-point layer of the
Da Prato--Debussche construction in
`monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`.
The sharper global Besov/Holder theorem remains quoted, but the monograph now
proves the Sobolev version that explains the mechanism without importing the
core contraction argument.

## Edits

- Added a Littlewood--Paley/Bony product lemma proving
  \(H^\beta H^\beta\subset H^\beta\) and
  \(H^\beta H^{-\kappa}\subset H^{-\kappa}\) for
  \(0<\kappa<1/4\), \(\beta=1+2\kappa\), on \(\mathbb T^2\).
- Added a two-dimensional lattice convolution bound for powers of the
  massive propagator and used it to sharpen the Wick-power Sobolev
  convergence theorem from \(H^{-s}\), \(s>1\), to every \(s>0\).
- Defined the DPD nonlinearity
  \(\mathcal N(Y,\mathbb X)=Y^3+3Y^2X+3YX^{(2)}+X^{(3)}\) and proved its
  local Lipschitz bound from the product estimates.
- Added a deterministic mild fixed-point theorem for the DPD remainder
  equation with enhanced noise in \(C([0,T];H^{-\kappa})^3\).
- Derived the heat-smoothing Duhamel gain
  \(T^{1-\theta}\), \(\theta=(1+3\kappa)/2<1\), and used it to construct the
  contraction.
- Extended `calculation-checks/constructive_scalar_spde_checks.py` to verify
  the exponent inequalities used by the product and smoothing estimates.
- Updated the chapter dossier and calculation-check index.

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed with clean final log scan.
- `pdfinfo monograph/tex/main.pdf` reports 1338 pages.

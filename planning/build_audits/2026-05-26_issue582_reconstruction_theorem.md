# Issue #582 Compact Reconstruction Theorem Pass

## Scope

- GitHub issue: `#582`.
- Manuscript locus:
  `monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`.
- Calculation-check locus:
  `calculation-checks/constructive_scalar_spde_checks.py`.

## Content Added

- Replaced the earlier reconstruction-theorem boundary with a compact
  finite-sector theorem suited to the local regularity structures appearing
  in dynamic \(\Phi^4_3\).
- Defined the parabolic scaling \(\mathfrak s=(2,1,\ldots,1)\), the scaled
  test functions \(\varphi_z^\delta\), the model seminorms for \(\Pi\) and
  \(\Gamma\), and the modelled-distribution norm for \(F\).
- Proved the coherence estimate for the local germ
  \(\zeta_z=\Pi_zF(z)\):
  \[
    |\langle\zeta_z-\zeta_{z'},\varphi_z^\delta\rangle|
    \le C\,\delta^\gamma
  \]
  whenever \(\|z-z'\|_{\mathfrak s}\le\delta\).
- Constructed the reconstructed distribution \(\mathcal RF\) by dyadic
  parabolic wavelet coefficients and proved convergence of the defining
  series from the inequality \(r>-\min A_{<\gamma}\).
- Proved the local reconstruction estimate by separating coarse scales
  \(\ell\ge\delta\) and fine scales \(\ell<\delta\).  The coarse sum uses
  \(r>\gamma\) to bound
  \(\sum_{\ell\ge\delta}\delta^r\ell^{\gamma-r}\), while the fine sum uses
  \(\alpha+r>0\) to bound
  \(\sum_{\ell<\delta}\delta^{\gamma-\alpha-r}\ell^{\alpha+r}\).
- Added the scaling-function block to the proof, with the condition
  \(\gamma<|\mathfrak s|\).
- Added calculation checks for the reconstruction exponent arithmetic.

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed.
- Independent log scan passed:
  `rg -n "LaTeX Warning: Reference|LaTeX Warning: Citation|Latex failed to resolve|Undefined control sequence|Overfull|Underfull|Fatal error|Emergency stop|Missing .* inserted|Token not allowed" monograph/tex/main.log monograph/tex/build/latexmk.out`
  returned no matches after the reference-stabilizing no-op build pass.
- `pdfinfo monograph/tex/main.pdf` reports `Pages: 1455`.

## Issue Status

This pass advances issue `#582` but does not close it.  Remaining components
include construction and convergence of the BPHZ-renormalized random model
for dynamic \(\Phi^4_3\), the nonlinear modelled-distribution fixed point,
local counterterm identification in the concrete cutoff equation, and the
SPDE-to-OS passage.

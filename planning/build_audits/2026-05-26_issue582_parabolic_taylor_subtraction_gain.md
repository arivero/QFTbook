# Issue #582 Parabolic Taylor-Subtraction Gain Pass

## Manuscript Scope

- `monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`

## Development

- Added the estimate `eq:spde-taylor-subtraction-gain`.
- The estimate states the exact scale gain from pairing an order-\(a\) dyadic
  kernel with a local Taylor remainder bounded by \(H\|h\|_{\mathfrak s}^r\).
- The calculation is a direct \(L^1\)-kernel estimate on the support
  \(B_{\mathfrak s}(0,A2^{-i})\), giving the improved scale
  \(2^{-(a+r)i}\).
- The surrounding text separates this local gain from the remaining BPHZ
  forest bookkeeping and from the dyadic convolution estimate already proved.

## Calculation Check

- Extended `calculation-checks/constructive_scalar_spde_checks.py` with exact
  arithmetic for a sample \(a=2\), \(r=3\), \(i=4\) Taylor-subtraction gain.

## Remaining Proof Obligations

- Specify and estimate the full BPHZ forest formula for the dynamic
  \(\Phi^4_3\) negative trees, including overlapping subgraphs and the
  conversion of local Taylor gains into compact model-seminorm bounds.

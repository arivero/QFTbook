# Issue #582 Dyadic Parabolic Convolution Bound Pass

## Manuscript Scope

- `monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`

## Development

- Added Proposition `prop:spde-dyadic-parabolic-convolution-bound`.
- The proposition states a deterministic parabolic convolution estimate for
  dyadic kernels of orders \(a\) and \(b\) on a space of homogeneous
  dimension \(Q\).
- The proof derives the support bound, the pointwise convolution estimate,
  the two geometric scale sums with \(\min(i,j)=k\), and the resulting
  \(L^\infty\) and \(L^1\) output bounds.
- The surrounding text identifies this as the unsubtracted kernel estimate
  onto which BPHZ Taylor-subtraction gains must later be attached.

## Calculation Check

- Extended `calculation-checks/constructive_scalar_spde_checks.py` with exact
  arithmetic for a sample \(Q=5\), \(a=2\), \(b=1\) convolution: the
  \(L^\infty\) exponent, the \(L^1\) exponent, the two geometric factors, and
  the finite sample bound.

## Remaining Proof Obligations

- Prove Taylor-subtraction scale gains for local BPHZ subgraphs.
- Apply the dyadic kernel estimate and the subtraction gains to the negative
  dynamic \(\Phi^4_3\) trees, including base-point, test-function, and scale
  regularity needed for the full model seminorm.

# Issue #582 Wiener-Chaos Moment Bound Pass

## Manuscript Scope

- `monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`

## Development

- Added Lemma `lem:spde-finite-wiener-chaos-moment-bound`.
- The lemma defines an isonormal Gaussian process, the Wick multiple integral
  \(I_q(f)\), derives the \(q!\) chaos isometry from the Wick exponential
  generating function, and bounds even moments by finite Wick-pairing
  combinatorics.
- Added the kernel-to-moment calculation for finite chaos coordinates.
- The calculation turns deterministic Hilbert-kernel bounds for finite chaos
  expansions into pointwise stochastic moment bounds and dyadic increment
  bounds for model coordinates.
- The surrounding text now separates the stochastic chaos estimate from the
  remaining deterministic kernel estimates and spatial/scale net estimates
  needed for the full BPHZ model seminorm.

## Calculation Check

- Extended `calculation-checks/constructive_scalar_spde_checks.py` with exact
  Gaussian polynomial checks for the second and third chaos isometry, the
  fourth moment of the second Hermite chaos, and a sample finite-chaos
  coordinate-moment constant.

## Remaining Proof Obligations

- Prove the deterministic BPHZ kernel estimates for every negative tree in
  dynamic \(\Phi^4_3\), including forest-subtracted power counting and
  regularity in the base point, scale, and test function.
- Convert pointwise coordinate moments into the full compact model seminorms
  used by Theorem `thm:spde-random-model-cauchy-criterion`.

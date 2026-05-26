# Issue #582 Random-Model Convergence Criterion Pass

## Manuscript Scope

- `monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`

## Development

- Added Theorem `thm:spde-random-model-cauchy-criterion`, a finite-sector
  dyadic Cauchy criterion for random models.
- The theorem assumes uniform \(L^p\) bounds on the analytic model seminorm
  and exponentially decaying \(L^p\) bounds on successive cutoff increments.
- The proof constructs the limiting model, passes the model identities to the
  limit, obtains the limiting analytic bound by Fatou's lemma, proves an
  explicit \(L^p\) geometric tail, and derives the almost-sure dyadic rate by
  Markov and Borel-Cantelli.
- The BPHZ theorem-boundary language was tightened: the remaining concrete
  task is now the proof of the uniform model moment bounds and dyadic Cauchy
  estimates needed by the criterion, not an unspecified convergence claim.

## Calculation Check

- Extended `calculation-checks/constructive_scalar_spde_checks.py` with exact
  arithmetic for the Markov/Borel-Cantelli exponent and the dyadic geometric
  tail used in the random-model convergence theorem.

## Remaining Proof Obligations

- Prove the actual BPHZ model estimates for the dynamic \(\Phi^4_3\) trees:
  kernel bounds after forest subtraction, uniform model moments, dyadic Cauchy
  estimates, and compatibility with the Schauder/product hypotheses of the
  modelled-distribution fixed point theorem.
- Prove the SPDE-to-OS passage for stationary solutions in the same regulator
  and local-coordinate chart as the constructive Euclidean measure.

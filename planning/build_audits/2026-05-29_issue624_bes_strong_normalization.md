# Issue #624: Strong BES Normalization Pass

## Scope

This pass replaces the one-line strong-coupling BES status statement in
Volume VII, Chapter 13 by a status-labeled theorem/proposition pair.  The
analytic strong-coupling solution of the BES equation remains quoted as a
theorem about the BES Riemann-Hilbert problem; the conversion to the
monograph's large-spin scaling-function normalization is derived explicitly.

## Manuscript Changes

- Added Quoted Theorem `qt:planar-n4-bes-strong-solution`, defining the
  conventional BES cusp function `Gamma_BES(g)=4g^2+...`, the Dirichlet beta
  values, Catalan's constant, and the shifted strong variable
  `g_s=g-3 log(2)/(4 pi)`.
- Stated the strong expansion

  `Gamma_BES(g)=2 g_s [1-c_2/g_s^2-c_3/g_s^3
  -(c_4+2 c_2^2)/g_s^4+O(g_s^-5)]`.

- Added Proposition `prop:planar-n4-bes-strong-monograph-normalization`,
  proving that the monograph normalization `f(g)=2 Gamma_BES(g)` gives

  `f(g)=4g_s-4c_2/g_s-4c_3/g_s^2
  -4(c_4+2c_2^2)/g_s^3+O(g_s^-4)`,

  hence

  `f(g)=4g-3 log(2)/pi-K/(4 pi^2 g)+O(g^-2)`.

## Calculation Check

- Added `check_bes_strong_scaling_function_normalization()` to
  `calculation-checks/planar_n4_integrability_checks.py`.
- The check verifies:
  - the weak-normalization comparison `f=2 Gamma_BES`;
  - the shift identity `4c_1=3 log(2)/pi`;
  - the Catalan coefficient `-K/(4 pi^2 g_s)`;
  - the shifted `zeta(3)`, `beta_D(4)`, and `K^2` coefficients.

## Source Note

The local reference copy used for coefficient verification is
`references/planar_n4_integrability/basso_korchemsky_kotanski_strong_cusp_0708.3933.pdf`
with extracted source in
`references/planar_n4_integrability/0708.3933_source/RevisedBKK.tex`.
The `references/` folder is not pushed.

## Remaining Issue #624 Items

This closes the immediate "strong BES beyond status line" weakness at the
level of coefficient statement and normalization conversion.  Remaining core
items are classical finite-gap / algebraic curve, Pohlmeyer reduction,
TBA-to-QSC equivalence, and any later attempt to replace the quoted BES
Riemann-Hilbert theorem by a fully self-contained derivation inside the
monograph.

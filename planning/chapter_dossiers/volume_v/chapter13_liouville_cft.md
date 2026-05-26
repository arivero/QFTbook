# Chapter 13: Liouville Conformal Field Theory

## Source Position

This chapter addresses issue #601 / Block R.  The conceptual spine is the
stringbook 2D CFT appendix material on Weyl anomaly, Liouville action,
Virasoro Ward identities, BPZ equations, and sewing; the monograph version
expands this into explicit definitions, convention checks, and theorem
boundaries rather than importing the appendix exposition.

## Notation Inventory

- `Sigma`: oriented closed smooth surface.
- `g`: Riemannian metric on `Sigma`.
- `phi`: real scalar field; classically smooth, quantum mechanically a
  distribution/GFF coordinate.
- `b`: Liouville coupling, positive.
- `Q`: background charge, `Q=b+b^{-1}` in the conformal normalization.
- `mu`: positive cosmological constant multiplying the exponential
  interaction.
- `V_alpha`: normal-ordered exponential `:exp(2 alpha phi):`.
- `P`: nonnegative Liouville scattering momentum, with
  `alpha=Q/2+iP`.
- `S(P)`: reflection phase in the cylinder scattering normalization.
- `h_alpha`: Liouville conformal weight `alpha(Q-alpha)`.
- `h_i`: external chiral conformal weights in a four-point Virasoro block.
- `h`: internal chiral conformal weight in a Virasoro Verma module.
- `G_2`: level-two Virasoro Gram/Shapovalov matrix in the
  `(L_-2|h>, L_-1^2|h>)` basis.
- `f_1`, `f_2`: first two normalized Virasoro four-point block
  coefficients in the `z`-channel expansion.
- `q(z)`: elliptic nome of the four-punctured sphere.
- `lambda(q)`: modular lambda function `theta_2(q)^4/theta_3(q)^4`.
- `g_1`, `g_2`: first two raw elliptic-coordinate block coefficients after
  substituting `z=lambda(q)`.
- `H(c,h_i,h;q)`: Zamolodchikov elliptic block after universal prefactors
  are removed.
- `Upsilon_b`: entire special function entering the DOZZ constant.
- `F_P`: Virasoro conformal block with internal Liouville momentum `P`.
- `M_{gamma,g}`: Gaussian multiplicative-chaos measure in probabilistic
  normalization.

## Claim Ledger

- Defines the classical Liouville action with metric, curvature term,
  exponential potential, and all parameters typed.
- Derives the Euler-Lagrange equation including the curvature and potential
  coefficients.
- Fixes the free-field OPE normalization and derives the improved stress
  tensor central charge `c=1+6Q^2`.
- Derives the exponential conformal weight `h_alpha=alpha(Q-alpha)` and the
  marginality condition `Q=b+b^{-1}` for the Liouville potential.
- Defines the Seiberg domain and checks the zero-mode integrability
  inequality.
- Defines the GMC measure used in the probabilistic construction and states
  the GKRV probabilistic construction as a `quotedtheorem`.
- Defines the reflection relation as a meromorphic identification of
  correlation functions.
- Adds the canonical asymptotic scattering basis on the cylinder and the
  delta-normalized primary `V_P`.
- States the continuous Liouville four-point conformal-block decomposition as
  a direct integral over `P in [0,infty)`.
- Defines normalized ordinary Virasoro four-point blocks with explicit
  nondegeneracy hypotheses through level two and derives `f_1` and `f_2`
  from the level-one and level-two Gram matrices.
- Records where the Gram-matrix formula fails without modification:
  degenerate Kac-determinant parameters require null quotients,
  meromorphic limits, or logarithmic extensions.
- Defines the elliptic nome \(q(z)\), the modular lambda expansion
  `lambda(q)=16q-128q^2+704q^3+O(q^4)`, and derives the first conversion from
  `z`-block coefficients `f_1,f_2` to raw elliptic coefficients `g_1,g_2`.
- States Zamolodchikov's elliptic recursion as a theorem boundary with
  explicit pole locations \(h_{m,n}\) and identifies the residue-products
  whose normalization must be synchronized with the DOZZ and chiral-block
  conventions.
- Defines `Upsilon_b`, states the DOZZ formula as a `quotedtheorem`, and names
  the proof boundary.
- Derives the scattering-normalized `P`-basis DOZZ representative from the
  conventional `alpha`-basis formula and records the external-leg phase
  convention.
- Proves the level-two null-vector coefficient for `alpha=-b/2` and derives
  the corresponding BPZ differential equation.
- Derives the degenerate OPE coefficient `C_-(alpha)` from the local
  one-screening Coulomb-gas integral, including the Dotsenko-Fateev
  meromorphic-continuation boundary and the gamma-function rewrites matching
  the chapter convention.
- Reduces the four-point function with one `V_{-b/2}` insertion to
  hypergeometric blocks, identifies the two local fusion exponents, and
  derives the explicit gamma-product DOZZ `b`-shift ratio from the
  `Upsilon_b` shift relation.
- Displays the Gauss hypergeometric connection formula used in the BPZ
  crossing argument, verifies the `z=1` fusion exponents, and states the
  genericity/meromorphic-continuation boundary for resonant parameters.
- Records an open problem for functorial/sewing closure and cross-links the
  Kontsevich-Segal ledger.

## Figure Ledger

- No figures added in the initial issue #601 pass.  Future additions should
  prioritize concrete sewing geometry, BPZ fusion channels, and momentum
  contour data only after the corresponding derivations are developed.

## Calculation Checks

- `calculation-checks/liouville_bpz_checks.py` verifies the fragile
  Virasoro arithmetic for the level-two null vector
  `(L_{-1}^2+b^2 L_{-2})|h>` at `h=-1/2-3b^2/4` and
  `c=1+6(b+b^{-1})^2`.
- The same script checks the formal `b`-power bookkeeping in the explicit
  DOZZ `b`-shift ratio, including the cancellation of all external-momentum
  powers and the final `b^{-4}` factor.
- The same script verifies the one-screening OPE power, the three
  Dotsenko-Fateev beta-integral gamma arguments, and the gamma-function
  rewrites of the meromorphic `C_-(alpha)` coefficient.
- The same script now also checks the affine parameter algebra in the
  hypergeometric connection matrix: the `z=1` exponent gap and the gamma
  arguments `C-A`, `C-B`, and `A+B-C`.
- The same script checks the level-two Virasoro Gram determinant, the
  level-one and level-two ordinary block coefficients, and the large-`c`
  global-block limit in exact rational arithmetic.
- The same script checks the modular-lambda expansion through
  `lambda(q)=16q(1-8q+44q^2+O(q^3))` and verifies the exact formulas for the
  raw elliptic \(q\)-coefficients `g_1` and `g_2`.

## Remaining Obligations

- Extend the elliptic-recursion discussion by adding the full
  Zamolodchikov residue-product normalization and higher-order recursive
  coefficients after the chiral vertex-operator normalization ledger is
  fixed.
- Develop Liouville boundary states only after the BCFT chapter is added; do
  not fold black-hole entropy or HKS/SSS material into this chapter.
- Complete the full functorial sewing comparison with the Volume IV
  Kontsevich-Segal open-problem ledger.

## Audit Notes

- 2026-05-26 issue #601 partial pass: added a dedicated compiled Liouville
  chapter with classical action, central-charge derivation, Seiberg/GMC
  construction status, DOZZ theorem boundary, BPZ null-vector derivation, and
  a calculation check.
- 2026-05-26 stringbook-spine expansion: added the asymptotic scattering
  basis, continuous conformal-block decomposition, `P`-basis DOZZ
  representative, degenerate hypergeometric BPZ block derivation, and explicit
  gamma-product DOZZ `b`-shift ratio.
- 2026-05-26 assumption-ledger pass: displayed the hypergeometric connection
  formula and added a calculation check for the connection-matrix exponent and
  gamma-argument algebra.
- 2026-05-26 screening pass: derived the degenerate one-screening
  Coulomb-gas coefficient `C_-(alpha)` in chapter conventions and added the
  corresponding gamma-argument and gamma-identity checks.
- 2026-05-26 Virasoro-block pass: added ordinary conformal-block
  coefficients through level two from Gram matrices, including
  nondegeneracy hypotheses and exact rational calculation checks.
- 2026-05-26 elliptic-recursion coordinate pass: added the elliptic nome,
  modular lambda expansion, first `z`-to-`q` block-coefficient conversion,
  and a theorem boundary for the full Zamolodchikov recursion with exact
  coefficient checks.

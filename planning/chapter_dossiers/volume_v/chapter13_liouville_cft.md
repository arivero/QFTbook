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
- `G_3`: level-three Virasoro Gram/Shapovalov matrix in the
  `(L_-3|h>, L_-2 L_-1|h>, L_-1^3|h>)` basis.
- `f_1`, `f_2`, `f_3`: first normalized Virasoro four-point block
  coefficients in the `z`-channel expansion.
- `q(z)`: elliptic nome of the four-punctured sphere.
- `lambda(q)`: modular lambda function `theta_2(q)^4/theta_3(q)^4`.
- `g_1`, `g_2`: first two raw elliptic-coordinate block coefficients after
  substituting `z=lambda(q)`.
- `H(c,h_i,h;q)`: Zamolodchikov elliptic block after universal prefactors
  are removed.
- `mu_B`: boundary cosmological constant in the boundary Liouville action.
- `K_g`: geodesic curvature of the boundary, paired with the outward normal.
- `s`: FZZT boundary parameter, related to `mu_B` by
  `cosh^2(pi b s)=mu_B^2 sin(pi b^2)/mu`.
- `u_b(P)`: common FZZT momentum-space boundary wavefunction factor.
- `U_s(P)`: FZZT disk one-point / boundary-state wavefunction
  `u_b(P) cos(2 pi s P)`.
- `ZZ_{m,n}`: discrete ZZ boundary state obtained as a finite difference of
  FZZT states at imaginary parameters `i(m/b +/- n b)`.
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
- Expands the constant-mode reduction of the probabilistic construction with
  the explicit normalization map
  `gamma=2b`, `alpha_i^prob=2 alpha_i`, the random GMC functional `Z_g`, and
  the gamma-function zero-mode integral producing the Seiberg inequality.
- Defines the reflection relation as a meromorphic identification of
  correlation functions.
- Adds the canonical asymptotic scattering basis on the cylinder and the
  delta-normalized primary `V_P`.
- States the continuous Liouville four-point conformal-block decomposition as
  a direct integral over `P in [0,infty)`.
- Defines normalized ordinary Virasoro four-point blocks with explicit
  nondegeneracy hypotheses through the level under discussion; derives
  `f_1`, `f_2`, and `f_3` from the level-one, level-two, and level-three
  Gram projectors.
- Displays the level-three Gram matrix, factors its determinant into the
  level-two Kac factor and the new level-three factor, and proves the
  large-`c` reduction of `f_3` to the global `SL_2` block coefficient.
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
- Expands the residue mechanism behind the elliptic recursion: the general
  Gram-projector formula for block coefficients, Kac-determinant simple
  zeros, singular-vector submodules of highest weight \(h_{m,n}+mn\),
  rank-one Shapovalov inverse residues, fusion-polynomial factorization, the
  conversion of the level shift to \((16q)^{mn}\), and the remaining analytic
  Mittag-Leffler/convergence proof boundary.
- Defines `Upsilon_b`, states the DOZZ formula as a `quotedtheorem`, and names
  the proof boundary.
- Derives the scattering-normalized `P`-basis DOZZ representative from the
  conventional `alpha`-basis formula and records the external-leg phase
  convention.
- Adds the pole-normalization derivation of the Liouville reflection phase
  `S(P)` from the `epsilon=Q/2+i(P1+P2+P3)` pole of the
  scattering-normalized DOZZ constant and the weak-coupling zero-mode
  integral.
- Adds the boundary Liouville action with the `Q K_g phi/(2 pi)` curvature
  term and derives the boundary Euler equation
  `nabla_n phi + Q K_g + 2 pi b mu_B exp(b phi)=0`.
- States the boundary marginality condition for `exp(b phi)` from the
  boundary dimension `b(Q-b)=1`.
- Defines FZZT boundary parameters, one-point functions, and boundary-state
  wavefunctions, with the boundary bootstrap isolated as a quoted theorem.
- Defines ZZ boundary states as finite differences of imaginary-parameter
  FZZT states and proves the hyperbolic wavefunction identity.
- Proves the level-two null-vector coefficient for `alpha=-b/2` and for the
  dual degenerate momentum `alpha=-1/(2b)`, deriving both BPZ differential
  equations with their distinct `b^2` and `b^{-2}` coefficients.
- Derives the degenerate OPE coefficient `C_-(alpha)` from the local
  one-screening Coulomb-gas integral, including the Dotsenko-Fateev
  meromorphic-continuation boundary and the gamma-function rewrites matching
  the chapter convention.
- Derives the dual one-screening coefficient for the
  `V_{-1/(2b)}` channel with a formal dual screening coefficient
  `tilde_mu`, while stating that this is a bootstrap-screening input rather
  than an extra term in the classical action.
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
  Virasoro arithmetic for the level-two null vectors
  `(L_{-1}^2+b^2 L_{-2})|h>` at `h=-1/2-3b^2/4` and
  `(L_{-1}^2+b^{-2} L_{-2})|h^vee>` at
  `h^vee=-1/2-3/(4b^2)`, both at `c=1+6(b+b^{-1})^2`.
- The same script checks the formal `b`-power bookkeeping in the explicit
  DOZZ `b`-shift ratio, including the cancellation of all external-momentum
  powers and the final `b^{-4}` factor.
- The same script verifies the one-screening and dual one-screening OPE
  powers, the Dotsenko-Fateev beta-integral gamma arguments, and the
  gamma-function rewrites of the meromorphic `C_-(alpha)` and
  `tilde C_-(alpha)` coefficients.
- The same script now also checks the affine parameter algebra in the
  hypergeometric connection matrix: the `z=1` exponent gap and the gamma
  arguments `C-A`, `C-B`, and `A+B-C`.
- The same script checks the level-two and level-three Virasoro Gram
  determinants, the level-one, level-two, and level-three ordinary block
  coefficients, and the large-`c` global-block limits in exact rational
  arithmetic.
- The same script checks the modular-lambda expansion through
  `lambda(q)=16q(1-8q+44q^2+O(q^3))` and verifies the exact formulas for the
  raw elliptic \(q\)-coefficients `g_1` and `g_2`.
- `calculation-checks/bcft_cardy_checks.py` verifies the exact hyperbolic
  identities that turn imaginary FZZT differences into ZZ wavefunctions and
  degenerate annulus kernels into finite shifted-character sums.

## Remaining Obligations

- Extend the elliptic-recursion discussion by adding the full
  Zamolodchikov residue-product normalization after the chiral
  vertex-operator normalization ledger is fixed.  The low-level Gram
  projector data now run through level three, but the all-level residue
  product remains a theorem-boundary normalization problem.
- Extend the Liouville boundary discussion to boundary two-point functions,
  boundary-condition-changing operators, and annulus spectral-density
  positivity only after the nonrational sewing framework is fixed; do not
  fold black-hole entropy or HKS/SSS material into this chapter.
- Complete the full functorial sewing comparison with the Volume IV
  Kontsevich-Segal open-problem ledger.

## Reference Intake

- Local sources consulted:
  `references/02_2d_cft/boundary_liouville_fzz_hep-th-0001012/blio.tex` and
  `references/02_2d_cft/liouville_pseudosphere_zz_hep-th-0101152/look.tex`.
  Used to check the FZZT boundary action, boundary one-point function,
  boundary-state wavefunction, and the ZZ/FZZT hyperbolic finite-difference
  conventions.  The monograph text rederives the variational boundary
  equation and the hyperbolic identities locally, while treating the boundary
  bootstrap solution as a theorem boundary.
- Local stringbook source consulted:
  `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`, lines
  around `\label{liouvillecftsec}` and the `c=1` FZZT/ZZ discussion.  Used to
  check the scattering-normalized \(V_P\) convention, two-point normalization
  `pi delta(P-P')`, the `P`-basis DOZZ representative, the pole extraction of
  `S(P)`, and the special \(b=1,c=25\) boundary-state normalization.

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
- 2026-05-27 Virasoro-block level-three pass: extended the ordinary
  conformal-block derivation to the level-three Shapovalov matrix, determinant
  factorization, finite projector formula for `f_3`, and exact rational
  checks of the sample coefficient and global-block limit.
- 2026-05-26 elliptic-recursion coordinate pass: added the elliptic nome,
  modular lambda expansion, first `z`-to-`q` block-coefficient conversion,
  and a theorem boundary for the full Zamolodchikov recursion with exact
  coefficient checks.
- 2026-05-26 boundary-state pass: added boundary Liouville action,
  variational boundary equation, FZZT one-point and boundary-state
  normalization, ZZ states as imaginary-FZZT finite differences, and exact
  hyperbolic identity checks coordinated with the BCFT chapter.
- 2026-05-26 dual-BPZ pass: added the independent
  `V_{-1/(2b)}` level-two null vector and dual BPZ equation, with exact
  Laurent checks of the `b^{-2}` coefficient.
- 2026-05-26 dual-screening pass: added the formal dual Coulomb-gas
  screening computation for the `V_{-1/(2b)}` shift channel, with the
  `tilde_mu` hypothesis and exact gamma-argument checks.

## Anti-Wrapper Audit

- 2026-05-29: demoted the boundary Euler equation to a worked variational
  paragraph.  The boundary condition remains explicit, but the proof is the
  direct fixed-metric first variation of the boundary action.
- 2026-05-29 seventh pass: expanded the BPZ-equation proof to display the
  \(L_{-1}\) insertion, the \(L_{-2}\) contour move, the primary OPE residue,
  and the separated-point scope before inserting the degenerate null vector.
- 2026-05-30 stringbook Liouville check: reopened the stringbook Liouville
  appendix and boundary-state passage, tightened the probabilistic zero-mode
  normalization map, and added the reflection-phase extraction from the
  scattering-normalized DOZZ pole.
- 2026-05-30 elliptic-recursion proof-boundary pass: added the Verma-module
  residue mechanism behind Zamolodchikov recursion, separating the algebraic
  Kac-determinant/null-vector content from the remaining analytic convergence
  theorem boundary.

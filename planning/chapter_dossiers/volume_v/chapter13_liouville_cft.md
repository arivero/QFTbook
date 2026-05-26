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
- `h_alpha`: Liouville conformal weight `alpha(Q-alpha)`.
- `Upsilon_b`: entire special function entering the DOZZ constant.
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
- Defines `Upsilon_b`, states the DOZZ formula as a `quotedtheorem`, and names
  the proof boundary.
- Proves the level-two null-vector coefficient for `alpha=-b/2` and derives
  the corresponding BPZ differential equation.
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

## Remaining Obligations

- Expand the DOZZ shift-ratio calculation check using the `Upsilon_b` shift
  relations.
- Add detailed conformal-block recursion examples beyond the first BPZ
  equation.
- Develop Liouville boundary states only after the BCFT chapter is added; do
  not fold black-hole entropy or HKS/SSS material into this chapter.
- Complete the full functorial sewing comparison with the Volume IV
  Kontsevich-Segal open-problem ledger.

## Audit Notes

- 2026-05-26 issue #601 partial pass: added a dedicated compiled Liouville
  chapter with classical action, central-charge derivation, Seiberg/GMC
  construction status, DOZZ theorem boundary, BPZ null-vector derivation, and
  a calculation check.

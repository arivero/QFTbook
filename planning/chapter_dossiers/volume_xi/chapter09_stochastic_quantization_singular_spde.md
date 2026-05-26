# Chapter 09: Stochastic Quantization And Singular SPDE

## Source Position

Volume XI now adds stochastic quantization and singular SPDE constructions as
a route between Euclidean constructive fields, renormalized dynamics, and OS
data.

## Notation Inventory

- `S`, `L`: finite-dimensional action and Langevin generator.
- `C_Lambda`, `xi_Lambda`: ultraviolet covariance cutoff and regularized
  white noise.
- `phi_Lambda`, `lambda_Lambda`, `c_Lambda`: regularized field and local
  coordinates of the scalar theory.
- `rho_epsilon`, `phi_epsilon`: mollifier and mollified field.
- `C_epsilon`: Gaussian contraction in Wick powers.
- `X`, `Y`: Ornstein-Uhlenbeck stochastic convolution and
  Da Prato--Debussche remainder.
- `(A,T,G)`, `Pi_z`, `Gamma_zz'`: regularity structure, model maps, and
  reexpansion maps.
- `C_{1,epsilon}`, `C_{2,epsilon}`: one-loop and two-loop local SPDE
  counterterm constants in the displayed BPHZ convention.
- `c_fin`: finite mass coordinate in the renormalized dynamic
  \(\Phi^4_3\) equation.
- `mu`: invariant Euclidean measure of the Markov process.
- `X_mathbb`: enhanced Da Prato--Debussche noise
  \((X,:X^2:,:X^3:)\).
- `R F`: reconstruction of a modelled distribution.

## Claim Ledger

- Proves the finite-dimensional invariant-measure identity for Langevin
  dynamics.
- Defines a regularized stochastic field equation as a gradient flow plus
  noise.
- Derives the Wick subtraction in the cubic drift from Gaussian contractions.
- Develops the Da Prato--Debussche decomposition for `Phi^4_2`, identifies
  the role of the enhanced noise, and marks the solution mechanism as a
  `quotedtheorem` pending a self-contained proof.
- Defines regularity structures, models, and the reconstruction theorem at the
  level needed for singular SPDE; the reconstruction theorem is now a
  `quotedtheorem` with the wavelet-coefficient mechanism recorded as a role
  explanation rather than a proof.
- Presents the renormalized `Phi^4_3` dynamic equation at cutoff with
  one-loop and two-loop local counterterm constants; the quoted theorem now
  separates local cutoff well-posedness, BPHZ-renormalized convergence,
  invariant-law construction, and identification with the constructive
  Euclidean \(\Phi^4_3\) measure after matching regulator and local
  coordinates.
- Separates regularity-structure, paracontrolled, and RG routes.
- Separates invariant-measure construction from the OS hypotheses needed for
  QFT reconstruction.
- Records a self-contained singular-SPDE proof stack as an open obligation:
  Wick powers, Schauder and multiplication estimates, energy estimates,
  invariant-law identification, reconstruction, BPHZ model convergence,
  fixed points in modelled distributions, and SPDE-to-OS passage.

## Figure Ledger

No figure is included in this pass.  Future figures should include Markov
flow to invariant measure, covariance-scale decompositions, and SPDE-to-OS
data maps.

## Audit Notes

- 2026-05-25 issue #575 pass: the Da Prato--Debussche solution mechanism,
  Hairer reconstruction theorem, and renormalized dynamic \(\Phi^4_3\) SPDE
  datum are no longer ordinary theorem blocks followed by proof sketches.
  They are marked as `quotedtheorem` blocks, their proof sketches are
  rewritten as role/status text, and Open Problem
  `op:self-contained-singular-spde-proof-stack` records the monograph's
  obligation to prove the quoted SPDE results internally rather than accept
  them on authority.
- 2026-05-25 issue #558 pass: the dynamic \(\Phi^4_3\) theorem boundary now
  states the four requested components explicitly: local cutoff
  well-posedness, renormalized convergence with \(C_{1,\epsilon}\) and
  \(C_{2,\epsilon}\), invariant measures of the limiting Markov process, and
  equality with the constructive Euclidean \(\Phi^4_3\) OS hierarchy only
  after the regulator chart and local coordinates are matched.

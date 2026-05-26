# Chapter 06: Four-Dimensional N=1 Gauge Dynamics

## Source Position

This chapter is the first concrete four-dimensional supersymmetric gauge
dynamics chapter after supersymmetric Wilsonian schemes and holomorphy.  It
sets up SQCD, chiral coordinates, holomorphic scales, and the first exact
chiral-coordinate constraints.  The 2026-05-26 development pass also imports
and expands the stringbook conifold gauge-theory material from
`/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`, especially
the Klebanov-Witten and Klebanov-Strassler discussion around lines
18380-18670, while rewriting the derivations in the monograph's notation and
status-boundary style.

## Notation Inventory

- `G=SU(N_c)`: gauge group for the chapter.
- `Q^i`, `tilde Q_j`: fundamental and antifundamental chiral superfields.
- `W_alpha`, `tau`: gauge field strength and holomorphic gauge coordinate.
- `Lambda_h^{b_0}`: invariant holomorphic scale.
- `M`, `B`, `tilde B`: meson, baryon, and antibaryon chiral coordinates.
- `S`: chiral glueball coordinate.
- `W_ADS`: Affleck-Dine-Seiberg superpotential coordinate.
- `k`: instanton number, normalized as in the BPST section of Volume II.
- `hyp:sqcd-one-instanton-calculus`: assumptions needed for using the
  semiclassical `N_f=N_c-1` SQCD instanton calculation as an \(F\)-term
  derivation.
- `kappa_Nc`: scheme-dependent nonzero one-instanton coefficient in the
  `N_f=N_c-1` ADS normalization.
- `I(beta,L)`: finite-volume Witten index on a spatial three-torus.
- `Y_i`, `x_i`: small-circle affine-Toda coordinates for pure `SU(N_c)`
  supersymmetric Yang-Mills.
- `gamma_Phi`: monograph anomalous-dimension convention
  `d log Z_Phi / d log mu`.
- `mathcal C_Phi`: half-normalized convention used in the stringbook
  appendices, related by `gamma_Phi = 2 mathcal C_Phi`.
- `G_KW=SU(N)_1 x SU(N)_2`: Klebanov-Witten gauge group.
- `A_i`, `B_j`: KW bifundamental chiral multiplets, transforming as
  `(N,bar N)` and `(bar N,N)`.
- `W_KW`: quartic conifold superpotential
  `h epsilon epsilon tr(A B A B)`.
- `U(1)_B`: baryonic symmetry, normalized in the monograph by
  `q_B(A)=+1`, `q_B(B)=-1`.
- `W_ij=A_i B_j`: mesonic conifold coordinates.
- `a_KW`, `c_KW`: KW central charges from Weyl-fermion R traces.
- `M`: fractional-rank difference in the Klebanov-Strassler cascade.
- `B_1`, `B_2` or `mathcal B_1`, `mathcal B_2`: NSVZ numerators for
  the two KS gauge factors.
- `hyp:n1-scft-bookkeeping-input`: assumptions needed before using
  `Delta=3R/2` as an infrared SCFT statement.
- `hyp:kw-lagrangian-branch-assumptions`: KW Lagrangian, branch, and
  conformal-manifold assumptions.
- `hyp:ks-cascade-input-assumptions`: Wilsonian, NSVZ, Seiberg-duality, and
  meson-integration assumptions for the cascade.

## Claim Ledger

- Defines SQCD Wilsonian data and holomorphic scale normalization.
- Computes the anomaly-free \(R\)-charge assignment in the stated trace
  normalization.
- Specializes the NSVZ coordinate beta function to SQCD with the chapter's
  trace convention.
- Defines the Witten index and explains the finite-volume pairing logic and
  the small-circle affine-Toda count for pure \(SU(N_c)\) SYM.
- Derives the allowed ADS superpotential form from dimension and \(R\)-charge
  constraints.
- States the analytic assumptions required for the semiclassical
  `N_f=N_c-1` SQCD one-instanton calculation: holomorphic regulator,
  maximal-rank Higgs patch, collective-coordinate separation, BPST
  topological normalization, and endpoint control by the holomorphic scale.
- Proves the `N_f=N_c-1` instanton zero-mode ledger: `2N_c` adjoint gaugino
  zero modes, `2N_c-2` matter zero modes, Yukawa lifting of `2N_c-2`
  adjoint modes, and two remaining Goldstino modes giving the `d^2 theta`
  superpotential measure.
- Derives the one-instanton ADS form
  `kappa_Nc Lambda_h^(2N_c+1)/det M` from the instanton scale factor,
  flavor invariance, dimension, and \(R\)-charge.
- Proves the holomorphic decoupling equation by matching the invariant
  holomorphic scale at a massive threshold.
- States the quantum modified constraint for \(N_f=N_c\) with explicit
  Wilsonian and infrared hypotheses.
- Adds superconformal SQCD bookkeeping: the chiral-primary relation
  `Delta=3R/2`, the chapter convention for `gamma`, the conversion to the
  stringbook `mathcal C` convention, NSVZ numerator cancellation at the
  candidate SQCD fixed point, and the meson unitarity-bound test for the
  lower edge of the conformal window.
- States an explicit hypothesis boundary for every later use of
  `Delta=3R/2`: existence of a unitary `N=1` SCFT, chiral-primary status,
  correct superconformal R-current after mixing, and no accidental symmetry
  changing the operator charge.
- Defines the KW gauge theory field content, global symmetries, baryon-charge
  normalization, and quartic superpotential.
- States the KW Lagrangian and branch assumptions before deriving F-terms,
  moduli, protected dimensions, and conformal-manifold data.
- Derives the KW F-term equations from the expanded superpotential rather
  than quoting the conifold branch.
- Proves the KW anomaly-free R-charge assignment and verifies that the
  superpotential has R-charge 2.
- Proves the KW NSVZ numerator cancellation at
  `R(A)=R(B)=1/2`, using `gamma_A=gamma_B=-1/2` in the monograph convention.
- Performs the KW `a`-maximization calculation for baryonic mixing and
  derives the exact finite-N central charges
  `a=27N^2/64-3/8`, `c=27N^2/64-1/4`.
- Proves the one-brane abelian conifold quotient
  `C[W_ij]/(W_11 W_22 - W_12 W_21)` and records the general commuting
  mesonic branch as `Sym^N(conifold)`.
- Lists protected meson and baryon dimensions from the superconformal
  R-charge, with the monograph's baryon-charge normalization.
- Quotes the local KW conformal-manifold theorem as an honest continuum SCFT
  input, after deriving the anomaly and marginality arithmetic.
- Defines the KS `SU(N+M) x SU(N)` cascade, derives the two NSVZ numerator
  signs near the KW anomalous dimension, proves the Seiberg-dual rank step,
  records the Euclidean division step count, derives the unequal-rank
  `U(1)_R` anomaly remnant `Z_{2M}`, and marks the use of Seiberg duality as
  a quoted field-theoretic input.
- States cascade assumptions explicitly: Wilsonian/NSVZ scheme, local
  numerator-sign interpretation, Seiberg duality for one strongly coupled
  node with the other weakly gauged, and legitimacy of integrating out
  massive mesons.

## Calculation Checks

- `calculation-checks/susy_n1_conifold_checks.py` verifies exact rational
  arithmetic for the new conifold material: KW R-anomaly cancellation,
  `gamma=2 mathcal C` conversion, superpotential R-charge, NSVZ numerator,
  `a`-maximization sign, central charges, conifold determinant relation,
  KS numerator signs, unequal-rank R-anomaly coefficients, Seiberg-dual
  magnetic rank, magnetic meson quadratic-form integration, cascade step
  count, and the `Z_{2M}->Z_2` vacuum count.
- `calculation-checks/susy_instanton_nekr_checks.py` verifies exact rational
  arithmetic for the ADS instanton expansion: general ADS dimension and
  \(R\)-charge, `N_f=N_c-1` zero-mode counts, and holomorphic decoupling
  exponent shifts.

## Figure Ledger

No figure is included.  Future diagrams should show the \(N_f<N_c\),
`N_f=N_c`, pure SYM, KW conifold branch, and KS cascade stairway as
chiral-coordinate spaces with their assumptions and anomaly data.

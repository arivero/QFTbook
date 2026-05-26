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
- `hat M`: light \(N_c\times N_c\) meson block used when a last massive
  flavor is decoupled from the `N_f=N_c+1` confining chiral description.
- `Lambda_+`, `Lambda_-`: holomorphic scales above and below the
  `N_f=N_c+1` to `N_f=N_c` mass threshold.
- `S`: chiral glueball coordinate.
- `W_ADS`: Affleck-Dine-Seiberg superpotential coordinate.
- `k`: instanton number, normalized as in the BPST section of Volume II.
- `hyp:sqcd-one-instanton-calculus`: assumptions needed for using the
  semiclassical `N_f=N_c-1` SQCD instanton calculation as an \(F\)-term
  derivation.
- `eq:ads-diagonal-higgs-patch`: local diagonal Higgs-patch coordinates for
  the explicit `N_f=N_c-1` instanton calculation.
- `prop:ads-higgs-patch-collective-coordinate-ledger`: explicit
  Higgs-patch gauge-breaking, bosonic-moduli, fermion-zero-mode, and
  Yukawa-lifting ledger for the ADS instanton calculation.
- `kappa_Nc`: scheme-dependent nonzero one-instanton coefficient in the
  `N_f=N_c-1` ADS normalization.
- `hyp:sqcd-quantum-modified-confining-input`: assumptions for comparing
  the `N_f=N_c` quantum-modified chiral ring with the `N_f=N_c+1`
  confining chiral-sector description.
- `W_{N_c+1}`: confining `N_f=N_c+1` superpotential
  `(B M tilde B - det M)/Lambda_+^(2N_c-1)`.
- `I(beta,L)`: finite-volume Witten index on a spatial three-torus.
- `Y_i`, `x_i`: small-circle affine-Toda coordinates for pure `SU(N_c)`
  supersymmetric Yang-Mills.
- `gamma_Phi`: monograph anomalous-dimension convention
  `d log Z_Phi / d log mu`.
- `mathcal C_Phi`: half-normalized convention used in the stringbook
  appendices, related by `gamma_Phi = 2 mathcal C_Phi`.
- `tilde N_c=N_f-N_c`: magnetic gauge rank in the SQCD duality section.
- `q_i`, `tilde q^j`: magnetic quark and antiquark chiral multiplets in
  Seiberg's SQCD dual variables.
- `mu_*`: dimension-one matching scale used when the magnetic singlet
  `M` is normalized as the electric composite `tilde Q Q`.
- `W_mag=(1/mu_*) M q tilde q`: magnetic SQCD superpotential.
- `hyp:sqcd-ir-comparison-hypotheses`: explicit continuum, current,
  superconformal-R, chiral-coordinate, and deformation-matching assumptions
  needed before comparing electric and magnetic SQCD infrared limits.
- `qt:sqcd-seiberg-duality-input`: quoted nonperturbative status boundary
  for SQCD Seiberg duality.
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
- Adds the explicit Higgs-patch collective-coordinate calculation behind the
  ADS derivation: local diagonal coordinates with `det M != 0`, complete
  breaking of `SU(N_c)`, charge-one bosonic moduli count `4N_c` from
  translations/size/orientations, index-theorem fermion zero-mode counts,
  and the rank statement for Yukawa lifting by nonzero Higgs expectation
  values.
- Derives the one-instanton ADS form
  `kappa_Nc Lambda_h^(2N_c+1)/det M` from the instanton scale factor,
  the reduced `d^4x_0 d^2 eta` instanton integral, flavor invariance,
  dimension, and \(R\)-charge.
- Proves the holomorphic decoupling equation by matching the invariant
  holomorphic scale at a massive threshold.
- States and sharpens the quantum modified constraint for \(N_f=N_c\) with
  explicit Wilsonian and infrared hypotheses.
- Proves uniqueness of a field-independent quantum modification from
  engineering dimension, flavor symmetry, baryon charge, anomaly-free
  \(R\)-charge, and holomorphic-scale data.
- Adds the `N_f=N_c+1` confining chiral-sector input and checks its
  superpotential dimension and \(R\)-charge.
- Derives the \(N_f=N_c\) quantum-modified constraint by adding
  `m M^L_L` to the `N_f=N_c+1` confining superpotential, integrating out
  the heavy block on the light branch, and using holomorphic scale matching
  `Lambda_-^(2N_c)=m Lambda_+^(2N_c-1)`.
- Adds superconformal SQCD bookkeeping: the chiral-primary relation
  `Delta=3R/2`, the chapter convention for `gamma`, the conversion to the
  stringbook `mathcal C` convention, NSVZ numerator cancellation at the
  candidate SQCD fixed point, and the meson unitarity-bound test for the
  lower edge of the conformal window.
- States an explicit hypothesis boundary for every later use of
  `Delta=3R/2`: existence of a unitary `N=1` SCFT, chiral-primary status,
  correct superconformal R-current after mixing, and no accidental symmetry
  changing the operator charge.
- Adds the general SQCD Seiberg-duality ledger as a status-bounded
  nonperturbative input rather than a citation-as-proof: electric/magnetic
  field content, magnetic rank `N_f-N_c`, baryon normalization, magnetic
  meson normalization, and the `M q tilde q / mu_*` superpotential.
- States `hyp:sqcd-ir-comparison-hypotheses`, separating continuum-limit,
  current-identification, R-current, chiral-sector, and deformation-matching
  assumptions before any electric/magnetic equivalence is used.
- Proves the magnetic gauge-`R` anomaly cancellation, magnetic
  superpotential \(R=2\), and magnetic NSVZ numerator cancellation in the
  monograph `gamma=d log Z/d log mu` convention.
- Proves electric/magnetic matching for the displayed global anomalies:
  `SU(N_f)_L^3`, `SU(N_f)_R^3`, mixed flavor-`R`, mixed flavor-baryon,
  `U(1)_B^2 U(1)_R`, `Tr R`, and `Tr R^3`.
- Records the SQCD phase ledger with explicit logical status: ADS runaway
  from the direct `N_f=N_c-1` instanton calculation plus holomorphic
  decoupling, quantum-modified `N_f=N_c`, confining `N_f=N_c+1`, free
  magnetic range, interacting conformal window, and free electric range.
- Checks the `N_f=N_c+1` confining superpotential
  `(B M tilde B - det M)/Lambda_h^(2N_c-1)` by dimension and \(R\)-charge.
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
- `calculation-checks/susy_n1_sqcd_duality_checks.py` verifies exact
  rational arithmetic for the general SQCD duality and phase ledger:
  dual-rank involution, baryon-charge map, electric/magnetic NSVZ numerator
  cancellation, magnetic gauge-`R` anomaly cancellation, magnetic
  superpotential dimension and \(R\)-charge, full global anomaly matching,
  `N_f=N_c+1` confining-superpotential checks, mass decoupling to the
  `N_f=N_c` quantum-modified constraint, and phase-window inequalities.
- `calculation-checks/susy_instanton_nekr_checks.py` verifies exact rational
  arithmetic for the ADS instanton expansion: general ADS dimension and
  \(R\)-charge, `N_f=N_c-1` zero-mode counts, Higgs-patch
  collective-coordinate counts, and holomorphic decoupling exponent shifts.

## Figure Ledger

No figure is included.  Future diagrams should show the \(N_f<N_c\),
`N_f=N_c`, pure SYM, KW conifold branch, and KS cascade stairway as
chiral-coordinate spaces with their assumptions and anomaly data.

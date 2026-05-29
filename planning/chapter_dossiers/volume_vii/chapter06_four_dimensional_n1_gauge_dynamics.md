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
status-boundary style.  The imported material is used only as a source of
field-theory conventions and candidate examples; no string compactification,
brane construction, or holographic interpretation is a premise of the chapter.

## Notation Inventory

- `G=SU(N_c)`: gauge group for the chapter.
- `Q^i`, `tilde Q_j`: fundamental and antifundamental chiral superfields.
- `W_alpha`, `tau`: gauge field strength and holomorphic gauge coordinate.
- `X_h=8 pi^2/g_h^2`, `X_c=8 pi^2/g^2`: holomorphic Wilsonian and
  canonical real gauge-coupling coordinates used in the SQCD NSVZ audit.
- `Lambda_h^{b_0}`: invariant holomorphic scale.
- `M`, `B`, `tilde B`: meson, baryon, and antibaryon chiral coordinates.
- `hat M`: light \(N_c\times N_c\) meson block used when a last massive
  flavor is decoupled from the `N_f=N_c+1` confining chiral description.
- `Lambda_+`, `Lambda_-`: holomorphic scales above and below the
  `N_f=N_c+1` to `N_f=N_c` mass threshold.
- `S`: chiral glueball coordinate.
- `W_VY`: pure-SYM Veneziano-Yankielowicz glueball superpotential
  `S(log(Lambda_h^(3N_c)/S^N_c)+N_c)` in the standard finite
  normalization.
- `prop:pure-sym-discrete-chiral-anomaly`: derivation of the pure-SYM
  anomalous `Z_{2N_c}` gaugino phase symmetry and its breaking to `Z_2` by a
  nonzero glueball condensate.
- `hyp:pure-sym-glueball-f-term-description`: Wilsonian chiral-sector
  assumptions under which a one-coordinate glueball \(F\)-term description is
  used.
- VY glueball-superpotential derivation: derivation of the VY representative and
  the critical equation `S^N_c=Lambda_h^(3N_c)`.
- Pure-SYM condensate branch/source-normalization calculation: derivation of
  the branch values, source identity, and theta-angle monodromy as consequences
  of the stated glueball \(F\)-term hypothesis.
- `prop:pure-sym-one-instanton-zero-mode-test`: pure-SYM charge-one
  instanton zero-mode saturation ledger, showing that separated
  \(S\)-correlators vanish for fewer than \(N_c\) insertions and that the
  first possible instanton test is the \(S^{N_c}\) correlator.
- Saturated pure-SYM Berezin coefficient convention: exterior-algebra
  coefficient extraction for the saturated \(N_c\)-insertion pure-SYM
  instanton Berezin integral, including the canonical coefficient, the
  identical-two-form \(N_c!\) convention, and the sign ledger.  This is
  recorded as calculation prose rather than a theorem-family claim.
- `prop:pure-sym-topological-sector-s-selection`: instanton-number selection
  rule showing that a charge-\(\nu\) self-dual sector requires
  \(\nu N_c\) separated \(S\)-insertions for zero-mode saturation, so the
  \(N_c\)-point chiral correlator is a charge-one test.
- `hyp:pure-sym-zero-mode-saturated-instanton-correlator`: analytic
  assumptions required before promoting the zero-mode-saturated
  \(N_c\)-point instanton ledger to a chiral correlator with nonzero
  coefficient.
- `prop:pure-sym-instanton-cluster-extraction`: conditional cluster
  extraction showing that an \(N_c\)-point instanton correlator can imply
  only the root equation \(s_\ell^{N_c}\propto\Lambda_h^{3N_c}\), not a
  branch-selected one-point condensate by itself.
- `hyp:pure-sym-finite-volume-index-problem`: finite-volume Hamiltonian,
  Gauss-law, spin-structure, global-form, and trace-class assumptions for the
  `SU(N_c)` Witten index.
- Finite-volume graded-trace calculation: positive-energy pairing and
  finite-volume index identity.
- Finite-volume symmetry-basis calculation: finite-dimensional
  linear algebra distinguishing finite-volume discrete-symmetry eigenstates
  from infinite-volume cluster branch states with nonzero condensate.
- `hyp:pure-sym-small-circle-affine-toda-input`: assumptions behind the
  small-circle monopole-instanton affine-Toda superpotential.
- Affine-Toda critical-point count: constrained affine-Toda
  critical-point count giving `N_c` isolated solutions.
- `prop:pure-sym-local-chiral-critical-index`: finite-dimensional
  holomorphic oscillator calculation showing that each nondegenerate chiral
  critical point contributes `+1` to the local Witten index.
- `hyp:pure-sym-index-continuation-massive-branch`: spectral-continuation and
  massive-branch hypotheses linking the small-circle count to 4D pure
  `SU(N_c)` SYM.
- `prop:pure-sym-index-condensate-ledger`: conditional assembly of
  `I_SU(Nc)=N_c`, the `N_c` condensate branches, and
  `Z_{2N_c}->Z_2`.
- `W_ADS`: Affleck-Dine-Seiberg superpotential coordinate.
- `k`: instanton number, normalized as in the BPST section of Volume II.
- `hyp:sqcd-one-instanton-calculus`: assumptions needed for using the
  semiclassical `N_f=N_c-1` SQCD instanton calculation as an \(F\)-term
  derivation.
- `eq:ads-diagonal-higgs-patch`: local diagonal Higgs-patch coordinates for
  the explicit `N_f=N_c-1` instanton calculation.
- Higgs-patch collective-coordinate calculation: explicit local
  gauge-breaking, bosonic-moduli, fermion-zero-mode, and exact gaugino-mode
  ledger for the ADS instanton calculation.
- Yukawa-lifting Berezin determinant calculation: finite-dimensional
  diagonal-patch Berezin determinant for the lifting matrix, separating the
  zero-mode saturation algebra from the later holomorphic `1/det M` argument.
- Radial Higgs-cutoff calculation: finite radial-integral check
  showing exactly how the Higgs expectation values cut off the instanton size
  integral on the maximal-rank ADS patch, while separating that real
  convergence estimate from the holomorphic `1/det M` denominator.
- `prop:ads-maximal-rank-meson-invariant`: invariant-theory lemma on the
  maximal-rank meson patch proving that special-flavor invariance and the
  ADS scaling degree force the reduced instanton factor to be `C/det M`.
- `kappa_Nc`: scheme-dependent nonzero one-instanton coefficient in the
  `N_f=N_c-1` ADS normalization.
- `prop:ads-holomorphic-decoupling-recursion`: finite-dimensional
  `F_X=0` elimination step propagating the one-instanton ADS seed from
  `N_f=N_c-1` to all `N_f<N_c` by holomorphic mass decoupling.
- `prop:massive-sqcd-to-pure-sym-condensate-branches`: finite-dimensional
  elimination of massive `N_f=n<N_c` SQCD with invertible mass matrix,
  deriving the pure-SYM branch superpotential and source identity from the
  ADS representative and holomorphic threshold matching.
- `prop:massive-sqcd-konishi-source-ledger`: finite-dimensional
  mass-source derivative and Konishi ledger on the same massive SQCD
  branches, deriving `dW_eff/dm_i^j=<M^i_j>` and
  `<M^a_j> m_i^j = <S> delta_i^a`.
- `hyp:sqcd-nsvz-coordinate-specialization`: assumptions for specializing
  the Chapter 05 holomorphic-canonical NSVZ coordinate relation to SQCD.
- SQCD NSVZ coordinate specialization: derivation of
  `X_h=X_c+N_c log g^2-N_f log Z_Q+kappa` and the specialized SQCD NSVZ
  beta function.
- SQCD central-charge bookkeeping: SQCD conformal-window
  `Tr R`, `Tr R^3`, \(a\), \(c\), and conditional free-field
  \(a_{\mathrm{UV}}-a_{\mathrm{IR}}\) comparison under the SCFT-input
  hypothesis.
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
- `prop:sqcd-seiberg-deformation-tests`: explicit mass-deformation and
  Higgs-deformation consistency tests for the SQCD magnetic field content,
  including the boundary to the `N_f=N_c+1` confining description.
- `G_KW=SU(N)_1 x SU(N)_2`: Klebanov-Witten gauge group.
- `A_i`, `B_j`: KW bifundamental chiral multiplets, transforming as
  `(N,bar N)` and `(bar N,N)`.
- `W_KW`: quartic conifold superpotential
  `h epsilon epsilon tr(A B A B)`.
- `U(1)_B`: baryonic symmetry, normalized in the monograph by
  `q_B(A)=+1`, `q_B(B)=-1`.
- `W_ij=A_i B_j`: mesonic conifold coordinates.
- `a_KW`, `c_KW`: KW central charges from Weyl-fermion R traces.
- KW necessary beta-function rank-count calculation
  check showing the two gauge NSVZ numerators and quartic-superpotential
  marginality defect are proportional to `1+gamma_A+gamma_B`.
- `hyp:n1-local-exact-marginality-chart`: finite-dimensional
  marginal-source chart hypotheses for turning beta-map rank into a local
  conformal-manifold dimension statement.
- `hyp:kw-exact-marginality-input`: KW continuum, source-chart,
  beta-completeness, contact-term, and nondegeneracy assumptions for the
  local exact-marginality statement.
- KW rank-one exact-marginality calculation: conditional derivation of the
  two-complex-dimensional KW local conformal locus from the rank-one beta map.
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
  trace convention, including the holomorphic-canonical coordinate relation,
  matter Konishi-rescaling coefficients, vector-multiplet denominator, and
  the status of the denominator pole as a coordinate-chart feature.
- Derives the pure-SYM discrete chiral anomaly in the chapter's adjoint-index
  convention, showing `Z_{2N_c}` and the `Z_{2N_c}->Z_2` condensate-phase
  quotient.
- States the pure-SYM glueball \(F\)-term assumptions explicitly:
  Wilsonian holomorphic scheme, one glueball coordinate on massive chiral
  branches, source normalization
  `Lambda_h^(3N_c) dW/dLambda_h^(3N_c)=S`, and finite-normalization
  dependence of the condensate constant.
- Derives the VY superpotential representative
  `S(log(Lambda_h^(3N_c)/S^N_c)+N_c)` from the dimensionless ratio
  `S^N_c/Lambda_h^(3N_c)` and the source identity, then derives
  `S^N_c=Lambda_h^(3N_c)` and the `N_c` isolated glueball critical points.
- Derives the pure-SYM condensate branch/source ledger: at a VY critical
  point `W_k=N_c S_k`, the source identity gives
  `L dW_k/dL=<S>_k`, and a loop of `L=Lambda_h^(3N_c)` around the origin
  shifts the branch label by one.
- Adds a pure-SYM charge-one instanton zero-mode test tied to the BPST
  normalization: \(2N_c\) adjoint gaugino zero modes force separated
  correlators with fewer than \(N_c\) \(S\)-insertions to vanish at the
  Berezin-integral level, while the first possible saturated chiral test is
  the \(N_c\)-point correlator with the same dimension and anomalous-charge
  ledger as \(S^{N_c}\sim\Lambda_h^{3N_c}\).
- Proves the exterior-algebra formula for the saturated pure-SYM instanton
  Berezin coefficient: writing each \(S(x_a)\) zero-mode restriction as an
  antisymmetric quadratic form \(K_a^{pq}\eta_p\eta_q\), the fixed-moduli
  zero-mode integral is exactly the coefficient of
  \(\eta_1\cdots\eta_{2N_c}\) in the product, with canonical coefficient
  `1` and identical-two-form coefficient `N_c!`.
- Proves the pure-SYM instanton-number selection rule for separated chiral
  \(S\)-correlators: a self-dual charge-\(\nu\) sector has \(2\nu N_c\)
  adjoint gaugino zero modes, hence the first possible saturated
  \(S\)-correlator has \(\nu N_c\) insertions; the \(N_c\)-point root-equation
  test is therefore restricted to the charge-one sector at the Berezin level,
  while anti-self-dual sectors belong to the conjugate \(\overline S\)
  channel.
- States the additional analytic assumptions needed before using the
  zero-mode-saturated \(N_c\)-point instanton calculation in pure SYM:
  regulator, saturated Berezin coefficient after bosonic moduli integration,
  instanton-size integral, nonzero-mode determinant, collision singularities,
  and boundary strata must be controlled; the elementary zero-mode count is
  not a direct proof of the one-point condensate.
- Proves the conditional cluster-extraction step: if a massive pure phase
  exists and the separated \(N_c\)-point chiral correlator clusters, then
  the instanton input gives only \(s_\ell^{N_c}=\kappa\Lambda_h^{3N_c}\);
  root selection requires the anomaly, index, and massive-branch data.
- Defines the Witten index with explicit finite-volume assumptions:
  simply connected `SU(N_c)`, spatial `T^3_L`, periodic gaugino spin
  structure, trivial flux sector, Gauss-law projection, exact regulated
  supersymmetry, trace-class heat operator, and finite zero-energy space.
- Proves the positive-energy boson-fermion pairing identity for the
  finite-volume Witten index and states the exact spectral caveat for
  invariance under volume/coupling/regulator deformations.
- Proves the finite-dimensional symmetry-basis/cluster-branch lemma: a
  cyclic branch representation has ordinary index `N_c`, vanishing nontrivial
  chiral-twined traces, zero diagonal `S` expectation in finite-volume
  symmetry eigenstates, and nonzero `S=s omega^k` only in the cluster branch
  basis.
- States the small-circle affine-Toda input with root data
  `alpha_i=e_i-e_{i+1}` and affine root `alpha_0=e_N-e_1`, two gaugino zero
  modes for each fundamental monopole event, and the instanton-weight
  product coordinate `eta`, with the local-index convention that each
  nondegenerate massive chiral critical point contributes one even ground
  state.
- Proves the constrained affine-Toda critical-point count: with
  `x_1...x_N=eta`, stationarity of `sum_i x_i` forces all `x_i` equal, so
  `x^N=eta`, and the constrained Hessian is nondegenerate.
- Proves the local chiral-oscillator index convention used in the
  small-circle count: an invertible complex symmetric Hessian is put in
  Takagi normal form, each one-dimensional chiral oscillator has a unique
  even Gaussian ground state, and the local contribution is `+1` rather than
  the real Morse sign of `Re W`.
- Assembles the conditional pure `SU(N_c)` index and condensate ledger:
  `I_SU(Nc)=N_c` under finite-volume/continuation hypotheses, and the
  glueball `F`-term hypothesis gives the `N_c` nonzero condensate phases and
  `Z_{2N_c}->Z_2`; the text explicitly states that the index alone does not
  prove confinement, a mass gap, or the condensate.
- Derives the allowed ADS superpotential form from dimension and \(R\)-charge
  constraints.
- Adds an explicit logic-of-argument paragraph for \(N=1\) SQCD: the
  \(N_f=N_c-1\) first-principles instanton calculation is the constructive
  seed; zero-mode counting, Yukawa lifting, the radial Higgs cutoff, and the
  invariant-theory denominator are separated before holomorphic mass
  decoupling is used to reach lower \(N_f\).
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
- Proves the finite-dimensional Berezin determinant for the Yukawa lifting
  matrix in the diagonal patch: the block action
  `sum_i a_i chi_i zeta_i + b_i tilde chi_i tilde zeta_i` saturates all
  lifted Grassmann variables, is nonzero exactly on `det M != 0`, leaves the
  two Goldstino modes, and gives an anti-holomorphic determinant factor that
  is explicitly distinguished from the final holomorphic ADS denominator.
- Proves the finite radial Higgs-cutoff estimate used in the ADS
  one-instanton patch:
  `int_0^infty rho^(2p-1) exp(-c H rho^2) d rho
  = (p-1)!/(2(cH)^p)`.  The text records the resulting large-size
  convergence and real homogeneity, and explicitly states that this estimate
  neither extends the calculation across `det M=0` nor determines the
  holomorphic `1/det M` factor.
- Proves the maximal-rank meson invariant used in the ADS denominator:
  an `SL(N_f,C)_L x SL(N_f,C)_R` invariant holomorphic function on
  `det M != 0` is a function of `det M`; the ADS homogeneity degree then
  forces `C/det M`, with the \(R\)-charge check displayed.
- Derives the one-instanton ADS form
  `kappa_Nc Lambda_h^(2N_c+1)/det M` from the instanton scale factor,
  the reduced `d^4x_0 d^2 eta` instanton integral, the proved
  maximal-rank meson invariant, dimension, and \(R\)-charge.
- Proves the holomorphic decoupling equation by matching the invariant
  holomorphic scale at a massive threshold.
- Proves the ADS decoupling recursion: after adding
  `m M^L_L` to the `(n+1)`-flavor ADS superpotential, the light-branch
  one-variable `F_X=0` equation gives the \(n\)-flavor ADS form, the scale
  matching `Lambda_-^(3Nc-n)=m Lambda_+^(3Nc-(n+1))`, and the coefficient
  recursion whose standard normalization is `C_n=N_c-n`.
- Derives pure-SYM branch superpotentials from massive SQCD decoupling:
  for `1 <= n < N_c`, invertible mass matrix `m`, and the standard ADS
  representative, the matrix \(F_M=0\) equation gives
  `m_i^j = Y (M^{-1})^j_i`, hence
  `Y^N_c = det(m) Lambda_n^(3N_c-n) = Lambda_0^(3N_c)` and
  `W_eff,k=N_c Y_k`; differentiating with respect to
  `Lambda_0^(3N_c)` gives the pure-SYM source identity.  The text states
  explicitly that this is a Wilsonian chiral-coordinate elimination,
  conditional on ADS and threshold hypotheses, not a mass-gap theorem.
- Derives the mass-source/Konishi ledger for the same massive SQCD branches:
  the envelope theorem at the holomorphic critical point gives
  `dW_eff/dm_i^j=<M^i_j>`, the matrix \(F_M=0\) equation gives
  `<M^a_j> m_i^j=<S> delta_i^a`, and the trace gives
  `m_i^j <M^i_j>=n<S>`.  The text separates this chiral-coordinate
  realization from the regulator-level local Konishi-current identity.
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
- Derives SQCD conformal-window central charges from the superconformal
  \(R\)-trace formulas:
  `Tr R=-N_c^2-1`, `Tr R^3=N_c^2-1-2N_c^4/N_f^2`, the resulting \(a,c\),
  and the exact free-field comparison factorization
  `a_UV-a_IR=N_c^2(3-y)^2(2y+3)/(48y^2)` with `y=N_f/N_c`, explicitly not
  used as a proof of a general \(a\)-theorem or of flow existence.
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
- Adds explicit deformation tests for the Seiberg-duality field content:
  an electric mass for one flavor maps to a rank-one magnetic Higgs branch
  `SU(N_f-N_c)->SU(N_f-N_c-1)` with the correct light-flavor rank, while a
  rank-`r` electric meson expectation value maps to masses for `r` magnetic
  flavor pairs and leaves the dual rank unchanged as
  `(N_f-r)-(N_c-r)=N_f-N_c`.
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
- Derives the KW beta-function rank count in the
  `SU(2)_A x SU(2)_B x U(1)_B` source chart:
  `B_1=B_2=N(1+gamma_A+gamma_B)` and the quartic-superpotential marginality
  defect is `1+gamma_A+gamma_B`.
- Replaces the previous quoted KW conformal-manifold statement with an
  explicit conditional exact-marginality chart: a holomorphic beta map,
  quotient/fixing of redundant source directions, current/contact-term
  completeness, and nonzero differential of the common defect.  Under these
  assumptions the holomorphic implicit-function theorem gives the
  two-complex-dimensional KW local conformal locus from the three sources
  `(tau_1,tau_2,h)` and one equation `E=0`.
- Performs the KW `a`-maximization calculation for baryonic mixing and
  derives the exact finite-N central charges
  `a=27N^2/64-3/8`, `c=27N^2/64-1/4`.
- Proves the rank-one abelian conifold quotient
  `C[W_ij]/(W_11 W_22 - W_12 W_21)` and records the general commuting
  mesonic branch as `Sym^N(conifold)`.
- Lists protected meson and baryon dimensions from the superconformal
  R-charge, with the monograph's baryon-charge normalization.
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
  KW beta-function rank count for gauge numerators and quartic marginality,
  the KW exact-marginality dimension count and tangent-kernel arithmetic,
  `a`-maximization sign, central charges, conifold determinant relation, KS
  numerator signs, unequal-rank R-anomaly coefficients, Seiberg-dual magnetic
  rank, magnetic meson quadratic-form integration, cascade step count, and
  the `Z_{2M}->Z_2` vacuum count.
- `calculation-checks/susy_n1_pure_sym_checks.py` verifies exact finite
  arithmetic for pure `N=1` SYM: adjoint anomaly coefficient, residual
  discrete chiral group, condensate orbit count, VY dimension/source/F-term
  checks, condensate branch monodromy, one-instanton adjoint zero-mode
  saturation for \(S^{N_c}\), instanton-number selection for separated
  \(S\)-correlators, saturated Berezin coefficient factorial/sign
  conventions, branch independence of the clustered \(N_c\)-point power,
  finite-volume symmetry-basis versus cluster-branch linear algebra,
  affine-Toda product-constraint telescoping, constrained Hessian
  nondegeneracy, local holomorphic chiral-oscillator index convention, local
  critical-point index contribution, and
  affine-Toda/Witten-index count matching.
- `calculation-checks/susy_n1_sqcd_duality_checks.py` verifies exact
  rational arithmetic for the general SQCD duality and phase ledger:
  dual-rank involution, baryon-charge map, SQCD holomorphic-canonical NSVZ
  coordinate-relation algebra, electric/magnetic NSVZ numerator
  cancellation, magnetic gauge-`R` anomaly cancellation, magnetic
  superpotential dimension and \(R\)-charge, SQCD conformal-window
  central-charge and conditional free-field
  \(a_{\mathrm{UV}}-a_{\mathrm{IR}}\) comparison factorization,
  full global anomaly matching,
  mass and Higgs deformation rank/dimension/`R`-charge tests,
  `N_f=N_c+1` confining-superpotential checks, mass decoupling to the
  `N_f=N_c` quantum-modified constraint, massive-SQCD-to-pure-SYM branch
  elimination, source-identity checks, mass-source/Konishi ledger checks,
  and phase-window inequalities.
- `calculation-checks/susy_instanton_nekr_checks.py` verifies exact rational
  arithmetic for the ADS instanton expansion: general ADS dimension and
  \(R\)-charge, `N_f=N_c-1` zero-mode counts, Higgs-patch
  collective-coordinate counts, radial Higgs-cutoff integral scaling,
  Yukawa-lifting Berezin determinant saturation and coefficient
  factorization, determinant-fiber transitivity and inverse-determinant
  homogeneity for the maximal-rank meson invariant, holomorphic decoupling
  exponent shifts, and ADS decoupling-recursion coefficient and one-variable
  `F_X=0` algebra.

## Figure Ledger

No figure is included.  Future diagrams should show the \(N_f<N_c\),
`N_f=N_c`, pure SYM, KW conifold branch, and KS cascade stairway as
chiral-coordinate spaces with their assumptions and anomaly data.

## Audit Notes

- 2026-05-29 anti-wrapper pass: demoted the KW beta-function rank count from
  proposition form to derivation prose.  The calculation remains as the
  local NSVZ/superpotential arithmetic used by the exact-marginality
  hypothesis; the existence and smoothness of the conformal locus remain
  explicit hypotheses.

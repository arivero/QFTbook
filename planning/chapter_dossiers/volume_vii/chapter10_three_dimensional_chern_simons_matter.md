# Chapter 10: Three-Dimensional Chern-Simons-Matter Theories

## Source Position

Volume VII follows the basic supersymmetric gauge-theory and Wilsonian
chapters with the main three-dimensional supersymmetric gauge-theory class
needed for localization and for the ABJM part of issue #588.

Reviewed source spine:

- `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`,
  lines 23220-23320: `3D` `N=2` Chern-Simons-matter field variables and
  component conventions.
- `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`,
  lines 14160-14510: ABJM gauge group, matter, moduli, monopole enhancement,
  and relation to the `C^4/Z_k` branch.
- GitHub issue #588: request for ABJM as a `3D` `N=6/N=8` SCFT, including
  Lagrangian datum, moduli, and localization conventions.
- GitHub issue #594: conformal-manifold worked examples; this chapter supplies
  the ABJM fixed-level ledger inside the SUSY field-theory volume.

## Notation Inventory

- `Q_alpha`, `bar Q_alpha`, `Z`: `3D` `N=2` supercharges and central charge.
- `G`, `P`, `A`, `k`: gauge group, principal bundle, connection, and
  Chern-Simons level.
- `sigma`, `lambda`, `D`: vector-multiplet scalar, fermion, and auxiliary
  field.
- `Phi_i`, `phi_i`, `R`, `W`: chiral multiplets, scalar fields,
  representation, and superpotential.
- `t_R^a`, `mu^a`: representation matrices and non-abelian moment-map
  coordinates in trace-delta normalization.
- `Q`, `tilde Q`, `varphi`, `J^a`: `3D` `N=3` hypermultiplet chirals,
  adjoint chiral, and quadratic current entering the adjoint-chiral
  elimination.
- `mu`, `zeta`, `m_i`: moment map, FI coordinate, and real masses.
- `T(R)`, `m`: representation index and monopole magnetic charge.
- `G_{N,k}`, `A`, `Ahat`: ABJM gauge group and the two gauge connections.
- `A_a`, `B_dot a`: bifundamental and antibifundamental ABJM chiral
  multiplets.
- `C_I`: the four complex scalar variables in the `SU(4)` presentation.
- `mathfrak D`: fixed QFT datum used in the local conformal-manifold
  definition.
- `h_ABJM=2 pi/k`: standard ABJM quartic-superpotential coefficient in this
  chapter's component convention.
- `A_D`, `B`: diagonal and anti-diagonal abelian gauge fields in the
  rank-one abelian quotient calculation.
- `lambda_i`, `mu_i`: `S^3` localization Cartan variables for the two
  `U(N)` gauge factors.
- `F(T)`: renormalized three-sphere free energy `-log |Z_{S^3}(T)|`.
- `mathcal F(R)`: Casini-Huerta renormalized entanglement function for a disk
  of radius `R`.
- `Q^A_B`: finite-regulator inverse free propagator in the planar
  Chern-Simons vector-model light-cone chart.
- `B^A_B`, `G^A_B`, `Sigma^A_B`: singlet bilocal, its leading large-`N`
  expectation, and the corresponding planar self-energy.
- `V^+`, `V^perp`, `K`: current matrices and the light-cone kernel
  `partial_-^{-1}` with the declared zero-mode prescription.

## Claim Ledger

- Defines the `3D` `N=2` algebra and keeps particle representations separate
  from off-shell superfields.
- States the Chern-Simons action, variation, field equation, level/contact
  term obligations, and boundary obligation.
- Proves that in light-cone gauge `A_-=0` the non-abelian Chern-Simons cubic
  term vanishes and the quadratic action is
  `(k/2 pi) int Tr(A_+ partial_- A_perp)`.
- Derives the light-cone current kernel
  `S_eff=-(2 pi/k) int J^+ partial_-^{-1} J^perp` at finite regulator,
  with the zero-mode/Gauss-law datum separated.
- Proves the planar color reduction of the Chern-Simons vector-model current
  kernel in terms of the singlet bilocal `B`, including the `O(N)` leading
  action and `O(1)` trace-subtraction scaling at fixed `lambda=N/k_eff`.
- Derives the finite-regulator planar Schwinger-Dyson equation
  `G(Q+Sigma)=1` and computes `Sigma` as the functional derivative of the
  leading light-cone bilocal interaction.
- Derives the Chern-Simons shifted D-term equation by eliminating the
  auxiliary field.
- Proves the non-abelian pure-Chern-Simons auxiliary equation
  `sigma^a=-(2 pi/k) mu^a` in trace-delta normalization and derives the
  ordered sextic scalar coefficient
  `-4 pi^2/k^2 (bar phi t^a phi)(bar phi t^b phi)(bar phi t^a t^b phi)`.
- Records the convention boundary for the induced `3D` Yukawa signs while
  fixing the coefficient magnitudes and the `1:2` relative factor.
- Proves the `3D` `N=3` adjoint-chiral elimination
  `W=-(k/8 pi) varphi^2+J varphi -> W_eff=(2 pi/k)J^2` as a polynomial
  chiral-ring calculation, independent of any string-theoretic realization.
- Records the parity-anomaly level shift and the Gauss-law electric charge of
  monopole operators.
- Defines ABJM as `U(N)_k x U(N)_{-k}` Chern-Simons-matter theory with four
  bifundamental chirals and quartic superpotential.
- Proves the opposite-level parity bookkeeping under orientation reversal and
  exchange of the two gauge factors.
- Defines a fixed-datum local conformal manifold and applies it to standard
  ABJM, distinguishing quantized levels and contact-term data from continuous
  scalar-primary deformations.
- Proves that the standard `N=6`, `SU(4)`-symmetric ABJM conformal locus at
  fixed `(N,k)` is zero-dimensional: `k` is integral, `h_ABJM=2 pi/k` is then
  fixed, real masses/FI coordinates are dimension-one deformations, and
  Yang-Mills kinetic terms are dimensionful regulator/UV-completion data.
- Proves the rank-one abelian ABJM branch quotient `C^4/Z_k` from the abelian BF
  reduction and residual finite gauge transformation.
- States the general commuting-branch moduli space
  `((C^4/Z_k)^N)/S_N` and `N=8` enhancement for `k=1,2` as a quoted theorem,
  because monopole sectors and global-form data enter.
- Specializes the `S^3` localization formula to ABJM and derives the
  denominator `prod_{i,j} 4 cosh^2(pi(lambda_i-mu_j))` from two conjugate
  bifundamental chiral pairs.
- Defines the renormalized `S^3` free energy with contact-term and framing
  scheme specified, and states the continuum `F`-theorem with its
  entanglement/continuum hypotheses rather than as a matrix-model slogan.
- Proves the endpoint comparison consequence for supersymmetric localized
  fixed points and proves additivity of `F` for product theories.
- Fixes the free chiral value `F_chiral=(1/2) log 2` in the round-sphere
  determinant convention.
- Evaluates the rank-one ABJM matrix integral distributionally:
  `Z_{S^3}^{ABJM}(1,k)=1/(4 |k|)`, hence `F=log(4 |k|)`.

## Calculation Checks

- `calculation-checks/susy_abjm_6d_checks.py` verifies the ABJM
  superpotential `R`-charge, parity action on levels `(k,-k)`, abelian
  BF K-matrix normalization, standard conformal-locus tangent count, `Z_k`
  orbifold order, commuting-branch dimension, and the `S^3` matrix-model
  denominator powers.  It also checks the free-chiral determinant
  normalization and the rank-one ABJM `S^3` integral factors.
- The same script verifies the non-abelian `3D` `N=2`
  Chern-Simons-matter `D`/`sigma` elimination coefficients, the
  convention-independent Yukawa magnitude ratio, and the `3D` `N=3`
  adjoint-chiral elimination coefficient.
- `calculation-checks/cs_matter_lightfront_checks.py` verifies the
  light-cone Chern-Simons quadratic factor, the first-order Gaussian source
  sign, trace-delta planar color scaling, the planar exchange and bilocal
  saddle scalings, the finite-matrix derivative of the bilocal interaction
  giving the self-energy, and the index convention in `G(Q+Sigma)=1`.

## Proof Obligations And Boundaries

- A fully rigorous continuum construction of `3D` supersymmetric
  Chern-Simons-matter theories remains open in the chapter.
- The planar self-energy equation is a leading large-`N` finite-regulator
  Schwinger-Dyson equation.  A future pass must solve the continuum integral
  equations in specific bosonic and fermionic conformal charts, including mass
  and contact-term tuning.
- The general ABJM moduli and supersymmetry-enhancement statements are kept
  as quoted theorem status because they use quantum monopole sectors and
  global-form data beyond the polynomial `N=2` Lagrangian.
- Future depth passes should add line-operator lattices, one-form symmetries,
  explicit monopole charge formulae, and background Chern-Simons contact-term
  matching for ABJM dualities.
- A future spinor-convention pass should choose one global `3D` Hermiticity
  convention for all component Yukawa signs and then upgrade the current
  coefficient-magnitude ledger to a signed formula.
- The zero-dimensional conformal-locus result is intentionally restricted to
  the standard `N=6`, `SU(4)` ABJM datum.  Less-symmetric `N=2`
  Chern-Simons-matter marginal candidates require their own beta-function,
  current-moment-map, and monopole-sector analysis.

## Figure Ledger

No figure is included in this pass.  Future figures should include monopole
flux spheres, CS Gauss-law dressing, the ABJM diagonal/anti-diagonal abelian
quotient, and the two-matrix `S^3` localization contour.

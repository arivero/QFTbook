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

## Claim Ledger

- Defines the `3D` `N=2` algebra and keeps particle representations separate
  from off-shell superfields.
- States the Chern-Simons action, variation, field equation, level/contact
  term obligations, and boundary obligation.
- Derives the Chern-Simons shifted D-term equation by eliminating the
  auxiliary field.
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

## Calculation Checks

- `calculation-checks/susy_abjm_6d_checks.py` verifies the ABJM
  superpotential `R`-charge, parity action on levels `(k,-k)`, abelian
  BF K-matrix normalization, standard conformal-locus tangent count, `Z_k`
  orbifold order, commuting-branch dimension, and the `S^3` matrix-model
  denominator powers.

## Proof Obligations And Boundaries

- A fully rigorous continuum construction of `3D` supersymmetric
  Chern-Simons-matter theories remains open in the chapter.
- The general ABJM moduli and supersymmetry-enhancement statements are kept
  as quoted theorem status because they use quantum monopole sectors and
  global-form data beyond the polynomial `N=2` Lagrangian.
- Future depth passes should add line-operator lattices, one-form symmetries,
  explicit monopole charge formulae, and background Chern-Simons contact-term
  matching for ABJM dualities.
- The zero-dimensional conformal-locus result is intentionally restricted to
  the standard `N=6`, `SU(4)` ABJM datum.  Less-symmetric `N=2`
  Chern-Simons-matter marginal candidates require their own beta-function,
  current-moment-map, and monopole-sector analysis.

## Figure Ledger

No figure is included in this pass.  Future figures should include monopole
flux spheres, CS Gauss-law dressing, the ABJM diagonal/anti-diagonal abelian
quotient, and the two-matrix `S^3` localization contour.

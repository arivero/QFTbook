# Chapter 07: Twists of Supersymmetric Theories

## Source Position

This chapter follows the cohomological-field-theory and topological
sigma-model chapters.  It supplies the representation-theoretic and
regulator-level meaning of a supersymmetric twist before the later
Witten-Donaldson chapter uses the Donaldson twist as a four-dimensional
cohomological gauge theory.

## Notation Inventory

- `Spin(d)`: Euclidean rotation group.
- `G_R`: compact internal R-symmetry group.
- `rho`: twisting homomorphism `Spin(d) -> G_R`.
- `Spin(d)_rho`: diagonal twisted rotation group.
- `Q`: scalar odd supercharge after twisting.
- `Q_Lambda`: regulated scalar odd symmetry.
- `lambda_Q`, `alpha_Q`, `v_Q`: gauge, flavor, and vector-field parameters
  appearing in the closure relation for `Q^2`.
- `P_R(M)`: R-symmetry background bundle induced by the twist.
- `F_Lambda^rho`, `Gamma_Lambda^rho`, `A_Lambda^rho`: regulated field space,
  integration cycle, and observable algebra of the twisted theory.
- `SU(2)_+`, `SU(2)_-`, `SU(2)_R`, `U(1)_r`: four-dimensional rotation and
  R-symmetry factors for `N=2` supersymmetry.
- `A`, `phi`, `bar phi`, `psi`, `eta`, `chi^+`, `H^+`: Donaldson-Witten
  twisted vector-multiplet fields.
- `q_V`, `q_A`: vector and axial R-charges in two-dimensional `N=(2,2)`
  theories.

## Claim Ledger

- Defines twisting as restriction of
  `Spin(d) x G_R` representations to the diagonal subgroup determined by
  `rho`.
- Describes the curved-manifold implementation through the induced
  R-symmetry background bundle `P_R(M)`.
- Defines scalar twisting supercharges and states the precise closure
  condition `Q^2 = gauge + flavor + Lie derivative`.
- Lists regulator-level twist data, including anomaly, integration-cycle,
  BV/field-space, and contact-term requirements.
- Proves the metric-independence criterion for twisted correlators from the
  regulated Ward identity and `Q`-exact metric response.
- Gives the four-dimensional `N=2` supercharge representations and proves
  the Donaldson-twist decomposition into scalar, one-form, and self-dual
  two-form supercharges.
- Decomposes the `N=2` vector multiplet into Donaldson-Witten differential
  forms.
- States the Donaldson-Witten `Q` transformations and proves off-shell
  closure `Q^2=delta_{-phi}`.
- Constructs the Mathai-Quillen gauge-fermion term that localizes to
  `F_A^+=0` and links it to the ASD deformation complex.
- Derives the Donaldson descent package from the universal equivariant
  curvature `F_A + psi + phi`.
- Gives the two-dimensional `N=(2,2)` charge table and identifies the scalar
  A- and B-twist supercharges.
- States the remaining continuum construction problem for twisted
  supersymmetric gauge theories.

## Calculation Ledger

- `calculation-checks/twisting_representation_checks.py` verifies the
  `SU(2)` Clebsch-Gordan arithmetic for the Donaldson twist, the twisted
  gaugino form dimensions, the two-dimensional A/B scalar-supercharge charge
  bookkeeping, and the Donaldson-Witten `Q^2=delta_{-phi}` closure ledger.

## Figure Ledger

No figure is included.  A later figure pass should add a compact diagram of
the diagonal `SU(2)_+ x SU(2)_R -> SU(2)'_+` embedding and a table comparing
untwisted spinor indices with twisted differential forms.

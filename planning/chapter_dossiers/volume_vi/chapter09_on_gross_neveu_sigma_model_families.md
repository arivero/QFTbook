# Chapter 09: `O(N)`, Gross-Neveu, And Sigma-Model Families

## Source Position

Volume VI moves from sine-Gordon, Thirring, and affine Toda examples to
asymptotically free two-dimensional families with nonabelian internal
symmetry.

## Notation Inventory

- `G`, `V`, `rho`: compact internal symmetry group, particle representation,
  and representation map.
- `S_VV(theta)`, `S_R(theta)`: two-particle scattering operators and channel
  eigenvalues.
- `sigma_1`, `sigma_2`, `sigma_3`, `Delta`, `z`: exact `O(N)` sigma-model
  vector S-matrix coefficient functions and gamma-function variables.
- `P_0`, `P_S`, `P_A`: singlet, symmetric-traceless, and antisymmetric
  projectors for the `O(N)` vector tensor square.
- `n`, `g`, `lambda`, `M`: nonlinear sigma-model field, kinetic coupling,
  large-`N` 't Hooft coupling, and dynamically generated mass.
- `psi^i`, `sigma`, `lambda_GN`: Gross-Neveu Majorana fermions, auxiliary
  scalar, and large-`N` coupling.
- `K_R(theta)`: TBA kernel derived from a channel eigenvalue.

## Claim Ledger

- Decomposes nonabelian two-particle scattering through representation theory.
- Derives the `O(N)` projector basis for invariant two-particle amplitudes.
- Displays the exact minimal `O(N)` sigma-model vector S-matrix in index form,
  with the gamma-function expression for `sigma_2` and the rational relations
  defining `sigma_1` and `sigma_3`.
- Identifies the Zamolodchikov-Faddeev Yang-Baxter component convention and
  the scalar-free rational `O(N)` tensor underlying factorization.
- Proves channel unitarity and crossing for the exact S-matrix by reducing the
  checks to the gamma recurrence and elementary rational identities.
- Defines the `O(N)` sigma-model ultraviolet datum and records the one-loop
  Ricci beta tensor relation.
- Derives the large-`N` sigma-model gap equation and the leading
  asymptotic-freedom beta function for the 't Hooft coupling.
- Introduces the Gross-Neveu auxiliary-field representation and derives the
  large-`N` mass-gap equation with the explicit `N` factor in the fermion
  determinant.
- Develops the model-specific nested-string source data for the `SU(N)` chiral
  Gross-Neveu and principal-chiral families: one `A_{N-1}` auxiliary nest for
  chiral Gross-Neveu, left/right doubled nests for the principal chiral model,
  the inverse-Cartan root-count ledger, concrete `SU(3)` and `SU(4)` examples,
  and the precise `N`-ality integrality obstruction.
- States the matching conditions between asymptotically free UV data,
  factorized scattering, form factors, and TBA kernels.

## Calculation Checks

- `calculation-checks/on_sigma_gn_checks.py` verifies the `O(N)` sigma-model
  gamma-function scalar identity, channel unitarity, crossing relations,
  finite-dimensional Yang-Baxter component identity, and the large-`N` cutoff
  gap equation and beta-function algebra.
- `calculation-checks/sigma_model_family_checks.py` verifies the `SU(N)`
  sine-mass bootstrap identities, rational matrix block, gamma-function scalar
  unitarity ledgers, and the exact `A_{N-1}` nested root-count and
  principal-chiral left/right doubling formulas.

## Anti-Wrapper Audit

- 2026-05-29 ninth pass: demoted the projective crossing tensor identity from
  proposition form to component-convention prose.  The crossing functions and
  tensor identifications remain explicit because they fix the later
  projective-channel unitarity checks, but the proof is only an index
  substitution once the convention is declared.

## Figure Ledger

No figure is included in this pass.  Future figures should include the
`O(N)` channel decomposition, Gross-Neveu auxiliary-field saddle, and TBA
kernel flow from scattering eigenvalues.

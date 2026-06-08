# Chapter 09: `O(N)`, Gross-Neveu, And Sigma-Model Families
Source-File: monograph/tex/volumes/volume_vi/chapter09_on_gross_neveu_sigma_model_families.tex

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
- States that continuous internal symmetry in the \(1+1\)-dimensional
  families labels multiplets, currents, and scattering tensors rather than an
  undeclared broken continuous order parameter; possible discrete order is a
  separate problem not covered by Coleman's theorem.
- Derives the `O(N)` projector basis for invariant two-particle amplitudes.
- Displays the exact minimal `O(N)` sigma-model vector S-matrix in index form,
  with the gamma-function expression for `sigma_2` and the rational relations
  defining `sigma_1` and `sigma_3`.
- Identifies the Zamolodchikov-Faddeev Yang-Baxter component convention and
  the scalar-free rational `O(N)` tensor underlying factorization.
- Checks channel unitarity and crossing for the exact S-matrix by reducing
  them to the gamma recurrence and elementary rational identities.
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
- 2026-05-30 anti-wrapper continuation: demoted the nested root-count ledger
  from lemma/proof form to derivational prose.  The inverse-Cartan singlet
  condition and \(N\)-ality integrality obstruction remain as the weight-space
  input for the TBA source vector, but the text no longer pretends that this
  bookkeeping is a theorem-level result.
- 2026-05-31 issue #691 continuation: demoted "Channel unitarity and
  crossing" from proposition/proof form to a normalization-check paragraph.
  The channel decomposition, gamma-function recurrence, and rational
  singlet/symmetric/antisymmetric checks remain explicit because they fix the
  exact \(O(N)\) sigma-model S-matrix conventions, but the argument is a
  convention-sensitive verification of an already displayed meromorphic
  tensor rather than an independent theorem.
- 2026-05-31 issue #691 continuation: demoted "Repulsive-sausage strip
  analyticity and block unitarity" from proposition/proof form to a
  paragraph-level bootstrap consistency check.  The denominator zero analysis
  and \(Q=2,1,0\) block-unitarity identities remain in the text and in the
  paired calculation script, while the constructive local-QFT realization
  question remains separated in the sausage bootstrap matching remark.
- 2026-05-31 issue #691 continuation: demoted "Analytic uniqueness of a
  matched two-particle kernel" from proposition/proof form to an analytic
  matching paragraph.  The boundary-value uniqueness derivation remains
  explicit, but the text now assigns the real mathematical burden to the
  regulator realization: neutral Haag--Ruelle scattering, meromorphic boundary
  control, pole/residue matching, finite-volume data, and form-factor data.
- 2026-06-04 issue #770 re-audit: added the Coleman continuous-symmetry
  guardrail for the \(O(N)\), Gross--Neveu, and sigma-model families, while
  leaving discrete chiral phase-selection questions separate.
- 2026-06-08 issue #844 semantic-status pass: demoted the projective
  scattering, supercoset status, and sausage bootstrap matching blocks
  from `controlledapproximation` to remarks.  They organize bootstrap and
  regulator-realization obligations, but they do not yet provide component
  error estimates.

## Figure Ledger

No figure is included in this pass.  Future figures should include the
`O(N)` channel decomposition, Gross-Neveu auxiliary-field saddle, and TBA
kernel flow from scattering eigenvalues.

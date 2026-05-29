# Volume IV Proof-Substance Audit

Date: 2026-05-28.

Scope: `monograph/tex/volumes/volume_iv`.

Standard applied: a theorem, proposition, corollary, or lemma is retained only
when the adjacent or explicitly referenced argument constructs the object,
checks the hypotheses, proves the estimate, or performs the claimed reduction.
Major external functional-analytic or operator-algebra inputs are marked as
`quotedtheorem`.

## Repairs Made

- `chapter01_wightman_fields_and_reconstruction.tex`: expanded
  `thm:wightman-reconstruction` into an actual proof block.  The construction
  now checks the null quotient, the unitary Poincare representation, spectral
  support, locality, field construction, and uniqueness of the reconstructed
  Wightman representation.
- `chapter02_osterwalder_schrader_reconstruction.tex`: converted
  `prop:polynomial-tube-bounds-boundary-values` to a quoted theorem.  The
  boundary-value theorem and cone-support Paley-Wiener input are several
  complex variables/distribution theory inputs, not proved in the manuscript at
  that point.
- `chapter03_algebraic_qft_local_nets_and_states.tex`: retained the theorem and
  proposition labels after reading the proofs.  The Wightman-to-AQFT statement
  is explicitly conditional on essential self-adjointness and strong locality of
  closures; the proof checks the local algebra construction rather than
  asserting an unconditional Wightman-to-net theorem.
- `chapter04_superselection_sectors_and_locality_properties.tex`: converted the
  Doplicher-Roberts reconstruction theorem, Tomita-Takesaki theorem, Connes
  cocycle theorem, nuclearity consequences, and Borchers-Wiesbrock structure
  theorem to `quotedtheorem`.  The finite type-I Connes computation and the
  Borchers commutator differentiation are retained only as local checks of
  displayed formulae.
- `chapter05_haag_ruelle_and_mathematical_scattering.tex`: added an explicit
  proof of the main Haag-Ruelle theorem as a reduction to the estimate package
  and its verification by stationary phase, almost locality, and spectral
  isolation.  Demoted the direct-integral velocity-fiber diagonality statement
  from proposition to remark because its proof only unpacks the definition of
  the direct-integral representation.
- `chapter06_kontsevich_segal_functorial_qft.tex`: retained the proof labels
  after reading them.  The allowability criterion is proved by real
  diagonalization and argument estimates; the cylinder positive-energy theorem
  reduces reflection positivity to the positive-generator semigroup theorem;
  the K-S-to-OS statement is conditional on the required flat-space tempered,
  reflection-positive, and spectral inputs.  The Lorentzian boundary
  construction remains a quoted theorem.

## Remaining Proof Obligations

- A fully self-contained proof of Haag-Ruelle scattering from the Wightman or
  Haag-Kastler axioms would require expanding the estimate package into a longer
  appendix, including the detailed finite-energy propagation bounds and the
  standard construction of regular creators from Arveson spectral transfer.
  The current chapter now states exactly where those estimates enter and proves
  the Hilbert-space conclusion from them.
- The operator-algebra structure theorems in Chapter 4 are correctly marked as
  quoted inputs.  A future appendix could prove selected modular-theory results
  if the monograph chooses to make Tomita-Takesaki or Connes theory
  self-contained.

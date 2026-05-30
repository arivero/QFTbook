# Chapter 01: Wightman Fields and Reconstruction

## Source Position

This chapter fixes the Lorentzian Hilbert-space field-presentation framework
used by the foundational volumes.  Its central object is now the cyclic
Wightman field presentation of
`def:cyclic-wightman-field-presentation`: Hilbert space, vacuum, Poincare
representation, common invariant domain, field-label adjunction and parity,
operator-valued tempered distributions, covariance, spectrum, graded locality,
and cyclicity.  The definition is explicitly tied to the framework-level
presentation `def:wightman-field-presentation-opening` in the opening
volume; this chapter specializes that framework to the cyclic tempered
Minkowski setting used in the reconstruction theorem.

## Notation Inventory

- `M = M^D`: Minkowski spacetime with mostly-plus metric.
- `Poinc`: proper orthochronous Poincare group.
- `V_+`, `overline V_+`: open and closed forward momentum cones.
- `mathfrak W`: cyclic Wightman field presentation.
- `H`, `Omega`, `U`, `D`: Hilbert space, vacuum, Poincare representation, and
  common invariant domain.
- `E_I`, `J`, `|.|`: field-label space, antilinear adjunction, and parity.
- `Phi_alpha(f)`: smeared operator-valued tempered distribution.
- `E_P`, `P_0`: joint spectral measure of translations and zero-momentum
  projection.
- `W_n`: vacuum Wightman distribution hierarchy.
- `N_W`: null subspace in the reconstruction pre-Hilbert space.
- `Theta_PCT`: antiunitary PCT operator.
- `P_Phi(O)`, `R_Phi(O)`: unbounded polynomial local field algebra and
  generated/affiliated represented von Neumann algebra when closure
  hypotheses are supplied.

## Claim Ledger

- Defines the cyclic Wightman field presentation before any theorem uses the
  term, separating the base presentation from the stronger pure-vacuum-sector
  condition.
- Explains that Hermitian real smearings are symmetric on the common domain,
  while essential self-adjointness and affiliation with local von Neumann
  algebras are additional analytic hypotheses.
- Distinguishes field coordinatizations from local observable nets; equality
  of the generated field algebra and a supplied net requires a comparison
  theorem, not notation.
- Defines the Wightman hierarchy, adjunction reversal on tensor-valued tests,
  covariance, spectral support, Hermiticity, locality, and positivity.
- Proves the cluster/unique-vacuum equivalence from the spectral theorem,
  locality, the Jost edge argument, and the Rajchman property for local matrix
  coefficients.
- States and proves Wightman reconstruction by finite test sequences, the
  positive semidefinite Wightman inner product, quotient by null vectors,
  completion, left-insertion fields, covariance, spectrum, adjunction,
  locality, cyclicity, and uniqueness.
- Develops the Wightman tube-analyticity mechanism from spectral support,
  covariance, and locality at Jost configurations.
- States the PCT theorem in four dimensions and sketches the proof by the
  Jost analytic identity followed by construction of the antiunitary on the
  reconstructed finite-sequence domain.
- Defines observable Wightman subpresentations for gauge theories as positive
  physical Hilbert-space field presentations affiliated with the specified
  observable local net.

## Proof Obligations And Boundaries

- The definition is a field presentation, not a construction of an interacting
  model.  Concrete models must still construct the Hilbert space, domain,
  fields, and Wightman distributions or obtain them by OS reconstruction.
- The pure vacuum sector is not an axiom of the base cyclic presentation; it
  is equivalent to weak clustering under the stated Wightman assumptions.
- Closure, essential self-adjointness, bounded functional calculus, and
  affiliation with local algebras are not automatic consequences of
  unbounded-field data.
- The PCT theorem still has a proof-reference boundary for the full Jost
  analytic machinery, although the chapter explains the distributional and
  Hilbert-space construction steps used by the theorem.
- Wightman-to-AQFT comparison requires extra closure and affiliation
  hypotheses and is developed separately in the AQFT chapter.

## Figure Ledger

- `fig:wightman-fields-to-local-algebras`: compares the unbounded-field route
  to observable algebras with the local-net route and marks the required
  comparison theorem.
- `fig:wightman-reconstruction`: finite test-function sequences, null
  quotient, Hilbert completion, and fields by left insertion.
- `fig:wightman-tube-analyticity`: spectral tube, extended tube, and Jost edge
  where locality identifies boundary values.

## Calculation Checks

- No numerical calculation script is attached to this chapter.  Verification
  is by LaTeX build, text audit, theorem-form audit, and proof-ledger review.

## Audit Notes

- 2026-05-30 issue #700 defining-property pass: added the upfront cyclic
  Wightman field presentation definition, separated pure-vacuum-sector
  uniqueness from the base Wightman data, redirected cluster, reconstruction,
  PCT, and observable-subpresentation prose to the named definition, and added
  this dossier so the foundational Wightman object is tracked explicitly.
- 2026-05-30 issue #701 navigation pass: cross-linked the detailed cyclic
  Wightman definition back to the opening framework-level Wightman
  presentation so the two definitions have an explicit specialization
  relation.

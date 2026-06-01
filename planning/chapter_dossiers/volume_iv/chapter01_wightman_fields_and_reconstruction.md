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
- `T_{n-1}=\{z_j=\xi_j-\ii\eta_j,\ \eta_j\in V_+\}`: mostly-plus forward
  Wightman tube in difference variables.
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
- Isolates the finite projection algebra in the cluster theorem: the cluster
  bilinear identity on the dense polynomial orbit is equivalent, by continuity
  of \(P_0\), to \(P_0=|\Omega\rangle\langle\Omega|\), while the analytic
  content remains the Jost/Rajchman decay after the vacuum atom is removed.
- States and proves Wightman reconstruction by finite test sequences, the
  positive semidefinite Wightman inner product, quotient by null vectors,
  completion, left-insertion fields, covariance, spectrum, adjunction,
  locality, cyclicity, and uniqueness.
- Develops the Wightman tube boundary-value package from spectral support:
  Fourier--Laplace holomorphy in the mostly-plus convention
  \(z=\xi-\ii\eta\), distributional boundary convergence, polynomial
  normal-growth estimates, complex Lorentz extension, and the QFT-specific
  locality input needed for distributional edge-of-the-wedge gluing at Jost
  configurations.
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

- `calculation-checks/wightman_cluster_spectral_checks.py`: exact finite
  Hilbert-space check for the cluster/vacuum-uniqueness theorem, covering the
  zero-momentum projection algebra, the equivalence between the cluster
  bilinear identity on a dense orbit and the rank-one vacuum projection, the
  product contribution of the vacuum atom, and removal of the zero atom by
  \((1-P_0)\).  This check does not certify the analytic Jost/Rajchman
  theorem used to prove decay of the non-vacuum spectral part.

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
- 2026-05-30 Wightman tube-sign pass: aligned the analytic-continuation
  section and Figure `fig:wightman-tube-analyticity` with the mostly-plus
  spectral-support convention \(z=\xi-\ii\eta\), \(\eta\in V_+\), matching
  the Lorentzian Green-functions and Reeh--Schlieder chapters.
- 2026-06-01 Wightman boundary-value proof pass: expanded the tube-analyticity
  paragraph into Proposition `prop:wightman-tube-boundary-value-package`,
  proving the QFT-specific spectral-support, boundary-value, covariance, and
  locality inputs in place while cross-referencing the analytic
  edge-of-the-wedge theorem used for the final gluing step.
- 2026-06-01 Wightman cluster projection pass: isolated the finite
  zero-momentum projection algebra in
  `thm:wightman-cluster-vacuum-uniqueness` and added
  `wightman_cluster_spectral_checks.py` so the product-vacuum term and
  rank-one projection equivalence are reproducible apart from the
  analytic Jost/Rajchman theorem boundary.

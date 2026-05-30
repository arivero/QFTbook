# Issue #288 CFT Reconstruction From OPE Data Pass

## Scope

- Addressed GitHub issue #288:
  `[Vol V Ch 9] CFT reconstruction theorem from OPE data not stated`.
- Target chapter:
  `monograph/tex/volumes/volume_iii/chapter09_operator_product_expansion.tex`.

## Content Added

- Added Section `sec:cft-reconstruction-from-ope-data`.
- Defined an abstract radial OPE datum:
  primary labels, conformal modules with null quotients, radial inner product,
  two-point pairings, three-point tensor structures and coefficients,
  convergent tree-level OPE series, channel compatibility for all OPE trees,
  Euclidean covariance, radial reflection positivity, and contact-term
  prescriptions.
- Added a conditional reconstruction block from a fully specified abstract
  radial OPE datum.
- Retrospective correction on 2026-05-30: this block is no longer a
  theorem-family statement.  It is now Construction
  `cons:conditional-cft-reconstruction-from-ope`, because the hard analytic
  and higher-coherence inputs are already part of the abstract radial OPE
  system.  The text verifies the assembly and patching of separated
  correlators from those inputs rather than presenting the input package as a
  theorem.
- Added Open Problem `op:bootstrap-completeness-from-ope-data`, separating the
  conditional construction from the inverse problem of reconstructing a full
  CFT from complete all-primary four-point OPE data, or complete
  generator four-point OPE data, together with unitarity, positivity, and
  four-point associativity constraints in \(D>2\).

## Verification Targets

- The reconstruction statement must not identify a single four-point crossing
  equation with existence of a CFT or uniqueness of that correlator.
- The discussion must distinguish exact complete all-primary/generator
  four-point OPE data, which may be rigid enough to determine the theory under
  additional hypotheses, from an isolated bootstrap equation.
- The construction must specify the extra hypotheses required to construct
  correlators: all-tree compatibility, convergence, positivity, contact terms,
  and Lorentzian boundary-value data when a Wightman theory is claimed.
- The OPE chapter dossier must record the theorem and the open problem.

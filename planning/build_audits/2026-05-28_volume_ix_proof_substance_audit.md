# Volume IX Proof-Substance Audit

Date: 2026-05-28.

Scope: `monograph/tex/volumes/volume_ix`.

This pass read the proof bodies in the global-symmetry, extended-operator,
boundary, defect, gauging, and symmetry-TFT volume.  The main repairs remove
theorem-like status from finite cochain identities, definition-unpacking
criteria, and fusion-ring arithmetic whose proof is useful but too immediate
to be presented as a proposition.

## Repairs Made

- `chapter05_discrete_theta_terms.tex`: demoted coboundary invariance on
  closed manifolds, the Pontryagin-square quadratic-refinement phase, and the
  discrete-theta line-lattice tilt to remarks.  The fractional \(PSU(N)\)
  instanton-number statement remains a proposition because the proof checks
  the projective characteristic class and its invariance under tensoring by a
  line bundle.
- `chapter06_anomaly_inflow_invertible_field_theories.tex`: demoted the
  anomaly-line cocycle law, local-counterterm ambiguity, finite higher-form
  bulk variation, wall trivialization criterion, and gauging/anomaly-line
  criterion to remarks.  Their calculations remain explicit, but the
  theorem-like signal is reserved for gluing of anomaly lines,
  Chern-Weil transgression, descent consistency, and convention-sensitive
  abelian inflow coefficients.
- `chapter08_boundaries_and_defects.tex`: demoted the Ising
  noninvertibility/fusion-dimension calculation and the inflow-line
  trivialization criterion to remarks.
- `chapter09_categorical_symmetry_and_defect_fusion.tex`: demoted the Ising
  defect quantum dimensions and the fusion action on local sectors to
  remarks.  They are finite fusion-ring checks, not independent theorems.
- `chapter10_duality_defects_and_gauging.tex`: demoted disjoint-union
  multiplicativity of the finite groupoid sum and the \(S,T\)-wall pairing
  preservation check to remarks.
- `chapter11_higher_group_symmetry_symmetry_tft.tex`: demoted closed-manifold
  gauge invariance of the finite cochain action to a remark.  The previous
  theorem titled `QED noninvertible chiral defects` had no proof environment
  and has been downgraded to a controlled approximation/construction
  statement, with the text now saying that a fully axiomatic theorem would
  require constructing compact QED, line sectors, and defect Hilbert spaces in
  a nonperturbative framework.

## Statements Retained

- Global-form and line-lattice results were retained where the proof uses
  central characters, Schur's lemma, finite Dirac pairings, maximal
  isotropicity, and explicit orthogonal-complement calculations.
- Extended-operator statements were retained where the proof derives shape
  variation from the stress-tensor Ward identity, proves the displacement
  criterion as a distributional statement, or computes higher-form Ward action
  by linking/intersection pairing.
- Renormalized Wilson-'t Hooft line statements were retained where the proof
  constructs the cocharacter singularity, computes the mutual locality phase,
  identifies screening by root/coroot charges, or classifies Cartan surface
  singularities modulo Weyl/cocharacter shifts.
- Confinement and phase statements were retained where the proof uses a
  screened finite quotient, transfer-matrix spectral extraction, endpoint
  variational bounds, Haar projection in strong coupling, or uniformly
  convergent cluster expansions.
- Anomaly-inflow statements were retained where the proof uses gluing of
  invertible bulk theories to construct anomaly lines, Chern-Weil
  transgression, descent/Wess-Zumino consistency, or explicit abelian
  gauge-gravitational inflow coefficients.
- Defect-category statements were retained where the proof establishes the
  displacement null quotient, fusion action by shrinking limits, reflection
  adjoints, dagger-category positivity, regular algebra identities, and
  self-dual finite gauging fusion rings.
- Gauging and duality-defect statements were retained where the proof derives
  slab fusion by a finite gauge sum, pair-of-pants holonomy selection,
  self-dual gauging noninvertibility, and residual quotient symmetry after
  normal-subgroup gauging.

## Remaining Proof Obligations

- The QED noninvertible chiral-defect construction is still a compact
  path-integral construction, not an axiomatic theorem of an already
  constructed four-dimensional QFT.  A future theorem would need a
  nonperturbative construction of compact QED with no dynamical monopoles,
  its magnetic one-form symmetry sectors, and its defect Hilbert spaces.
- Finite higher gauging is quoted as a finite topological/defect-network
  theorem.  The monograph currently proves the local finite cochain fusion
  mechanism; a complete QFT theorem requires constructing the relevant
  one-form symmetry surfaces, junctions, and anomaly trivializations in each
  interacting theory.
- The gauge-Higgs analytic-corridor statement remains a conditional
  cluster-expansion result.  The proof gives the analytic-continuation
  mechanism under uniform convergence; the existence of the corridor is a
  separate constructive input.
- Strong-coupling confinement remains a controlled lattice-regime mechanism.
  Promoting it to a continuum confinement theorem requires a continuum limit,
  mass-gap/infrared control, and renormalized line operators with stable
  asymptotics.

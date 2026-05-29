# Volume VII Proof-Substance Audit

Date: 2026-05-28.

Scope: `monograph/tex/volumes/volume_vii`.

This pass read the proof bodies in Volume VII rather than only scanning for
environment names.  The criterion used was the current monograph standard:
theorem-like form is reserved for statements whose proof constructs an object,
computes a convention-sensitive result, proves a representation-theoretic or
geometric classification, or derives an estimate under explicit hypotheses.
Statements whose proof only unpacks a definition, performs one-line algebra,
or records a useful but immediate diagnostic were demoted to remarks or
controlled approximations.

## Repairs Made

- `chapter01_supersymmetry_algebras_and_representations.tex`: demoted the
  equal-boson-fermion supertrace count to a remark.  The grading count remains
  in the exposition, but it does not carry independent theorem weight.
- `chapter05_nonrenormalization_holomorphy.tex`: demoted the perturbative
  Wilsonian superpotential statement to a controlled approximation.  The text
  now makes clear that a theorem-level claim requires a specified
  supersymmetric regulator or BV pushforward scheme, not only the usual
  diagrammatic holomorphy argument.
- `chapter06_four_dimensional_n1_gauge_dynamics.tex`: demoted the pure-SYM
  instanton cluster extraction, the s-confining superpotential checks, and two
  Klebanov-Witten arithmetic normalizations to remarks.  The computations are
  retained, but the theorem signal is reserved for statements with actual
  anomaly matching, decoupling, F-term elimination, instanton, index, or branch
  construction content.
- `chapter09_two_dimensional_supersymmetric_models.tex`: demoted the A/B twist
  scalar-supercharge spin table and the abelian duality Hessian inversion to
  remarks.  Both remain useful local calculations, but their proof bodies were
  bookkeeping rather than domain theorems.
- `chapter10_three_dimensional_chern_simons_matter.tex`: demoted the
  Chern-Simons \(D\)-term square completion, the \(\mathcal N=3\) adjoint
  chiral elimination, the zero-dimensional ABJM conformal-locus diagnostic,
  and the supersymmetric \(F\)-theorem product comparison to remarks.
- `chapter11_six_dimensional_superconformal_theories.tex`: demoted the
  six-dimensional Yang-Mills coupling dimension count and the ADE anomaly
  table arithmetic to remarks.  They remain as convention checks, but not as
  propositions.
- `chapter12_planar_n4_spectral_problem_spin_chains.tex`: demoted the
  one-loop beta-function cancellation bookkeeping, the local conformal
  manifold dimension count, the duality quotient, and the restriction of the
  \(SO(6)\) Hamiltonian to the \(SU(2)\) sector to remarks.
- `chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`: demoted the
  hexagon bridge-length formula and the cusp-as-defect-ground-state-energy
  interpretation to remarks.  The main analytic and finite-difference
  constructions in the QSC section remain theorem-level.
- `chapter16_supersymmetric_localization_compact_manifolds.tex`: demoted the
  Uhlenbeck stratum dimension count and the Bremsstrahlung derivative algebra
  to remarks, repaired stale cross-references, and removed duplicated prose in
  the ADHM small-instanton discussion.

## Statements Retained

- Supersymmetry algebra and representation-theory statements were retained
  where the proof explicitly constructs oscillator modules, massless helicity
  pairs, central-charge tensor structure, or the BPS singular-value bound.
- Superspace, superfield, and supersymmetric gauge-theory component formulae
  were retained where the proof computes component transformations, chiral
  \(F\)-term coefficients, Wess-Zumino gauge representatives, curvature
  covariance, auxiliary-field elimination, or anomaly cancellation with the
  stated conventions.
- BV/Wilsonian supersymmetric scheme results were retained where the proof
  uses the BV Laplacian/Stokes identity, quantum master equation, semigroup
  pushforward, or an explicit finite-dimensional Darboux-circle model.
- Four-dimensional \(\mathcal N=1\) and \(\mathcal N=2\) gauge-dynamics
  propositions were retained where the proof performs NSVZ coordinate
  differentiation, branch/source normalization, instanton zero-mode counting,
  Berezin saturation, decoupling, holomorphic elimination, index computation,
  Picard-Lefschetz transformation, Seiberg-Witten curve degeneration, ADHM
  counting, or Nekrasov fixed-point calculation.
- Two-dimensional supersymmetric-model statements were retained where the
  proof computes Jacobi rings, residue pairings, topological \(A\)-model
  constant maps, duality from a first-order path integral, Coulomb critical
  equations, and GLSM chamber quotients.
- Three-dimensional Chern-Simons-matter statements were retained where the
  proof derives the light-cone quadratic action/current kernel, planar color
  reduction, finite-regulator Schwinger-Dyson equation, ABJM rank-one quotient,
  sphere-integral reduction, trace-class Fermi-gas kernel, Fredholm expansion,
  phase-space coefficient, or Airy transform.
- Planar \(\mathcal N=4\) integrability statements were retained where the
  proof performs nontrivial Zhukovsky continuation, crossing monodromy, DHM
  residue continuation, Bethe-Yang density counting, nested Bethe equation
  derivation, fused-kernel/Y-system calculation, Hirota factorization,
  Q-system determinant/Pfaffian compatibility, weak-coupling Baxter
  elimination, or hexagon Watson-factor derivation.
- Localization statements were retained where the proof establishes the
  localization deformation identity, evaluates the finite normal Gaussian,
  tracks the \(H\)-function determinant convention, proves the \(\mathcal N=4\)
  determinant cancellation, excludes the ADHM small-instanton stratum inside
  the finite-dimensional resolution, computes one-box fixed points, or derives
  the planar circular Wilson loop from the Gaussian equilibrium measure.

## Remaining Proof Obligations

- The one-loop planar \(\mathcal N=4\) scalar Hamiltonian is retained because
  it is central and convention-sensitive, but it still needs a diagrammatic
  appendix that writes the complete propagator, quartic, gauge-exchange, and
  self-energy calculation rather than summarizing the cancellation.
- The asymptotic Bethe ansatz, mirror TBA, Q-system, QSC, and hexagon
  constructions contain substantial internal algebraic derivations, but the
  full route from the four-dimensional gauge theory to each integrability
  structure remains conditional on additional spectral and planar-limit
  hypotheses.  Those hypotheses should be made increasingly explicit as the
  integrability volume matures.
- The Chern-Simons-matter vector-model and ABJM chapters derive several
  finite-regulator or matrix-model consequences, but the existence of the
  corresponding conformal fixed points and the removal of regulators must be
  developed as separate nonperturbative or controlled perturbative statements.
- Six-dimensional SCFT material still separates protected/anomaly data from
  full QFT construction.  Any promotion from protected consistency checks to
  theorem-level QFT existence would require a construction of the theory or a
  precise compactification limit with controlled convergence.
- Localization on compact manifolds still contains an explicit hypothesis at
  the point where the continuum supersymmetric path integral is identified
  with a resolved equivariant integral.  A theorem-level treatment needs a
  regulator, integration cycle, and limiting argument compatible with the BV
  quantum master equation.

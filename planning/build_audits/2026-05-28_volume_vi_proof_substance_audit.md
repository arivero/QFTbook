# Volume VI Proof-Substance Audit

Date: 2026-05-28.

Scope: `monograph/tex/volumes/volume_vi`.

## Repairs Made

- `chapter01_factorized_scattering_and_integrability.tex`: demoted the
  rapidity-kinematics calculation and the Watson-exchange ordered-basis check
  from propositions to remarks.  Their computations remain in the text, but
  they do not carry independent theorem weight.
- `chapter02_two_dimensional_scattering_analyticity_bootstrap.tex`: demoted
  the elementary scalar-block algebra statement to a remark.  The pole,
  unitarity, and crossing calculations are retained as explicit algebra.
- `chapter04b_nested_bethe_ansatz_matrix_bethe_yang.tex`: demoted the origin
  of the \(SU(N)\) nested Bethe equations to a remark and stated explicitly
  that a full proof would require the recursive nested monodromy construction,
  transfer-matrix eigenvalue formula, and pole-cancellation argument at every
  level.  A later typographic overfull line in the remark heading was also
  fixed.
- `chapter05_thermodynamic_bethe_ansatz.tex`: demoted the Lee-Yang ultraviolet
  plateau calculation to a controlled approximation.  The constant-Y-system
  and dilogarithm calculation remains visible, but the finite-size TBA input is
  not represented as a theorem proved from first principles.
- `chapter06_integrable_rg_flows_perturbed_cft.tex`: demoted the first-order
  relevant-source scaling, \(\phi_{1,3}\) minimal-model data, plateau
  reduction, and necessary matching conditions for integrable flows where the
  proof bodies were algebraic bookkeeping or structural diagnostics rather than
  independent theorems.
- `chapter07_mirror_channel_tba_finite_size_wrapping.tex`: demoted the mirror
  pressure/vacuum-energy identity to a remark and the one-winding excited-state
  F-term to a controlled approximation.  The mirror-channel trace and
  one-winding expansion remain, while the stronger theorem-form signal is
  reserved for statements with actual variational or remainder estimates.
- `chapter09_on_gross_neveu_sigma_model_families.tex`: demoted pole
  assignment in the projective rank-one block, the nonabelian-bosonization
  central-charge check, the \(SU(N)\) sine-spectrum fusing-angle check, the
  sausage-metric endpoint observation, and the rational \(O(3)\) limit of the
  repulsive sausage matrix from propositions to remarks.  Each retained
  calculation is useful, but each proof body was direct substitution or limit
  bookkeeping.
- `chapter10_bridges_to_nonintegrable_two_dimensional_qft.tex`: demoted the
  first-order finite-volume mass shift to a controlled approximation, the
  semi-local pole obstruction to a remark, and the TCSA OPE power counting to a
  remark.  The finite-volume and OPE computations remain in the exposition.
- `chapter11_finite_volume_form_factors_spectral_expansions.tex`: demoted the
  Bethe-Yang around-the-circle phase to a construction, the off-diagonal and
  diagonal finite-volume form-factor formulae to controlled approximations,
  and the Gaudin-determinant cancellation in the two-point spectral sum to a
  remark.
- `chapter11_finite_volume_form_factors_spectral_expansions.tex`: strengthened
  the Gaudin state-counting statement.  The proposition now states precise
  hypotheses on the rapidity region, the \(C^2\) Bethe-Yang map, positivity of
  the Gaudin density, and uniform inverse-Jacobian control, and the proof gives
  a lattice-cube/Riemann-sum estimate with an \(O(L^{n-1})\) boundary
  contribution.

## Statements Retained

- Factorization, higher-spin support, scattering-chamber consistency, ZF
  associativity, and chamber extension remain theorem/proposition material
  because their proof bodies use support arguments, associativity constraints,
  or chamber-by-chamber construction rather than mere notation checks.
- The residue identities, Yang-Baxter component checks, sine-Gordon unitarity
  and pole computations, vertex-operator OPE dimension calculation, Coleman
  relation, and Mandelstam-line Fermi exchange were retained because they
  compute nontrivial analytic or algebraic content.
- The TBA variational equation, mirror TBA variational proof, two-winding
  cluster expansion, and vacuum Luescher remainder bound were retained because
  the proofs perform a variational derivation or an explicit controlled
  expansion/estimate.
- The Gross-Neveu, sigma-model, WZW, coset, KZ, rational Yang-Baxter,
  principal-chiral, symmetric-space, large-\(N\), and sausage-family
  propositions were retained where the proof bodies perform an actual tensor,
  projector, Lax-pair, Ward-identity, current-algebra, curvature, or analytic
  uniqueness calculation.
- The finite-volume golden-rule and two-particle decay-width propositions were
  retained because the proofs perform a limiting density-of-states calculation
  and connect the finite-volume matrix element to the continuum phase-space
  normalization.

## Remaining Proof Obligations

- A fully internal proof of the nested algebraic Bethe ansatz for the
  \(SU(N)\) chain should eventually be written as a recursive construction of
  Bethe vectors, transfer-matrix eigenvalues, pole cancellations, and
  completeness hypotheses.  The present text records the mechanism rather than
  claiming completeness.
- Finite-volume form-factor formulae, diagonal finite-volume matrix elements,
  and finite-volume regularization of spectral sums remain controlled
  approximations unless one adds a proof infrastructure for exponential
  finite-volume corrections and disconnected diagonal limits.
- TBA formulae derived from exact scattering data are still conditional on the
  thermodynamic and mirror-channel constructions.  The variational equations
  are proved from the stated entropy/energy functionals, but the route from a
  microscopic QFT to those functionals remains a major domain theorem.
- The sigma-model and Gross-Neveu S-matrix families still need a later
  constructive or axiomatic existence discussion if the monograph is to promote
  them from integrable scattering data to fully constructed Wightman or
  Euclidean QFTs.
- Supersphere and projective-super one-loop formulae were read and retained as
  computations, but a future appendix should expand the supergeometry
  conventions, regularization of signs, and target-space curvature identities
  before treating them as reference-grade derivations.

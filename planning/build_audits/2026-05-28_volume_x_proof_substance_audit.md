# Volume X Proof-Substance Audit

Date: 2026-05-28

Scope: read the theorem-like statements and the bodies of their proofs in
`monograph/tex/volumes/volume_x`.  The purpose was not a mechanical environment
count.  Each proof was checked for whether it actually constructs, estimates,
computes, or reduces a stated claim under explicit hypotheses.  Statements whose
proofs were only definition-unpacking, trace/chain-rule bookkeeping, or
conditional dimensional analysis were demoted to remarks.

## Demoted wrappers

- `chapter01_kms_states_and_thermal_correlators.tex`: demoted the bosonic
  fluctuation-dissipation identity to `Remark~\ref{rem:bosonic-fdt-kms}`.  The
  displayed identity is an algebraic substitution of detailed balance into the
  symmetrized correlator, with the zero-frequency distributional caveat stated.
- `chapter02_finite_temperature_path_integrals.tex`: demoted trace cyclicity
  around the thermal circle to `Remark~\ref{rem:trace-cyclicity-thermal-circle}`.
  It is an important convention-fixing identity, but the verification is only
  cyclicity of a finite trace.
- `chapter05_hydrodynamics_from_ward_identities.tex`: demoted the ideal
  hydrodynamic equations and ideal entropy current to
  `Remark~\ref{rem:ideal-hydro-equations}` and
  `Remark~\ref{rem:ideal-entropy-conservation}`.  Both are direct substitutions
  of the ideal constitutive relations into the Ward identities and first law.
- `chapter06_schwinger_keldysh_hydrodynamic_effective_actions.tex`: demoted the
  gauge-invariance Ward identity and the diffusion equation from the `a`-phase to
  `Remark~\ref{rem:sk-hydro-gauge-invariance-ward-identity}` and
  `Remark~\ref{rem:sk-hydro-diffusion-equation}`.  The useful variational
  computations remain, but the proof content is integration by parts after the
  action has already been written.
- `chapter08_kinetic_theory_controlled_limit.tex`: demoted the quasiparticle
  drift projection to `Remark~\ref{rem:kinetic-quasiparticle-drift-projection}`.
  The calculation is the shell projection of the displayed ansatz.
- `chapter09_anomalous_and_topological_transport.tex`: demoted the hydrostatic
  Chern-Simons variation to `Remark~\ref{rem:hydrostatic-cs-variation}`.  The
  variation is retained as convention-fixing algebra.
- `chapter12_qcd_phase_structure_plasma_dense_matter.tex`: demoted finite-volume
  center one-point vanishing, thermodynamic derivative identities, the Linde
  scale dimensional argument, the susceptibility-radius diagnostic, the
  logarithmic residue corollary, and the physical CFL Goldstone count to remarks:
  `rem:qcd-center-finite-volume-loop-zero`,
  `rem:qcd-thermodynamic-derivative-identities`, `rem:qcd-linde-scale`,
  `rem:qcd-baryon-radius-diagnostic-status`, `rem:qcd-nfl-quark-residue`, and
  `rem:qcd-cfl-goldstone-count`.

## Statements kept after reading the proof bodies

- KMS analytic-elements density, finite Gibbs KMS, detailed balance, finite
  Lehmann representations, retarded boundary values, and Mazur projection were
  kept: their proofs construct analytic functions, spectral measures, boundary
  values, or Hilbert-space projections and fix sign conventions.
- The Schwinger-Keldysh finite constraints, largest-time cancellation,
  source-response kernel, CTP positivity, diffusion-matrix stability, and the
  density FDT from the diffusion action were kept.  These proofs use unitarity,
  positivity, branch exchange, or noncommuting matrix resolvent identities rather
  than slogan-level assertions.
- The Debye mass computations, HTL transversality/Landau-cut derivations,
  finite Markov entropy-production theorem, GKSL complete-positivity proof, and
  finite collision H-theorem were kept because they give actual finite-regulator
  or controlled-approximation calculations.
- In the QCD phase chapter, the finite-regulator analyticity and Lee-Yang
  obstruction statements, source-curvature formula, Polyakov-loop character
  expansion, strong-coupling tube, heavy-quark hopping term, Weiss potential,
  Banks-Casher relation, integrated nonsinglet axial Ward identity, pole
  saturation GMOR logic, low-temperature pion-gas correction, HTL/HDL
  calculations, dense non-Fermi-liquid self-energy, magnetic gap equation and
  exponent, one-gluon color factor, gauge averaging of CFL order, Higgs screening
  mass matrix, collective-mode dispersions, and CFL anomaly-matching statements
  were kept after reading their proof bodies.

## Remaining standard

This pass only audited the theorem-like wrapper status and proof substance in
Volume X.  It did not certify every physical approximation in Volume X as final;
controlled approximations still require their separate domain-of-validity passes.

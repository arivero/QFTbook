# Issue #844 Controlled-Approximation Status Audit

Date: 2026-06-07.

Scope: status-surface repair for recent Ch09/Ch20D inserts, plus one repo-wide
finite-laboratory slip found by the same search.

Changes made:

- Added a `tools/audit_theorem_form.py` check for `controlledapproximation`
  titles containing `gate`, `map`, `diagnostic`, or `laboratory` when the body
  lacks visible approximation controls or a component estimate.
- Reclassified exact or proof-obligation Ch09 mirror blocks:
  `rem:glsm-mirror-dterm-rg-schur-obligation`,
  `rem:glsm-mirror-boundary-defect-obligation`,
  `constr:glsm-global-form-flux-lattice-datum`,
  `constr:glsm-chiral-superpotential-phase-isometry-lattice`,
  `constr:cigar-liouville-asymptotic-deformation-filter`, and
  `rem:cigar-liouville-pathwise-fake-fixed-point-obligation`.
- Reclassified Ch20D instanton status slips:
  `ex:instanton-finite-source-functional-laboratory`,
  `constr:instanton-mass-source-rg-channel-transport`,
  `constr:instanton-crossed-helicity-projection`, and
  `rem:instanton-same-coordinate-amplitude-rate-obligation`.
- Reclassified the Vol XII finite retained Ward-completion block as
  `ex:semiclassical-retained-ward-completion-laboratory`.
- Recorded the status rule in `planning/12_strict_writing_harness.md`.

Remaining `controlledapproximation` titles with status-like vocabulary after
the pass are intentional:

- `Duality and stability gate for SVZ extractions` declares a Borel window,
  OPE/duality/threshold controls, pole and residue remainders, and displayed
  bounds.
- `Measured small-\(x\) observable map` declares the measured finite-regulator
  functional, impact-factor matching, rapidity factorization topology, finite
  `Q` and truncation remainders, and residual controls.
- `Instanton observable assembly map` declares a retained one-instanton
  window, physical projection, absolute residual bound, and noncancellation
  margin.

Quality conclusion: the repaired blocks now separate exact finite
constructions, examples, and proof-obligation maps from genuine controlled
approximations.  The physics content is unchanged: the Schur-complement,
source-metric, boundary/defect, Liouville pathwise, instanton RG-frame,
helicity-projection, and amplitude-to-rate arguments still expose the same
observable obligations, but no longer overclaim theorem-form status.

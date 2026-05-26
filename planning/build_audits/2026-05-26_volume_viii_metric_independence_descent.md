# Volume VIII Metric Independence And Descent Audit

## Scope

- Deepened
  `monograph/tex/volumes/volume_viii/chapter01_metric_independence_and_cohomological_observables.tex`.
- Added
  `calculation-checks/cohomological_metric_descent_checks.py`.
- Updated the calculation-check index and the Volume VIII Chapter 1 dossier.

## Mathematical Content Added

- Replaced the previous schematic \(T_{\mu\nu}=QG_{\mu\nu}\) discussion by a
  renormalized stress-tensor response formula with explicit contact insertion
  \(C_{\delta g}(X)\).
- Defined a cohomological Ward datum: graded insertion algebra, odd nilpotent
  derivation \(\delta_Q\), admissible insertions, expectation functional, and
  anomaly-free Ward identity.
- Proved metric independence for a one-parameter family of metrics from the
  exactness of the full metric response, including contact and insertion
  variation terms.
- Isolated failure mechanisms: BV anomaly, boundary/noncompact field-space
  terms, and contact terms changing the observable algebra.
- Added descent equations for form-valued observables and proved homological
  invariance of integrated descendants in \(Q\)-cohomology.
- Added the Donaldson-type quadratic observable as the first gauge-theoretic
  example of descent, with normalization caveats tied to trace conventions.
- Added a finite-dimensional de Rham model explaining \(Q\)-Stokes and
  \(Q\)-exact deformation independence.

## Verification

- Passed: `python3 calculation-checks/cohomological_metric_descent_checks.py`.
- Passed: `git diff --check`.
- Passed: `tools/audit_monograph_text.sh`.
- Passed: `tools/audit_chapter_dossiers.sh`.
- Passed: `tools/build_monograph.sh`.
- Confirmed: `monograph/tex/main.pdf` builds to 1353 pages by `pdfinfo`.

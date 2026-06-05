# Issue #769 phi4 cut-to-running pass

Date: 2026-06-05.

Scope:

- Chapter: Volume II, Chapter 6, generalized unitarity and one-loop reduction.
- Local target: massless \(\lambda\phi^4\) scalar four-point reconstruction.
- Companion evidence:
  `calculation-checks/generalized_unitarity_reduction_checks.py`.

Substance audit:

- This is a physics-amplitude completion of an existing example, not a new
  isolated algebra cell.
- The previous scalar example reconstructed the crossed bubble logarithms from
  cuts and stated that local counterterms are cut-invisible.  The new pass
  carries that same example through the UV-subtraction gate: crossed-channel
  pole, local counterterm convention, one-loop running, and finite local
  scheme choice.
- The negative controls are the physically relevant shortcuts: a single-channel
  cut misses the factor of three in the pole/beta coefficient, and a finite
  subtraction constant remains invisible to all channel cuts.

Quality boundary:

- The pass does not claim to close #769.  It strengthens the acceptance item
  connecting reconstructed virtual amplitudes to renormalization data in a
  complete scalar example.
- It keeps the full infrared-safe observable assembly as a separate later gate;
  the scalar example is UV-local and does not replace the gauge-theory
  real-radiation/factorization discussion.

Verification completed:

- Generalized-unitarity companion check.
- Targeted runner pass for `generalized_unitarity_reduction_checks`.
- Full Python calculation suite.
- Focused Chapter 6 theorem/display/negative-scope/style audits.
- Chapter dossier and monograph text audits.
- Calculation-check inventory and evidence-contract audits.
- Process-metadata leak scan on the touched TeX/check files.
- Full monograph build and log scan.

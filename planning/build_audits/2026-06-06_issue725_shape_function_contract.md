# Issue #725/#630 Shape-Function Contract Pass

Date: 2026-06-06

## Scope

- Promoted `calculation-checks/shape_function_convolution_checks.py` to an
  extended evidence contract.
- Added a finite moment-truncation negative control: two shape distributions
  with identical normalization, \(\Omega_1\), and \(\Omega_2\) agree on
  quadratic endpoint tests but differ on a finite endpoint bin.
- Added the observable-level residual
  \(B_{\rm shape}^{(m)}(\mathcal F)\) to Volume II Chapter 19b for fits that
  replace the full Wilson-line shape distribution by finitely many moments.

## Quality Re-Audit

- Physics depth: the pass strengthens the measured endpoint-spectrum
  interpretation of shape functions.  It prevents the common overread that an
  \(\Omega_1\) or \((\Omega_1,\Omega_2)\) fit supplies the full endpoint
  spectrum.
- Coherence: the new residual belongs directly after the smeared moment
  expansion, where the chapter already explains the controlled smooth-test
  Taylor expansion.
- Scope guard: the pass does not claim a new SCET factorization theorem or a
  Euclidean reconstruction of the lightlike Wilson-line matrix element; those
  remain declared imported inputs.

## Verification Target

- Focused shape-function companion and evidence-contract audit.
- Ch19b theorem/display/style/negative-scope checks.
- SCET factorization occurrence ledger after source-line shifts.
- Full Python calculation-check suite and full monograph build.

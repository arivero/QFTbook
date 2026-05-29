# Nineteenth Cross-Volume Wrapper Pass

Date: 2026-05-29.

Purpose: continue issue #691's audit of statements whose theorem-family
environment overstated the mathematical content.  This pass focused on cases
where the useful calculation is a direct endpoint-covariance check, Hermite
normal form count, Laplace-principle extraction under already-declared
spectral hypotheses, or finite permutation algebra verification.

## Demotions

This pass demoted four theorem-family wrappers to prose calculations:

- `Gauge covariance of the open light-ray operator` became the Wilson-line
  endpoint-transformation calculation, with the transformation law retained as
  a numbered equation for later PDF, quasi-PDF, TMD, and HQET uses.
- `Connected torus covers` became the Hermite-normal-form count of connected
  unbranched covers of a complex torus.
- `Transfer-matrix extraction of the static potential` became the spectral
  measure and elementary Laplace-principle calculation under the already
  stated transfer-matrix hypotheses.
- `Rational-block unitarity and Yang--Baxter equation` became the finite
  permutation-algebra check for the rational \(SU(N)\) matrix block.

The theorem-form audit now guardrails these titles against reappearing as
theorem/proposition/lemma/corollary environments.

## Current Counts

- theorem/proposition/lemma/corollary environments in `monograph/tex/volumes`:
  619.
- proof environments in `monograph/tex/volumes`: 614.
- short/cue-heavy heuristic queue after this pass: 133 candidates, split as
  3 score-four, 14 score-three, and 116 score-two items.  The top three
  score-four candidates have been read and remain in the queue because their
  present theorem-family status is still plausible: finite Grassmann
  reflection positivity supplies a reusable positivity criterion, the
  largest-time identity is the graph-level cancellation mechanism behind
  perturbative cutting rules, and the positive-energy supersymmetric pairing
  is the structural Witten-index cancellation used later in the index
  discussion.

## Verification

The following checks were run after the edits:

- stale-label scan for the four removed labels: clean;
- `python3 tools/audit_theorem_form.py`: clean;
- `tools/audit_negative_scope_prose.py`: clean;
- `tools/audit_monograph_text.sh`: clean;
- `python3 tools/audit_unnumbered_display_labels.py`: clean;
- `git diff --check`: clean;
- `tools/build_monograph.sh`: clean;
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2583`.

The full build and log scan completed cleanly.

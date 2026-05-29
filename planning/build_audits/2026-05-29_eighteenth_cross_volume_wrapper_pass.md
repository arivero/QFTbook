# Eighteenth Cross-Volume Wrapper Pass

Date: 2026-05-29.

Purpose: continue issue #691's end-to-end theorem/proposition-status audit,
with attention to wrappers whose proof content is a convention substitution,
finite-dimensional determinant or character calculation, elementary spectral
bound, source-differentiation identity, or direct bound-state pole
bookkeeping.  The goal is not to remove useful calculations, but to stop
presenting them as theorem-level machinery when the genuine content lies in
the surrounding definitions, hypotheses, or later analytic arguments.

## Demotions

This pass demoted eleven theorem-family wrappers to paragraphs while
preserving the useful formulas and derivations:

- `Hatted beta functions and redundant directions` became a coordinate-change
  paragraph in the sigma-model coupling-space discussion.  The genuine issue
  is the scheme dependence of beta-function representatives and the geometric
  meaning of redundant directions, not the displayed Lie-derivative algebra.
- `Parafermion central charge, weights, and identification` became coset data
  calculation from Sugawara central charges and branching labels.
- `Cyclic permutation twist weight` became the covering-coordinate
  Schwarzian calculation of the ground twist weight.
- `Free-boson rotation twist weight` became the shifted-oscillator
  zero-point calculation for a complex boson with rotation monodromy.
- `Nilpotent Taylor coefficient of a chiral \(F\)-term` became the component
  Taylor calculation of the \(\theta^2\) coefficient.
- `Source curvature as an integrated connected correlator` became the
  finite-regulator source-differentiation calculation identifying
  susceptibility with volume growth of a connected correlator.
- `Direct fusion pole in the breather amplitudes` became pole bookkeeping in
  the sine-Gordon breather S-matrix formula.
- `Finite BF partition function` became the finite Fourier-transform and
  cohomology cardinality calculation.
- `Covariance of the Abelian Dirac coupling` became the local representative
  change calculation for the QED covariant derivative.
- `One-particle residue bound for a canonically normalized field` became the
  positive-measure bound inside the Kallen-Lehmann discussion.
- `Leading Coulombic \(1S\) quarkonium level` became the hydrogenic
  pNRQCD coordinate calculation, with the limitations of the chart retained
  explicitly in the surrounding prose.

The theorem-form audit was also extended with guardrails for these titles so
that the same wrappers do not reappear later as theorem/proposition/lemma or
corollary environments.

## Current Counts

- theorem/proposition/lemma/corollary environments in `monograph/tex/volumes`:
  623.
- proof environments in `monograph/tex/volumes`: 618.
- short/cue-heavy heuristic queue after this pass: 137 candidates, split as
  3 score-four, 15 score-three, and 119 score-two items.  This remains a
  reading queue rather than a defect count.

## Verification

The following checks were run after the edits:

- stale-label scan for the eleven removed theorem labels: clean;
- `python3 tools/audit_theorem_form.py`: clean;
- `tools/audit_negative_scope_prose.py`: clean;
- `tools/audit_monograph_text.sh`: clean;
- `python3 tools/audit_unnumbered_display_labels.py`: clean;
- `git diff --check`: clean;
- `tools/build_monograph.sh`: clean;
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2583`.

The full build and log scan completed cleanly.

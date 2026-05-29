# Seventeenth Cross-Volume Wrapper Pass

Date: 2026-05-29.

Purpose: continue issue #691's end-to-end audit of theorem/proposition status,
with particular attention to statements whose proof environment merely performs
a finite-dimensional integration by parts, a convention substitution, a descent
bookkeeping step, or a finite algebra identity.

## Demotions

This pass demoted eleven theorem-family wrappers to paragraphs while preserving
the formulas and the useful checks:

- `Finite-regulator Schwinger--Dyson identity` became the finite-regulator
  Schwinger--Dyson identity and large-\(N\) closure paragraph.  The integration
  by parts is no longer presented as a proposition; the genuine physics input is
  the planar bilocal color reduction plus the factorization hypothesis.
- `Quadratic Green--Schwarz descent` became a descent calculation.  The text now
  distinguishes the sign-convention computation from the substantive
  six-dimensional anomaly-polynomial input.
- `Regular algebra identities` became a finite group-algebra calculation inside
  the categorical-symmetry discussion.
- `Higher-form Ward action` became the linking-number form of the Ward action,
  rather than a proposition proving the definition of the symmetry defect.
- `Basic Schwinger--Keldysh constraints` became a finite-system unitarity and
  positivity paragraph.
- `Index of the fixed-domain deformation complex` became an index calculation
  feeding the stable-map expected dimension.
- `Preserved Virasoro algebra` became the boundary stress-tensor gluing
  calculation for the single preserved Virasoro copy.
- `Conjugate-pair and real-representation cancellation` became anomaly
  coefficient bookkeeping in the Hermitian-generator convention.
- `Scattering-normalized DOZZ representative` became the normalization
  conversion from DOZZ to the \(P\)-basis.
- `Compact coset central charge and primary data` became a level-shift and
  Cartan-factor calculation.
- `Cigar central charge and primary data` became the parallel noncompact coset
  data calculation.

## Current Counts

- theorem/proposition/lemma/corollary environments in `monograph/tex/volumes`:
  634.
- proof environments in `monograph/tex/volumes`: 629.
- short/cue-heavy heuristic queue after this pass: 147 candidates, split as
  3 score-four, 15 score-three, and 129 score-two items.  This remains a
  reading queue, not a defect count.

## Verification

The following checks were run after the edits:

- stale-label scan for the eleven removed theorem labels;
- `python3 tools/audit_theorem_form.py`;
- `tools/audit_negative_scope_prose.py`;
- `tools/audit_monograph_text.sh`;
- `python3 tools/audit_unnumbered_display_labels.py`;
- `git diff --check`;
- `tools/build_monograph.sh`;
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`.

The full build and log scan completed cleanly.  The built PDF has 2583 pages.

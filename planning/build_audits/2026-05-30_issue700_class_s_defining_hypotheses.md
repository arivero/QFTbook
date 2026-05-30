# Issue #700 Class-S Defining-Property Pass

## Scope

This pass addresses the immediate class-\(S\) failure mode in GitHub issue
#700: the manuscript used "class-\(S\) theory" as if the four-dimensional QFT
had already been defined, while the data were scattered across anomaly,
tensor-branch, defect, and Hitchin-base discussions.

## Manuscript Changes

- Added Hypothesis `hyp:six-d-two-zero-ade-qft` near the opening of Volume
  VII, Chapter 11.  It names the conditional object
  \(\mathfrak T_{6d}[\mathfrak g]\) and aggregates the defining properties
  used in the chapter: ADE Lie algebra data, positive-energy
  \(OSp(8^\ast|4)\) representation, tensor-branch quotient, anomaly
  polynomial, BPS root-lattice strings, finite defect group, circle
  compactification, and conditional compactification functoriality.
- Added Hypothesis `hyp:class-s-compactification-datum` at the beginning of
  the Riemann-surface compactification section.  It defines the conditional
  class-\(S\) object
  \(\mathfrak T_{\mathfrak g}[C,\{(p_a,\mathfrak D_a)\};\eta]\) from the
  tuple of surface, marked points, defect data, and twist sign.
- Rewrote the Hitchin-base discussion so it explicitly assumes the two
  hypotheses in the smooth unpunctured case, rather than treating the Hitchin
  base as a definition of the QFT.
- Rewrote the status ledger so it references the named hypotheses instead of
  retrospectively aggregating the chapter's scattered data.
- Tightened `planning/12_strict_writing_harness.md` with a rule that every
  non-Lagrangian or non-axiomatically constructed central object must have an
  upfront Definition or Hypothesis block aggregating its defining properties.
- Updated the chapter dossier accordingly.

## Accuracy Boundary

The new blocks are hypotheses, not definitions in the constructive sense.  The
chapter still does not construct the interacting six-dimensional local QFT or
the class-\(S\) four-dimensional QFT from first principles.  The point of the
pass is to make the logical dependency explicit: downstream anomaly and
Hitchin-base formulae are consequences/tests of the named conditional objects.

## Verification Completed

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`, clean full build and log scan; output:
  `monograph/tex/main.pdf` at 2670 pages.

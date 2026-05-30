# Issue #700 Chern--Simons Defining-Datum Pass

## Scope

This pass addresses the Volume VIII Chapter 4 case in GitHub issue #700.  The
chapter previously began from the local Chern--Simons functional and then
introduced level quantization, framing, Wilson lines, boundary WZW theory, and
modular data as consequences.  That organization left the central object
underdefined: the local action alone is not a globally defined quantum
Chern--Simons theory.

## Manuscript Changes

- Added Definition `def:chern-simons-defining-datum` near the chapter opening.
  The datum is
  \(\mathfrak C=(G,\lambda,\mathfrak f,\mathfrak L,\mathfrak b)\): compact
  gauge group, integral level/differential-cohomology lift, framing anomaly
  convention, framed line-operator labels, and boundary/polarization data.
- Added Hypothesis `hyp:quantum-chern-simons-theory`, naming the conditional
  quantum object \(Z_{\mathfrak C}\).  The hypothesis states the required
  surface state spaces, framed-link cobordism amplitudes, gluing law,
  flat-connection semiclassical limit, modular line data when available, and
  WZW boundary cancellation.
- Rewrote the phase-space, Wilson-line, and \(SU(2)_k\) example prose to
  refer back to the named definition/hypothesis rather than treating
  quantization, framing, or modular data as implicit.
- Updated the chapter dossier with notation, claim ledger, proof boundaries,
  and an issue #700 audit note.

## Accuracy Boundary

The new quantum object is a hypothesis, not a claimed regulator-level
construction.  The chapter continues to record the comparison problem among
perturbative configuration-space integrals, geometric quantization, WZW
conformal blocks, modular tensor categories, and functorial gluing as an open
problem.

## Verification Completed

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`, clean full build and log scan; output:
  `monograph/tex/main.pdf` at 2671 pages.

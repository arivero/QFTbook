# OS Boundary-Value And Distributional EOW Proof Layer

Date: 2026-05-29

Related issue: #695

## Scope

This pass tightened the OS reconstruction boundary-value discussion around the
transition from Euclidean Schwinger data to Lorentzian Wightman distributions.
The distributional edge-of-the-wedge theorem is already stated in Volume I,
Chapter 11 as `thm:distributional-edge-of-the-wedge`; the OS chapter now cites
that theorem explicitly at the Jost-configuration step instead of hiding the
analytic-continuation input in prose.

## Changes

- Added explicit references from the OS boundary-value package to
  `thm:distributional-edge-of-the-wedge`.
- Added a local lemma proving the Fourier--Laplace boundary/cone-support
  direction used in the OS spectral-support step.
- Kept Vladimirov's general converse boundary-value theorem as a quoted
  pure-mathematics theorem; the QFT-specific work remains the derivation of
  polynomial tube bounds and spectral support from the OS hypotheses.

## Verification

- `git diff --check`
- `python3 tools/audit_unnumbered_display_labels.py`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh && tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- direct reference scan: no missing refs across 5357 refs and 6319 labels
- `pdfinfo monograph/tex/main.pdf`: 2594 pages

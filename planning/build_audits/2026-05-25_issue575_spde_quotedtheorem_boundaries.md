# 2026-05-25 Issue #575 SPDE Theorem-Boundary Pass

GitHub issue: #575, concerning proof sketches under theorem environments in
`monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`.

## Manuscript Changes

- Converted the Da Prato--Debussche solution mechanism from `theorem` plus
  `proof[Proof of the mechanism]` into a `quotedtheorem` followed by
  role/status text.
- Converted the regularity-structure reconstruction theorem from `theorem`
  plus `proof[Why this is the needed theorem]` into a `quotedtheorem`;
  retained the wavelet-coefficient explanation as motivation and explicitly
  states the missing proof obligations.
- Converted the renormalized dynamic \(\Phi^4_3\) SPDE datum from `theorem`
  plus `proof[Proof architecture]` into a `quotedtheorem`; the BPHZ model,
  compactness, fixed-point, reconstruction, and invariant-measure steps are
  now named as theorem-level estimates rather than presented as proved.
- Added Open Problem `op:self-contained-singular-spde-proof-stack`, listing
  the monograph-internal proof stack needed for singular SPDE constructions:
  Wick-power convergence, parabolic Schauder estimates, Besov or Holder
  multiplication, energy estimates, invariant-law identification,
  reconstruction theorem, BPHZ model convergence, fixed points in modelled
  distributions, concrete counterterm identification, and SPDE-to-OS passage.
- Added references in a footnote to Da Prato--Debussche, Hairer, and the
  Hairer--Mourrat--Weber regularity-structures treatment as theorem-boundary
  sources, not final authority.
- Converted the chapter's labelled displayed equations to numbered
  `equation` environments so cross-references attach to equation counters.

## Status

This pass closes the proof-posture bug: sketches are no longer presented as
proofs.  It does not pretend that the monograph now contains complete proofs
of the Da Prato--Debussche theorem, Hairer's reconstruction theorem, or the
renormalized dynamic \(\Phi^4_3\) construction.  Those are now explicit proof
obligations.

## Verification

- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean; the monograph built to
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf`: 1255 pages.

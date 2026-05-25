# 2026-05-25 Issue #573 Phi4_3 Theorem-Boundary Pass

GitHub issue: #573, concerning
`thm:phi-four-three-constructive-output` in
`monograph/tex/volumes/volume_xi/chapter02_constructive_scalar_models_os_data.tex`.

## Manuscript Changes

- Converted the constructive \(\Phi^4_3\) output result from an ordinary
  theorem followed by `proof[Proof architecture]` into a `quotedtheorem`.
- Removed the false local proof posture: the four analytic components of the
  constructive proof now appear as status text rather than as a proof
  environment.
- Added a local statement that the quoted theorem is a proof obligation for
  this monograph, not an authority claim based on physics literature.
- Added Open Problem `op:self-contained-phi-four-three-proof`, listing the
  missing monograph-internal proof tasks: phase-cell decomposition,
  small-field and large-field norms, stability, local-coordinate extraction,
  scale-dependent polymer bounds, uniform infinite-volume convergence,
  reflection positivity, and OS growth.
- Tightened `planning/12_strict_writing_harness.md`: QFT-specific
  `quotedtheorem` blocks are only interim honesty boundaries unless a
  self-contained proof is supplied, the statement is downgraded, or the
  missing proof is recorded as an explicit proof obligation.
- Converted nearby labelled display math to numbered `equation` environments
  so cross-references point to equation counters.

## Status

This pass fixes the immediate proof-integrity problem: a four-bullet proof
architecture is no longer presented as a proof.  It does not close the deeper
mathematical project of proving the constructive \(\Phi^4_3\) theorem inside
the monograph.  That deeper obligation is now explicit in the manuscript.

## Verification

- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean; the monograph built to
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf`: 1254 pages.

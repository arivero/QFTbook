# Issues #480/#482/#483 Axiom And Constructive Status Pass

## Trigger

- `claude_review.md` flagged the need to distinguish theorem-bearing
  frameworks from completed constructions and to avoid making Wightman/OS/AQFT
  frameworks appear to be universal definitions.
- GitHub issues #480, #482, and #483 requested a constructive-QFT status table,
  a constructive-context paragraph near OS reconstruction, and an explicit
  opening section on expected properties versus defining conditions.

## Manuscript Edits

- Added Section `sec:status-axiom-systems-constructive-examples` to
  `monograph/tex/volumes/volume_i/chapter01_what_is_qft.tex`.
- Added Open Problem `op:axiomatic-comparison-physical-examples` on the
  comparison between Wightman fields, OS data, Haag--Kastler local nets, and
  functorial/path-integral data.
- Added Remark `rem:os-constructive-status-inputs` to
  `monograph/tex/volumes/volume_iv/chapter02_osterwalder_schrader_reconstruction.tex`,
  immediately after the path-integral-to-OS reconstruction corollary.
- Updated the Volume I Chapter 1 dossier with the new claims and completed
  issue references.

## Substance

- The text now states that Wightman, OS, local-net, constructive,
  perturbative, and functorial/path-integral presentations are
  theorem-bearing frameworks whose hypotheses must remain attached to the
  theorems proved in them.
- The text identifies the path-integral/Kontsevich--Segal aspiration as a
  gluing-compatible assignment of amplitudes and correlators on a category of
  backgrounds with sources.
- The text calibrates the frameworks against actual constructive results,
  cross-referencing the Volume XI constructive status table and separating
  low-dimensional constructed models, scalar triviality regimes, and open
  four-dimensional gauge-theory constructions.

## Verification

- `git diff --check` passed.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` passed in
  `monograph/tex`.
- `main.pdf` now builds to 1191 pages.

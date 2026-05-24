# Issue 373: Lorentzian Labelled Quartic Vertex Convention

## Scope

GitHub issue #373 noted that Volume I, Chapter 11 displayed both the labelled
\(-\ii g\) quartic vertex and the unlabelled \(-\ii g/4!\) insertion, but did
not explicitly state which symmetry factors remain when the labelled rule is
used.

## Fix

- Added a local convention statement immediately after the Lorentzian
  \(\phi^4\) vertex rule.
- Stated that the quartic \(4!\) has already been absorbed into the labelled
  vertex \(-\ii g\).
- Defined the remaining graph factor as
  \(1/|\operatorname{Aut}_{\mathrm{ext}}\Gamma|\), with external labels fixed.
- Applied this directly to the following tadpole: the residual automorphism has
  order \(2\), since it interchanges the two internal half-edges forming the
  loop, giving the coefficient \(-\ii g/2\).
- Updated the Chapter 11 dossier.

## Verification Plan

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

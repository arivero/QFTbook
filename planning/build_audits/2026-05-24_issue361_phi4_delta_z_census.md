# 2026-05-24 Issue #361 Phi-Four Field-Strength Census

GitHub issue #361 flagged that the first counterterm census could be read as
deriving inclusion of the \(D=4\), \(\phi^4\) field-strength counterterm from
the one-loop tadpole discussion, even though the one-loop tadpole is independent
of external momentum.

Changes made:

- Rewrote the \(D=4\), \(\phi^4\) census paragraph to state explicitly that
  \(\delta Z^{(1)}_{\phi^4}=0\) is only a one-loop graph-specific result.
- Identified the two-loop sunset as the first logarithmically divergent
  momentum-dependent two-point contribution whose \(p^2\) Taylor coefficient is
  canceled by \(\delta Z\).
- Moved the finite-list closure burden onto the following power-counting
  argument: higher \(n\)-point functions with \(n\ge 6\) have negative
  superficial degree of divergence.
- Updated the chapter dossier so future audits keep the one-loop census,
  two-loop sunset, and power-counting closure logically separate.

Verification targets:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

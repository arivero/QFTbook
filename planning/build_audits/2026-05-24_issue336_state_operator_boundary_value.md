# 2026-05-24 Issue #336 State--Operator Boundary-Value Audit

## Issue

GitHub issue #336 flagged that Volume III, Chapter 4 treated the
operator-from-state direction of radial quantization as an existence side
condition rather than a theorem-level statement.

## Edits

- Added `def:scaling-operator-classes`, separating local scaling operators of
  definite dimension from the BPZ/radial Hilbert completion.
- Added `def:local-radial-boundary-value-state`, specifying the distributional
  data required for a definite-energy radial state to define a local insertion
  at the origin.
- Added `thm:operator-from-state-radial-boundary-value`, proving uniqueness
  modulo radial null operators and identifying radial completeness with
  existence of the stated local boundary values on each eigenspace.
- Rewrote `thm:state-operator-correspondence` degree-by-degree:
  \(\mathcal V_{\rm loc}^{(\Delta)}\simeq\ker(D_{\rm rad}-\Delta)\).
  The algebraic direct sum is dense after BPZ/radial completion; generic
  completed sphere states are not local operators.
- Corrected the OPE opening in Volume III, Chapter 9 so a separated product
  creates a sphere state whose local-operator partial sums converge in
  BPZ/radial norm, rather than a literal local operator product at the origin.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean; rebuilt
  `monograph/tex/main.pdf` at 745 pages.

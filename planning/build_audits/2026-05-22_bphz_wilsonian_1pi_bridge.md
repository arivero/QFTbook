# 2026-05-22 BPHZ--Wilsonian--1PI Bridge

## Scope

Volume III had developed BPHZ subtractions, the 1PI renormalization group,
and Wilsonian cutoff flow in separate chapters.  This pass adds the missing
comparison layer inside the Wilsonian chapter, after the continuum-limit
construction.

## Manuscript Changes

- Updated
  `monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex`.
- Added a terminal section, "The Bridge to BPHZ and 1PI Coordinates."
- Defined the finite-regulator setup with
  \(\mu\ll\Lambda\ll\Lambda_0\), low source support, and nonexceptional 1PI
  subtraction momenta.
- Stated the connected-functional equality
  \[
    W_\Lambda^{\rm low}[J]=W_{\Lambda_0}[J]
  \]
  as the consequence of the Gaussian convolution identity.
- Explained that \(L_\Lambda\) is an action for the remaining low field; 1PI
  coordinates require low-mode integration followed by Legendre transform.
- Added a proposition comparing BPHZ, Wilsonian, and 1PI descriptions under
  stated assumptions on locality, finite projectors, and derivative-expansion
  control.
- Added a bridge figure mapping:
  regulated bare action, BPHZ \(R\)-operation, Wilsonian pushforward,
  connected low-source functional, Legendre transform, Wilsonian coordinates,
  and 1PI projected coordinates.
- Clarified that Wilsonian and 1PI beta-function components are comparable
  only after a matching map has been specified.

## Planning Updates

- Updated `planning/04_master_architecture.md` to record the bridge as a
  completed baseline and move the target to worked examples and operator
  insertions.
- Updated `planning/13_development_dependency_map.md` so the next Volume III
  target is anomalous dimensions, source renormalization, and operator
  mixing using this bridge.
- Updated the Wilsonian chapter dossier with construction tasks, claim
  ledger entries, figure requirements, and audit notes for the bridge.

## Verification

- Strict phrase scan on the edited chapter and associated planning files:
  clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean.
- Rendered bridge pages from `monograph/tex/main.pdf`:
  `/tmp/qft_bphz_wilsonian_bridge-302.png`,
  `/tmp/qft_bphz_wilsonian_bridge-303.png`, and final corrected page
  `/tmp/qft_bphz_wilsonian_bridge_final-304.png`.
  The bridge diagram, proposition block, proof, and gauge-theory handoff were
  visually inspected.

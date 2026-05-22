# 2026-05-22 One-Loop BPHZ--Wilsonian--1PI Matching Audit

## Scope

This pass strengthens the bridge between BPHZ subtractions, Wilsonian
effective actions, and 1PI subtraction coordinates by adding a worked
one-loop scalar quartic example.  The goal is to replace a purely structural
comparison by an explicit finite-regulator calculation with all maps named.

## Manuscript Changes

- Updated
  `monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex`.
- Added "One-Loop Matching in the Quartic Scalar Theory."
- Defined the covariance split
  \(C_{\Lambda_0}=C_\Lambda+C_>\) and the four-point bubble functional
  \(\mathcal B_{A,B}(\mathcal P)\).
- Proved the finite-regulator bubble decomposition into low-low, high-high,
  and mixed covariance assignments.
- Wrote the one-loop Wilsonian quartic vertex correction from the high-high
  bubble, including the bubble symmetry factor in the
  \((g_0/4!)\phi^4\) convention.
- Added a figure showing how the full regulated bubble maps to the Wilsonian
  quartic vertex, the low-field 1PI loop, and local matching coordinates.
- Wrote the BPHZ-subtracted one-loop 1PI four-point kernel at the symmetric
  subtraction configuration.
- Wrote the finite-regulator Wilsonian low-field kernel and the matching map
  from \(u_4(\Lambda;\mathcal S_\mu)\) to \(g(\mu)\).
- Made the mixed covariance term explicit as generated Wilsonian vertices
  followed by low-field integration, with its low-momentum Taylor expansion
  assigned to local matching data and omitted irrelevant coordinates.

## Planning Updates

- Updated the Wilsonian chapter dossier with the new construction task,
  claim, figure requirement, and audit note.
- Updated the master architecture and dependency map so the next target is
  the source-dependent operator bridge and observable correlator tightening.

## Verification

- Strict phrase scans on the edited manuscript and planning files found no
  prohibited framing.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed and produced
  `monograph/tex/main.pdf`.
- Rendered the new matching figure page as
  `/tmp/qft_one_loop_matching_render_fixed-309.png` and inspected it
  visually; the mixed-covariance label collision found in the first render was
  fixed.
- Inspected the following matching-equation page; the multiline equations are
  legible and remain within the text block.

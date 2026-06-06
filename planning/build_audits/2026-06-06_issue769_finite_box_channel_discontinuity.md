# 2026-06-06 Issue 769 Finite Box Channel-Discontinuity Audit

## Scope

- Added `ca:finite-box-channel-discontinuity-closure` to Volume II Chapter 6
  immediately after the physical branch of the reduced two-scale box master.
- Added `check_finite_box_channel_discontinuity_closure()` to
  `calculation-checks/generalized_unitarity_reduction_checks.py`.
- Updated the calculation-check inventory and the Chapter 6 dossier.

## Depth Audit

- This pass is a physics-facing master-integral closure, not another isolated
  finite identity.  It connects the solved box master, its branch prescription,
  the \(s\)-channel endpoint logarithm, lower/subtraction jumps, and an
  independently normalized Cutkosky comparison.
- The finite check verifies the stripped jump
  \(\widehat{\operatorname{Disc}}_s\mathcal F_\Box=-\log(s/(-t))\) and rejects
  Euclidean-master, wrong-sheet, omitted-lower-sector, omitted-subtraction, and
  self-defined-cut shortcuts.
- The pass also records a necessary limitation: channel discontinuities do not
  fix the additive Euclidean boundary constant, so the finite hard remainder
  still requires the boundary data from the master-integral solution.

## Scope Guard

- Process and issue-tracking details are confined to planning files.
- The TeX addition stays inside loop-amplitude physics: physical branch data,
  Cutkosky closure, master transport, and finite hard remainders.
- This does not claim to close #769; fuller production multi-scale families and
  higher-loop amplitude examples remain open.

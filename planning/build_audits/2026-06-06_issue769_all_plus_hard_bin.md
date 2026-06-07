Issue: #769
Date: 2026-06-06
Area: Volume II, Chapter 6 loop-amplitude bridge

Scope
- Added `ca:all-plus-rational-hard-function-bin` after the five-point all-plus
  rational amplitude.
- Extended `calculation-checks/generalized_unitarity_reduction_checks.py` with
  `check_all_plus_rational_hard_function_bin()`.
- Updated the calculation-check inventory and the Chapter 6 dossier.

Quality audit
- This is a physics-placement pass, not a new isolated algebraic cell.  The
  new text connects the cut-invisible rational amplitude to its finite hard
  contribution: zero Born interference in an all-plus helicity sector and
  nonzero lower-loop-squared hard contribution after color-metric assembly.
- The scope is deliberately bounded.  The block does not claim a complete NNLO
  collider observable; it identifies the finite hard-function slot that must
  still be combined with real-virtual, double-real, subtraction, and
  factorization terms.
- Directives and issue-tracking language remain in planning files only.

Verification plan
- Run the focused generalized-unitarity companion.
- Run focused Chapter 6 theorem/display/prose/style audits.
- Run dossier, monograph-text, inventory, evidence, full Python, and full
  monograph build checks before posting to the issue.

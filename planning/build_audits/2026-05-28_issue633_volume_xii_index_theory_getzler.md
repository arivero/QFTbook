# 2026-05-28 -- Issue #633, Volume XII index-theory density uplift

## Target

Issue #633 flags Volume XII chapter 06 as a Tier-A theorem-density gap:
the local Atiyah-Singer index theorem was quoted, and the heat-kernel
coefficients used later in curved-background QFT were not derived in a local
form.

## Changes

- Added the Lichnerowicz formula with the chapter's Clifford and curvature
  conventions.
- Added the Laplace-type operator convention and the local heat-kernel
  coefficient definition.
- Added the first Seeley-DeWitt coefficients `a_0`, `a_2`, `a_4`, together
  with the transport-recursion derivation used to compute their coincidence
  limits.
- Replaced the quoted local index theorem by a theorem statement and a
  Getzler-rescaling/Mehler-kernel proof of the local index density
  `Ahat(TM) ch(E)`.
- Expanded the public calculation check for the `Ahat` genus expansion through
  degree eight.

## Verification

- `python3 calculation-checks/background_index_theory_checks.py`
- `python3 -m py_compile calculation-checks/background_index_theory_checks.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

## Status

This materially reduces the first Tier-A item in #633 but does not close the
issue.  Remaining Tier-A items include the microlocal Hadamard recursion in
Volume XII chapter 09, BPHZ theorem density in Volume II chapter 09, bound
state pole structure in Volume II chapter 03, fixed-point theorem density in
Volume III chapter 01, and the 6D `(2,0)` chapter.

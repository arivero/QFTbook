# 2026-05-26 Liouville Dual Screening Pass

## Scope

Issue #606 / Volume V Liouville depth follow-up.  This pass extends the
dual BPZ material by deriving the local Coulomb-gas coefficient for the
\(V_{-1/(2b)}\) degenerate shift channel.

## Substantive Edits

- Added a proposition deriving the formal dual one-screening coefficient
  \(\widetilde C_-(\alpha)\) using the dual screening operator \(V_{1/b}\).
- Stated explicitly that the coefficient \(\widetilde\mu\) is a
  bootstrap-screening input and not an additional classical interaction term
  in the Liouville action.
- Checked the dual OPE power
  \(2(h_{\alpha+1/(2b)}-h_\alpha-h_{-1/(2b)})\) against the free-field
  contractions.
- Rewrote the dual Dotsenko--Fateev beta-integral result into the
  \(b^{-4}\gamma(b^{-2})/\gamma(2\alpha/b)\) form used by the
  self-dual shift ledger.
- Extended `calculation-checks/liouville_bpz_checks.py` with exact affine
  gamma-argument checks and a numerical gamma-function rewrite check for the
  dual screening coefficient.
- Updated the calculation-check inventory, Chapter 13 dossier, stringbook
  crosswalk, and this build audit note.

## Verification

Final verification for this pass:

- `python3 calculation-checks/liouville_bpz_checks.py`
- `python3 -m py_compile calculation-checks/liouville_bpz_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The TeX build completed cleanly at 1844 pages.

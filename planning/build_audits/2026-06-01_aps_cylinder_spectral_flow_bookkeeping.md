# 2026-06-01 APS Cylinder Spectral-Flow Bookkeeping

## Scope

Volume XII Chapter 7 now records the exact APS cylinder identity before
passing to anomaly phases modulo \(\mathbb Z\).  The pass separates the
incoming endpoint-kernel term, the orientation reversal
\(\xi(-B_0)=-\xi(B_0)+h(B_0)\), and the sign with which a simple
negative-to-positive eigenvalue crossing contributes to the chosen APS
cylinder index representative.

## Manuscript Changes

- Added an exact-cylinder-bookkeeping paragraph after the cylinder variation
  formula for the reduced eta invariant.
- Displayed
  \[
    \operatorname{Ind}(D_X^{+,\mathrm{APS}})
    =
    I_X(E)-\xi(B_1)+\xi(B_0)-h(B_0)
  \]
  and the equivalent identity for \(\xi(B_1)-\xi(B_0)\).
- Explained that the exponentiated phase only uses the congruence modulo
  \(\mathbb Z\), while the exact representative fixes the APS endpoint and
  spectral-flow sign convention.

## Calculation Checks

- Extended `calculation-checks/eta_global_anomaly_checks.py` with exact
  rational checks for the endpoint-kernel APS cylinder identity.
- Added a finite simple-crossing model verifying that, in the chapter's
  boundary-orientation convention, the pure crossing contribution to the
  cylinder index is \(-\operatorname{sf}(B_t)\).

## Verification

Clean in this pass:

- `python3 calculation-checks/eta_global_anomaly_checks.py`
- `python3 -m py_compile calculation-checks/eta_global_anomaly_checks.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported `Pages: 2796`.

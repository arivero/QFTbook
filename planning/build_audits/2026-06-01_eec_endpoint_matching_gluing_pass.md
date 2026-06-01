# EEC endpoint matching gluing pass

Date: 2026-06-01

Issue context: GitHub #519, modern energy-correlator development.

## Scope

This pass adds the distributional endpoint-matching ledger for the normalized
energy-energy correlator in Volume II, Chapter 19.  The new passage treats the
open-interval bulk/endpoint-subtracted distribution \(\mathcal R\), the
coincident-detector atom \(K_+\delta(1-\zeta)\), and the back-to-back endpoint
atom \(K_-\delta(1+\zeta)\) as a declared gluing datum.  The two exact detector
moment identities fix \(K_+\) and \(K_-\) when both are matching coordinates,
or become a scheme-consistency test when \(K_+\) is fixed independently by the
nonperturbative contact definition.

The point is not a new theorem.  It is the minimal distributional bookkeeping
needed before perturbative endpoint formulae can be compared with the
nonperturbative detector distribution.

## Files

- `monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`
- `calculation-checks/energy_correlator_sum_rule_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_dis.md`

## Verification

- `python3 calculation-checks/energy_correlator_sum_rule_checks.py`
- `python3 -m py_compile calculation-checks/energy_correlator_sum_rule_checks.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`

All checks passed.  The full monograph build completed cleanly at 2825 pages.

## Closure status

Issue #519 remains open.  This pass addresses the endpoint-matching bookkeeping
gap, but the issue still tracks the full modern energy-correlator program,
including all-order light-ray OPE/mixing structure and higher-loop/frontier
analytic material.

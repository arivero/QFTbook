# 2026-05-26 Issue #519 EEC Sum-Rule Pass

GitHub issue: #519, concerning the modern energy-correlator/light-ray
observable program.

## Manuscript Changes

Volume II, Chapter 19 now includes Proposition
`prop:qcd-eec-sum-rules`.

- Defines the eventwise EEC distribution \(E_{2,X}(\zeta)\) in
  \(\zeta=\cos\chi\) for a physical hadronic final state.
- Proves the exact zeroth moment
  \(\int_{-1}^{1}E_{2,X}(\zeta)d\zeta=1\).
- Proves the exact first moment
  \(\int_{-1}^{1}\zeta E_{2,X}(\zeta)d\zeta=0\) in the color-singlet
  center-of-mass frame.
- Identifies the coincident-detector contact contribution at \(\zeta=1\) as
  \((\sum_r z_r^2)\delta(\zeta-1)\).
- Adds a remark explaining that perturbative calculations, resummed endpoint
  formulas, numerical approximations, and showers must specify the same contact
  convention before the sum rules can be checked.

This is a nonperturbative detector-observable layer: it uses only the physical
calorimetric measure of the final state, not colored parton labels.

## Calculation Checks

Added `calculation-checks/energy_correlator_sum_rule_checks.py`, which checks
the two moment identities and contact weights for exact finite events in
rational arithmetic.

`calculation-checks/README.md` and the QCD chapter dossier were updated.

## Verification

Completed before commit:

- `python3 calculation-checks/energy_correlator_sum_rule_checks.py`
- `python3 -m py_compile calculation-checks/energy_correlator_sum_rule_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full monograph build completed cleanly and produced
`monograph/tex/main.pdf` with 1765 pages.

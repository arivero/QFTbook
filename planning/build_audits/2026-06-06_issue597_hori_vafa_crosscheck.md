# 2026-06-06 Issue #597 Hori--Vafa Cross-Check Audit

## Scope

- Target issue: #597, instanton development with physics-facing measure and
  observable assembly.
- Chapter touched: Volume VII, Chapter 09, two-dimensional supersymmetric
  models.
- Companion check: `calculation-checks/susy_2d_lg_glsm_checks.py`.

## Substance Audit

- Physics target: the degree-one `P^{N-1}` A-twisted instanton coefficient as
  a QFT observable, not a formal mirror-root identity.
- New controlled approximation:
  `ca:cpn-hv-residue-instanton-cross-check`.
- Main mechanism: compare the Hori--Vafa mirror residue with the direct
  finite-regulator vortex/A-model coefficient only after transporting the
  vortex fugacity, retained instanton-measure integral, FI coordinate,
  determinant-line orientation, operator map, continuum residuals, and
  off-pairing contacts in one package.
- Re-audit result: aligned with the monograph standard.  This pass responds to
  the Hori--Vafa scrutiny and instanton-depth concerns by strengthening the
  amplitude/observable comparison layer.  It does not add another isolated
  moduli-space or residue cell, and it keeps planning directives out of TeX.

## Exact Checks Added

- Exact telescope:
  `C_A - S_1(q_mir) = R_vort + q_Lambda(I_Lambda,1-1)
  + (q_Lambda-q_mir) + R_op + R_cont`.
- Residual majorant including vortex, measure, FI-transport, operator, and
  continuum terms.
- Off-pairing residual budget for direct A-model contacts when the mirror root
  sum vanishes.
- Negative controls:
  mirror residue cannot bypass an unsaturated zero-mode gate; a stable-map
  line count does not supply the vortex fugacity; a stale FI coordinate changes
  the residue; and an orientation flip changes the direct vortex package even
  when the formal root sum still looks unchanged.

## Verification Plan

- Focused syntax and 2D SUSY GLSM checks.
- Focused Chapter 09 text audits.
- Calculation inventory/evidence audits.
- Dossier and monograph text audits.
- Full Python calculation suite and full monograph build after any fallout is
  repaired.

## Verification Results

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
  passed.
- `python3 calculation-checks/susy_2d_lg_glsm_checks.py` passed.
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
  passed.
- Focused Chapter 09 audits passed:
  `tools/audit_theorem_form.py`,
  `tools/audit_unnumbered_display_labels.py`,
  `tools/audit_negative_scope_prose.py --fail`, and
  `tools/audit_style_density.py --window 120 --stride 60 --fail --limit 20`.
- Global inventory/evidence/dossier/text audits passed:
  `python3 tools/audit_calculation_check_inventory.py`,
  `python3 tools/audit_calculation_evidence_contracts.py`,
  `tools/audit_chapter_dossiers.sh`, and
  `tools/audit_monograph_text.sh`.
- `tools/run_calculation_checks.sh --python-only` passed across the full
  Python calculation suite.
- `tools/build_monograph.sh` passed; the clean built PDF is
  `monograph/tex/main.pdf`.

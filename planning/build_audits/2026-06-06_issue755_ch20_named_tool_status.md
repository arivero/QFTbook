# 2026-06-06 Issue #755 Ch20 Named-Tool Status Audit

## Scope

- Target issue: #755, named-physics-theorem/status and exposition clarity.
- Chapter touched: Volume II, Chapter 20, chiral axial anomalies.
- Cross-relevant issue: #597, because the same chapter contains the BPST,
  ADHM, 't Hooft-vertex, and instanton-amplitude material.

## Substance Audit

- Added `rem:chapter20-named-tool-status-ledger` near the chapter entrance.
- The pass classifies the status of the triangle anomaly, heat-kernel/Fujikawa
  measure trace, Atiyah--Singer and APS index inputs, local BRST descent,
  Adler--Bardeen nonrenormalization, theta-sector/topological-susceptibility
  conventions, BPST/ADHM instanton measure data, and 't Hooft/instanton
  amplitude constructions.
- This is an exposition and scope repair rather than a new lemma or finite
  calculation cell.  It keeps the physics architecture readable by stating
  which parts are locally derived, which parts are imported analytic theorems,
  which are finite-regulator controlled approximations, and which physical
  amplitudes still require source, LSZ, spectral, infrared, cut, or matching
  data.

## Verification Plan

- Focused Chapter 20 theorem-form, unnumbered-display-label, negative-scope,
  and style-density audits.
- Focused BPST instanton calculation companion, because the ledger touches
  the instanton-amplitude reading of that section.
- Dossier and strict monograph text audits.
- Full monograph build/log scan after any fallout is repaired.

## Verification Results

- `git diff --check` passed.
- Metadata/process leak scan on the edited TeX for issue, directive,
  planning, and audit markers returned no matches.
- Focused Chapter 20 audits passed:
  `python3 tools/audit_theorem_form.py --root ...chapter20...tex`,
  `python3 tools/audit_unnumbered_display_labels.py --root ...chapter20...tex`,
  `python3 tools/audit_negative_scope_prose.py --root ...chapter20...tex --fail`,
  and
  `python3 tools/audit_style_density.py --root ...chapter20...tex --window 120 --stride 60 --fail --limit 20`.
- `python3 calculation-checks/bpst_instanton_normalization_checks.py` passed.
- `tools/run_calculation_checks.sh --python-only --only bpst_instanton_normalization_checks`
  passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/audit_monograph_text.sh` passed after replacing loose
  "certificate" wording in the reader-facing status ledger.
- `tools/build_monograph.sh` passed; the clean built PDF is
  `monograph/tex/main.pdf` at 3396 pages.

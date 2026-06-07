# 2026-06-07 Issue #597/#844 Instanton Observable-Map Status Re-audit

## Scope

- Primary target: #597, instantons as physical amplitudes rather than
  moduli-space-only infrastructure.
- Cross-cut target: #844, formal status machinery should not promote maps or
  residual ledgers to controlled approximations.
- Monograph target:
  `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.

## Substance

- Demoted the final instanton observable-map block from
  `controlledapproximation` to `remark`, with label
  `rem:instanton-observable-handoff-map`.
- Kept the physics content: the same finite-regulator instanton density can
  feed hard source coefficients, theta curvature, \(U(1)_A\)-odd
  zero-mode-zone kernels, and real-time axial rates only through different
  final physical maps.
- Added an explicit status boundary: the map is not a controlled estimate by
  itself; each selected row needs its own projection, positivity or
  continuation data, and residual budget.
- Updated the companion finite check so raw observable-map obligations fail a
  controlled-estimate certification, while row-wise projection budgets pass.
- Updated the Chapter 20D dossier to record the status demotion and the paired
  evidence.

## Quality Audit

- This pass deliberately avoids adding another instanton cell.  It improves
  the physical architecture by making the final observable choice part of the
  amplitude calculation rather than a label swap after the hard coefficient is
  assembled.
- The repair is local to the instanton physical-amplitude chapter and its
  evidence companion.  It does not alter the earlier hard four-source,
  normal-fluctuation, cluster, or projection formulae.
- The monograph TeX contains no process directives, review-monitoring notes,
  issue references, or planning language.

## Verification

- Focused checks passed:
  `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`;
  `PYTHONPATH=calculation-checks python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`;
  `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`.
- Focused Chapter 20D audits passed:
  `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`;
  `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`;
  `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`;
  `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --window 120 --stride 60 --fail --limit 20`;
  `tools/audit_monograph_text.sh monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- TeX process-language scan passed:
  `rg -n "claude|review|directive|monitor|issue #|GitHub|planning/build_audits" monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
  returned no matches.
- Metadata and dossier audits passed:
  `python3 -m json.tool calculation-checks/evidence_contracts.json >/dev/null`;
  `python3 tools/audit_calculation_check_inventory.py`;
  `python3 tools/audit_calculation_evidence_contracts.py`;
  `tools/audit_chapter_dossiers.sh`.
- Global checks passed:
  `tools/run_calculation_checks.sh --python-only`;
  `tools/build_monograph.sh`;
  `git diff --check`.

## Freshness

- `claude_review.md` was unchanged since 2026-06-03 07:48:35 PDT.
- Saved monitor automations remained `PAUSED`.
- Open issues were refreshed before this note.  The latest prior #597 comment
  was `8324cb32` (`Gate instanton amplitudes by physical coordinate`) at
  2026-06-07T12:24:56Z; the latest prior #844 comment was `ade94bc6`
  (`Demote SoV residual map status`) at 2026-06-07T12:37:15Z.

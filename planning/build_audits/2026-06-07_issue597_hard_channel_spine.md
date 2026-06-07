# Build Audit: Issue #597 Hard-Channel Spine

Date: 2026-06-07

## Scope

- Added `rem:instanton-su3-nf2-hard-channel-spine` and
  `eq:instanton-su3-nf2-hard-channel-spine` near the opening of Vol II Ch20D.
- Purpose: repair chapter architecture by keeping one named
  \(SU(3)\), \(N_f=2\) hard instanton channel visible from collective density
  through zero-mode source selection, normal-source response,
  Haar/LSZ/size-window transport, and final physical projection.
- This is not an ADHM/moduli-space extension and not a new continuum
  instanton theorem.  It is a physics-facing trace that prevents later
  determinant, source, size-window, and observable-map blocks from reading as
  adjacent local infrastructure.

## Companion Evidence

- Extended `instanton_physical_amplitude_architecture_checks.py` with
  `check_named_hard_channel_trace_spine()`.
- The check binds the new TeX label to a finite exact hard-channel stage
  product and rejects moduli/density-only, omitted normal-source response,
  omitted Haar/LSZ/size-window transport, raw Euclidean pre-projection, and
  linear-amplitude-as-rate shortcuts.
- Updated the calculation-check README, evidence contract tags, and Ch20D
  dossier.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `python3 tools/audit_theorem_form.py monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_unnumbered_display_labels.py monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_negative_scope_prose.py monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail --limit 20`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

Repo-wide `python3 tools/audit_style_density.py --fail --limit 20` still
reports pre-existing density windows in Vol VII/VIII/X chapters; the scoped
Ch20D style-density audit is clean.

## Monitor Note

- `claude_review.md` remained unchanged in the pre-edit monitor check
  (`Jun 3 07:48:35 2026`).
- Saved hourly monitor automations remain paused per user request.

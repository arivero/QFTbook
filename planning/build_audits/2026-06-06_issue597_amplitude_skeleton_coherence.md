# Issue #597 Amplitude Skeleton Coherence

Date: 2026-06-06

## Scope

This pass is a coherence repair for the heavily developed instanton section
in Volume II, Chapter 20.  The existing local estimates already separated
moduli data from determinants, zero-mode saturation, source matching,
endpoint control, sector isolation, and physical projection.  The remaining
reader risk was architectural: the section entrance moved too quickly from
the amplitude datum into BPST/ADHM geometry.

The manuscript insertion is `ca:one-instanton-amplitude-skeleton`, placed
immediately after `def:one-instanton-amplitude-datum` and before the ADHM
analysis.  It writes the canonical finite-regulator source coefficient as
an integral of:

- classical exponential and theta phase;
- collective-coordinate Jacobian;
- nonzero-mode determinant package;
- Berezin zero-mode source coefficient;
- source/color-singlet/OPE/amputation/hadron matching;
- size-window, endpoint, screening, or tail-subtraction factor.

It then separates the physical map from internal, sector, physical-bridge,
and scheme residual groups.  The purpose is to make the whole amplitude
pipeline visible before the reader enters the moduli-space details.

## Evidence Companion

`calculation-checks/bpst_instanton_normalization_checks.py` updates
`check_instanton_amplitude_pipeline_stage_bookkeeping()` so the finite
stage product includes the size-window factor explicitly.  The check now
rejects a size-window-omitted shortcut in addition to moduli-only and
determinant-omitted shortcuts, while preserving the source-frame reshuffling
identity and residual telescope.

## Verification

- `python3 -m py_compile calculation-checks/bpst_instanton_normalization_checks.py`
- `python3 calculation-checks/bpst_instanton_normalization_checks.py`
- `tools/run_calculation_checks.sh --python-only --only bpst_instanton_normalization_checks`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --fail`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `git diff --check`
- `tools/build_monograph.sh`

The full build completed clean and produced
`monograph/tex/main.pdf` at 3399 pages.

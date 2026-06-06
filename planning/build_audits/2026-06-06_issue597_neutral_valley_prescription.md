# Issue #597: Neutral-Pair Valley Prescription

## Scope

This pass extends the instanton physical-amplitude chapter at the point where
the one-instanton coefficient first meets connected pair corrections.  The
new block treats the neutral instanton--anti-instanton attractive
quasi-zero-mode as a lateral-prescription problem in a chosen source and
projection coordinate.

The addition is physics-facing amplitude infrastructure.  It is not an ADHM or
moduli-space expansion, and it does not treat the valley as an ordinary
positive molecule integral.  The point is to keep the pair prescription,
perturbative lateral ambiguity, zero-mode overlap, nonzero-mode determinant,
source insertion, endpoint window, and physical projection in the same
observable coordinate.

No directive, review, monitoring, or issue-tracking text was inserted into the
monograph TeX.

## Companion Evidence

`calculation-checks/instanton_physical_amplitude_architecture_checks.py` now
contains `check_neutral_pair_valley_prescription()`.  The check uses exact
rational `(PV, ambiguity)` pairs to model the valley lateral value and its
perturbative partner in one source coordinate.

The finite check verifies:

- same-coordinate cancellation of the valley and perturbative ambiguities;
- pair-only lateral values remain prescription dependent;
- principal-value-only valley integrals omit the lateral residue;
- vacuum-frame residue cancellation does not transport to a different source
  coordinate;
- dropping the source projection changes the pair residue;
- residual prescription dependence is bounded by the declared Borel and
  valley residuals.

This companion does not prove a continuum valley/renormalon theorem, nor a
complete instanton-pair resummation.  It checks the finite identity and the
negative controls needed by the chapter claim.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --window 120 --stride 60 --fail --limit 20`
- `rg -n "directive|claude_review|GitHub|issue #|monitor|planning/build_audits" monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh` clean, producing `monograph/tex/main.pdf` at
  3466 pages.

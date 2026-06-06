# Issue #597 Hard Four-Fermion Instanton Benchmark Pass

## Scope

- Expanded `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- Targeted the user concern that instanton development should prioritize
  physical amplitudes, fluctuation/source data, and endpoint control over
  moduli-space geometry.
- No process directive, monitoring note, or GitHub issue text was inserted into
  monograph TeX.

## Physics Substance

- Added the hard two-flavor four-source benchmark as a concrete
  `t Hooft-style amplitude channel.
- The new section organizes the amplitude through center conservation, shared
  Haar/orientation projection, right/left zero-mode source determinants,
  amputation/source-frame data, hard zero-mode form factors, size-window tails,
  and physical projection.
- Derived the SU(3), `N_f=2` hard-source powers:
  `b0=29/3`, local size power `rho^(32/3) d rho`,
  RG-invariant hard scaling `Lambda_ht^(29/3) Q^(-35/3)`, and dimension `-2`
  for the four-fermion coefficient.
- Recorded the endpoint warning: with four hard individual zero-mode slots the
  tail is convergent but slow, `3*6^4 prod c_l^(-3) R^(-1/3)+O(R^(-7/3))`;
  with one missing hard slot the same source profile no longer controls the
  large-size endpoint.
- Added a same-theory hard-scale ratio bound, making explicit which gates cancel
  and which data must be transported rather than silently absorbed into a
  determinant constant.

## Companion Check

- Extended `calculation-checks/instanton_physical_amplitude_architecture_checks.py`.
- New exact rational checks cover the hard `rho` and `Q` power ledger, the slow
  tail coefficient, the missing-hard-slot negative control, the center/rank/
  Haar/amputation gate ledger, determinant-only ratio rejection, source-window
  transport, and the ratio residual bound.
- Updated `calculation-checks/README.md` and the chapter dossier to record the
  new evidence surface.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture_checks`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --window 120 --stride 60 --fail --limit 20`
- `rg -n "issue #|directive|claude_review|GitHub|planning/build_audits|monitor" monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`
- `git diff --check`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`

All verification passed.  The compiled PDF has 3428 pages.

## Residual Limits

- This pass does not claim a full continuum scattering theorem for instanton
  amplitudes.
- The new benchmark is deliberately narrower: it makes the hard four-source
  amplitude gate and endpoint structure visible in the dedicated chapter, using
  exact finite checks and the larger BPST companion as evidence.

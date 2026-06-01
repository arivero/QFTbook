# Generalized Hydrodynamics Bridge Pass

## Scope

Issue #703 statmech-to-QFT absorption, Volume VI Chapter 5.

## Edit

Added an Euler-scale generalized-hydrodynamics section to the TBA chapter.
The section defines local root densities and filling functions, the dressing
equation, effective velocity `v_eff=(E')^dr/(p')^dr`, and the conditional
root-density continuity equation.  It derives charge-current conservation from
the root-density equation and separates this algebraic check from the open
problem of proving the Euler-scale closure from a local integrable QFT.  A
hard-rod calibration solves the finite collision-shift effective-velocity
equations as a non-QFT algebraic laboratory for the same state-dependent
velocity mechanism.

## Calculation Check

Added `calculation-checks/generalized_hydrodynamics_checks.py`, verifying the
finite-grid dressing/current identity and the hard-rod effective-velocity
solution.

## Verification

- `python3 calculation-checks/generalized_hydrodynamics_checks.py`
- `python3 -m py_compile calculation-checks/generalized_hydrodynamics_checks.py`
- `tools/run_calculation_checks.sh --list | rg -n "selected Python|generalized_hydrodynamics|selected Wolfram"`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported `Pages:           2800`.

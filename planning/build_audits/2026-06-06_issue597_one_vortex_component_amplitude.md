# 2026-06-06 Issue #597 One-Vortex Component-Amplitude Audit

## Scope

- Target: Volume VII, Chapter 9, the two-dimensional `N=(2,2)` GLSM and
  Hori--Vafa scrutiny lane.
- Issue: #597, instantons as physical amplitudes rather than moduli-space
  geometry alone.
- Local focus: turn the one-vortex source-functional bridge into a concrete
  finite component-amplitude extraction.
- Calculation companion: `calculation-checks/susy_2d_lg_glsm_checks.py`.

## Substance Added

- Added `ca:glsm-one-vortex-component-amplitude-cell`.
- The new cell projects two component sources to overlap vectors on the two
  universal fermion zero modes.
- The Berezin integral extracts the oriented source minor
  `u_{A,+}u_{B,-}-u_{A,-}u_{B,+}`.
- A primed nonzero-mode contact term is kept separate from the protected
  vortex coefficient.
- The component residual bound now includes source, propagator, determinant,
  zero-mode, compactification, operator, and continuum slots.

## Quality Audit

- This is a physical source-amplitude pass, not a moduli-space expansion.
- It prevents the Hori--Vafa monomial or protected coefficient from being used
  as a substitute for a component amplitude.
- It makes parallel source overlaps a genuine zero-mode saturation failure,
  even when the protected vortex coefficient is nonzero.
- Process and issue-tracking language stays in this planning audit and the
  dossier, not in monograph TeX.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
  passed.
- `python3 calculation-checks/susy_2d_lg_glsm_checks.py` passed.
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
  passed.
- Focused Ch09 theorem-form, unnumbered-display-label, negative-scope, and
  style-density audits passed.
- Process-language scan of the touched TeX and calculation-check surfaces
  found no matches.
- `git diff --check` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/audit_monograph_text.sh` passed after replacing the weak phrase
  "schematic form" by a finite-regulator component-amplitude statement.
- `python3 tools/audit_calculation_check_inventory.py` passed.
- `python3 tools/audit_calculation_evidence_contracts.py` passed.
- `tools/build_monograph.sh` passed; `monograph/tex/main.pdf` rebuilt and
  log-scanned clean at 3451 pages.
- `tools/run_calculation_checks.sh --python-only` passed; Wolfram checks were
  not selected.

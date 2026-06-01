# Weak Integrability-Breaking Collision-Cell Pass

## Scope

Issue #703 statmech-to-QFT absorption, Volume VI Chapter 5.

## Edit

Added a weak-integrability-breaking kinetic-cell section after the
Euler-scale GHD bridge.  The section defines a finite collision-cell datum:
cell states, stationary weights, detailed-balance transition rates, exact
conserved cell observables, occupation variables, and the projected collision
functional.  It proves the finite relative-entropy production identity and
the exact conservation of transition-graph charges before introducing the
controlled kinetic scaling ansatz
\[
  \partial_t\rho_i+\partial_x(v_i^{\rm eff}\rho_i)
  =
  \varepsilon^2 C_i[P_{x,t}]
  +
  R_i^{(\varepsilon,\ell,X)} .
\]
The text explicitly separates this finite algebra from the open microscopic
problem of deriving the transition rates and the vanishing remainder from a
local integrable QFT perturbed by a local operator.

## Calculation Check

Added `calculation-checks/weak_breaking_collision_cell_checks.py`, verifying
detailed balance, exact projected energy conservation, relaxation of a
higher Bethe-type charge under allowed transitions, and the symmetrized
relative-entropy production identity.

## Verification

- `python3 calculation-checks/weak_breaking_collision_cell_checks.py`
- `python3 -m py_compile calculation-checks/weak_breaking_collision_cell_checks.py`
- `tools/run_calculation_checks.sh --list | rg -n "selected Python|weak_breaking_collision_cell|selected Wolfram"` reported 210 Python checks and 2 Wolfram Language checks.
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported `Pages:           2803`.

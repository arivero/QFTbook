# Volume VI q-oscillator RLL development

## Scope

- Addressed the explicit trigonometric rank-one q-oscillator \(L\)-operator
  gap tracked in issue #694.
- Added the six-vertex \(R\)-matrix convention, the Fock q-oscillator
  realization, the Borel-generator normalization, and the local RLL identity
  directly to Volume VI Chapter 5B.
- Added an exact rational finite-basis regression check for the component
  identity
  \(R_{12}(-x/y)L^{(+)}_{\mathcal F,13}(x)L^{(+)}_{\mathcal F,23}(y)
    =L^{(+)}_{\mathcal F,23}(y)L^{(+)}_{\mathcal F,13}(x)R_{12}(-x/y)\).

## Verification

- `python3 calculation-checks/nested_integrability_checks.py`
- `python3 -m py_compile calculation-checks/nested_integrability_checks.py`

## Remaining Issue #694 Work

- More model-specific nested TBA/string examples for principal chiral model
  and Gross--Neveu families still remain before #694 should be closed.

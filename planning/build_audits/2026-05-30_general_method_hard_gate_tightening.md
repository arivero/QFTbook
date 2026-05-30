# General-Method Hard-Gate Tightening

Date: 2026-05-30

## Directive

General-method machinery should not be exposed in a specialized chapter at all
if the specialized chapter has no concrete result to extract using it.

## Harness Change

- Tightened `planning/12_strict_writing_harness.md` so the rule is an explicit
  hard rejection criterion.
- Defined a concrete result as a stated observable, spectral datum, bound,
  coefficient, pole location, susceptibility, matrix element, continuum
  extrapolation, or controlled numerical/analytic comparison whose definition
  uses the model-specific field content, regularization, symmetry channel, and
  limit.
- Stated that a future plan, generic route, or possible later application does
  not qualify.

## Targeted Context Audit

Reviewed the current remaining method-related hits:

- Pure Yang--Mills glueball spectroscopy in Volume II: acceptable.  The text
  names GEVP only as a general finite-regulator method and keeps the local
  content to Wilson-loop source spaces, cubic channels, reflection positivity,
  and continuum/infinite-volume spectral data.
- QCD spectroscopy in Volume II: acceptable.  The references to GEVP are tied
  to source-overlap interpretation, finite-volume energy extraction, and
  subsequent pole reconstruction; the chapter does not teach the general GEVP
  method locally.
- Integrability bridge in Volume VI: acceptable.  The chapter explicitly says
  that no nonintegrable finite-volume spectrum is extracted there and therefore
  does not expose TCSA machinery beyond a cross-reference.
- VOA logarithmic character discussion in Volume V: not a general numerical
  method placement issue; "generalized eigenvalue" is representation-theoretic
  language for \(L_0\) Jordan structure.

No manuscript relocation was required in this pass.

# 2026-05-27 Volume I Spinor Grassmann Formalization

## Scope

Issue #615 asks for substantial Volume I chapters to be upgraded from flowing
derivations to labeled theorem/proof structure.  This pass targets Volume I,
Chapter 16, because it converts massive spinor intertwiners into local Dirac
fields, proves the free-field CAR locality sign, and fixes the finite
Berezinian algebra underlying fermionic path integrals.

## Manuscript Changes

- Added definitions for the spinor convention/intertwiner data and the free
  charged Dirac field with CAR.
- Proved the free Dirac equations from the momentum-space intertwiners and
  recorded the oscillator charge convention giving charge \(+1\) to
  \(\widehat\psi\).
- Recast the free spinor statistics-sign calculation as a proposition: ordinary
  commutators give a nonlocal even scalar kernel, while CAR give the
  Pauli--Jordan distribution acted on by a local Dirac operator.
- Added a definition of finite fermionic configuration superspaces as locally
  super-ringed spaces or functor-of-points objects.
- Proved the purely odd Berezinian transformation law from top-coefficient
  extraction.
- Recast the finite Berezin Gaussian and contraction formulas as a proposition
  and supplied the determinant, source-shift, and integration-by-parts proof.
- Recast the coherent-state resolution and the trace/supertrace endpoint sign
  distinction as labeled propositions with finite two-state proofs.

## Companion Checks

- Added `calculation-checks/spinor_grassmann_checks.py`.
- The script checks the finite sign algebra behind the free Dirac phase
  equations, \(U(1)\) oscillator charge ledger, CAR locality sign, odd Dirac
  bracket, purely odd Berezinian inverse determinant, one-pair Berezin
  Gaussian normalization, and coherent-state trace/supertrace endpoint signs.
- Updated the calculation-check README and the Chapter 16 dossier.

## Verification

Completed before commit:

- `python3 calculation-checks/spinor_grassmann_checks.py`
- `python3 -m py_compile calculation-checks/spinor_grassmann_checks.py`
- weak-language scan on the edited chapter, dossier, audit note, check script,
  and calculation-check README
- long-line scan on the edited chapter, dossier, audit note, check script, and
  calculation-check README
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported 2120 pages

# 2026-05-27 Volume I Maxwell Formalization

## Scope

This pass continues issue #615 on Volume I formalization.  It targets
Chapter 18, the Maxwell constraints and gauge-fixing chapter, because this
chapter supplies the free gauge representative, Gupta--Bleuler quotient, and
field-strength observable bridge used by the later QED, BRST, nonabelian
gauge-theory, and BV developments.

## Manuscript Changes

- Separated Proposition `prop:field-strength-descends-gupta-bleuler` from its
  proof, making the claim that field-strength smearings descend to the
  Gupta--Bleuler quotient and agree with reduced helicity correlators a
  theorem-level statement with an explicit proof.
- Separated Proposition `prop:maxwell-field-strength-one-photon-spectral-data`
  from its proof, making the gauge-parameter cancellation, helicity spectral
  representation, \(C_\mu\)-independence, and normalization \(Z_A=1\) traceable
  as a single result.
- Removed a duplicated closing paragraph left at the end of the chapter.

## Companion Checks

- Added `calculation-checks/maxwell_gauge_checks.py`.
- The script checks the finite sign and normalization algebra behind the
  chapter: axial-gauge inverse, covariant-gauge inverse, Faddeev--Popov slice
  Jacobian, Gupta--Bleuler null quotient, helicity-completeness
  \(C_\mu\)-term cancellation, and cancellation of longitudinal representative
  terms from field-strength correlators.
- Updated the calculation-check README and the Chapter 18 dossier.

## Verification

Completed before commit:

- `python3 calculation-checks/maxwell_gauge_checks.py`
- `python3 -m py_compile calculation-checks/maxwell_gauge_checks.py`
- weak-language scan on the edited chapter, dossier, audit note, check script,
  and calculation-check README
- long-line scan on the edited chapter, dossier, audit note, check script, and
  calculation-check README
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported 2114 pages.

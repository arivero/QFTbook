# 2026-05-27 Volume I Massless Helicity Formalization

## Scope

Issue #615 asks for the substantial Volume I chapters to be upgraded from
flowing derivations to labeled theorem/proof structure.  This pass targets
Volume I, Chapter 17, because the massless little group, gauge-boson
polarization representatives, and spinor-helicity conventions are
convention-sensitive and load-bearing for later gauge-theory chapters.

## Manuscript Changes

- Added a definition of the massless orbit and standard section \(L(k)\).
- Proved that the future-null little algebra is \(ISO(2)\), with one
  transverse rotation and two null translations.
- Proved the null-translation matrix properties: Lorentz invariance, fixing
  the reference null momentum, and additive parameter composition.
- Added a definition of massless helicity representations and a proposition
  isolating the continuous-spin alternative.
- Proved the Wigner cocycle identity and helicity-frame change law.
- Proved explicitly that little-group translations act on vector
  polarization representatives by \(k_\mu\)-shifts.
- Proved field-strength descent to the helicity line and the auxiliary-vector
  polarization-projector transversality identities.
- Added formal statements for spinor-helicity frames, the mostly-plus
  determinant identity, BCFW on-shell kinematics, BCFW recursion with boundary
  term, and the adjacent-negative Parke--Taylor MHV amplitude under explicit
  tree-level hypotheses.

## Companion Checks

- Added `calculation-checks/massless_helicity_checks.py`.
- The script checks the finite matrix and spinor algebra behind the chapter:
  \(T^T\eta T=\eta\), \(Tq=q\), null-translation parameter addition,
  polarization shifts, transverse projector identities, the spinor determinant
  identity, and BCFW momentum conservation/on-shellness.
- Updated the calculation-check README and the Chapter 17 dossier.

## Verification

Completed before commit:

- `python3 calculation-checks/massless_helicity_checks.py`
- `python3 -m py_compile calculation-checks/massless_helicity_checks.py`
- weak-language scan on the edited chapter, dossier, audit note, check script,
  and calculation-check README
- long-line scan on the edited chapter, dossier, audit note, check script, and
  calculation-check README
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported 2108 pages

# 2026-05-27 Volume I LSZ Formalization

## Scope

This pass continues issue #615 on Volume I formalization.  It targets
Chapter 13, the LSZ reduction chapter, because it is the logical bridge from
the nonperturbative Haag--Ruelle \(S\)-operator to perturbative scattering
calculations.  The pass strengthens the chapter without moving perturbative
Feynman-graph scattering before Haag--Ruelle and LSZ.

## Manuscript Changes

- Added Definition `def:lsz-external-boundary-value-extraction`, making the
  LSZ operation a distributional mass-shell boundary-value coefficient after
  wave-packet smearing.
- Added a proof block for Theorem `thm:lsz-wave-packet`, with the steps
  separated into Haag--Ruelle approximants, locality/time-ordering,
  large-time pole selection, and on-shell wave-packet pairing.
- Added the invariant-denominator/linear-residue calculation, recording the
  mostly-plus denominator factorization and the relation between the invariant
  coefficient \(-iZ_\phi\) and the two linear \(k^0\)-pole residues.  This was
  later demoted from a proposition to a worked paragraph in the anti-wrapper
  pass.
- Added Proposition `prop:lsz-pole-spectral-projection`, proving the
  Hilbert-space spectral-projection identity behind the one-particle pole.
- Added the external-pole stability calculation, recording that local contact
  terms and zero-overlap field components do not contribute to external LSZ
  residues and that nonzero interpolating-field coordinate changes cancel
  against the corresponding \(Z_{\phi'}^{-1/2}\) factors.  This was later
  demoted from proposition form in the anti-wrapper audit.
- Added Proposition `prop:lsz-large-time-pole-selector`, recording the
  incoming/outgoing contour calculation that selects the relevant Feynman
  pole in the large-time limit.

## Companion Checks

- Added `calculation-checks/lsz_residue_checks.py`.
- The script checks the finite convention algebra behind the chapter:
  mostly-plus denominator factorization, partial-fraction signs, per-leg LSZ
  cancellation, all-incoming momentum bookkeeping, and Lorentzian
  source-derivative phase compensation.
- Updated the calculation-check README and the Chapter 13 dossier.

## Verification

Completed before commit:

- `python3 calculation-checks/lsz_residue_checks.py`
- `python3 -m py_compile calculation-checks/lsz_residue_checks.py`
- weak-language scan on the edited chapter, dossier, audit note, check script,
  and calculation-check README
- long-line scan on the edited chapter, dossier, audit note, check script, and
  calculation-check README
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported 2113 pages.

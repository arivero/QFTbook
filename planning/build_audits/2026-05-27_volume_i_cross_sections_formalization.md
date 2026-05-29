# 2026-05-27 Volume I Cross-Section Formalization

## Scope

This pass continues issue #615 on Volume I formalization.  It targets
Chapter 14, the cross-section, phase-space, and partial-wave unitarity
chapter, because it is the first chapter after LSZ where the nonperturbative
\(S\)-operator is converted into measurable scattering probabilities.

## Manuscript Changes

- Added Definition `def:scattering-transition-probability-event-class`,
  making the Hilbert-space transition probability into an outgoing event
  class the primary object before sharp-momentum kernels are introduced.
- Added Definition `def:invariant-amplitude-convention`, recording the
  ordered \(T\)-matrix and invariant-amplitude convention inherited from LSZ.
- Added Proposition `prop:sharp-momentum-density-limit-cross-section`, proving
  the regulated delta-square density limit used by the plane-wave
  cross-section formula.
- Added Definition `def:invariant-final-state-phase-space`, Proposition
  `prop:invariant-two-particle-flux`, and Definition
  `def:differential-cross-section-invariant-data`, separating phase-space
  measure, flux, and cross-section data.
- Added the two-body phase-space reduction derivation,
  deriving the \(D=4\) two-body phase-space coefficient and \(2\to2\)
  differential cross section.
- Added Theorem `thm:sharp-kernel-unitarity-optical-theorem`, proving the
  amplitude-level unitarity relation and optical theorem with the correct
  Hilbert-space adjunction ordering.
- Added Proposition `prop:partial-wave-unitarity-circle`, proving the elastic
  unitarity circle and inelastic disk in \(b_\ell=\beta a_\ell\).

## Companion Checks

- Added `calculation-checks/cross_section_partial_wave_checks.py`.
- The script verifies the finite rational algebra behind the Kallen momentum
  formula, invariant flux, two-body phase-space coefficient, identical
  \(\phi^4\) tree cross-section coefficient, ordered \(16\pi\) partial-wave
  normalization, and elastic/inelastic partial-wave unitarity geometry.
- Updated the calculation-check README and the Chapter 14 dossier.

## Verification

Completed before commit:

- `python3 calculation-checks/cross_section_partial_wave_checks.py`
- `python3 -m py_compile calculation-checks/cross_section_partial_wave_checks.py`
- weak-language scan on the edited chapter, dossier, audit note, check script,
  and calculation-check README
- long-line scan on the edited chapter, dossier, audit note, check script, and
  calculation-check README
- `git diff --check`
- `tools/build_monograph.sh`
- second `tools/build_monograph.sh` cross-reference settling pass
- `rg -n "undefined|Rerun|Warning" monograph/tex/main.log | tail -n 40`
  reported no unresolved reference warnings
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported 2116 pages.

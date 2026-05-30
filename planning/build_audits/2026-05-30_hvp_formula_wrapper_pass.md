# 2026-05-30 HVP Formula Wrapper Pass

## Scope

Anti-wrapper pass on Volume II,
`chapter19c_standard_model_hybrid_definition.tex`, in the muon \(g-2\)
hybrid-observable section.

The former lemma `Dispersive form of leading HVP` was already more modest than
proposition rank, but the proof content was still a formula derivation: insert
the hadronic vacuum-polarization scalar into the one-loop Pauli-kernel
representation, use the once-subtracted spectral representation of the
gauge-invariant electromagnetic current-current correlator, interchange the
positive integrals, and simplify the Feynman-parameter kernel.

## Changes

- Removed the lemma/proof wrapper.
- Kept the labelled formulae
  `eq:sm-hvp-dispersive`, `eq:sm-hvp-kernel`,
  `eq:sm-hvp-feynman-parameter`, and
  `eq:sm-hvp-subtracted-dispersion`.
- Rewrote the passage as `Dispersive leading-HVP formula`, explicitly stating
  that it is not an independent theorem about QCD.  The nonperturbative
  content remains the hadronic current-current spectral data.
- Updated the Standard Model chapter dossier and added the old title to the
  theorem-form harness so it cannot reappear as a theorem-family wrapper.

## Status

This continues issue #691 and also respects the Standard Model/hybrid-QFT
directive: phenomenological formulae are kept as precise matched-coordinate
derivations, not as overpromoted theorem statements.

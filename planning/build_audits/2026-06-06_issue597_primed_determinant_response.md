# Issue #597 Primed Determinant Response Audit

## Scope

- Volume II Ch20D, normal-fluctuation/source-response section.
- Target: make the source-dependent response of the one-loop fluctuation
  determinant visible as part of the physical instanton amplitude pipeline.
- This is fluctuation and measure normalization work, not an ADHM or
  moduli-space expansion.

## Changes

- Added `ca:instanton-primed-determinant-source-response`.
- The new block derives the primed bosonic determinant response
  `-1/2 Tr'(G R) + 1/4 Tr'(G R G R)` and the Dirac nonzero-mode response
  `Tr'(G_F S) - 1/2 Tr'(G_F S G_F S)`, with finite counterterms in the same
  regulator coordinate.
- Updated `instanton_physical_amplitude_architecture_checks.py` with an exact
  rational finite-matrix regression for the determinant expansion and negative
  controls for unprimed zero-mode-regulated traces, wrong bosonic signs, and
  determinant-constant-only shortcuts.
- Updated the calculation-check README and Ch20D dossier.

## Re-Audit

- The added TeX is physics derivation and fluctuation-normalization logic only.
  No directive, review, monitoring, or issue-process language was added to the
  monograph.
- The pass strengthens the chapter's amplitude flow: the determinant is not
  just a universal density constant or a moduli-space factor; when the selected
  source/background perturbs the quadratic normal operator, the amplitude
  receives a primed resolvent trace contribution in the same gauge slice and
  counterterm scheme.

# Lieb-Robinson And Quasi-Adiabatic Phase-Stability Pass

Date: 2026-05-31

## Trigger

GitHub issue #703 tracks statmech-to-QFT absorption.  After adding the finite
\(\mathbb Z_2\) gauge-code laboratory, the remaining finite-locality thread
needed the actual locality machinery that lets a regulated gapped Hamiltonian
path transport local phase data.

## Edits

- Added a finite-regulator locality section to Volume IX, Chapter 7 immediately
  after the declared phase definition.
- Defined finite interaction terms, interaction-overlap degree, interaction
  boundary, and overlap-chain distance.
- Proved the finite path-count Lieb--Robinson estimate directly from Duhamel's
  formula, commutator expansion, overlap-chain counting, and the factorial
  tail bound.
- Derived isolated-band spectral transport from the finite projection identity
  \(P^2=P\), with the global projection generator displayed separately from
  any locality conclusion.
- Introduced the quasi-adiabatic filter convention
  \(\widehat F_\gamma(\omega)=i/\omega\) outside the gap and verified the
  finite off-diagonal transport equation
  \(\partial_sP_\Lambda=i[D_\Lambda,P_\Lambda]\).
- Explained the locality mechanism by combining the filter time-window split
  with the Lieb--Robinson leakage estimate for evolved local terms.
- Added a public calculation check for overlap-chain counting, LR exponential
  tails, two-level spectral-flow algebra, and the quasi-local tail split.
- Updated the calculation-check manifest, Volume IX Chapter 7 dossier, and
  statmech crosswalk.

## Verification Plan

- Run the new locality/spectral-flow calculation check.
- Run theorem-form, display-label, text, negative-scope, and chapter-dossier
  audits.
- Build the monograph and scan the log.
- Comment on #703 as a completed finite-locality subpass while keeping the
  issue open for the remaining statmech absorption tracks.

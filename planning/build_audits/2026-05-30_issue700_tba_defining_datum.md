# 2026-05-30 Issue #700 TBA Defining Datum Pass

## Scope

Issue #700 listed Volume VI Chapter 5 as a defining-property gap: the
Thermodynamic Bethe Ansatz chapter developed Bethe--Yang equations, densities,
entropy, pseudoenergy, and finite-size energy from equations in prose, but the
central TBA object was not crystallized as a named datum at the chapter
opening.

## Manuscript Changes

- Added `def:diagonal-massive-tba-datum` at the start of
  `volume_vi/chapter05_thermodynamic_bethe_ansatz.tex`.
- The datum aggregates:
  - species set and positive masses;
  - diagonal real-axis scattering amplitudes and phase branches;
  - logarithmic derivative kernels as functions or distributions;
  - circle quantization shifts;
  - thermodynamic root-density convergence and the density constraint;
  - exclusion-statistics entropy convention;
  - thermal and mirror-channel normalizations.
- Updated the Bethe--Yang section to unpack the named datum rather than
  beginning from an implicit recipe.
- Added a label to the finite-size ground-state-energy section so the datum
  can point to the normalization used by the chapter.
- Updated the Volume VI Chapter 5 dossier.

## Audit Status

This is a definition-integrity pass.  It does not change the variational TBA
proof or the Majorana/Lee--Yang computations.  It makes explicit which
objects and assumptions those derivations use.


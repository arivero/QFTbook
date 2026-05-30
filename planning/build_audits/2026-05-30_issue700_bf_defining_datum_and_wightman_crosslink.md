# 2026-05-30 Issue #700/#701 BF Datum And Wightman Cross-Link Pass

## Scope

This pass addresses two concrete audit findings.

- Issue #700 listed Volume VIII Chapter 3 as a major defining-property gap:
  BF theory was developed from action-level prose without an upfront block
  naming the central object and its constituent data.
- Issue #701 noted that the detailed Wightman definition in Volume IV Chapter
  1 needed an explicit relation to the framework-level Wightman presentation
  introduced in the opening volume.

## Manuscript Changes

- Added `def:closed-manifold-bf-theory-datum` at the opening of
  `volume_viii/chapter03_bf_theory.tex`.
- The datum now aggregates the closed oriented manifold, compact gauge group,
  principal bundle, invariant pairing, field space, exponentiated action,
  ordinary gauge symmetry, \(B\)-shift symmetry, reducibility status, extended
  observable data, and quantization status.
- Added a section label for the finite \(\mathbb Z_N\) cochain model so the
  definition can point to the precise finite abelian realization.
- Updated the nonabelian section opening to state that it unpacks the named
  datum.
- Updated `volume_iv/chapter01_wightman_fields_and_reconstruction.tex` to
  identify `def:cyclic-wightman-field-presentation` as the cyclic, tempered,
  Minkowski-space specialization of the framework-level definition
  `def:wightman-field-presentation-opening`.
- Updated the Volume VIII Chapter 3 and Volume IV Chapter 1 dossiers.

## Audit Status

The BF edit is a definition-integrity pass rather than a proof wrapper.  It
does not promote any finite algebraic calculation to theorem form.  The
remaining issue #700 defining-property targets still include SUSY moduli
spaces, TBA, anomaly inflow, discrete theta terms, and several partial gaps
listed in the issue thread.


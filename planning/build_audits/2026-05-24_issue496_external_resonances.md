# Issue #496 External Resonances Audit

## Scope

- Oldest open GitHub issue addressed after #491.
- Expanded the resonance chapter beyond the warning that resonances are absent
  from ordinary LSZ external states.
- Added a local pole-residue construction, rigged-Hilbert/Gamow boundary, and
  obstruction ledger.

## Manuscript Changes

- Added `Pole-Factorized Resonance Objects` with definitions of local pole
  neighborhoods, residue kernels, rank-one factorization, normalization
  equivalence, and nested residues for several isolated resonance variables.
- Added an inherited-properties proposition proving field-redefinition
  invariance, covariance, stable-channel unitarity constraints, and BRST
  representative independence by applying residue functionals to
  stable-channel amplitudes.
- Added a Gamow-functional section separating rigged-Hilbert representations
  of pole data from normalizable Hilbert-space external particles.
- Added threshold, coupled-channel, overlapping-pole, line-shape, and
  long-range/massless obstructions.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean, including final log scan.

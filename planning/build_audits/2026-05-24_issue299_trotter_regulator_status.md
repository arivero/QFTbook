# Issue #299 Audit: Trotter Applicability Depends on the QFT Regulator

## GitHub Issue

- #299, opened 2026-05-22:
  `[Vol I Ch 11] Trotter formula reused inappropriately for QFT`.

## Manuscript Changes

- `monograph/tex/volumes/volume_i/chapter08_scalar_path_integrals_and_euclidean_green_functions.tex`
  now contains a finite-dimensional Schrödinger-regulator criterion.
- The paragraph states the precise finite-dimensional regulator hypotheses
  under which Chapter 4's Trotter--Kato/Feynman--Kac theorem applies:
  `E_\Lambda\simeq\mathbb R^{M_\Lambda}`, positive constant-coefficient
  kinetic quadratic form, and a locally Kato bounded-below potential
  `U_\Lambda` defining a closed semibounded Friedrichs form.
- The accompanying explanation reduces the regulator Hamiltonian to the
  finite-dimensional Schrödinger theorem of Chapter 4 by a linear change of
  variables.  This is deliberately not presented as an independent proposition:
  the mathematical theorem is the Chapter 4 Trotter--Kato/Feynman--Kac result.
- The chapter now names finite spatial lattices in finite boxes and genuine
  finite-mode stable polynomial truncations as examples where the theorem can
  be invoked.
- The chapter now explicitly excludes continuum smooth cutoffs that leave
  infinitely many spatial modes, formal covariance cutoffs, direct Euclidean
  spacetime lattice actions without a transfer-matrix/Hamiltonian
  construction, and purely perturbative cutoffs from the automatic Trotter
  argument.
- The compact symbol `[D\phi]` is now explicitly said not to imply a positive
  Borel measure; positive Borel measures are one mathematical object for some
  bosonic Euclidean scalar theories, not the definition of a general QFT path
  integral.

## Planning Updates

- Updated the Chapter 8 dossier framework, notation, definition ledger, claim
  ledger, and audit targets to enforce the regulator distinction.

## Verification

- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed; full TeX build and final log scan clean.

# Build Audit: Issue #597 Hard-Amplitude Assembly Ledger

Date: 2026-06-06

Scope:
- Continued the dedicated instanton physical-amplitude chapter in
  `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- Added an assembled hard-channel formula that combines the determinant scheme
  constant, hard zero-mode source kernel, nonzero-mode source quotient,
  zero-mode/source stability, and physical projection in one amplitude
  coordinate.
- Updated the companion check, calculation-check inventory, and Chapter 20D
  dossier.

Physics-depth rationale:
- This pass targets the physical amplitude built from the BPST saddle, rather
  than the geometry of the instanton moduli space.
- The new ledger prevents separate infrastructure blocks from becoming a
  loose list of cells: the hard four-source coefficient is controlled only
  after all channel factors multiply the same Haar-projected, amputated,
  windowed, and physically projected kernel.
- The error budget is absolute by default and requires a noncancellation
  margin before any relative hard-scale statement is justified.

Companion evidence:
- `calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  now verifies the assembled multiplicative error bound on a signed hard
  window, rejects determinant-only assembly, rejects signed-window relative
  control without a noncancellation margin, and checks that an untransported
  source quotient changes a same-scheme hard ratio.

Scope guard:
- No directives, issue-tracker text, or monitoring instructions were inserted
  into monograph TeX.
- This pass advances the amplitude/source/fluctuation side of issue #597.

# Build Audit: Issue #597 Individual Zero-Mode Slot

Date: 2026-06-06

Scope:
- Continued the instanton physical-amplitude lane in
  `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- Added an amplitude-facing derivation of the individual singular-gauge BPST
  zero-mode slot form factor and its hard endpoint tail.
- Updated the focused companion check, calculation-check inventory, and Chapter
  20D dossier.

Physics-depth rationale:
- This pass opens a compressed input in the hard `t Hooft-style four-fermion
  benchmark.  The large-size endpoint is controlled by the Fourier transform of
  individual external zero-mode slots, not by the instanton moduli space.
- The derivation records the cancellation of the apparent `t^(-1)` Bessel
  product terms and the resulting `F_zm(cs/2)=6 c^(-3)s^(-3)+O(s^(-5))`
  slot tail.
- It separates differentiated fermion slots from fused bilinear-density
  sources, whose `z K_1(z)` kernel has exponential large-momentum decay.

Companion evidence:
- `calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  now derives the `3/(4t^3)` and `6 z^(-3)` coefficients by exact rational
  algebra, verifies the four-slot product tail and `R^(-1/3)` endpoint
  coefficient, and rejects fused-density endpoint substitution and hidden
  unamputated-residue absorption.

Scope guard:
- No directives, issue-tracker text, or monitoring instructions were inserted
  into monograph TeX.
- This is not ADHM or compactification infrastructure.  It advances the
  fluctuation/source/amplitude side of the instanton chapter.

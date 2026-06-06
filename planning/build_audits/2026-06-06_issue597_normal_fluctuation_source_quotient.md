# Build Audit: Issue #597 Normal-Fluctuation Source Quotient

Date: 2026-06-06

Scope:
- Continued the instanton physical-amplitude lane in
  `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- Added a local finite Gaussian quotient for source-dependent nonzero-mode
  fluctuations in a selected hard instanton channel.
- Updated the focused companion check, calculation-check inventory, and Chapter
  20D dossier.

Physics-depth rationale:
- The pass targets the source/fluctuation part of an instanton amplitude, not
  ADHM or compactification infrastructure.
- The determinant constant normalizes the nonzero-mode Gaussian measure, but a
  selected four-source amplitude also needs the fluctuation average of the
  source insertion under that same measure.
- The new block separates the Gaussian source mean, the covariance with the
  nonzero-mode interaction weight, the quadratic `1/2 Tr(QC)` source trace
  correction, and the absolute residual bound.

Companion evidence:
- `calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  now verifies the finite source quotient covariance identity, the Cauchy
  covariance bound, the quadratic trace correction, propagation through a
  signed hard window using the absolute mass, and rejection of a relative
  quotient after zero-mode rank loss.

Scope guard:
- No directives, issue-tracker text, or monitoring instructions were inserted
  into monograph TeX.
- This pass advances the fluctuation/source/amplitude side of issue #597.

# Issue #319: Scattering Time-Ordered Correlator Status

## Issue

The Vol II scattering chapters used \(Z_\phi\), time-ordered Green functions,
Feynman graphs, and Feynman-parameter integrals without a local declaration of
which path-integral or operator status was operative.

## Resolution

- Added `def:scattering-time-ordered-correlator-status` at the opening of the
  scattering-kernel chapter.
- Declared three allowed statuses for time-ordered correlators in the
  scattering chapters:
  - exact Hilbert-space distributions with spectral one-particle pole data;
  - Euclidean reconstructed distributions after OS/analytic-continuation
    hypotheses;
  - formal or regulator-dependent perturbative coefficients.
- Stated explicitly that Haag--Ruelle defines the scattering operator as
  \(\Omega_{\mathrm{out}}^*\Omega_{\mathrm{in}}\), not by a path integral.
- Added local reminders in the Bethe--Salpeter and analyticity/Landau
  chapters.
- Updated the relevant chapter dossiers.

## Verification

Run from a clean worktree:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

# Build Audit: Issue #311 BV Half-Density Measure

Issue: GitHub #311, concerning the undefined measure in BV integrals over a
gauge-fixing Lagrangian submanifold.

Resolution:

- Added a finite-dimensional half-density section to the BV chapter.  The
  canonical BV operator \(\Delta_{1/2}\) acts on half-densities on the odd
  symplectic BV space.
- Introduced a normal reference half-density \(\sigma_0\) as part of the
  quantum BV regulator datum.  Its square is the Berezinian density, and it
  induces the function BV Laplacian
  \(\Delta_{\sigma_0}F=\sigma_0^{-1}\Delta_{1/2}(F\sigma_0)\).
- Defined the density on the gauge-fixing Lagrangian by restriction:
  \(D_{\sigma_0,\Psi}\Phi=\iota_\Psi^*\sigma_0\).  This replaces the
  undefined \([D\Phi]\) in the 1PI BV source functional.
- Rewrote the QME and Wilsonian BV pushforward in semidensity form:
  \(\Delta_{1/2}(\exp(\ii S/\hbar)\sigma_0)=0\) and integration of
  semidensities over the high-mode Lagrangian cycle.

Verification:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

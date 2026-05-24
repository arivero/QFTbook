# Build Audit: Issue #310 Regulated Measure Conventions

Issue: GitHub #310, concerning the conflicting meanings of
\([D\phi]_\Lambda\).

Resolution:

- Added Definition `def:regulated-scalar-integration-conventions` in Volume I,
  Chapter 8.  The finite-dimensional bosonic scalar reference density is
  \(D_\Lambda^{\rm ref}\phi\).  The Gaussian measure
  \(\dd\mu_{C_\Lambda}\) carries the quadratic kinetic form.  The full
  Euclidean density \(\dd\rho_{\Lambda,S}\) is the interaction weight times
  that Gaussian measure.
- Rewrote the Euclidean scalar correlator convention so the same formula is
  expressed either with \(D_\Lambda^{\rm ref}\phi\,e^{-S_{E,\Lambda}}\) or
  with \(\dd\mu_{C_\Lambda}\,e^{-L_\Lambda}\), with the kinetic factor placed
  explicitly.
- Rewrote Wilsonian source and low-field formulas to use the Gaussian measures
  \(\dd\mu_{C_\Lambda}\) and
  \(\dd\mu_{\widehat C_{\Lambda_0,\Lambda}}\), instead of using the same
  compact symbol for both reference density and Gaussian measure.
- Updated the generating-functional and local-counterterm chapters to state
  which regulated integration object is being used.  For gauge, fermionic,
  BV, Lorentzian oscillatory, dimensional-regularization, or algebraic
  regularizations, the integration object must be specified by the
  construction rather than inherited from the scalar reference-density symbol.

Verification:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

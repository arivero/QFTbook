# BCFT Boundary Gradient Proof-Boundary Pass

Date: 2026-05-30

## Scope

- Addressed the quoted-theorem proof-debt discipline attached to the boundary
  entropy gradient formula in Volume V, Chapter 14.
- Cross-checked the general-method placement rule against the remaining GEVP
  and TCSA references found by targeted search.

## Manuscript Changes

- Expanded the mechanism following the boundary entropy gradient formula.
- Made explicit the boundary deformation convention
  \(S_\partial(\lambda)=S_\partial(0)+\lambda^a\int\phi_a\).
- Displayed the coupling derivative of \(\log z\), the integrated trace
  insertion, and the finite Ward susceptibility with kernel
  \(K_L(\tau)=1-\cos(2\pi\tau/L)\).
- Stated exactly where contact-term control, quotienting by redundant
  derivatives, and reflection positivity enter.  The text no longer lets the
  quoted theorem hide those analytic inputs behind a one-paragraph summary.

## General-Method Audit Result

- The remaining GEVP references in QCD spectroscopy and pure Yang--Mills are
  cross-references to the general finite-volume method in Volume XI and are
  tied to concrete source/channel data.
- The integrability bridge does not expose TCSA machinery locally; it points to
  the numerical-method chapter and states that no model-specific truncation
  calculation is being performed there.
- No new specialized chapter was found teaching a general numerical method
  without a concrete model-specific result.

## Issue Links

- Improves #697 by expanding a CFT quoted-theorem proof boundary.
- Supports closure of #699: the current targeted search found no remaining
  GEVP/TCSA-style method-placement violation in the audited files.

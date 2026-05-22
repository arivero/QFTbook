# 2026-05-22 QCD Beta-Function Determinant Coefficients

## Scope

The QCD one-loop beta-function chapter already followed the local source
logic: background-field gauge, a background 1PI effective action, a
constant-background extraction of the logarithmic curvature term, and the
source coefficient
\[
  b=\frac{11}{12}C_A-\frac{N_f}{3}T_R .
\]
The remaining weakness was that the ghost and vector determinant coefficients
were recorded as final logarithmic coefficients.  This pass makes that step
self-contained.

## Manuscript Changes

- Updated
  `monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`.
- Added the flat-space heat-kernel logarithmic coefficient for a Laplace-type
  operator \(\mathcal L=-\nabla^2+E\).
- Defined the bundle curvature \(\Omega_{\mu\nu}=[\nabla_\mu,\nabla_\nu]\)
  and derived the pole normalization from the proper-time representation.
- Stated the adjoint trace sign
  \[
    \operatorname{tr}_{\rm ad}(\operatorname{ad}\widetilde F_{\mu\nu}
    \operatorname{ad}\widetilde F^{\mu\nu})
    =
    -C_A\widetilde F^a_{\mu\nu}\widetilde F^{a\mu\nu}.
  \]
- Derived the Dirac contribution by applying the heat-kernel coefficient to
  \(-\mathcal D_\psi^2\), including the factor \(1/2\) relating the
  first-order determinant to the squared operator.
- Derived the scalar adjoint ghost coefficient \(+C_AI_\epsilon/12\).
- Derived the background-Feynman-gauge vector one-form coefficient
  \(-5C_AI_\epsilon/3\), including the \(E_A^2\) and connection-curvature
  pieces separately.
- Preserved the source arithmetic
  \[
    -\frac12\left(-\frac53\right)+\frac1{12}=\frac{11}{12}.
  \]

## Planning Updates

- Updated the QCD chapter dossier to record that determinant coefficients are
  now derived through the heat-kernel coefficient rather than asserted.
- Retained the source warning that the Ben Lou comparison transcription has
  the ghost determinant summary coefficient wrong relative to the handwritten
  source.

## Verification

- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean.
- Rendered edited pages from `monograph/tex/main.pdf`:
  `/tmp/qft_qcd_heatkernel_final-398.png`,
  `/tmp/qft_qcd_heatkernel_final-399.png`,
  `/tmp/qft_qcd_heatkernel_final-400.png`.
  The dense equations and paragraph flow were visually inspected.

## Remaining Boundary

This pass does not develop the two-loop beta function or the full
background-field renormalization of all gauge-fixing parameters.  Its purpose
is the one-loop coefficient required by the source order and by the QCD
asymptotic-freedom discussion.

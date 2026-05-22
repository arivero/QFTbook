# 2026-05-22 253b Stress Trace And Conformal Currents Source Audit

## Scope

- Source block: `references/253b lecture notes 2023.pdf`, pages 119--123.
- Local transcription comparison:
  `transcription/tex/253b/scattering_rg_qcd.tex`, around the stress tensor
  trace and conformal-current block.
- Additional comparison:
  `references/253b transcribed lecture notes.tex`, around the same source
  block.
- Manuscript home:
  `monograph/tex/volumes/volume_ii/chapter13_stress_tensor_trace_scale_invariance_and_conformal_currents.tex`.

## Source Content Checked

- Translation covariance of a scalar field,
  \(\phi'(x')=\phi(x)\) for \(x'^\mu=x^\mu+\delta a^\mu\), and the active
  variation \(\delta\phi=-\delta a^\mu\partial_\mu\phi\).
- The Noether localization
  \(\delta a^\mu\mapsto\delta a^\mu(x)\) with the possible
  \(\partial_\mu\delta a_\nu\,\mathcal D^{\mu\nu}\phi\) term, and the
  Euclidean convention
  \(\delta S=-\int\dd^Dx\,\partial_\mu\delta a_\nu T^{\mu\nu}\).
- Dilatations as the special local parameter
  \(\delta a^\mu(x)=\sigma x^\mu\), giving
  \(\delta S=-\sigma\int\dd^Dx\,T^\mu{}_\mu\).
- The scalar-field scaling convention
  \(\mathcal D^\mu{}_\mu\phi=-(D-2)\phi/2\), the equivalent finite
  transformation
  \(\phi'(x')=(1+\sigma)^{-(D-2)/2}\phi(x)\), and the direct check that
  \(S_{\rm kin}=\frac12\int(\partial\phi)^2\) is invariant up to a total
  derivative.
- Operator engineering dimensions
  \(d_I(\epsilon)=d-\epsilon+\delta_I(\epsilon)\) and the scale
  transformation \(O_I'(x')=(1+\sigma)^{-d_I(\epsilon)}O_I(x)\).
- The regulated action
  \(S=S_{\rm kin}+\int\dd^{d-\epsilon}x\,g_I^\epsilon O_I\) and the bare
  trace identity
  \(T^\mu{}_\mu=\delta_I(\epsilon)g_I^\epsilon O_I\), modulo total
  derivatives and equation-of-motion terms.
- The MS relation for \(g_I^\epsilon\), bare \(\mu\)-independence, and the
  equation
  \[
    \delta_I(\epsilon)g_I^\epsilon
    =
    \sum_J(\beta_J+\epsilon\delta_J^{(1)}\lambda_J)
    \frac{\partial g_I^\epsilon}{\partial\lambda_J}.
  \]
- The finite separated-point trace identity
  \(T^\mu{}_\mu=\sum_J\beta_J[O_J]_\mu\).
- Fixed points, conformal Killing vectors, the current
  \(j^\mu_\xi=T^{\mu\nu}\xi_\nu\), and the conservation derivation from
  symmetry, conservation, and tracelessness of the stress tensor.
- The CKV examples: translations, rotations, dilatations, and special
  conformal transformations.
- The virial-current possibility
  \(T^\mu{}_\mu=\partial_\mu V^\mu\), the conserved dilatation current
  \(D^\mu=x_\nu T^{\mu\nu}-V^\mu\), and the distinction from special
  conformal currents unless improvement data remove the trace.

## Manuscript Changes

- Added the explicit scalar kinetic-term scaling calculation, including the
  chosen \(\mathcal D^\mu{}_\mu\) convention and the integration-by-parts
  cancellation.
- Confirmed that the trace identity is stated as a finite flat-space
  separated-insertion identity with contact terms and improvement data kept
  separate.
- Confirmed that the conformal-current discussion is conditional on a
  conserved symmetric traceless stress tensor, and that the virial-current
  caveat is retained instead of converting fixed points into conformal
  symmetry by assertion.
- Updated the chapter dossier and the no-skip coverage register to mark this
  source block as certified.

## Rendered Check

- Handwritten source pages rendered from
  `references/253b lecture notes 2023.pdf`:
  `/tmp/253b_119_123-119.png` through `/tmp/253b_119_123-123.png`.
- Compiled manuscript pages rendered from `monograph/tex/main.pdf`:
  `/tmp/qft_trace_final-266.png` through `/tmp/qft_trace_final-272.png`.
- Visual checks covered the local-translation figure, scale/engineering trace
  figure, MS trace identity figure, CKV-current figure, and
  virial/improvement figure.  No cropped equations, overlapping labels, or
  missing figure elements were found in the audited pages.

## Verification

- `tools/build_monograph.sh` completed cleanly after the TeX edits.
- The strict monograph text audit inside the build completed cleanly.
- `tools/audit_monograph_text.sh` completed cleanly.
- `git diff --check` completed cleanly.

This promotes handwritten 253b pages 119--123 to certified coverage after the
stress-tensor trace and conformal-current source audit.

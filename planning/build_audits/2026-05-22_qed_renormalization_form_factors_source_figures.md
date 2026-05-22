# 2026-05-22 QED Renormalization and Form-Factor Source/Figure Audit

Scope: `monograph/tex/volumes/volume_i/chapter20_qed_renormalization_and_electromagnetic_form_factors.tex`.

## Source Block

- Handwritten source rendered from `references/253a lectures 2022.pdf`, trace
  pp. 224--244.
- Secondary comparison used `references/253a_notes.tex`, but the handwritten
  pages were treated as authoritative where the transcription was ambiguous.
- This block begins with bare and renormalized QED variables and ends with the
  one-loop anomalous magnetic moment \(g_{\mathrm{mag}}=2+\alpha/\pi+O(\alpha^2)\).

## Corrections and Expansions

- Clarified the charge convention from the handwritten page: \(e=e^B Z_A^{1/2}\).
  The factor \(Z_\psi\) is attached to the spinor covariant derivative and
  organizes the Ward relation \(Z_1=Z_\psi\); it is not part of the
  representative gauge charge.
- Corrected the current used in the form-factor calculation to
  \(j^\mu=-iZ_A^{-1}eZ_\psi\bar\psi\gamma^\mu\psi\), derived from the
  renormalized Maxwell equation.
- Expanded the transversality argument: current-current conservation at
  separated points gives a transverse noncontact kernel, and differentiating
  the photon Dyson series relates this to \(k_\mu\Pi^{\mu\nu}=0\) up to local
  contact terms.
- Added the dimensional-regularization details for the vacuum-polarization
  calculation: Feynman parameter, shifted mass \(M_x^2\), angular averaging
  \(p_\mu p_\nu\mapsto D^{-1}\eta_{\mu\nu}p^2\), the averaged numerator, and
  the two scalar integrals analytically continued in \(D\).
- Made the pole part of \(Z_A\) explicit:
  \(Z_A=1-e^2(6\pi^2\epsilon)^{-1}+\text{finite}\).
- Tightened the form-factor decomposition by spelling out the parity
  restriction, the role of the Gordon identity, and the distributional meaning
  of charge normalization for plane-wave states.
- Expanded the magnetic-moment extraction, including the antisymmetric
  integration-by-parts step that converts the background vector potential into
  the magnetic field strength.
- Added the source-page bookkeeping for the current vertex: bare-field LSZ
  \(Z_\psi^{1/2}\) factors versus renormalized-field counterterms, and the
  tree-plus-vacuum-polarization chain contributing only to \(F(k^2)\).

## Figure and Render Check

- Source diagrams checked: photon Dyson series, photon counterterm, fermion
  vacuum-polarization loop, current insertion, and one-loop vertex correction.
- Rendered manuscript pages:
  `monograph/tex/build/visual_audit_qed_renorm_20260522/qedren-321.png` through
  `qedren-328.png`.
- Visual result: equations and diagrams fit without overlaps; the vertex
  correction labels are legible; the dense vacuum-polarization derivation page
  remains readable.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`

All were clean on 2026-05-22.

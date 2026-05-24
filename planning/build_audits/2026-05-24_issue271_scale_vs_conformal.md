# Issue #271 Audit: Scale Versus Conformal Status

## Scope

- GitHub source of truth: issue #271 was verified open before this pass.
- Manuscript target: `monograph/tex/volumes/volume_iii/chapter01_fixed_points_and_conformal_data.tex`.
- Dossier target: `planning/chapter_dossiers/volume_iii/chapter01_fixed_points_conformal_data.md`.

## Manuscript Change

- Added `Remark~\ref{rem:cft-opening-scale-versus-conformal}` immediately
  after the fixed-point trace equation, where the virial current first appears
  in the CFT volume.
- Defined the conserved dilatation current
  \(D^\mu=x_\nu\widehat T^{\mu\nu}-V^\mu\) and tied scale invariance to
  \(\widehat T^\mu{}_\mu=\partial_\mu V^\mu\).
- Stated the conformal criterion as the vanishing of the virial obstruction
  class in the improvement/contact-term quotient, including the scalar
  improvement formula and the removable-virial condition.
- Recorded the dimension-dependent status: two-dimensional theorem
  formulations require explicit analytic hypotheses; four-dimensional
  anomaly/dilaton arguments are conditional and are not used as an
  unconditional theorem; in other dimensions conformal Ward identities or a
  traceless improved stress tensor remain part of the stated CFT data.
- Cross-referenced the fuller stress-tensor discussion in
  `Remark~\ref{rem:scale-conformal-dimension-status}`.

## Verification

- Passed: `git diff --check`.
- Passed: `tools/audit_monograph_text.sh`.
- Passed: `tools/audit_chapter_dossiers.sh`.
- Passed: `tools/build_monograph.sh`.

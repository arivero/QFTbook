# 2026-05-24 Issue #366 Trace-Identity Pole Cancellation

GitHub issue #366 flagged that the MS trace-identity bridge suppressed the
finite-part operation behind
\(\epsilon\delta_J^{(1)}\lambda_J\mathcal O^{\rm MS}_{J,\epsilon}\).

Changes made:

- Rewrote the proof of the flat-space renormalized trace identity to introduce a
  separated test density and the Laurent expansion of
  \(\mathcal O^{\rm MS}_{J,\epsilon}\).
- Displayed explicitly that pole residues \(C_{J,r}\) are supported on collision
  diagonals, so the \(\epsilon\delta_J^{(1)}\lambda_J\) term vanishes after
  restriction to separated insertions.
- Added the contact-distribution caveat: on unrestricted test densities,
  multiplication by \(\epsilon\) sends the simple pole residue to a finite local
  distribution and shifts higher pole residues.
- Connected the cancellation of negative powers to the MS pole equations
  following from \(\dd g_I^\epsilon/\dd\log\mu=0\).
- Updated the stress-tensor chapter dossier.

Verification targets:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

# 2026-05-25 Issue 552: Chern-Simons Boundary WZW Derivation

## Scope

Issue #552 flagged that Volume VIII Chapter 4 asserted the
Chern-Simons/Wess-Zumino-Witten boundary relationship without displaying the
boundary variational calculation or Polyakov-Wiegmann identity.

## Edits

- Replaced the brief boundary paragraph by a holomorphic-polarization
  calculation on \(\partial M=\Sigma\).
- Displayed the on-shell boundary variation of the Chern-Simons action and
  the boundary polarization term, giving
  \(k(2\pi)^{-1}\int_\Sigma {\rm tr}(A_z\delta A_{\bar z})\).
- Defined the level-\(k\) WZW functional with its Wess-Zumino extension term.
- Added a lemma proving the Polyakov-Wiegmann identity from the
  product Maurer-Cartan form and Stokes' theorem.
- Added the gauged chiral WZW boundary action and showed that its
  \(A_{\bar z}\)-variation cancels the polarized Chern-Simons boundary
  variation for a flat boundary connection \(A_z=-\partial_zg\,g^{-1}\).
- Displayed the resulting level-\(k\) affine current algebra/OPE.

## Targeted Verification

No calculation script was edited for this text-only derivation pass.

## Repository Verification

- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

The monograph build and log scan completed cleanly.  The rebuilt PDF has
1282 pages.

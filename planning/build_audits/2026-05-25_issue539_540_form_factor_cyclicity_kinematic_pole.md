# Build Audit: Issues 539 and 540 Form-Factor Cyclicity and Kinematic Pole

Date: 2026-05-25

## Scope

Development pass on
`monograph/tex/volumes/volume_vi/chapter04_form_factor_bootstrap_local_operators.tex`,
addressing the cyclicity and kinematic annihilation-pole derivation gaps.

## Mathematical Changes

- Replaced the one-sentence cyclicity motivation by a proposition with
  explicit hypotheses: Wightman boundary values, spectrum-condition
  forward-tube analyticity, locality, one-particle crossing through the
  physical rapidity strip, and absence of singularities on the
  \(2\pi i\)-continuation path.
- Derived cyclicity by crossing the first incoming particle to an outgoing
  antiparticle using \(p(\theta+i\pi)=-p(\theta)\), applying locality at the
  boundary of the tube, and crossing back to the incoming ordered state.
- Promoted the kinematic-pole formula to a labeled equation and a proposition
  stating the exact singular part of the form factor near
  \(\theta'=\theta+i\pi\).
- Displayed the direct Cauchy kernel \(i/z\), the scattered contribution
  after moving the particle through all spectators by Watson exchange, and
  the reversed local coordinate \(z_{\rm rev}=-z\) that gives the relative
  minus sign.
- Updated the Volume VI Chapter 4 dossier.

## Verification

- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed; `monograph/tex/main.pdf` was rebuilt
  without log-scan failures.
- `pdfinfo monograph/tex/main.pdf` reports 1272 pages.

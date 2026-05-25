# 2026-05-25 Issue #571 P(phi)2 Stability Pass

GitHub issue: #571, concerning the proof of
`thm:p-phi-two-finite-volume-uv-limit` in
`monograph/tex/volumes/volume_xi/chapter02_constructive_scalar_models_os_data.tex`.

## Manuscript Changes

- Added the `quotedtheorem` environment to `monograph/tex/preamble.tex` so
  imported mathematical theorems can be marked explicitly rather than hidden
  inside ordinary proof prose.
- Tightened `planning/12_strict_writing_harness.md`: imported theorems must
  use `quotedtheorem`, state hypotheses and conclusion, state their local
  role, and must not carry a `proof` environment unless the proof is actually
  reproduced.
- Added Definition `def:p-phi-two-negative-sobolev-norm` for the finite-volume
  negative Sobolev control norm used in the \(P(\phi)_2\) stability estimate.
- Added Quoted Theorem `qthm:p-phi-two-stability`, a precise
  Nelson--Glimm--Jaffe--Spencer/Guerra--Rosen--Simon stability statement:
  \[
    V_{\varepsilon,\Lambda}(\phi)
    \ge
    -A_\Lambda
    -B_\Lambda\|\phi\|_{H^{-s}(\Lambda_1)}^\alpha,
    \qquad 0<\alpha<2,
  \]
  with constants independent of the ultraviolet mollifier and with uniform
  exponential integrability of the finite-volume density.
- Rewrote the proof of the finite-volume ultraviolet theorem so that the
  analytic chain is displayed:
  Wick-power \(L^p\) convergence from logarithmic covariance integrability and
  hypercontractivity; the quoted stability theorem; Sobolev almost-sure
  membership from the elliptic covariance bound and Weyl's law; Fernique;
  Young's inequality for the subquadratic exponent; uniform integrability;
  and Holder control of polynomial insertions.

## Status

The pass does not pretend to reproduce the full multi-scale
Glimm--Jaffe--Spencer stability proof.  It makes that theorem an explicit
external theorem boundary and closes the hidden-proof gap in the local
finite-volume UV theorem.  The deeper cluster-expansion gaps remain assigned
to #555 and #572.

## Verification

- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean; the monograph built to
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf`: 1252 pages.

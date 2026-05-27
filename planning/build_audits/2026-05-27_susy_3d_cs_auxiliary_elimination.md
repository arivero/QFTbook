# Build Audit: SUSY Three-Dimensional Chern-Simons Auxiliary Elimination

Date: 2026-05-27

Branch: `codex/susy-gauge-dynamics-localization`

## Scope

This pass incorporates and deepens the stringbook component-action material on
`3D` supersymmetric Chern-Simons-matter theories inside the QFT monograph,
without using any string-theoretic argument as a foundation.

## Substantive Edits

- Added a Volume VII Chapter 10 proposition for non-abelian `3D`
  `N=2` pure Chern-Simons-matter auxiliary elimination, with explicit
  hypotheses on the compact gauge group, unitary representation, trace
  convention, absence of Yang-Mills regulator terms, absence of real masses,
  FI terms, and superpotential terms.
- Derived the `D`-constraint
  `sigma^a=-(2 pi/k) mu^a` and the ordered sextic scalar interaction
  `-4 pi^2/k^2 (bar phi t^a phi)(bar phi t^b phi)(bar phi t^a t^b phi)`.
- Added a convention boundary for induced Yukawa signs in `3D`, while fixing
  the convention-independent coefficient magnitudes and the relative `1:2`
  factor.
- Added a Volume VII Chapter 10 proposition for `N=3` adjoint-chiral
  elimination:
  `W=-(k/8 pi) varphi^2+J varphi` implies
  `W_eff=(2 pi/k)J^2`.
- Extended `calculation-checks/susy_abjm_6d_checks.py`, its README entry, and
  the Chapter 10 dossier with the new checks and proof ledger.

## Verification

- `python3 calculation-checks/susy_abjm_6d_checks.py`: passed.
- `python3 -m py_compile calculation-checks/susy_abjm_6d_checks.py`: passed.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean before this audit note; rerun after adding the
  note before finishing.
- `tools/build_monograph.sh`: passed and produced
  `monograph/tex/main.pdf` with 1975 pages and file size 7908371 bytes.

# 2026-05-27 QCD HQET Wilson-Line Limit

## Scope

- Added a heavy-quark effective theory section to Volume II, Chapter 19 after
  the static-source/QCD-string material and before the discussion of physical
  QCD external states.
- Fixed the mostly-plus velocity convention \(v^2=-1\), the transverse
  projector \(D_\perp^\mu=(\delta^\mu{}_\nu+v^\mu v_\nu)D^\nu\), and the
  projected heavy field \(h_v\) with \(P_v^\pm=(1\pm i\gamma_v)/2\).
- Defined the finite-regulator HQET datum as a gauge-covariant Wilsonian
  comparison of renormalized QCD matrix elements with a local \(1/m_Q\)
  expansion.
- Proved the static propagator/Wilson-transporter identity for the leading
  HQET operator, stated and proved the static spin/flavor symmetry, and derived
  the free residual-dispersion expansion that supplies the kinetic correction.
- Added an explicit controlled-approximation statement for what a truncated
  heavy-mass expansion asserts for smeared gauge-invariant matrix elements.
- Added a public calculation check for the projector, transverse projector,
  residual-momentum, dispersion, and Wilson-line differential-equation
  algebra.

## Checks

- `python3 calculation-checks/qcd_hqet_checks.py`
- `python3 -m py_compile calculation-checks/qcd_hqet_checks.py`
- `git diff --check -- ...` on the changed manuscript, calculation-check,
  README, and dossier files.
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`: 2160 pages, 8754040 bytes, PDF 1.5.

## Status

This pass supplies the first rigorous HQET foundation in the QCD chapter.  It
does not yet develop the full anomalous-dimension, current-matching,
heavy-hadron spectroscopy, or NRQCD/pNRQCD treatments; those should be later
QCD/heavy-flavor development passes built on this operator datum.

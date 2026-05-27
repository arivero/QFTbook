# 2026-05-27 Issue #628 QCD Phase Holonomy-Potential Pass

## Scope

- Continued the #628 QCD phase-structure depth pass in Volume X,
  Chapter 12.
- Added a controlled high-temperature Polyakov-holonomy section after the
  center-order-parameter discussion.
- Defined the constant commuting holonomy
  \(P=\operatorname{diag}(e^{i\theta_1},\ldots,e^{i\theta_{N_c}})\) with
  determinant-one constraint and center action.
- Derived the one-loop gluonic holonomy potential from thermal oscillator
  sums and the background-gauge cancellation to two physical adjoint
  polarizations.
- Derived the antiperiodic massless Dirac-quark contribution at
  \(\mu_q=0\).
- Proved that the pure-glue one-loop potential is minimized exactly at center
  holonomies \(P=z\mathbf1\), and recovered the free-gluon free-energy
  density.
- Computed the uniform center-symmetric holonomy free energy and its cost
  above the perturbative center-broken minimum.
- Recorded the fundamental-quark holonomy term as an explicit center source
  and checked that \(P=\mathbf1\) reproduces the negative free-quark pressure.
- Extended `calculation-checks/qcd_phase_checks.py` with exact rational
  checks for the Weiss-potential coefficients, the center-symmetric cost, the
  free-quark holonomy coefficient, and center-charge bookkeeping.

## Checks

- `python3 calculation-checks/qcd_phase_checks.py` passed.
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py` passed.
- `git diff --check -- monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex calculation-checks/qcd_phase_checks.py calculation-checks/README.md planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md planning/build_audits/2026-05-27_issue628_qcd_phase_holonomy_potential.md` passed.
- `tools/build_monograph.sh` passed with strict text audit and final log scan
  clean.
- `pdfinfo monograph/tex/main.pdf` reports 2186 pages.

## Status

This supplies a concrete controlled thermal gauge-theory example inside the
QCD phase chapter.  It does not close #628: remaining work includes
interacting Polyakov-loop effective theories, lattice-continuum status
ledgers, quantitative QGP observables, high-density EFT, and controlled
examples of dense phases.

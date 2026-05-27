# 2026-05-27 Issue 494: Heat-Bath And Overrelaxation Layer

## Scope

This pass continues issue #494 by adding the finite-regulator heat-bath and
overrelaxation layer to Volume XI, Chapter 6.  The goal is to state the
invariant-measure claims as exact conditional-probability theorems rather
than as algorithmic lore.

Touched files:

- `monograph/tex/volumes/volume_xi/chapter06_monte_carlo_and_sign_problems.tex`
- `calculation-checks/heatbath_overrelaxation_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_xi/chapter06_monte_carlo_and_sign_problems.md`
- `planning/build_audits/2026-05-27_issue494_heatbath_overrelaxation_layer.md`

## Mathematical Content Added

- Added a general finite-regulator heat-bath theorem using a regular
  conditional probability
  \(d\nu(x,y)=d\nu(x\mid y)d\nu_Y(y)\).
- Proved exact heat-bath detailed balance by writing the pair measure
  \(d\nu_Y(y)d\nu(x\mid y)d\nu(x'\mid y)\delta_y(dy')\), which is symmetric
  in \(x,x'\).
- Derived the single-link \(SU(2)\) Wilson conditional density using the
  staple form
  \(Q(U)=\frac12\operatorname{Re}\operatorname{tr}(U_eV_e)+Q_{\widehat e}\)
  and the quaternionic polar decomposition \(V_e=c_eW_e\).
- Reduced the exact \(SU(2)\) heat-bath density to the scalar quaternion
  density
  \(\sqrt{1-x_0^2}e^{\beta c_ex_0}\,dx_0\), with uniform angular direction
  on \(S^2\).
- Defined the microcanonical overrelaxation map
  \(\mathcal O_{W_e}(U_e)=W_e^{-1}U_e^{-1}W_e^{-1}\).
- Proved overrelaxation is an involution, preserves the local Wilson score,
  and preserves Haar measure by being a composition of inversion and fixed
  left/right multiplication.
- Stated precisely that overrelaxation alone is not an ergodic sampler; it is
  an invariant-measure-preserving deterministic move used together with
  stochastic updates.

## Calculation Check

Added `calculation-checks/heatbath_overrelaxation_checks.py`, which verifies:

- finite conditional heat-bath detailed balance with exact rational weights;
- \(SU(2)\) staple reduction \(V=cW\);
- overrelaxation involution;
- local score preservation;
- orthogonality and absolute Jacobian one for the \(S^3\) overrelaxation map.

## Verification

- `python3 calculation-checks/heatbath_overrelaxation_checks.py`: passed;
  printed `All finite heat-bath and overrelaxation checks passed.`
- `python3 -m py_compile calculation-checks/heatbath_overrelaxation_checks.py`:
  passed.
- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed; rebuilt
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2090`.

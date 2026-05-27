# 2026-05-27 Volume XI Lattice Perturbation/Tadpole Pass

## Scope

This pass continues issue #631 by adding perturbative lattice-coordinate and
tadpole-normalization material to Volume XI, Chapter 5.

## Substantive Additions

- Added the perturbative link coordinate
  \(U_\mu(x)=\exp\{-\ii g_0aA_\mu(x+a\widehat\mu/2)\}\) in the
  trace-delta generator convention.
- Stated the Wilson-action coupling convention \(\beta=N/g_0^2\) matching
  \(\frac{1}{4g_0^2}\int\operatorname{tr}F_{\mu\nu}F_{\mu\nu}\) at tree
  level.
- Derived the linearized lattice curvature and the quadratic Wilson action.
- Derived the gauge-fixed tree-level lattice kernel and its inverse
  propagator in terms of \(\widehat p_\mu=2a^{-1}\sin(ap_\mu/2)\).
- Recorded the small-\(a\) lattice momentum artifact
  \(\widehat p^2=p^2-\frac{a^2}{12}\sum_\mu p_\mu^4+O(a^4p^6)\).
- Defined plaquette mean-link/tadpole normalization and the boosted coupling
  coordinate \(g_{\rm TI}^2=g_0^2/u_0^4\) as finite perturbative
  bookkeeping.
- Added `calculation-checks/lattice_perturbation_tadpole_checks.py` to verify
  the finite algebra.

## Verification

- Passed: `python3 calculation-checks/lattice_perturbation_tadpole_checks.py`
- Passed: `python3 -m py_compile calculation-checks/lattice_perturbation_tadpole_checks.py`
- Passed: primitive-fraction scan on touched files.
- Passed: `git diff --check` on touched files.
- Passed: `tools/build_monograph.sh`
- Built PDF: `/Users/xiyin/QFT/monograph/tex/main.pdf`, 2236 pages.

## Remaining Work

- Chapter 5 still needs a fuller lattice perturbation-theory vertex
  derivation, explicit one-loop examples tied to gauge-invariant observables,
  and cluster-runnable Wilson-flow/static-potential code connected to the
  definitions in the text.

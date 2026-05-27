# 2026-05-27 Volume XI Symanzik Scaling-Window Pass

## Scope

This pass deepens Volume XI, Chapter 4 by adding an explicit Symanzik
cutoff-effect layer to the continuum-limit discussion.  The aim is to turn
the statement that hypercubic artifacts must be controlled into a concrete
distributional expansion with an improvement calculation.

## Substantive Additions

- Added a Symanzik expansion datum: a scaling trajectory, renormalized
  operator coordinates, continuum local distributions, and a stated
  distributional remainder.
- Derived the nearest-neighbor free scalar tree-level cutoff expansion for
  smeared two-point functions,
  \[
    \frac1{p^2+m^2}
    +a^2
    \frac{\sum_\mu p_\mu^4/12-\delta m_2}{(p^2+m^2)^2}
    +O(a^4),
  \]
  including the hypercubic but non-\(O(D)\)-invariant artifact
  \(\sum_\mu p_\mu^4\).
- Added a tree-level improved scalar kernel
  \(K_a^{\rm imp}=m_a^2+\hat p_a^2+a^2\sum_\mu\hat p_{\mu,a}^4/12\) and
  proved cancellation of the \(O(a^2)\) two-point artifact when the mass
  coordinate is tuned.
- Added a status remark emphasizing that interacting Symanzik expansions
  require actual distributional bounds, operator-mixing control, and
  irrelevant-operator estimates; the local-operator list is not a proof.
- Extended the continuum-scaling companion checks with the tree-level
  propagator artifact and improved-kernel cancellation.

## Verification

- Passed: `python3 calculation-checks/continuum_scaling_window_checks.py`
- Passed: `python3 -m py_compile calculation-checks/continuum_scaling_window_checks.py`
- Passed: primitive-fraction scan on touched files.
- Passed: `git diff --check` on touched files.
- Passed: `tools/build_monograph.sh`
- Built PDF: `/Users/xiyin/QFT/monograph/tex/main.pdf`, 2225 pages.

## Remaining Work

- The chapter still needs a comparable interacting example with actual
  estimates, ideally tied to the rigorous RG chapter, and the lattice gauge
  chapters should eventually include a gauge-field Symanzik improvement
  derivation with reflection-positivity status labels.

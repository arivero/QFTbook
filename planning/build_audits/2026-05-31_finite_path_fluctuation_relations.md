# 2026-05-31 Finite Path-Measure Fluctuation Relations Pass

## Scope

- Continued the statmech-to-QFT absorption track in GitHub issue #703.
- Target chapter:
  `monograph/tex/volumes/volume_x/chapter10_nonequilibrium_steady_states_open_systems.tex`.

## Substance

- Added a finite continuous-time jump-process path space before discussing
  continuum nonequilibrium QFT or Schwinger--Keldysh influence functionals.
- Defined labelled trajectories, forward path densities, reversed protocols,
  time-reversed trajectories, and the absolute-continuity hypothesis needed
  for the Radon--Nikodym logarithm.
- Proved the finite path-measure fluctuation identity
  \[
    \left\langle e^{-\Sigma}\right\rangle_F=1
  \]
  by explicit cancellation of waiting-time factors and normalization of the
  reversed path measure.
- Identified the mean entropy production as a relative entropy of history
  measures.
- Derived the Jarzynski identity as the single-thermal-reservoir,
  Gibbs-endpoint specialization with protocol work
  \(W_{\rm ext}=\int_0^T \partial_t E_{i(t)}(t)\,dt\).
- Stated the continuum-QFT theorem boundary: regulator, work measurement or
  replacement protocol, time reversal, and convergence of history measures
  must all be specified.

## Calculation Check

- Expanded `calculation-checks/nonequilibrium_open_system_checks.py` with:
  - a continuous-time finite jump-path ratio check verifying cancellation of
    waiting-time factors;
  - an exactly enumerated driven two-state Jarzynski check.

## Status Boundary

This pass proves finite-regulator path-measure identities.  It does not
construct continuum interacting-QFT nonequilibrium history measures; that
remains the open problem stated at the end of the chapter.

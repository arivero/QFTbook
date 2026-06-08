# Issue #844 small-x observable-interface status pass

Date: 2026-06-08.

Scope:

- Targeted Volume II Chapter 19, the small-\(x\) measured-observable hotspot
  cited in the #844 semantic `controlledapproximation` review.
- Re-audited the block formerly titled `Measured small-\(x\) observable map`.

Before:

- The block was a `controlledapproximation` even though its main content was an
  interface list: exact measured functional, impact-factor map, rapidity
  factorization, projective Wilson-line limit, evolution/closure residuals, and
  finite-\(Q\)/endpoint/power remainders.
- The list was useful, but it did not itself supply impact-factor, rapidity,
  evolution, and power estimates for a measured QCD channel.

After:

- The interface is now `rem:qcd-small-x-measured-observable-interface`.
- It explicitly says that named residuals are proof obligations until a process
  estimate, regulator comparison, or imported theorem supplies a norm and range.
- The adjacent `ca:qcd-small-x-leading-dis-dipole-channel` remains the
  controlled approximation: it supplies the virtual-photon kernel, rapidity
  split, BK-error propagation through the measured kernel, endpoint primitives,
  and small-\(r\) color-transparency boundary.

Material retained:

- The exact measured functional \(\mathfrak T_{Q,Y}[\varphi]\).
- The Wilson-line coordinate \(\mathcal S^{\rm sx}_{Q,Y}[\varphi]\).
- The six residual classes for impact factor, rapidity, projective regulator,
  evolution, closure, and power terms.
- The leading inclusive-DIS dipole formula and its finite companion checks.

Material removed or demoted:

- No physics formula was removed.
- The interface lost `controlledapproximation` status because named residual
  slots are not component estimates.

Independent evidence retained:

- `qcd_bfkl_small_x_checks.py` still verifies trace-delta color normalization,
  transverse inversion covariance, BFKL characteristic constants, finite
  Wilson-line diffusion, BK-closure arithmetic, projective weak-limit budgets,
  and the leading DIS photon-kernel bin.
- The companion now also rejects promotion of the interface while
  impact-factor, rapidity, evolution, and power residuals remain named slots.

Unresolved theorem boundary:

- This pass does not prove continuum JIMWLK, small-\(x\) factorization in QCD,
  nonperturbative impact-factor matching, rapidity-scheme matching beyond the
  finite model, or physical endpoint/power estimates.
- Those remain process-specific QCD estimates or imported theorem obligations
  before a measured small-\(x\) prediction can be considered controlled beyond
  the leading inclusive-DIS dipole window.

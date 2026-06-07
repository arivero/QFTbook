Issue #851 CP^{N-1} stable-map representative-independence audit
================================================================

Scope
-----

- Target: Volume VII Chapter 09, degree-one `CP^{N-1}` stable-map/contact block.
- Companion: `calculation-checks/susy_2d_lg_glsm_checks.py`.
- Issue: #851, repairing the prior Boolean compactification/contact formula.

Quality audit
-------------

- The previous block was too strong and wrong for a primary Gromov-Witten
  invariant: it let coincident point representatives or a hyperplane through a
  point add indicator-valued boundary contributions and change the invariant
  from `1` to `2`.
- The replacement states the primary invariant as an evaluation-class pairing
  on the compactified stable-map space.  Non-transverse representatives now
  mean the chosen affine chart is invalid; the invariant is recovered by
  deformation to transverse cycles or refined/excess intersection.
- Contact constants are no longer attached to the primary invariant.  They are
  allowed only for separately declared collision-sensitive source observables,
  point-splitting prescriptions, or composite-source renormalizations.
- The companion now checks the intersection-ring invariant and treats the old
  Boolean indicator arithmetic as a failing negative control.

Scope boundary
--------------

- This does not prove the continuum GLSM vortex regulator limit, the full
  nonzero-mode determinant, or the original-to-mirror operator map.
- It corrects the direct A-model stable-map side so the monograph no longer
  confuses representative failure with a new primary topological contribution.

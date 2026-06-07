Issue #597 same-coordinate positive-rate residual audit
=======================================================

Scope
-----

- Target: Volume II Chapter 20D, `rem:instanton-same-coordinate-amplitude-rate-obligation`.
- Companion: `calculation-checks/instanton_physical_amplitude_architecture_checks.py`.
- Purpose: close a physics-depth gap in the instanton amplitude-to-rate handoff.

Quality audit
-------------

- The change is not another moduli-space cell.  It strengthens the physical
  observable map after source differentiation, fluctuation response,
  amputation/crossing, and projection have already produced a physical vector.
- The positive rate now has an explicit residual propagation bound
  `n L (2 M_a epsilon_a + epsilon_a^2) + B_Q`, so theta-phase cancellation is
  not allowed to hide projection, fluctuation, measurement-basis, completeness,
  or binning errors.
- The companion uses a finite two-bin measurement matrix where the bound is
  exact, then verifies that omitting either the amplitude/projection residual
  or the measurement/completeness residual underbudgets the physical cut.
- The passage remains inside the monograph's physics argument.  Planning
  language and issue/directive bookkeeping stay in this audit and dossier
  files, not in the `.tex` chapter.

# 2026-06-06 Issue #597/#725: GLSM Source-Frame Calibration

Scope:
- Volume VII Chapter 09, two-dimensional `(2,2)` GLSM/Hori--Vafa lane.
- Physics-facing instanton amplitude refinement, not a moduli-space expansion.
- Promotes `susy_2d_lg_glsm_checks.py` to an extended evidence contract.

Substance:
- Added `ca:glsm-one-vortex-source-frame-calibration`.
- A Hori--Vafa monomial supplies a common topological/fugacity factor, but a
  component amplitude also requires the direct source-frame integral
  `J_AB=sum_p K_p(Delta_AB+C'_AB)`.
- A reference component amplitude can calibrate a target component only through
  the directly computed ratio `J_AB/J_CD`; the mirror fugacity alone cannot
  supply zero-mode source minors or primed contact terms.
- The text records the reference-denominator noncancellation condition and a
  residual bound including target, reference, and source-frame transport errors.

Companion evidence:
- Added `check_one_vortex_source_frame_calibration()` to
  `calculation-checks/susy_2d_lg_glsm_checks.py`.
- Negative controls reject mirror-fugacity-only component amplitudes,
  contact-omitted source ratios, parallel-source zero-mode shortcuts, and
  zero-reference denominator calibration.
- The GLSM companion now has an extended evidence contract with explicit
  convention tags for charge/FI conventions, Hori--Vafa variables,
  determinant-line/zero-mode orientation, and the projective A-twisted
  observable coordinate.

Re-audit notes:
- The edit follows the physics-first instanton directive: it develops the
  fluctuation/source-amplitude side of the two-dimensional instanton story.
- No GitHub, monitoring, Claude, or directive language was added to monograph
  TeX; issue/process notes remain in planning and dossiers.
- Hori--Vafa remains a protected-data benchmark, not an authority substituted
  for the direct vortex calculation.

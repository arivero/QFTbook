# Cross Sections and Unitarity Normalization Pass

Date: 2026-05-22

Scope:
- Rewrote the chapter on cross sections, phase space, partial waves, and unitarity.
- Kept the logical placement after Haag-Ruelle scattering and LSZ, so scattering probabilities and cross sections are defined from the nonperturbative scattering operator before sharp-momentum formulae are used.
- Fixed the normalization chain from asymptotic Hilbert-space probabilities to invariant amplitudes, invariant phase space, invariant flux, two-body kinematics, optical theorem, and partial waves.
- Distinguished the distinguishable-particle and identical-boson partial-wave conventions used later in the high-energy-bounds chapter.
- Reworked the cross-section diagram so the incoming flux, effective area, and final channel are visually separated and directly tied to the equations.

Verification:
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- Rendered affected PDF pages 118--125 at 150 dpi and inspected the chapter-opening pages, cross-section figure, two-body phase-space derivation, optical theorem, and partial-wave normalization pages.

Follow-up:
- The next detailed scattering pass should connect this normalization chapter more tightly to the later dispersion-relation chapter, especially where high-energy bounds use identical-particle conventions.

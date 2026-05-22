# QED External States Source and Figure Audit

Date: 2026-05-22

## Scope

- Revised
  `monograph/tex/volumes/volume_i/chapter19_quantum_electrodynamics_and_external_states.tex`
  against the 253a QED source block.
- Kept the chapter on the source-order side of the conceptual boundary:
  gauge-fixed Green-function Feynman rules and LSZ residues are developed
  only after the nonperturbative scattering and LSZ chapters.
- Left bare/renormalized QED, photon self-energy, and form factors to
  Chapter 20.

## Source Visual Checks

- Handwritten QFT source images:
  `monograph/tex/build/source_visual_trace/253a_trace-216.png` through
  `monograph/tex/build/source_visual_trace/253a_trace-223.png`.
- Source content checked against `transcription/tex/253a/foundations.tex`,
  roughly lines 9114--9545.
- The immediately preceding handwritten trace pages `253a_trace-212.png`
  through `253a_trace-215.png` were assigned to Chapter 18, since they contain
  photon one-particle matrix elements, polarization completeness, and the
  comparison with the field-strength Wightman function.

## Content Added Or Tightened

- Rechecked the QED representative transformation law, covariant derivative,
  and gauge invariance of the Dirac-Maxwell Lagrangian.
- Expanded the charged-insertion discussion with an explicit Wilson-line
  proof for a singly charged insertion and for the bilocal neutral insertion
  \(\psi(x)\exp[-\ii g\int_y^x A]\bar\psi(y)\).
- Stated that Wilson-line operators may require short-distance
  renormalization, separately from the gauge-covariance calculation.
- Clarified that the path integral is a regulated Gaussian/Berezin expansion
  around the Maxwell and Dirac free functionals.
- Made the external LSZ factors index-explicit for outgoing/incoming
  electrons, positrons, and photons, and added the convention relating
  all-incoming Fourier variables to physical future-directed momenta.
- Added a compact external-factor diagram showing residues attached to
  amputated kernels.
- Rechecked the Compton two-channel diagram, reduced amplitude, and
  tree-level Ward cancellation under the polarization representative shift
  \(e_\mu^h\mapsto e_\mu^h+\alpha k_\mu\).
- Kept the infrared boundary explicit: fixed-photon-number hard amplitudes
  require an infrared regulator or inclusive/dressed completion in the
  long-range charged theory.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`

The build completed cleanly and produced `monograph/tex/main.pdf`. The strict
monograph text audit run by the build script was clean.

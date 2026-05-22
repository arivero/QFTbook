# Spinor, Grassmann, LSZ, and Path-Integral Boundary Audit

Date: 2026-05-22

## Scope

- Certified the 253a handwritten source block pp. 166--189 into
  `monograph/tex/volumes/volume_i/chapter16_spinor_fields_fermionic_statistics_and_grassmann_path_integrals.tex`.
- Consulted `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`,
  section "The path integral", especially lines around 19381--19525, for the
  bosonic and fermionic time-slicing, coherent-state completeness, ordered
  Berezin measure, and thermal boundary-condition derivations.
- Added the bosonic Euclidean trace boundary-condition derivation to
  `monograph/tex/volumes/volume_i/chapter04_lagrangian_formalism_and_quantum_mechanical_path_integrals.tex`.

## Source Visual Checks

- Handwritten QFT source images:
  `monograph/tex/build/source_visual_trace/253a_trace-166.png` through
  `monograph/tex/build/source_visual_trace/253a_trace-189.png`.
- Source content checked against `transcription/tex/253a/foundations.tex`,
  roughly lines 6916--8175.
- Stringbook source checked against
  `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`, section
  "The path integral"; the identical local side copy
  `/Users/xiyin/vps/string_notes.tex` was also searched for line anchoring.

## Manuscript Rendering

- Chapter 4 render:
  `monograph/tex/build/manuscript_visual_trace/chapter04_path_integral_trace-048.png`
  through `chapter04_path_integral_trace-054.png`.
- Chapter 16 render:
  `monograph/tex/build/manuscript_visual_trace/chapter16_spinor_grassmann-286.png`
  through `chapter16_spinor_grassmann-299.png`.
- The rendered Chapter 16 pages include:
  - two-state fermion oscillator diagram;
  - coherent-state time-slicing diagram;
  - spinorial LSZ residue diagram;
  - direct/exchange four-fermion vertex diagram.

## Content Added Or Tightened

- Explicit \(\gamma_5\), \(P_\pm\), and \(B=\gamma_2\) conventions.
- Charge-conjugation covariance and Majorana/Weyl projection checks.
- Finite-dimensional Grassmann mechanics with second-class constraints and
  Dirac brackets.
- Two-state Grassmann oscillator Hamiltonian and Pauli-matrix representation.
- Berezin Gaussian integration-by-parts proof of the two-point contraction.
- Coherent-state completeness relation with the ordered Berezin sign.
- Ordered finite-dimensional coherent-state kernel with explicit global sign.
- Fermionic trace, anti-periodic thermal boundary condition, and
  supertrace/periodic boundary condition.
- Canonical Dirac momentum and equal-time bracket.
- Locality argument fixing equality of the conjugate spinor pole residues.
- Spinorial LSZ pole table and representative residue figure.
- First four-fermion vertex with direct-minus-exchange sign and figure.
- Bosonic Euclidean trace and periodic boundary condition in Chapter 4.

## Checks

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/build_monograph.sh`: clean; produced
  `monograph/tex/main.pdf`.

## Remaining Follow-Up

- The next 253a handwritten block begins with massless little-group/helicity
  material around p. 190 and belongs to the massless-particle chapter.
- The stringbook path-integral appendix also contains semiclassical,
  instanton, Borel, Lefschetz-thimble, BRST, and BV material that should be
  absorbed later only with QFT-side definitions and assumptions.

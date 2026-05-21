# Foundations Dependency And Opening Chapter Pass

Date: 2026-05-22

Scope:

- Added `planning/13_development_dependency_map.md` as a non-reader-facing
  dependency skeleton for Volumes I--XII.
- Re-audited Volume I, Chapter 1 against the stricter writing harness.
- Updated the Volume I, Chapter 1 dossier and planning README.

Source checks:

- Rechecked the source-note spine for the opening local QFT postulates,
  early Green-function spectral theory, Kallen--Lehmann representation,
  Haag--Ruelle asymptotic states, and LSZ.
- Preserved the required order: local quantum data, Green functions and
  path-integral constructions, Kallen--Lehmann, perturbative Green functions,
  Haag--Ruelle scattering, LSZ, and perturbative scattering amplitudes.

Substantive changes:

- Stated the local algebra convention: \(\Obs(\mathcal O)\) is a concrete
  unital \(*\)-subalgebra of \(\mathcal B(\Hilb)\) unless a \(C^*\)- or von
  Neumann closure is explicitly declared.
- Defined the Poincare group, \(\mathcal B(\Hilb)\), \(\mathcal U(\Hilb)\),
  spacelike separation of regions, the graded commutator convention, and the
  joint spectral measure notation used for \(\operatorname{Spec}(P)\).
- Strengthened the definitions of Wightman, local-net, and Euclidean
  presentations by recording domains, test-function spaces, positivity, state
  functionals, and reflection positivity at the level of definitions.
- Replaced loose orientation language by object-level statements about
  constructions, hypotheses, and comparison maps.

Verification:

- Passed strict monograph text audit.
- Ran deferred-topic scan over active TeX; hits were ordinary localization
  terminology and the engineering-dimension use of "defect", not premature
  AdS/CFT, localization, bootstrap, or defect-program material.
- Passed `tools/build_monograph.sh`.
- Rendered PDF page 21 to
  `/tmp/qft_opening_visual_audit/page-21.png` and visually checked
  `fig:opening-framework-comparison`; label placement is legible after the
  geometry adjustment.

# General-Method Global Exposure Pass

Date: 2026-05-30

Scope:
- `monograph/tex/volumes/volume_vi/chapter10_bridges_to_nonintegrable_two_dimensional_qft.tex`
- `monograph/tex/volumes/volume_vii/chapter07b_susy_yang_mills_family_spectra.tex`
- `planning/12_strict_writing_harness.md`
- related chapter dossiers

Principle:
- General-method machinery should not be exposed in a specialized chapter at
  all if the specialized chapter has no concrete result to extract using it.

Actions:
- Pure \(\mathcal N=1\) SYM spectral chapter: removed the explicit GEVP
  equation and generic residual-pole estimate.  The chapter now states only
  the even-scalar, odd-scalar, and fermionic channel data and the
  supersymmetry-restoration diagnostic.
- Integrable-to-nonintegrable two-dimensional bridge chapter: removed the
  local TCSA regulator definition and OPE counterterm-power derivation.  The
  chapter now keeps only the CFT-deformation Hamiltonian coordinate chart and
  points to Volume XI for the Hamiltonian-truncation machinery.
- Writing harness: promoted the principle to a global rule for the entire
  monograph.

Remaining audit queue:
- Continue searching specialized chapters for detailed numerical,
  algorithmic, bootstrap, localization, or RG-comparison machinery that is not
  attached to an actual result in that chapter.
- Current candidates include late-volume examples using ratio estimators,
  semidefinite-programming packaging, localization templates, and categorical
  construction apparatus without computed invariants.

# Issue #634 Higgs Large-Field And Standard Model Hybrid Prose Pass

## Scope

- Reworked the Standard Model chapter's high-scale Higgs/RG discussion so that
  large-field statements are formulated as claims about specified
  renormalized coupling charts, optional Wilsonian/EFT extensions, or
  semiclassical decay functionals.
- Removed the old chart phrasing from the chapter prose and
  replaced bureaucratic wording with direct mathematical language: coupling
  chart, renormalized perturbative construction, matching map, regulator data
  where a regulator is actually part of the object, and specified observable.
- Tightened the Standard Model harness rule so phenomenology folklore and BSM
  model-building claims are not treated as theory definitions or UV
  completions without regulator/constructive data.
- Reviewed the chapter's definitions end to end for conceptual rigor: local
  field content now says which bundles the fermions and Higgs sections inhabit,
  the electroweak scalar expansion is explicitly a Higgs-background chart
  rather than literal breaking of gauge redundancy, and EFT/RG statements now
  state the subtraction, matching, field-range, and optional-regulator
  assumptions on which they depend.
- Corrected the hybrid Standard Model definition so it is not described as a
  finite-cutoff electroweak EFT: the baseline object is nonperturbative QCD
  matrix elements together with the all-orders renormalized perturbative
  electroweak chiral gauge theory, weak EFTs, and matching data.
- Added the QCD--electroweak coupling datum as a separate part of the hybrid
  definition: electroweak perturbation theory couples to the nonperturbative
  QCD sector through specified color-gauge-invariant local QCD operators with
  stated composite-operator schemes, Ward identities, and contact terms.
- Clarified that the product \(SU(3)_c\times SU(2)_L\times U(1)_Y\) is local
  charge and bundle/global-form bookkeeping, not the gauge group of a single
  completed hybrid path-integral QFT.
- Added a distinction between auxiliary electroweak regularization, weak-EFT
  Wilsonian data, an optional hybrid-regulated construction with continuum
  Wightman QCD, and a hypothetical full cutoff path integral for the coupled
  product data.
- Added the possible formal hybrid path-integral route where QCD remains a
  continuum Wightman sector and only the electroweak/source layer is
  UV-regulated, while emphasizing that this is extra mathematical data beyond
  the baseline all-orders perturbative electroweak definition.

## Manuscript Changes

- Added an opening paragraph explaining the Standard Model as a hybrid
  construction rather than a single completed four-dimensional constructive
  QFT theorem.
- Expanded the Higgs quartic section with:
  - a definition of high-scale RG continuation as an ODE for renormalized
    coupling coordinates;
  - a proof that minimal-subtraction running does not itself define a
    Wilsonian cutoff theory;
  - precise conditions for quartic-positivity and metastability claims;
  - an explicit derivation of the dimension-six \(O_H=(H^\dagger H)^3\)
    large-field contribution and the general higher-operator/quartic ratio;
  - a proposition that the baseline hybrid Standard Model definition implies
    no unconditional Higgs large-field stability or metastability theorem.
- Rewrote SMEFT, oblique-parameter, hybrid-definition, chiral-lattice, and
  muon \(g-2\) prose to reduce "datum/ledger/certification" language where it
  was obscuring the actual mathematical content.
- Clarified that the scale \(\Lambda\) in the SMEFT expansion is a reference
  scale for dimensionless coupling coordinates, not a hidden cutoff parameter
  of Standard Model predictions.
- Added the field-redefinition hypothesis needed for equation-of-motion
  operators: the regulator must admit the near-identity change of variables,
  and any local Jacobian changes local coupling coordinates rather than
  producing an independent observable.
- Recast the one-loop Standard Model RG equations as a mass-independent
  minimal-subtraction chart with stated active fields and separated it from
  threshold matching, broken-phase expansions, and Wilsonian cutoff data.

## Calculation Checks

- Extended `calculation-checks/standard_model_anomaly_checks.py` with exact
  checks for the Higgs radial dimension-six expansion, the general
  higher-operator ratio, and the \(\beta_\lambda|_{\lambda=0}\) identity.
- Renamed the new check helpers from the old chart/basis vocabulary to
  coupling-chart/basis vocabulary.
- Updated `calculation-checks/README.md` and the chapter dossier to describe
  these checks in coupling-chart and two-point-coordinate language.

## Verification

- `python3 calculation-checks/standard_model_anomaly_checks.py`
- `python3 -m py_compile calculation-checks/standard_model_anomaly_checks.py`
- `git diff --check -- calculation-checks/README.md calculation-checks/standard_model_anomaly_checks.py monograph/tex/volumes/volume_ii/chapter19c_standard_model_hybrid_definition.tex planning/chapter_dossiers/volume_ii/chapter19c_standard_model_hybrid_definition.md planning/12_strict_writing_harness.md`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

The full monograph build and log scan are clean.  The generated PDF has 2356
pages.

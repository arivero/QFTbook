# Build Audit: Volume X KMS Foundations Depth Pass

## Scope

- Branch: `main`.
- Files edited:
  - `monograph/tex/volumes/volume_x/chapter01_kms_states_and_thermal_correlators.tex`
  - `planning/chapter_dossiers/volume_x/chapter01_kms_states_and_thermal_correlators.md`
  - `calculation-checks/kms_foundation_checks.py`
  - `calculation-checks/README.md`

## Substantive Changes

- Expanded the chapter from a compact statement of KMS, detailed balance, and
  Kubo formulas into a self-contained thermal-foundation chapter.
- Added analytic-element and analytic-core definitions, with a Gaussian
  smearing lemma proving density of entire analytic observables in a
  \(C^\ast\)-dynamical system.
- Replaced the one-sentence finite Gibbs trace claim by an energy-basis proof
  of the KMS strip boundary condition.
- Declared the Fourier convention and derived finite-volume spectral
  detailed balance from delta-function spectral sums.
- Added the bosonic fluctuation--dissipation identity with the
  zero-frequency singular-sector caveat.
- Expanded linear response from the interaction-picture source expansion and
  tied the retarded sign convention to the shear Kubo formula.
- Added three figures: KMS strip, retarded support, and the logical path from
  QFT conserved-density data to hydrodynamic constitutive relations.
- Added a public calculation check for the finite KMS boundary condition,
  spectral reconstruction, fluctuation--dissipation identity, and retarded
  sign convention.

## Verification Plan

- `python3 calculation-checks/kms_foundation_checks.py`
- `python3 -m py_compile calculation-checks/kms_foundation_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

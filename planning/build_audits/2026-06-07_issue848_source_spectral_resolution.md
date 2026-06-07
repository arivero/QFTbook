# 2026-06-07 Issue 848 Source Spectral-Resolution Audit

## Scope

- Added `constr:cigar-liouville-source-spectral-resolution` in Vol VII Ch09
  after the finite-volume Robin/domain diagnostic.
- The new construction assembles the noncompact reflection phase-density shift,
  reference Plancherel measure, local source row, pole residues, and contact
  terms into a source-normalized Euclidean two-point coordinate
  `G_{O,alpha}^{I}(beta)`.
- This is a physics-observable bridge for #848: protected Liouville labels and
  a unitary reflection coefficient are not enough unless the spectral measure
  and source normalization produce the same local correlator.

## Quality Boundary

- This is not a derivation of the Hori--Kapustin equivalence, the Liouville
  path-integral two-point normalization, the full cigar Plancherel theorem, or
  all pole residues.
- The reflection formula remains an imported target.  The finite companion
  checks how such target data enter an observable and rejects shortcuts that
  omit the phase-density derivative, source row, or pole residues.
- No issue, review, directive, or planning language was added to the TeX.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- focused Vol VII Ch09 theorem/display/text/negative-scope/style/leakage
  audits
- evidence-contract, inventory, dossier, and JSON audits
- full `tools/run_calculation_checks.sh --python-only`
- full `tools/build_monograph.sh`

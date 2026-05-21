# RG Vector Field Invariants Audit

Date: 2026-05-21.

Development pass:

- Added the multi-coordinate transformation law for beta functions as vector
  fields on the renormalized theory family.
- Stated fixed points as coordinate-invariant zeros of the RG vector field.
- Derived the similarity transformation of the linearized RG matrix at a fixed
  point under finite scheme changes.
- Clarified that critical exponents are eigenvalues of the linearized flow,
  while exactly marginal directions require higher-order analysis and quotient
  by redundant field-redefinition directions.

Verification:

- `tools/audit_monograph_text.sh`
- deferred-topic scan for AdS/CFT, supersymmetry, bootstrap, large \(N\),
  localization, and defect material in active volumes
- hard-coded chapter-number scan
- `tools/build_monograph.sh`

Result:

- All checks passed.
- The compiled manuscript is
  `/Users/xiyin/QFT/monograph/tex/main.pdf`.

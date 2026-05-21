# Operator Cotangent Mixing Audit

Date: 2026-05-21.

Development pass:

- Added the tangent-cotangent interpretation of renormalized local operators.
- Stated coupling displacements as tangent vectors and operator insertions as
  dual cotangent data.
- Derived the inverse-Jacobian transformation of operator representatives under
  finite coordinate changes.
- Clarified the sign and index order of operator anomalous dimensions as the
  negative dual action of the linearized RG flow.

Verification:

- `tools/audit_monograph_text.sh`
- deferred-topic scan for AdS/CFT, supersymmetry, bootstrap, large \(N\),
  localization, and defect material in active volumes
- hard-coded chapter-number scan
- `tools/build_monograph.sh`

Result:

- All checks passed.
- The compiled manuscript is `/Users/xiyin/QFT/monograph/tex/main.pdf`.

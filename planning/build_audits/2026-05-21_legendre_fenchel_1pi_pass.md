# Legendre-Fenchel 1PI Pass

Date: 2026-05-21.

Development pass:

- Added the finite-regulator Legendre--Fenchel definition of the Euclidean
  effective action.
- Distinguished the exact convex-conjugate definition from the differentiable
  local Legendre transform used when the source-field map is invertible.
- Stated the subgradient condition replacing the inverse source map in
  non-invertible or degenerate cases.
- Archived the outdated orphan 1PI renormalization-group stub outside the
  active volume tree.

Verification:

- `tools/audit_monograph_text.sh`
- deferred-topic scan for AdS/CFT, supersymmetry, bootstrap, large \(N\),
  localization, and defect material in active volumes
- hard-coded chapter-number scan
- active-volume orphan chapter scan
- `tools/build_monograph.sh`

Result:

- All checks passed.
- The compiled manuscript is `/Users/xiyin/QFT/monograph/tex/main.pdf`.

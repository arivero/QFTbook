# LSZ Projection Bridge Audit

Date: 2026-05-21.

Development pass:

- Strengthened the LSZ chapter by adding a spectral-projection formulation of
  the one-particle pole.
- Made explicit the role of the mass-shell spectral projection \(P_1\), the
  mass-shell restrictions of test functions, and the induced two-point
  mass-shell kernel.
- Clarified that LSZ external reduction is projection onto the isolated
  one-particle subspace in each external variable, followed by connected
  truncation and comparison with Haag--Ruelle wave operators.

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

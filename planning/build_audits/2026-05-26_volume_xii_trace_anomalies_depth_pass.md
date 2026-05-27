# 2026-05-26 Volume XII Trace-Anomalies Depth Pass

## Scope

- Rewrote `monograph/tex/volumes/volume_xii/chapter03_trace_anomalies.tex`
  from a scaffold into a self-contained curved-background trace-anomaly
  chapter.
- Added the metric-source convention for
  `W[g,lambda] = -log Z`, the stress-tensor sign convention, Weyl response,
  and trace-anomaly density.
- Proved Wess-Zumino consistency from commutativity of local Weyl variations
  and recorded finite counterterm shifts as Weyl coboundaries.
- Derived the Weyl variations of `sqrt(g)`, `R`, and
  `int sqrt(g) R^2`; fixed the `b`-coefficient shift in the
  four-dimensional anomaly convention.
- Added the two-dimensional anomaly and Wess-Zumino action with an explicit
  variation check.
- Added the four-dimensional parity-even anomaly basis with explicit
  `E_4`, `W^2`, and `nabla^2 R` representatives, including the scheme
  status of the `nabla^2 R` term.
- Added the heat-kernel derivation of the conformal-scalar coefficients and
  the determinant ledger for Weyl fermions, Dirac fermions, and Maxwell
  vectors.
- Added the `N=4` Yang-Mills free-field central-charge check
  `a=c=dim(G)/4`.
- Added the contact-term interpretation and a precise nonperturbative open
  problem for deriving trace anomalies from curved-background QFT data.
- Updated the Volume XII chapter dossier and calculation-check README.

## Calculation Check

- Added `calculation-checks/trace_anomaly_checks.py`.
- The script checks the conformal-scalar heat-kernel curvature combination,
  cancellation of the scalar `R^2` term, the four-dimensional `R^2`
  counterterm Weyl variation, free-field `a,c` arithmetic, the `N=4`
  `a=c` sum, constant-curvature identities, and the two-dimensional
  Wess-Zumino variation.

## Verification

- `python3 calculation-checks/trace_anomaly_checks.py`
  - Passed: `All curved trace-anomaly checks passed.`
- `python3 -m py_compile calculation-checks/trace_anomaly_checks.py`
  - Passed.
- `tools/audit_monograph_text.sh`
  - Passed as part of `tools/build_monograph.sh`.
- `tools/audit_chapter_dossiers.sh`
  - Passed before the final TeX notation fix.
- `tools/build_monograph.sh`
  - First run exposed an actual TeX error: `\slashed` was undefined in the
    new Dirac determinant notation.
  - Fixed by writing the squared Dirac operator as `P_{\mathcal D}` and
    `\mathcal D^2`, avoiding an undeclared macro.
  - Final run passed with a clean log scan.
- `pdfinfo monograph/tex/main.pdf`
  - Pages: 1822.

## Residual Work

- Add a compact local-Weyl-cohomology figure in a later figure pass.
- Give full determinant derivations for spinor and Maxwell fields in an
  appendix or calculation note if the curved-background chapters become a
  primary reference for free-field anomaly computations.

# Issue #473 Audit: Trace-Anomaly Type Classification

## Scope

GitHub issue #473 reported that the stress-tensor/Weyl chapter discussed
two- and four-dimensional anomaly coefficients but did not give the
type-A/type-B conformal-anomaly classification in general even dimension, nor
the explicit \(D=2,4,6\) lists.

## Manuscript Changes

- Split the former anomaly-coefficient section into:
  - `Weyl Anomaly Density and Contact Ward Identities`;
  - `Classification of Conformal Anomalies`;
  - `Anomaly Coefficients and Stress-Tensor Correlators`.
- Added the Wess--Zumino consistency condition
  \[
    \delta_{\omega_1}\mathbf A_{\omega_2}
    -\delta_{\omega_2}\mathbf A_{\omega_1}=0
  \]
  and stated the anomaly as local Weyl cohomology modulo metric counterterms.
- Defined the parity-even closed-bulk classification in even dimension:
  type A from \(E_{2n}\), type B from Weyl-invariant scalar densities, and
  type D from counterterm variations.
- Added the explicit \(D=2\) list: \(E_2=R\), no independent parity-even
  type-B density.
- Added the explicit \(D=4\) list:
  \(E_4\), \(W_{\mu\nu\rho\sigma}W^{\mu\nu\rho\sigma}\), and the
  scheme-dependent \(\nabla^2R\), including the variation of the local
  \(R^2\) counterterm.
- Added the explicit \(D=6\) parity-even bulk list:
  one Euler coefficient and three type-B classes \(I_1,I_2,I_3\), with
  \(I_3\) defined modulo type-D terms.
- Added a local-scope warning that boundaries, defects, global terms, and
  parity-odd orientation-dependent candidates require separate data.

## Calculation Checks

- Added `calculation-checks/trace_anomaly_classification_checks.py`.
- The script checks:
  - parity-even bulk type-A/type-B counts in \(D=2,4,6\);
  - engineering dimensions of the listed type-B densities;
  - the \(-12\) coefficient in
    \(\delta_\omega\int\sqrt g\,R^2=-12\int\sqrt g\,\omega\nabla^2R\) in
    \(D=4\);
  - the finite integer normalization factors underlying
    \((4\pi)^{-2}\) and \((4\pi)^{-3}\).

## Verification Plan

- Run `python3 calculation-checks/trace_anomaly_classification_checks.py`.
- Run `git diff --check`.
- Run the monograph text and dossier audits.
- Build the monograph and inspect the rendered pages containing the new
  classification section.

## Verification Results

- `python3 calculation-checks/trace_anomaly_classification_checks.py` passed.
- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` passed with a clean log scan.
- `pdfinfo monograph/tex/main.pdf` reported 869 pages.
- Rendered and inspected physical PDF pages 778--780, covering the anomaly
  density definition, Wess--Zumino consistency condition, type-A/type-B/type-D
  classification, the \(D=2,4,6\) lists, and the stress-correlator transition.

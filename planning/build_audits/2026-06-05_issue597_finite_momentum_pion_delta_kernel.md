# Issue #597 finite-momentum pion-delta kernel pass

Date: 2026-06-05.

Scope:

- Chapter: Volume II, Chapter 20, chiral axial anomalies.
- New monograph label:
  `ca:finite-momentum-pion-delta-instanton-source-kernel`.
- Companion check:
  `check_finite_momentum_pion_delta_instanton_source_kernel()` in
  `calculation-checks/bpst_instanton_normalization_checks.py`.

Substance audit:

- This is not an ADHM/moduli-space enlargement.  It uses the already
  normalized BPST zero-mode density to assemble a named physical source
  kernel for the two-flavor \(U(1)_A\)-odd \(\pi-\delta\) channel.
- The local contact coefficient is demoted to a zero-momentum limit:
  \(2\zeta_{\mathcal S}^{(2)}f(0)\).  The retained finite-momentum statement
  is the convolution with \(|\widehat h_\rho(q)|^2\), carrying the same
  determinant, source-normalization, and endpoint residual budgets.
- The pass records the physical boundary: the result is a short-distance
  instanton source kernel, not a full hadronic susceptibility.  Pole
  isolation, screening/Goldstone propagation, and long-distance spectral
  weights remain assigned to the IR residual and the color-singlet spectral
  analysis.

Negative controls:

- A point-split test with vanishing local contact can still have finite
  source-width response.
- A constant test recovers the local zero-momentum contact.
- A hard alternating source is suppressed by zero-mode smearing and cannot be
  assigned the local vertex norm.
- Determinant, endpoint, and IR errors remain additive residual budgets rather
  than signed cancellations.

Expected verification:

- Run the focused BPST normalization check.
- Run the calculation evidence/inventory audits.
- Run Chapter 20 prose/form-label audits and the full monograph build.

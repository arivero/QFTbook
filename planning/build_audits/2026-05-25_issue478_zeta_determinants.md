# Build Audit: Issue #478 Spectral Zeta Determinants

## Scope

Addressed GitHub issue #478, which asked for a self-contained introduction to
zeta-function regularization of functional determinants with an explicit
worked example.

## Manuscript Changes

- Added `sec:spectral-zeta-determinants` to Volume I, Chapter 8, immediately
  after the free Euclidean Gaussian measure.
- Defined the spectral zeta function for positive self-adjoint elliptic
  operators with compact resolvent, including zero-mode separation, the
  heat-kernel Mellin formula, meromorphic continuation, the determinant scale
  \(\mu\), and the formula
  \(\log\det_\zeta(A/\mu^r)=-\zeta_A'(0)-\zeta_A(0)\log\mu^r\).
- Explained that the \(\mu\)-dependence is governed by the local heat-kernel
  coefficient \(\zeta_A(0)\), keeping regularization distinct from
  renormalization/subtraction coordinates.
- Proved the one-loop quadratic-fluctuation formula
  \(\Gamma_1=\frac12\log\det_\zeta(A_{\phi_{\rm cl}}/\mu^r)\) for positive
  bosonic fluctuations, with zero modes and fermionic statistics separated.
- Worked out the thermal oscillator determinant on \(S^1_\beta\):
  \(\det_\zeta(-\dd_\tau^2+\omega^2)=4\sinh^2(\beta\omega/2)\), recovering
  the canonical oscillator partition function.
- Added the zeta finite part of the massless scalar circle Casimir energy,
  \(E_0^\zeta=-\pi/(6L)\), with zero-mode and vacuum-energy normalization
  separated.

## Calculation Check

- Added `calculation-checks/zeta_determinant_checks.py`.
- The script checks the periodic resolvent identity used in the oscillator
  determinant, the derivative of \(\log\det_\zeta A_\omega\), equality with
  the canonical oscillator trace, the rational value
  \(\zeta_{\rm R}(-1)=-1/12\), and the sign of the determinant scale
  dependence.

## Verification Results

- `python3 calculation-checks/zeta_determinant_checks.py` passed.
- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` passed clean.
- `pdfinfo monograph/tex/main.pdf` reports 882 pages.
- Rendered and visually inspected affected physical PDF pages 153--155,
  containing the determinant definition, one-loop proposition, oscillator
  determinant, and circle Casimir example.

# Issue #315 Mode-Cutoff Limit Status Audit

## Issue

GitHub issue #315 reported that the Euclidean quantum-mechanical Gaussian
chapter used a finite mode cutoff but did not state the status of the
cutoff-removal limit.

## Resolution

- Replaced the informal infinite product in the harmonic-oscillator example
  by a finite-dimensional integral
  \(\langle F\rangle_{T,N}\) over \(\mathbb R^N\).
- Defined the projected path \(q^{(N)}\) and finite action \(S_{E,T,N}\).
- Stated that the free oscillator's finite-\(T\) covariance is obtained as an
  actual \(N\to\infty\) Gaussian moment limit, using summability of the mode
  covariance.
- Stated separately that interacting cutoff removal means coefficientwise
  perturbative \(N_{\rm max}\to\infty\) or \(\Lambda\to\infty\) after
  regulator dependence is displayed; no nonperturbative measure or power
  series convergence is inferred.
- Updated the Chapter 5 dossier with the new symbols, definition, claim, and
  audit note.

## Verification

- Working-tree verification before commit:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`

# 2026-05-26 DPD Besov Fixed-Point Audit

## Scope

This pass develops the deterministic Besov--Holder rough Da Prato--Debussche
local solution map in Volume XI, Chapter 9.

## Mathematical Content

- Added Proposition `prop:spde-besov-heat-smoothing`, a dyadic heat-semigroup
  smoothing estimate for \(e^{t(\Delta-m^2)}:
  \mathcal C^\rho\to\mathcal C^{\rho+2\theta}\) with \(t^{-\theta}\) loss,
  together with the corresponding Duhamel estimate with \(T^{1-\theta}\)
  gain.
- The proof controls each dyadic heat block by an \(L^1\)-kernel estimate for
  the annular heat multiplier, then applies Young's inequality and the
  integrability of \((t-s)^{-\theta}\) for \(\theta<1\).
- Added Theorem `thm:spde-dpd-besov-local-fixed-point`.
  For \(0<\kappa<\alpha<2-\kappa\), enhanced noise in
  \(C([0,T];\mathcal C^{-\kappa})^3\), and initial data in
  \(\mathcal C^\alpha\), the DPD mild equation has a unique solution in
  \(C([0,T];\mathcal C^\alpha)\) on a data-controlled time interval.
- The fixed-point proof combines the Besov rough-product theorem, the dyadic
  heat-smoothing estimate with
  \(\theta=(\alpha+\kappa)/2<1\), and Banach contraction.  It also proves
  local Lipschitz dependence on the initial condition and enhanced noise.
- The calculation-check companion verifies the exponent arithmetic
  \(\theta=(\alpha+\kappa)/2\), \(1-\theta>0\), and
  \(-\kappa+2\theta=\alpha\) for a representative admissible pair.

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed.
- `pdfinfo monograph/tex/main.pdf` reports 1536 pages.
- Final log scan found no LaTeX warnings, undefined-control-sequence errors,
  fatal errors, emergency stops, overfull boxes, or underfull boxes.

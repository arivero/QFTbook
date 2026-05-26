# 2026-05-26 DPD Besov-Energy Compatibility Audit

## Scope

This pass connects the Besov--Holder local Da Prato--Debussche solution map
to the smooth energy-compactness framework on the common approximation domain
where both kinds of convergence are available.

## Mathematical Content

- Added Proposition `prop:spde-dpd-besov-energy-compatibility`.
  Smooth enhanced-noise approximants converging in
  \(C([0,T];\mathcal C^{-\kappa})^3\), with initial data converging in
  \(\mathcal C^\alpha\), converge to the canonical Besov fixed point in
  \(C([0,T];\mathcal C^\alpha)\) on a common local time interval.
- The proof uses the local Lipschitz part of the Besov fixed-point theorem.
  Since Bony's product agrees with ordinary multiplication on smooth inputs,
  each smooth PDE solution is the Besov fixed point for its smooth data.
- Under the additional Lebesgue convergence assumptions
  \(X_{1,n}\to X_1\) in \(L^4\), \(X_{2,n}\to X_2\) in \(L^2\), and
  \(X_{3,n}\to X_3\) in \(L^{4/3}\), the same limit is identified with the
  energy-compactness limit.
- The integrated DPD energy inequality is then passed to the canonical Besov
  solution for every terminal time in the common local interval by invoking
  the previously proved compactness and closedness propositions.
- The text explicitly records the logical role of this compatibility result:
  the singular stochastic theorem still requires replacing the displayed
  Lebesgue pairings by rough paracontrolled or Besov energy pairings.
- Removed a duplicated sentence in the Fourier Aubin--Lions proof.
- Added a calculation-check companion for the exponent arithmetic used in the
  compatibility argument.

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed.
- `pdfinfo monograph/tex/main.pdf` reports 1537 pages.
- Final log scan found no LaTeX warnings, undefined-control-sequence errors,
  fatal errors, emergency stops, overfull boxes, or underfull boxes.

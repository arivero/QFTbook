# 2026-05-26 DPD Energy Compactness Audit

## Scope

This pass develops the compactness half of the smooth-to-rough
Da Prato--Debussche energy argument in
`monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`.

## Mathematical Content

- Added Proposition `prop:spde-dpd-energy-compactness`.
- The proposition assumes a cutoff-uniform bound on the smooth initial
  \(L^2\) norms and on the enhanced-noise norms
  \(X_{1,n}\in L^4(Q_T)\), \(X_{2,n}\in L^2(Q_T)\), and
  \(X_{3,n}\in L^{4/3}(Q_T)\).
- It proves uniform bounds for the smooth remainders in
  \(L^\infty_tL^2_x\), \(L^2_tH^1_x\), \(L^4_{t,x}\), and
  \(\partial_tY_n\in L^{4/3}_tH^{-1}_x\).
- It gives the weak compactness extraction needed by the preceding
  closedness theorem, including terminal weak \(L^2\) convergence after
  identifying the limit by scalar \(W^{1,4/3}\) compactness.
- The calculation-check companion now verifies the exponent identities behind
  the \(L^{4/3}\) drift bound for \(Y^3\), \(Y^2X_1\), \(YX_2\), and \(X_3\).

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed.
- `pdfinfo monograph/tex/main.pdf` reports 1530 pages.
- Log scan for LaTeX warnings, undefined control sequences, fatal errors,
  emergency stops, overfull boxes, and underfull boxes found no matches.

# 2026-05-26 DPD Distributional-Limit Audit

## Scope

This pass develops the smooth-to-rough identification step for the
Da Prato--Debussche remainder in
`monograph/tex/volumes/volume_xi/chapter09_stochastic_quantization_singular_spde.tex`.

## Mathematical Content

- Added Lemma `lem:spde-fourier-aubin-lions`, a self-contained torus
  compactness theorem.  The proof uses Fourier projection: high modes are
  uniformly small by the \(L^2_tH^1_x\) bound, while each finite-mode
  projection is compact by an explicit \(W^{1,4/3}\)-to-continuous-time
  Arzela-Ascoli argument.
- Added Proposition `prop:spde-dpd-distributional-limit`.
- The proposition assumes strong convergence of smooth enhanced noises in
  the Lebesgue spaces used by the energy theory:
  \(X_{1,n}\to X_1\) in \(L^4\), \(X_{2,n}\to X_2\) in \(L^2\), and
  \(X_{3,n}\to X_3\) in \(L^{4/3}\).
- It upgrades DPD compactness to strong \(L^r_{t,x}\) convergence of the
  remainders for every \(r<4\), then passes
  \(Y_n^3\), \(Y_n^2X_{1,n}\), \(Y_nX_{2,n}\), and \(X_{3,n}\) to the limit
  in \(L^1\).
- It derives the endpoint weak formulation of the limiting distributional
  DPD equation, including the initial and terminal pairings.
- The calculation-check companion now verifies the interpolation and product
  exponent arithmetic behind this limit passage.

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed.
- `pdfinfo monograph/tex/main.pdf` reports 1532 pages.
- Log scan for LaTeX warnings, undefined control sequences, fatal errors,
  emergency stops, overfull boxes, and underfull boxes found no matches.

# Build Audit: Issue #608 Sobolev Tightness Criterion

## Scope

- Continued the constructive/stochastic quantization development in
  `volume_xi/chapter09_stochastic_quantization_singular_spde.tex`.
- Added a self-contained Hilbert-scale compactness criterion showing how a
  cutoff-uniform \(H^{-\eta}\) moment with \(0<\eta<\kappa\) implies
  tightness of cutoff laws in \(H^{-\kappa}\).
- Updated the \(\Phi^4_2\) stochastic-quantization assembly theorem so the
  tightness hypothesis points to the new criterion while still recording
  that the required interacting moment estimate is a separate constructive
  input.

## Mathematical Content

- The compactness proof is explicit in Fourier coordinates on
  \(\mathbb T^2\).
- For the \(H^{-\eta}\)-ball \(K_R\), the high-frequency tail obeys
  \[
    \|(1-P_M)\phi\|_{H^{-\kappa}}^2
    \leq
    \langle M\rangle^{-2(\kappa-\eta)}
    \|\phi\|_{H^{-\eta}}^2 .
  \]
- The total-boundedness covering step uses the square-root form
  \(\|(1-P_M)\phi\|_{H^{-\kappa}}\le
  \langle M\rangle^{-(\kappa-\eta)}R\).
- Finite-dimensional total boundedness of \(P_MK_R\), the uniform tail
  bound, and Fatou closedness prove compactness of \(K_R\) in
  \(H^{-\kappa}\).
- Markov's inequality gives the quantitative tightness estimate
  \[
    \nu_N(K_R^c)\le C R^{-p}.
  \]

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed for the edited files.
- `tools/build_monograph.sh` passed and produced
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf` reports 1525 pages.
- `rg -n "LaTeX Warning|Undefined control sequence|Fatal error|Emergency stop|Overfull|Underfull" monograph/tex/main.log`
  returned no matches.

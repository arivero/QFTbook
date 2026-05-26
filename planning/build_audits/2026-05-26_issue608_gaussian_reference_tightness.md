# Build Audit: Issue #608 Gaussian Reference Tightness

## Scope

- Continued the issue #608 stochastic-quantization proof chain in
  `volume_xi/chapter09_stochastic_quantization_singular_spde.tex`.
- Added the massive free Gaussian cutoff estimate that supplies the reference
  negative-Sobolev summability threshold on \(\mathbb T^2\).
- Updated the \(\Phi^4_2\) assembly theorem to point to the free reference
  estimate while keeping the interacting cutoff-uniform moment estimate as a
  separate constructive input.

## Mathematical Content

- For the free cutoff field
  \[
    \phi_N=\sum_{\lambda_\alpha\le N^2}
      g_\alpha(\lambda_\alpha+m^2)^{-1/2}e_\alpha ,
  \]
  the chapter proves
  \[
    \sup_N\mathbb E_{\gamma_N}\|\phi_N\|_{H^{-\eta}}^2<\infty
    \qquad \text{for every }\eta>0 .
  \]
- The proof computes the moment exactly as
  \[
    \sum_{\lambda_\alpha\le N^2}
      (1+\lambda_\alpha)^{-\eta}(\lambda_\alpha+m^2)^{-1}
  \]
  and bounds it by the two-dimensional lattice sum
  \(\sum_{k\in\mathbb Z^2}(1+|k|^2)^{-1-\eta}\).
- The lattice sum is proved convergent by dyadic annuli:
  annulus cardinality \(O(2^{2j})\) times summand size
  \(O(2^{-2(1+\eta)j})\) gives \(O(2^{-2\eta j})\).
- Combining this estimate with the Sobolev compactness criterion gives free
  cutoff tightness in \(H^{-\kappa}\) whenever \(0<\eta<\kappa\).

## Verification

- `python3 calculation-checks/constructive_scalar_spde_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed for the edited files.
- `tools/build_monograph.sh` passed and produced
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf` reports 1526 pages.
- `rg -n "LaTeX Warning|Undefined control sequence|Fatal error|Emergency stop|Overfull|Underfull" monograph/tex/main.log`
  returned no matches.

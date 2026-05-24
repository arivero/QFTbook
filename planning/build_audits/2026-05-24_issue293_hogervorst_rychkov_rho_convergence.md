# Issue #293 Hogervorst--Rychkov Radial Convergence Pass

## Scope

- Addressed GitHub issue #293:
  `[Vol V Ch 9] Hogervorst-Rychkov radial-block convergence not named`.
- Target chapter:
  `monograph/tex/volumes/volume_iii/chapter09_operator_product_expansion.tex`.

## Content Added

- Downloaded the Hogervorst--Rychkov paper into `references/` for local
  verification; the references folder remains ignored by Git.
- Added Theorem `thm:hogervorst-rychkov-rho-convergence`.
- Stated the convergence domain:
  radial conformal-block series converge absolutely, uniformly on every
  closed subdisk \(|\rho|\le q<1\), in the reflection-positive Euclidean
  radial configuration \(\bar\rho=\rho^*\).
- Derived the conformal map:
  with \(w=\sqrt{1-z}\) and \(\operatorname{Re}w>0\),
  \(\rho=(1-w)/(1+w)\), so the cut \(z\)-plane maps to the \(\rho\)-unit disk.
- Re-derived the convergence estimate from radial Hilbert-space spectral
  projections, Cauchy--Schwarz, finite level multiplicity, and the finiteness
  of the heat-kernel norms
  \(\|q^{D_{\rm rad}/2}A\|\), \(\|q^{D_{\rm rad}/2}B\|\), rather than relying
  on the literature citation alone.
- Displayed the crossing-symmetric value
  \(\rho(1/2)=3-2\sqrt2\approx0.1716\).

## Verification Targets

- The chapter must name the Hogervorst--Rychkov radial coordinate theorem and
  state the full unit-disk convergence domain.
- The result must be backed by a local derivation using the monograph's radial
  reconstruction hypotheses.
- The chapter dossier must record the theorem and theorem-boundary
  assumptions.

# Core Depth Pass 5

Date: 2026-05-21

Scope: a focused expansion of the core manuscript, keeping deferred topics out of
the active monograph and strengthening points where later arguments rely on
precise structural statements.

## Content Added

- Added the BRST doublet lemma in the gauge-fixing chapter.  The new section
  states the doublet hypotheses, defines the doublet number operator and
  contracting homotopy, proves the identity `sh + hs = N`, and records the
  consequence that positive doublet-number classes are cohomologically trivial.
- Added the soft-photon number distribution in the infrared QED chapter.  The
  new section derives the Poisson distribution of unresolved photons from the
  eikonal measure, explains the logarithmic divergence of the mean photon
  number, and separates finite inclusive probabilities from vanishing fixed
  finite-photon exclusive probabilities.
- Added Callan--Symanzik equations with renormalized operator insertions in the
  renormalized-operator chapter.  The new section fixes notation for operator
  mixing, includes the field anomalous dimension and beta-function terms, and
  explains the role of contact terms and fixed-point diagonalization.
- Added Haag duality and the dual net in the AQFT chapter.  The new section
  defines causal complements, states locality as an inclusion, defines Haag
  duality as an equality, introduces the dual net, and explains why duality is
  the right setting for localized superselection endomorphisms.
- Added DHR statistics operators and conjugates in the superselection chapter.
  The new section introduces transported endomorphisms, exchange intertwiners,
  conjugate sectors, conjugate equations, and statistical dimension.

## Verification

- `tools/build_monograph.sh`
  - Passed.
  - Built `monograph/tex/main.pdf`.
  - Log scan reported clean.
- `pdfinfo monograph/tex/main.pdf`
  - 316 pages.
- `git diff --check`
  - Passed after this audit note was added.
- `tools/audit_monograph_text.sh`
  - Passed after this audit note was added.
- Deferred-topic scan over active volume TeX files
  - Passed after this audit note was added.

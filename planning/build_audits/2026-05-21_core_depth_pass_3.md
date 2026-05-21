# Core Depth Pass 3

Date: 2026-05-21

Scope: deepen the compiled core monograph across all active volumes while
preserving the current focus on foundational QFT, scattering, renormalization,
core CFT, and reconstruction frameworks.

## Content Added

- Added canonical Kallen--Lehmann spectral-weight normalization, including the
  equal-time commutator sum rule and the resulting \(0\le Z\le1\) bound for a
  canonically normalized scalar interpolating field.
- Added Wightman tube analyticity from the spectrum condition, explaining how
  the \(i\epsilon\) prescription is the two-point boundary-value instance of
  the general forward-tube analytic structure.
- Added a scale-hierarchy explanation of the forest formula, clarifying why
  nested Taylor operators act from smaller subgraphs to larger graphs and why
  overlapping subdivergences are represented by separate compatible forests.
- Tightened radial-quantization conventions in the unitarity-bound chapter and
  added the level-one \(SO(D)\) decomposition for spinning symmetric traceless
  primaries.
- Added the OS reconstructed-field domain construction, including Euclidean
  insertion on the positive-time quotient and Lorentzian Wightman boundary
  values with Hamiltonian time evolution.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- Deferred-topic scan over `monograph/tex/volumes`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

Result: strict text audit clean; monograph build and log scan clean.

PDF: `/Users/xiyin/QFT/monograph/tex/main.pdf`, 309 pages.

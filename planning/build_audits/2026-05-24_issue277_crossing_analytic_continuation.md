# Issue #277 Audit: Crossing and Analytic Continuation

## Scope

- GitHub issue: #277, ``[Vol V Ch 9] Crossing derivation glosses analytic
  continuation step''.
- Manuscript file:
  `monograph/tex/volumes/volume_iii/chapter09_operator_product_expansion.tex`.
- Dossier file:
  `planning/chapter_dossiers/volume_iii/chapter09_operator_product_expansion.md`.

## Manuscript Changes

- Expanded the associativity section from a structural paragraph into a
  channel-domain argument.
- Described nested OPE associativity as equality of spectral expansions of the
  same radial Hilbert-space vector in a common nested Euclidean domain.
- Displayed the \(s\)-channel radial variables and convergence domain
  \(\mathcal D_s\), and the crossed \(t\)-channel variables and domain
  \(\mathcal D_t\).
- Derived the identical-scalar crossing equation from permutation symmetry of
  the separated Euclidean correlator and the ratio of the two scalar
  prefactors.
- Stated that crossing compares analytic continuations of channel sums, not
  unrelated power series at distinct OPE corners.

## Verification

- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed.

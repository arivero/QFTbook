# Issue #769 all-plus evidence-independence repair

## Scope

- Target: Volume II Chapter 6, `ca:all-plus-rational-hard-function-bin`, and
  `calculation-checks/generalized_unitarity_reduction_checks.py`.
- Review concern: the four-gluon all-plus formula was corrected, but the
  companion still hard-coded the decisive SU(3) trace Gram matrix, null
  relation, and kinematic ratio evidence.

## Repair

- The TeX now states the SU(3) Fierz identity used to contract the trace
  tensors and records the four-point momentum-conservation identity behind the
  common ordered all-plus ratio.
- The companion derives the nine-by-nine trace Gram matrix from Fierz
  contractions of the six single traces and three double traces, with the
  second trace factor reversed for the Hermitian color pairing.
- The companion row-reduces the derived Gram matrix to obtain the rank-eight
  trace null relation, derives the single-trace sum norm \(135\), and obtains
  the \(1215 |r|^2\) all-plus hard square from those generated data.
- The single-ratio spinor check was replaced by three independent exact
  rational four-point on-shell samples.
- A separate crossed real \(2\to2\) physical-region sample checks
  \(\tilde\lambda_i=\pm\bar\lambda_i\), all-outgoing momentum conservation,
  equality of the ordered ratios, the BDK double-trace sum, and the Hermitian
  norm \(R^\dagger G R\).
- The strict-cut, omitted-double-trace, and stale-metric negative controls
  remain in the executable check.

## Re-audit

- Physics depth: this pass improves the evidence chain for a physical
  hard-function contribution, not a tangential color-algebra annex.
- Scope: the five-point formula remains explicitly bounded as a leading-color
  partial-amplitude template; the completed hard-square calculation is the
  four-point trace-color example.
- Process hygiene: issue/review language remains in this planning audit and
  dossier entry, not in the TeX chapter.

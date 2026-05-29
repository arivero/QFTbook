# Issue #691 trivial-proof resolution ledger

Scope: GitHub issue #691 flagged 47 theorem/proposition/lemma/corollary
wrappers whose proofs were direct substitutions, restatements of hypotheses,
or applications of a definition.  The resolution rule used here is:

- If the mathematical content is a definition-level consequence, an algebraic
  check, a one-line functional-analytic identification, or a direct use of a
  theorem already stated nearby, it belongs in a remark or the surrounding
  prose rather than in theorem form.
- If the item is load-bearing and can be made substantive, the theorem-form
  wrapper may remain only after the statement is sharpened and the proof
  supplies the missing argument.

## Resolved in this pass

- `prop:distributional-matrix-elements`: demoted to
  `rem:distributional-matrix-elements`; the text now states the Schwartz
  kernel identification as the meaning of the continuity hypothesis.
- `prop:charge-balance-spacetime-slab`: demoted to
  `rem:charge-balance-spacetime-slab`.
- `prop:four-point-moment-cumulant-decomposition`: demoted to
  `rem:four-point-moment-cumulant-decomposition`.
- `prop:gupta-bleuler-weak-lorenz-condition`: demoted to
  `rem:gupta-bleuler-weak-lorenz-condition`.
- `prop:reflection-positivity-closed-under-scaling-limits`: demoted to
  `rem:reflection-positivity-closed-under-scaling-limits`.
- `prop:primary-correlator-finite-covariance`: demoted to
  `rem:primary-correlator-finite-covariance`.
- `prop:buscher-involutive`: demoted to `rem:buscher-involutive`.
- `prop:tq-pole-bethe-equations`: demoted to
  `rem:tq-pole-bethe-equations`.
- `prop:sw-period-integrability`: retained as a proposition, but rewritten as
  a genuine period-matrix integrability result.  The new proof differentiates
  periods at fixed flat cycles, applies the Riemann bilinear relation to the
  normalized holomorphic differentials
  `omega_J = partial lambda_SW / partial a^J`, proves symmetry of
  `tau_IJ`, and then applies the Poincare lemma on a contractible Coulomb
  patch to construct the holomorphic prepotential.
- `cor:bv-gauge-fixing-independence`: demoted to
  `rem:bv-gauge-fixing-independence`; the cross-reference in the BF chapter
  was updated.
- `prop:displacement-criterion-topological-defect`: demoted to
  `rem:displacement-criterion-topological-defect`.
- `prop:defect-fusion-acts-by-composition`: demoted to
  `rem:defect-fusion-acts-by-composition`.
- `prop:qcd-lee-yang-zero-free-analytic-limit`: demoted to
  `rem:qcd-lee-yang-zero-free-analytic-limit`.
- `prop:gamma5-hermiticity-determinant-positivity`: demoted to
  `rem:gamma5-hermiticity-determinant-positivity`.
- `lem:eta-integer-jump`: demoted to `rem:eta-integer-jump`; the following
  reference was updated.

## Already resolved before this pass

The following issue #691 entries were already absent from theorem/proposition
form in the current source when this pass began, due to the preceding
proof-substance audit passes:

- `cor:covariance-localization-regions`
- `prop:tree-level-amputated-euclidean-four-point-kernel`
- unlabeled "Suppression of irrelevant boundary memory" in Volume II,
  Chapter 16
- `prop:qcd-tmd-finite-scheme-change`
- `prop:nilpotency-from-master-equation`
- `prop:primary-infinitesimal-action`
- `prop:crossing-as-plancherel-identity`
- `prop:liouville-bcft-hyperbolic-kernels`
- `cor:n2-chiral-primary-ramond-ground-state`
- `prop:first-order-relevant-source-scaling`
- `prop:broken-charge-matrix-identity`
- `prop:form-factor-spectral-convergence-criterion`
- `prop:susy-f-term-selection-rule`
- `prop:kw-central-charges`
- `prop:abelian-sine-transfer-status`
- `prop:six-d-yang-mills-coupling-dimension`
- `prop:planar-n4-dispersion-shortening`
- `prop:functorial-extraction-criterion`
- `prop:cs-level-quantization`
- `thm:cohomological-metric-independence`
- `prop:discrete-theta-coboundary-invariance`
- `prop:gauging-requires-trivialized-anomaly-line`
- `prop:fm-ratio-exponential-scaling`
- `prop:inflow-line-trivialization`
- `prop:ising-defect-noninvertible`
- `prop:ising-defect-quantum-dimensions`
- `prop:st-walls-preserve-dirac-pairing`
- `prop:zn-one-form-symtft-gauge-invariance`
- `cor:qcd-nfl-quark-residue`
- `prop:projected-rg-zero-spurious`
- `prop:universality-equivalence-relation`
- `prop:index-berezin-zero-mode-rule`

## Verification

After the edits:

- `python3 tools/audit_theorem_form.py` passes.
- `python3 tools/audit_negative_scope_prose.py` passes.
- `git diff --check` passes on the files edited in this pass.
- A label scan over every issue #691 label leaves only
  `prop:sw-period-integrability`, which is intentionally retained after
  substantive strengthening.

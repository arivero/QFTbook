# 2026-05-24 Issue #279 Trace-Anomaly Central Charges Pass

## Scope

- GitHub issue: #279, "[Vol V Ch 3] Trace-anomaly central charges (a, c in
  4D; c in 2D) absent from main text".
- Manuscript target:
  `monograph/tex/volumes/volume_iii/chapter03_stress_tensor_weyl_structure_and_improvement.tex`.
- Dossier target:
  `planning/chapter_dossiers/volume_iii/chapter03_stress_tensor_weyl_structure_improvement.md`.

## Content Added

- Defined the Weyl-anomaly density \(\mathcal A[g]\) by the metric-source
  variation of the renormalized generating functional and fixed its sign
  relative to the chapter's stress-tensor convention.
- Stated how metric derivatives of \(\mathcal A[g]\) enter traced
  stress-tensor Ward identities as contact distributions, keeping separated
  flat-space tracelessness distinct from source-response contact terms.
- Added the two-dimensional normalization
  \(\mathcal A_2[g]=-c_{2d}R/(24\pi)\) and tied \(c_{2d}\) to the holomorphic
  stress-tensor two-point function.
- Added the four-dimensional anomaly form
  \[
    \mathcal A_4[g]=(16\pi^2)^{-1}
    (c_{\rm W}W^2-a_{\rm W}E_4+b_{\rm D}\nabla^2R),
  \]
  with \(b_{\rm D}\) identified as counterterm-dependent.
- Connected \(c_{\rm W}\) to the Chapter 8 two-point normalization through
  \(C_T=40c_{\rm W}/\pi^4\).
- Connected the Chapter 8 parity-even \(TTT\) structures to the anomaly data:
  \(c_{\rm W}\) is the Ward-fixed \(C_T\) combination, \(a_{\rm W}\) is the
  Euler-anomaly functional extracted from the traced three-point Ward identity,
  and the third combination is separated \(TTT\) data.
- Recorded the free-field \(TTT\) basis anomaly map for real scalars, Dirac
  fermions, and Maxwell vectors.

## Harness

- Passed: `git diff --check`
- Passed: `tools/audit_monograph_text.sh`
- Passed: `tools/audit_chapter_dossiers.sh`
- Passed: `tools/build_monograph.sh`

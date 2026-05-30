# CFT OPE Reconstruction Wrapper Audit

Date: 2026-05-30

Scope:
- `monograph/tex/volumes/volume_iii/chapter09_operator_product_expansion.tex`
- `planning/chapter_dossiers/volume_iii/chapter09_operator_product_expansion.md`
- historical build-audit notes for issue #288 and issue #640

Reason:
- The former theorem `thm:conditional-cft-reconstruction-from-ope` had real
  conceptual value, but its load-bearing content was not in the theorem
  statement.  The nontrivial assumptions are the positivity, radial
  convergence, all-tree compatibility, covariance, reflection positivity,
  contact-term prescription, and Lorentzian boundary-value inputs listed in
  Definition `def:abstract-radial-ope-system`.

Action:
- Demoted the theorem-family block to Construction
  `cons:conditional-cft-reconstruction-from-ope`.
- Replaced the proof environment by a verification paragraph, so the text no
  longer creates the impression that the abstract OPE-system hypotheses have
  been derived.
- Updated the open-problem reference from "Theorem" to "Construction" and
  clarified that finite or single-four-point bootstrap data do not by
  themselves generate a CFT.
- Updated the chapter dossier and historical audit records so future passes do
  not preserve the stale theorem wrapper.

Status:
- This is a #691-style anti-wrapper correction and also supports #697's CFT
  proof-debt discipline: theorem-family environments should be reserved for
  genuine mathematical assertions whose substance is in the proof, not for
  assembly procedures whose hypotheses already contain the hard content.

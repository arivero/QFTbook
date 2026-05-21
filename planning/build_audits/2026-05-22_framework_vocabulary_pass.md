# Framework Vocabulary Uniformization Pass

Date: 2026-05-22

Scope:

- Volume I compiled framework chapters on Wightman fields and AQFT local nets.
- Follow-up to the development dependency map and opening-chapter re-audit.

Source checks:

- Rechecked the opening local-QFT postulates and the placement of Wightman,
  algebraic, Euclidean, Kallen--Lehmann, Haag--Ruelle, and LSZ material in the
  source-note order.
- Used this pass only to align conventions and symbols; no theorem-level claim
  was added without proof.

Changes:

- Wightman chapter now uses the same Minkowski symbol \(M=\mathbb M^D\),
  translation convention \(U(b,1)=\exp(-\ii b^\mu P_\mu)\), joint spectral
  measure notation, and graded commutator convention as the opening chapter.
- Wightman field labels were separated from translation vectors:
  \(\alpha,\beta\in I\) are field labels and \(b\in\mathbb R^D\) is a
  translation vector.
- AQFT chapter now declares \(M=\mathbb M^D\), \(\mathcal P_+^\uparrow\), and
  \(\mathcal O\in\mathcal K(M)\) explicitly, and its displayed local-net
  notation is aligned with the opening framework.
- Figures 2.1, 3.1, and 3.2 were visually sampled after rebuilding.

Verification:

- Passed strict monograph text audit.
- Passed `git diff --check`.
- Passed `tools/build_monograph.sh`.
- Rendered PDF pages 25, 30, and 31 to
  `/tmp/qft_framework_visual_audit/` and visually checked the affected
  Wightman and AQFT diagrams.

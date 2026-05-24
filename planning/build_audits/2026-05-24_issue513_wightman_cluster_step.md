# Issue 513 Wightman Cluster Step

Date: 2026-05-24

Scope:
- Strengthened `monograph/tex/volumes/volume_iv/chapter01_wightman_fields_and_reconstruction.tex`.
- Addressed GitHub issue #513 on the analytic step in the vacuum-projector,
  unique-translation-invariant-vacuum, and weak-cluster equivalence theorem.

Changes:
- Replaced the compressed one-sentence Jost-domain assertion by
  Lemma `lem:wightman-jost-cluster-step`.
- The lemma now displays the forward and reversed matrix coefficients, the
  finite spectral measure, the open Jost edge where locality identifies the
  two boundary values, and the edge-of-the-wedge continuation.
- The proof isolates the one-parameter spectral measure for a spacelike
  translation direction, removes the zero-momentum atom by \(1-P_0\), excludes
  additional point-spectrum contributions by the forward/backward spectral
  support intersection, and states the Jost-domain Rajchman theorem in the
  precise form used for the continuous spectral component.
- The main cluster theorem now invokes this lemma rather than hiding the
  analytic step inside a sentence.

Verification:
- `git diff --check` clean.
- `tools/audit_monograph_text.sh` clean.
- `tools/audit_chapter_dossiers.sh` clean.
- `tools/build_monograph.sh` clean; output rebuilt at
  `monograph/tex/main.pdf`.

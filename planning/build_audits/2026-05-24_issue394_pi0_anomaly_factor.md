# Issue 394: Neutral-Pion Electromagnetic Anomaly Factor

Date: 2026-05-24.

Issue:

- GitHub #394 flagged that the electromagnetic specialization of the
  axial-flavor anomaly must retain the anticommutator factor
  \(\{q,q\}=2q^2\).
- Without this factor, the \(\pi^0F\widetilde F\) coefficient would be
  \(e^2/(32\pi^2f_\pi)\) rather than the anomaly-matched
  \(e^2/(16\pi^2f_\pi)\) for \(N_c=3\).

Fix:

- Made the specialization explicit in
  `monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex`:
  \[
    \operatorname{Tr}(T^a\{q,q\})
    =
    2\operatorname{Tr}(T^aq^2),
    \qquad
    \operatorname{Tr}(T^3\{q,q\})=1/3.
  \]
- Displayed the equivalent Ward identity with coefficient
  \(-N_ce^2(8\pi^2)^{-1}\operatorname{Tr}(T^aq^2)F\widetilde F\).
- Updated the chapter dossier to record the corrected normalization.

Verification to run:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

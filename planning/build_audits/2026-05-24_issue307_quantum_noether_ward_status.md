# Build Audit: Issue #307 Quantum Noether Ward Status

Issue:

- GitHub #307: `[Vol I Ch 10] Noether currents quantum status not connected
  to path-integral framework`.

Files changed:

- `monograph/tex/volumes/volume_i/chapter07_symmetries_noether_theorem_and_stress_tensors.tex`
- `planning/chapter_dossiers/volume_i/chapter07_symmetries_noether_stress_tensor.md`

Resolution:

- Added the regulated quantum Noether Ward identity
  `eq:quantum-noether-ward-regulated` to the quantum-current section.
- The new identity states that the localized-parameter Noether relation in
  correlation functions is a source-functional distributional identity with
  contact terms supported at operator insertions.
- The text identifies the additional local term
  \(\mathcal A_{\epsilon,R}\) as coming from the variation of the regulated
  integration density and from source-chart counterterms.
- The fermionic case is tied to the finite Berezinian density framework of
  Volume I, Chapter 16.
- The fixed-point CFT usage is cross-referenced to
  `sec:cft-source-functionals-ward-contacts` and
  `def:cft-fixed-point-source-bracket-status`.

Verification:

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean full XeLaTeX build and log scan;
  generated `/Users/xiyin/QFT/monograph/tex/main.pdf`.

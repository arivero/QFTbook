# Global Anomaly, Goldstone, And Harness Tightening Pass

Date: 2026-05-22.

Reference intake:
- Downloaded H. Leutwyler, "On the foundations of chiral perturbation theory",
  arXiv:hep-ph/9311274, into
  `references/sound_references/leutwyler_foundations_chiral_perturbation_hep-ph_9311274.pdf`.
- Created readable sidecar
  `references/sound_references/leutwyler_foundations_chiral_perturbation_hep-ph_9311274.txt`
  with `pdftotext -layout`.
- Downloaded Edward Witten, "Fermion Path Integrals And Topological Phases",
  arXiv:1508.04715, into
  `references/sound_references/witten_fermion_path_integrals_topological_phases_1508.04715.pdf`.
- Created readable sidecar
  `references/sound_references/witten_fermion_path_integrals_topological_phases_1508.04715.txt`
  with `pdftotext -layout`.
- Updated `references/sound_references/README.md` to record both sources and
  their roles.

Harness tightening:
- Extended `tools/audit_monograph_text.sh` to fail on reader-facing markers of
  slogan/lore prose, including "slogan", "lore", "folklore",
  "roughly speaking", "miracle", "surprise" language, "modern language", and
  negative principle framing such as "not a claim about".
- Updated the rigor and workflow planning files so principles such as anomaly
  matching, universality, and reconstruction must be unpacked into
  object-level claims with stated equivalence relations.
- Added an explicit requirement that examples test definitions, hypotheses, or
  invariants rather than decorate the prose.

Development pass:
- Rewrote the global anomalies, spontaneous symmetry breaking, and pions
  chapter around background anomaly cocycles, local counterterm equivalence,
  finite anomaly classes, and anomaly matching as equality of cocycle classes.
- Added a finite \(SU(2)\) anomaly example using a Weyl doublet, a mapping
  torus, a Pfaffian line, and a mod-two Dirac index.
- Reworked Goldstone theorem material as a Ward-identity and spectral-support
  derivation with stated assumptions.
- Rewrote the pion effective action with external flavor backgrounds, mass
  spurions, derivative counting, and the Wess--Zumino--Witten coefficient.
- Added a dedicated chapter dossier for this chapter.

Visual audit:
- Rendered pages around the revised chapter to
  `/tmp/qft_global_anomaly_visual_audit`.
- Inspected the anomaly-matching figure on rendered page
  `/tmp/qft_global_anomaly_visual_audit/page-306.png`; labels and arrows are
  legible and tied to the cocycle statement in the text.

Verification:
- `tools/audit_monograph_text.sh`
- deferred-topic scan over active monograph TeX files
- hard-coded chapter-number scan over active monograph TeX files
- active-volume orphan chapter scan
- `tools/build_monograph.sh`
- `git diff --check`

Result:
- All checks passed.
- The compiled manuscript is `/Users/xiyin/QFT/monograph/tex/main.pdf`.

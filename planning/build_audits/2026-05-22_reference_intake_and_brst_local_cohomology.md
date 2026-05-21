# Reference Intake and Local BRST Cohomology Pass

Date: 2026-05-22.

Reference intake:
- Downloaded Glenn Barnich, Friedemann Brandt, and Marc Henneaux, "Local BRST
  cohomology in gauge theories", arXiv:hep-th/0002245, into
  `references/sound_references/barnich_brandt_henneaux_local_brst_cohomology_hep-th_0002245.pdf`.
- Created readable sidecar
  `references/sound_references/barnich_brandt_henneaux_local_brst_cohomology_hep-th_0002245.txt`
  with `pdftotext -layout`.
- Updated the sound-reference shelf README and the quality workflow so external
  references are downloaded, transcribed, and dossiered before use.

Development pass:
- Added a local BRST cohomology section to the gauge-fixing chapter.
- Defined the local function algebra \(\mathcal F_{\mathrm{loc}}\), local forms
  \(\Omega^p_{\mathrm{loc}}\), \(H^g(s)\), and \(H^{g,D}(s\mid d)\).
- Separated local operator cohomology from integrated local-functional
  cohomology modulo total derivatives.
- Recorded the roles of \(H^{0,D}(s\mid d)\) for counterterms and
  \(H^{1,D}(s\mid d)\) for anomaly candidates.
- Clarified that \((\bar c,B)\) is a nonminimal contractible pair and that the
  doublet lemma supplies the explicit homotopy.
- Added a dedicated chapter dossier for gauge fixing, ghosts, and BRST.

Verification:
- `tools/audit_monograph_text.sh`
- deferred-topic scan over active monograph TeX files
- hard-coded chapter-number scan over active monograph TeX files
- active-volume orphan chapter scan
- `tools/build_monograph.sh`

Result:
- All checks passed.
- The compiled manuscript is `/Users/xiyin/QFT/monograph/tex/main.pdf`.

# Anomaly Descent and Consistent Currents Pass

Date: 2026-05-22.

Reference intake:
- Downloaded Adel Bilal, "Lectures on Anomalies", arXiv:0802.0634, into
  `references/sound_references/bilal_lectures_on_anomalies_0802.0634.pdf`.
- Created readable sidecar
  `references/sound_references/bilal_lectures_on_anomalies_0802.0634.txt`
  with `pdftotext -layout`.
- Updated `references/sound_references/README.md` to record the source and its
  role in the anomaly chapter.

Development pass:
- Expanded the chiral and axial anomalies chapter's descent discussion.
- Fixed the convention boundary between the Hermitian Yang--Mills connection
  used in the gauge-theory chapters and the anti-Hermitian connection used for
  characteristic forms.
- Stated the six-form anomaly polynomial, the Chern--Simons five-form, and the
  ghost-number-one four-form representative for four-dimensional left-handed
  Weyl fermions.
- Added the consistent-current, Bardeen--Zumino-current, and covariant-current
  distinction, including the Wess--Zumino consistency condition and the
  cohomological meaning of local gauge-anomaly cancellation.
- Added a dedicated chapter dossier for chiral and axial anomalies.

Verification:
- `tools/audit_monograph_text.sh`
- deferred-topic scan over active monograph TeX files
- hard-coded chapter-number scan over active monograph TeX files
- active-volume orphan chapter scan
- `tools/build_monograph.sh`

Result:
- All checks passed.
- The compiled manuscript is `/Users/xiyin/QFT/monograph/tex/main.pdf`.

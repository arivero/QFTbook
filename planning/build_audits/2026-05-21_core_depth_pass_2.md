# Core Depth Pass 2

Date: 2026-05-21

Scope: deepen the compiled core monograph without restoring the deferred
AdS/CFT, defect, localization, large-\(N\), or premature supersymmetric/CFT
material.

## Content Added

- Added a section on renormalized trajectories and universality to the
  Wilsonian effective field theory chapter.  The new material formulates
  universality in terms of relevant coordinates, irrelevant coordinates,
  linearized RG eigenvalues, and suppression by powers of
  \(\Lambda_R/\Lambda_0\).
- Added Wess--Zumino consistency and anomaly descent to the anomaly chapter.
  The new section states the consistency condition, its BRST cohomological
  form, the descent from a six-form anomaly polynomial, and the distinction
  between gauged anomaly cancellation and global anomaly matching.
- Added a spectral formulation of the Goldstone theorem to the spontaneous
  symmetry breaking chapter, connecting a nonzero current-order-parameter
  commutator to massless support in the spectral measure and to the Goldstone
  effective fields.
- Added the explicit identical-scalar four-point crossing relation to the OPE
  chapter, presenting it as associativity of convergent local OPE expansions
  rather than as a separate dynamical assumption.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- Deferred-topic scan over `monograph/tex/volumes`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

Result: strict text audit clean; monograph build and log scan clean.

PDF: `/Users/xiyin/QFT/monograph/tex/main.pdf`, 307 pages.

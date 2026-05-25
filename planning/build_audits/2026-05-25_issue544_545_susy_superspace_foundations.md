# Build Audit: Issues 544 and 545 Superspace Foundations

Date: 2026-05-25

## Scope

Substantive development pass on
`monograph/tex/volumes/volume_vii/chapter02_superspace_superfields_local_actions.tex`,
addressing the open supersymmetry-foundations gaps on chiral component
transformations and the absence of Wess--Zumino/vector-superfield examples.

## Mathematical Changes

- Fixed the odd-parameter convention for component supersymmetry variations,
  including the distinction from commuting parameters used to label operator
  transformations.
- Derived the chiral-multiplet component transformations by acting with the
  chiral-coordinate supercharges and extracting coefficients of
  \(1,\theta^\alpha,\theta^2\).
- Added the off-shell closure statement for the chiral multiplet and derived
  it from the supertranslation algebra without using equations of motion.
- Added the canonical Wess--Zumino model component Lagrangian for multiple
  chiral fields, with the nilpotent Taylor expansion of \(W(\Phi)\), auxiliary
  equations, and scalar potential derivation.
- Introduced real vector superfields, chiral gauge transformations, and
  Wess--Zumino gauge as a local representative rather than a gauge-invariant
  formulation.
- Added the Abelian field-strength expansion \(W_\alpha\) in Wess--Zumino
  gauge and tied the gauge kinetic term back to the monograph's
  \(1/(4g^2)\operatorname{tr}(F^2)\) normalization.
- Updated the Volume VII Chapter 2 dossier to record the new definitions,
  derivations, and claim ledger entries.

## Verification

- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed; `monograph/tex/main.pdf` built cleanly.
- `pdfinfo monograph/tex/main.pdf` reports 1265 pages.

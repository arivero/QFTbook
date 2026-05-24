# Issue #248 Ward--Takahashi Versus Slavnov--Taylor Pass

## Scope

- Oldest active GitHub issue: `#248`, on the missing conceptual distinction
  between QED Ward--Takahashi identities and nonabelian Slavnov--Taylor
  identities.
- Manuscript loci:
  - `monograph/tex/volumes/volume_i/chapter20_qed_renormalization_and_electromagnetic_form_factors.tex`
  - `monograph/tex/volumes/volume_ii/chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex`
- Planning loci:
  - `planning/chapter_dossiers/volume_i/chapter20_qed_renormalization_form_factors.md`
  - `planning/chapter_dossiers/volume_ii/chapter18_gauge_fixing_ghosts_brst.md`

## Content Added

- In the QED chapter, photon self-energy transversality is now identified as
  the two-photon consequence of a linear Abelian Ward--Takahashi identity
  \(\mathcal W_\alpha\Gamma_{\rm inv}=0\).
- The QED chapter now explicitly contrasts this with the nonabelian
  Slavnov--Taylor identity, whose 1PI form is quadratic in \(\Gamma\).
- In the BRST chapter, the Slavnov--Taylor section now explains the
  connected-to-1PI Legendre-transform mechanism: ordinary sources \(J\) become
  field derivatives of \(\Gamma\), while BRST-variation sources \(K,L\) remain
  external coordinates, producing products such as
  \((\delta\Gamma/\delta A)(\delta\Gamma/\delta K)\).
- The text states that the quadratic form is the 1PI expression of the
  homological BRST structure and motivates the antifield/BV formulation.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`

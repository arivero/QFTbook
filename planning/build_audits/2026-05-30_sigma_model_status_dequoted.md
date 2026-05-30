# Sigma-Model Status Boundaries De-Quoted

Date: 2026-05-30

Scope:

- `monograph/tex/volumes/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.tex`
- `planning/chapter_dossiers/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.md`

Changes:

- Converted the higher-loop supersymmetric sigma-model status block from
  `quotedtheorem` to `remark`.  The paragraph records the perturbative
  large-radius status of superspace beta-function computations and the
  scheme-dependence of many lower-loop terms; it is not a locally proved
  theorem about nonperturbative existence of compact Calabi--Yau SCFTs.
- Converted the bosonic cigar spectrum status block from `quotedtheorem` to
  `remark`.  The continuous-spectrum, reflection, and discrete-residue data
  are exact noncompact CFT data not derivable from the local large-level
  metric and stress-tensor formulas alone; presenting this as a theorem in
  the manuscript without the full harmonic-analysis construction would be
  misleading.

Verification plan:

- The edit is theorem-form/prose only; no calculation-check script is affected.
- Run the standard TeX/audit/build suite before committing.

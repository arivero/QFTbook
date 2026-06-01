# 2026-06-01 Chern-Simons-Matter Bilocal Ladder Pass

## Scope

Volume VII, Chapter 10 already derived the light-cone Chern-Simons Gaussian
constraint, the planar color reduction, and the leading bilocal self-energy
equation.  GitHub issue #596 still asks for the exact Chern-Simons-matter
large-`N` solution layer.  This pass adds the next finite-regulator step:
the bilocal Hessian and planar singlet Bethe-Salpeter equation from which
two-point functions of singlet bilinears are computed.

## Manuscript Changes

- Added a subsection deriving the collective bilocal action
  `Tr(QB)+I_LC[B]-Tr log B` for ordinary finite-regulator bosonic
  fundamentals.
- Derived the stationary equation `Q+Sigma[G]-G^{-1}=0`, matching the
  existing planar Dyson equation.
- Derived the Hessian
  `Tr(G^{-1}XG^{-1}Y)+I_LC''(X,Y)` and the explicit light-cone interaction
  Hessian
  `-2*pi*lambda*(Tr(V^+ X K V^perp Y)+Tr(V^+ Y K V^perp X))`.
- Introduced the source-response equation and amputated planar vertex
  `Gamma_W + K_G(G Gamma_W G)=W`.
- Stated the normalized singlet two-point function as
  `N^{-1} Tr(W_1 delta_{W_2}G)+O(N^{-2})`.
- Kept the scope honest: this is an exact finite-regulator large-`N`
  bilocal equation, not yet a continuum solution of the bosonic or fermionic
  Chern-Simons vector-model integral equations.

## Verification

- `python3 calculation-checks/cs_matter_lightfront_checks.py`: passed.
- `python3 -m py_compile calculation-checks/cs_matter_lightfront_checks.py`:
  passed.
- `git diff --check`: passed.
- `python3 tools/audit_theorem_form.py`: passed.
- `python3 tools/audit_unnumbered_display_labels.py`: passed.
- `tools/audit_negative_scope_prose.py`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed; rebuilt
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`:
  `Pages:           2808`.

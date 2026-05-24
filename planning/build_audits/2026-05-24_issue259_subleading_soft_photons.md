# Issue #259 Subleading Soft Photon Pass

## Scope

- Oldest active GitHub issue: `#259`, on the absence of subleading soft
  theorem and asymptotic-symmetry context in
  `monograph/tex/volumes/volume_ii/chapter22_infrared_divergences_and_inclusive_qed.tex`.
- Required repair: add a careful remark on subleading soft theorems, their
  relation to the leading-log exponentiation used in the chapter, and the
  asymptotic-symmetry/memory interpretation.

## Content Added

- Added the remark "Subleading soft photons" after the leading multi-soft
  factorization argument.
- Stated the Low expansion for one additional photon under explicit
  perturbative hypotheses: massive charged external particles, smooth hard
  amplitude near \(k=0\), and fixed infrared regulator.
- Defined
  \[
    S_h^{(0)}(k)
    =
    \sum_n
    {g_n p_n\cdot e_h^*(k)\over \eta_n p_n\cdot k}
  \]
  and the subleading operator
  \[
    S_h^{(1)}(k)
    =
    -i\sum_n
    {g_n e^*_{h,\mu}(k)k_\nu J_n^{\mu\nu}\over
    \eta_n p_n\cdot k}.
  \]
- Defined \(J_n^{\mu\nu}\) as the total Lorentz generator on the \(n\)-th
  external datum and displayed the scalar orbital part, with spin matrices
  \(\Sigma_n^{\mu\nu}\) added for spinning particles.
- Clarified the distributional meaning of \(J_n^{\mu\nu}\) on the mass shell
  and momentum-conservation surface.
- Explained by power counting that \(S^{(0)}S^{(0)*}\) produces the
  \(\dd\omega/\omega\) endpoint logarithm, while the leading--subleading
  interference contributes \(\dd\omega\) in the massive case.
- Stated that subleading multi-soft insertions are differential-operator
  products with contact terms, so the independent one-photon multiplication
  structure is a leading-eikonal property.
- Added the asymptotic-symmetry interpretation carefully: in QED the leading
  soft photon theorem is a large-\(U(1)\) Ward identity at null infinity with
  electromagnetic memory as the classical counterpart; BMS is the
  gravitational analogue.
- Updated the chapter dossier.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`

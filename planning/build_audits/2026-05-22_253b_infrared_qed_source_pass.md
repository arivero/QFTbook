# 2026-05-22 253b Infrared QED Source Pass

## Scope

- Source block: second-sequence handwritten material, pages 56--70.
- Primary PDF:
  `references/253b lecture notes 2023.pdf`.
- Manuscript home:
  `monograph/tex/volumes/volume_ii/chapter22_infrared_divergences_and_inclusive_qed.tex`.
- Control files:
  `planning/chapter_dossiers/volume_ii/chapter08_infrared_divergences_inclusive_qed.md`
  and `planning/source_inventory/253a_253b_no_skip_coverage_register.md`.

## Source Content Checked

- Soft photon emission from an external scalar line, including the
  \(p\cdot e^*/(p\cdot k-\ii\epsilon)\) eikonal denominator.
- Spinor-QED numerator reduction, showing that the leading soft factor is
  independent of spin.
- The sign convention \(\eta_n=+1\) for outgoing and \(\eta_n=-1\) for
  incoming hard charged lines.
- Multi-soft factorization and the two-soft-photon ordering identity on a
  single external line.
- Physical-polarization sum
  \(\sum_h e_{h,\mu}e^*_{h,\nu}=\eta_{\mu\nu}+k_\mu c_\nu+k_\nu c_\mu\)
  and cancellation of the \(c_\mu\)-dependent terms by hard charge
  conservation.
- The logarithmic real-emission integral in \(D=4\), including the Feynman
  parameter, polar-axis angular integral, and the relative-velocity
  coefficient \(\beta_{nm}\).
- The exponent \(A_{\beta\alpha}\), its nonnegativity from the real-emission
  kernel, and the leading real-soft factor \((E_T/\mu)^{A_{\beta\alpha}}\).
- Virtual soft photon exchange between distinct external lines and the
  eikonal integral \(J_{nm}\).
- Exponentiation of distinct-line virtual soft photons.
- Same-line virtual soft photons, the current form-factor argument, and the
  LSZ infrared factor \(Z_{\rm IR}\).
- Scalar and spinor electromagnetic current decompositions, including
  \(F(0)=1\), \(F(0)+G(0)=1\), and finite one-loop
  \(G(0)=-g^2/(8\pi^2)+O(g^4)\).
- The formal same-line loop \(J_{11}\), its relation to \(J_{12}\), and the
  scalar-QED self-energy derivative producing the same logarithm in \(Z\).
- \(k^0\)-plane pole locations for \(J_{nm}\), separating the real logarithm
  from phase contributions.
- The virtual modulus \((\mu/M)^{A_{\beta\alpha}/2}\), rate factor
  \((\mu/M)^{A_{\beta\alpha}}\), and finite inclusive product
  \((E_T/M)^{A_{\beta\alpha}}\).
- Fixed-photon-number vanishing as \(\mu\to0\), KLN enlargement for collinear
  degeneracy, coherent soft dressing, and the Abelian-Higgs photon-mass
  regulator.

## Manuscript Changes

- Added the explicit spinor soft-factor derivation from the nearly on-shell
  Dirac numerator.
- Added the two-soft-photon ordering identity before the general multi-soft
  factorization figure.
- Expanded the real-emission logarithm by deriving the angular integral rather
  than quoting it.
- Added the electromagnetic form-factor insertion and the same-line LSZ
  cancellation logic, including \(Z_{\rm IR}\), \(J_{12}\), formal \(J_{11}\),
  \(G(0)\), and the self-energy derivative check.
- Added a same-line virtual soft-loop figure showing absorption into the
  infrared part of the external LSZ factor.
- Added the \(k^0\)-pole list and the intermediate three-dimensional formula
  for \(\operatorname{Re}J_{nm}\).
- Updated the chapter dossier and the no-skip source coverage register.

## Rendered Check

Completed after the full build on 2026-05-22.

- Handwritten source pages rendered from
  `references/253b lecture notes 2023.pdf`:
  `/tmp/253b_56_70-056.png` through `/tmp/253b_56_70-070.png`.
- Compiled manuscript pages rendered from `monograph/tex/main.pdf`:
  `/tmp/qft_ir_render-336.png` through `/tmp/qft_ir_render-344.png` and
  `/tmp/qft_ir_render_extra-345.png`.
- Rendered checks covered the spinor soft factor, two-soft-photon ordering
  identity, external-line soft-factorization figure, real-emission angular
  integral, form-factor/LSZ same-line cancellation passage, same-line
  cancellation figure, \(k^0\)-pole and real-part formulas, real/virtual
  cancellation figure, inclusive fixed-\(N\) statement, dressed-state formula,
  and Abelian-Higgs regulator figure.

## Verification

- `tools/build_monograph.sh` completed cleanly.
- The strict monograph text audit inside the build completed cleanly.
- `tools/audit_monograph_text.sh` completed cleanly before the build.
- `git diff --check` completed cleanly before the build.

This promotes handwritten 253b pages 56--70 to certified coverage after the
infrared-QED source and figure audit.

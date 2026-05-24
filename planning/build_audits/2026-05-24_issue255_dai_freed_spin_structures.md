# Issue #255 Dai--Freed And Spin-Structure Pass

## Scope

- Oldest active GitHub issue: `#255`, on the finite \(SU(2)\) anomaly and
  mapping-torus discussion in
  `monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex`.
- Required repair: name the Dai--Freed/APS eta-invariant framework, make the
  spin requirement explicit, and state the spin-structure dependence of the
  mapping-torus invariant.

## Content Added

- Replaced the unqualified phrase "compact spin four-manifold" by the structured
  datum \((M,\sigma_M)\), with the explicit statement that a Weyl fermion is
  not defined on a merely oriented four-manifold.
- Wrote the Weyl operator and Pfaffians as depending on \(\sigma_M\):
  \(D^+_{B,\sigma_M}\).
- Constructed the mapping-torus spin structure \(\sigma_g\) by gluing the
  product spin structure on \(M\times[0,1]\), and stated that twisting the
  spin structure can change the mod-two index.
- Rewrote the mod-two index as
  \[
    \zeta(X_g,\sigma_g,E_g)
    =
    \dim\ker\mathcal D_{X_g,\sigma_g,E_g}\pmod 2 .
  \]
- Named the Dai--Freed formulation of determinant/Pfaffian-line holonomy and
  its APS eta-invariant origin, then stated the pseudoreal \(SU(2)\)
  specialization
  \[
    \operatorname{Hol}_{\mathrm{DF}}(X_g,\sigma_g,E_g)
    =
    (-1)^{\zeta(X_g,\sigma_g,E_g)}.
  \]
- Updated the finite inflow formulas to include structured backgrounds:
  \(\mathcal I_5[Y,\sigma_Y,B_Y]\) and
  \(\mathcal I_5[X_g,\sigma_g,B_g]\).
- Updated the chapter dossier.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`

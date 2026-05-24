# Issue #254 Wess--Zumino Integrability Pass

## Scope

- Oldest active GitHub issue: `#254`, on the derivation of the
  Wess--Zumino consistency condition in
  `monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`.
- Required repair: do not merely state that gauge variations form a Lie
  algebra; display the integrability derivation showing that, when
  \(\mathcal A(\zeta,A)=\delta_\zeta W[A]\), the commutator of first
  variations of \(W\) produces the Wess--Zumino condition.

## Content Added

- Defined the infinitesimal gauge-variation derivation on a functional:
  \[
    \delta_\zeta F[A]
    =
    \int_M d^4x\,
    \frac{\delta F}{\delta A_\mu^a(x)}(D_\mu\zeta)^a(x),
    \qquad
    D_\mu\zeta=\partial_\mu\zeta+[A_\mu,\zeta].
  \]
- Stated the regulator/formal-local-functional qualification under which the
  functional derivative and chain-rule manipulations are being used.
- Proved closure on the background connection:
  \[
    [\delta_{\zeta_1},\delta_{\zeta_2}]A_\mu
    =
    D_\mu[\zeta_1,\zeta_2],
  \]
  by expanding \(D_\mu\) and using the Jacobi identity.
- Applied the same commutator to \(W[A]\) to derive
  \[
    \delta_{\zeta_1}\mathcal A(\zeta_2,A)
    -
    \delta_{\zeta_2}\mathcal A(\zeta_1,A)
    =
    \mathcal A([\zeta_1,\zeta_2],A),
  \]
  and described it as an integrability condition for a proposed local anomaly
  to be the gauge variation of a single effective action.
- Updated the anomaly chapter dossier.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`

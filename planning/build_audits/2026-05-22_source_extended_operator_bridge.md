# 2026-05-22 Source-Extended Operator Bridge Audit

## Scope

This pass strengthens the local-operator and anomalous-dimension chapter by
connecting its source-renormalization chart to the finite-regulator Wilsonian
construction and to 1PI insertion kernels.

## Manuscript Changes

- Updated
  `monograph/tex/volumes/volume_ii/chapter12_renormalized_operators_and_minimal_subtraction.tex`.
- Added the section "Source-Extended Wilsonian Representatives."
- Stated the Euclidean source convention:
  \[
    -\delta W/\delta\eta=\langle O\rangle .
  \]
- Defined a local differential source map
  \(\eta_0=\mathcal Z_\Lambda\eta_\Lambda\), with constant sources as the
  zero-momentum specialization.
- Defined the source-extended Wilsonian pushforward
  \(L_\Lambda[\phi;\eta_\Lambda]\) at finite regulator.
- Defined the Wilsonian composite insertion
  \(\mathcal O_{\Lambda,A}^{\rm W}
    =\delta L_\Lambda/\delta\eta_\Lambda^A\).
- Stated the finite-regulator connected-functional identity
  \[
    W_\Lambda^{\rm low}[J,\eta_\Lambda]
    =
    W_{\Lambda_0}[J,\eta_0(\eta_\Lambda)]
  \]
  for low source support.
- Defined the 1PI insertion representative
  \[
    \mathcal O_{\Lambda,A}^{\Gamma}
    =
    -\delta\Gamma_\Lambda/\delta\eta_\Lambda^A .
  \]
- Added a figure showing the maps from bare sources to Wilsonian insertions,
  connected low-source functionals, Legendre transform, and projected 1PI
  mixing data.
- Added the scale-dependent source-coordinate transformation law
  \[
    \widetilde\gamma
    =
    M\gamma M^{-1}-(\dd M/\dd t)M^{-1}.
  \]

## Planning Updates

- Updated the operator/MS chapter dossier with construction tasks, claim
  ledger entries, figure requirements, and audit notes.
- Updated the Volume III master-architecture target to record that the
  operator-insertion bridge is now present and that worked examples remain.
- Updated the dependency map so the next Volume III target is worked examples
  and continuum-limit estimates, with gauge extensions routed through BV.

## Verification

- Strict monograph text audit: clean.
- Strict phrase scan on the edited manuscript and planning files: clean apart
  from intentional planning-language guardrails.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean.
- Rendered the newly added source-bridge page from `monograph/tex/main.pdf`:
  `/tmp/qft_operator_source_bridge_final2-280.png`.
  The source map, Wilsonian insertion, connected insertion, 1PI insertion, and
  anomalous-dimension connection-law display were visually inspected.  The
  source-bridge figure was revised after the first rendering to remove label
  collisions and to keep the map readable at print size.

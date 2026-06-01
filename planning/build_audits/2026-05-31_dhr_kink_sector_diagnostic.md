# DHR Kink-Sector Diagnostic Pass

## Scope

- GitHub issue context: #695, foundational/AQFT proof-debt and substantial
  example development.
- Edited chapter:
  `monograph/tex/volumes/volume_iv/chapter04_superselection_sectors_and_locality_properties.tex`.

## Change

- Added a diagnostic paragraph after the Doplicher--Roberts reconstruction
  boundary and before the split-property section.
- The new text treats a broken two-dimensional constructive scalar model with
  phase representations \(\pi_\sigma\), far-tail order-parameter observables
  \(B_L(R)\), \(B_R(R)\), and tail values \(m_\sigma\).
- It proves the representation-theoretic obstruction visible from the DHR
  definition: bounded-region DHR localization relative to a vacuum phase
  \(\pi_{\sigma_0}\) would make both far tails lie in
  \(\Obs(\mathcal O^\perp)\), hence would force their weak limits to equal
  \(m_{\sigma_0}\mathbf1\).  A soliton with \(m_{\sigma_-}\neq m_{\sigma_+}\)
  is therefore a boundary-condition sector rather than a bounded DHR charge.

## Status

This pass does not assert model existence of kink Hilbert spaces or tail
limits.  It records the exact logical implication once those constructive
inputs are proved, making the DHR/DR theorem boundary concrete in an
interacting low-dimensional example.

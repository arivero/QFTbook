# Almost-local Gauss-law wrapper demoted

Date: 2026-05-31

Related issues: GitHub #691, with background from #527 and #528.

## Scope

This pass audited the charged-sector Haag--Ruelle obstruction in
`volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`.  The
local Gauss-law obstruction is a genuine theorem-level statement because it
uses the large-sphere charge limit, locality of the observable net, and a
domain argument.  The subsequent almost-local extension is important for the
charged Haag--Ruelle problem, but after the local theorem is established it is
the closed-graph passage for the charge operator.

## Change

- Replaced the proposition/proof shell titled "No almost-local observable
  coordinate for nonzero Gauss charge" by paragraph-level prose.
- Preserved the precise hypotheses: norm approximation by local observables,
  closedness of \(Q\), and charge-domain containment.
- Preserved the conclusion that an unscreened charged vector cannot be
  produced by an almost-local operator in the gauge-invariant observable net.
- Updated the later missing-estimate discussion so it refers to the
  almost-local closure above rather than to a proposition number.
- Added a theorem-form audit guard against reintroducing the old title as
  theorem/proposition/lemma/corollary content.

## Status

This keeps theorem-family rank for the substantive Gauss-law obstruction and
for the actual Haag--Ruelle estimates.  The almost-local extension remains
visible exactly where the ordinary Haag--Ruelle localization hypothesis fails
for charged sectors.

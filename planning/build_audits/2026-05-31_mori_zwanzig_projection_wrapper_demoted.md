# Mori-Zwanzig projection wrapper demoted

Date: 2026-05-31

Related issue: GitHub #691.

## Scope

This pass audited the finite-regulator Kubo--Mori projection identity in
`volume_x/chapter04_spectral_functions_kubo_transport.tex`.  The identity is
useful because it locates precisely where hydrodynamic closure enters, but at
finite regulator its derivation is the block decomposition of the Liouville
equation followed by Duhamel's formula.

## Change

- Replaced the proposition/proof shell titled "Finite-regulator projection
  identity" by paragraph-level derivation prose.
- Preserved the projected identity, the slow-coordinate equation, the
  frequency matrix, the memory kernel, and the extra forcing term for
  \(QX_0\ne0\).
- Kept the subsequent theorem-boundary prose that separates exact finite
  dynamics from thermodynamic decay, \(k\to0\) control, Drude-sector
  subtraction, and Markovian hydrodynamic closure.
- Added a theorem-form audit guard against reintroducing the old title as
  theorem/proposition/lemma/corollary content.

## Status

This demotion leaves the formula available at the point of use while avoiding
the false impression that the finite-dimensional Duhamel block identity is
the deep transport theorem.  The actual mathematical burden remains the
closure from projected kernels to hydrodynamic transport coefficients.

# SUSY Superfield Wrapper Pass

Date: 2026-05-30

Related issue: #691

## Scope

This pass continued the anti-wrapper audit in Volume VII, Chapter 2.  The
chapter contains convention-sensitive component calculations that must remain
available to the reader, but whose proof content is coefficient extraction in a
finite Grassmann algebra or finite two-spinor matrix algebra.  Those are not
theorem-family results.

## Demotions

- `Component transformations of a chiral multiplet` was demoted from
  proposition/proof form to paragraph-level derivation.  The off-shell closure
  statement and all component formulae remain, with the derivation explicitly
  tied to the odd-parameter convention and chiral-coordinate supercharge action.
- `Wess--Zumino gauge as a representative` was demoted from proposition/proof
  form to a representative construction.  The text now presents the gauge slice
  as local field-coordinate data rather than as a gauge-invariant statement
  about supersymmetry.
- `Gauge kinetic coefficient in Wess--Zumino gauge` was demoted from lemma/proof
  form to a convention check in prose.  The finite
  \(\sigma^{\mu\nu}\)-contraction identity, the
  \([W^\alpha W_\alpha]_{\theta^2}\) coefficient, and the
  \(-F^2/(4g^2)+D^2/(2g^2)\) normalization remain explicit and are still backed
  by the companion calculation script.

## Harness

`tools/audit_theorem_form.py` now rejects reintroducing these three titles as
theorem-family wrappers.

## Status

This pass does not close #691.  It removes another cluster of calculation-only
formal wrappers from the supersymmetry setup, while preserving the formulas and
the convention checks needed for later gauge-theory chapters.

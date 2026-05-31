# Half-Sided Modular Inclusion Finite-Dimensional Diagnostic

Date: 2026-05-31

GitHub issue: #695, foundational reconstruction/AQFT proof debt.

## Scope

Volume IV, Chapter 4 uses Borchers--Wiesbrock half-sided modular inclusions as
an external operator-algebraic theorem boundary.  The surrounding exposition had
already separated the deep construction of the positive translation group from
the elementary differentiated commutator.  This pass adds a finite-dimensional
diagnostic that makes the infinite-dimensional content sharper.

## Change

Inserted a comparison argument after the standard-real-subspace formulation:
if \(\mathcal M\) is finite dimensional and
\(\sigma_t^{\mathcal M}(\mathcal N)\subset\mathcal N\) for \(t\ge0\), then
the restriction of \(\sigma_t^{\mathcal M}\) to the vector subspace
\(\mathcal N\) is injective and hence surjective.  The inclusion is therefore
equality for \(t\ge0\), and the group law gives equality for all
\(t\in\mathbb R\).

The point is a diagnostic rather than a new theorem-level result.  It locates
the proper half-sided modular semigroup in infinite-dimensional
standard-subspace geometry of local algebras, while finite matrix algebras give
only two-sided modular invariance.

## Status

This strengthens the proof-boundary exposition for #695 but does not close it.
The issue still tracks the larger foundational obligations around
operator-algebra structural theorem boundaries and substantial interacting
examples.

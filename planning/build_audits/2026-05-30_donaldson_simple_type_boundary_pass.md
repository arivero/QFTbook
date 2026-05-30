# Donaldson Simple-Type Boundary Pass

Date: 2026-05-30

## Scope

This pass advances issue #698 in Volume VIII, Chapter 8.  The target is the
Donaldson simple-type structure theorem boundary.

## Changes

- Expanded the theorem-boundary discussion to separate the geometric input from
  the algebraic consequences.
- The text now explains that the simple-type relation makes the point operator
  satisfy the minimal polynomial \(T^2-4\) on the Donaldson functional and that
  the reduced series selects the \(+2\) eigensummand in the chapter's
  normalization.
- The deep Donaldson input is identified as the finite set of characteristic
  exponential weights after removing the universal Gaussian factor, with no
  polynomial prefactors.
- Added the constant-coefficient ODE
  \[
    \prod_K(\partial_t-\langle K,v\rangle)F(h+tv)=0
  \]
  satisfied by the Gaussian-reduced finite exponential sum.
- Extended `calculation-checks/donaldson_sw_comparison_checks.py` with an
  exact Vandermonde/moment-reconstruction check for finite exponential sums.

## Proof-Form Status

The Donaldson simple-type structure theorem remains quoted mathematical
infrastructure.  The chapter now makes explicit what is theorem-level
four-manifold geometry and what follows by linear algebra once the finite set
of basic classes is known.

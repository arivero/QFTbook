# Issue #325 Audit: Wilsonian Finite-Coordinate Cutoff-Removal Estimate

## Concern

The Wilsonian chapter described continuum-limit removal as a dynamical
mechanism and gave an irrelevant-coordinate suppression estimate, but it had
to state precisely which hypotheses imply a retained-coordinate limit as
\(\Lambda_0\to\infty\).

May 29 anti-wrapper audit update: the estimate is deliberately no longer a
numbered theorem.  Its substance is the displayed variation-of-constants
estimate from explicit tuning, semigroup, boundedness, and generated-integral
convergence hypotheses.  Presenting it as a theorem hid too much of the
cutoff-removal problem inside the hypotheses.

## Manuscript Changes

- Added a forward reference in the `Renormalizability as a Continuum Limit`
  section to the finite-coordinate estimate, separating the Wilsonian
  mechanism from the proof of its hypotheses.
- The estimate assumes:
  - existence of tuning of retained bare coordinates so that
    \(u(t_R)=u_R\);
  - the solution remains in the finite-coordinate RG chart;
  - the irrelevant semigroup bound;
  - uniformly bounded irrelevant bare coordinates;
  - uniform convergence of the generated irrelevant-coordinate integral with a
    stated power remainder.
- The conclusion now states the actual continuum-limit object:
  \[
    z_R(t_0;u_R)\to (u_R,V_R(u_R)).
  \]
- The derivation uses variation of constants, the boundary-memory suppression
  estimate, and the generated-integral remainder bound.
- The estimate also records that every continuous finite-coordinate projected
  low-energy quantity \(Q(z_R)\) converges, with the same power estimate when
  \(Q\) is Lipschitz.

## Logical Status After Fix

The monograph now distinguishes:

1. The finite-regulator Wilsonian flow identity.
2. The finite-coordinate cutoff-removal estimate, whose derivation is
   self-contained once the stated estimates are assumed.
3. The separate analytic or constructive task of proving those estimates in a
   specific model and norm.

Thus the continuum-limit statement is no longer only a mechanism in prose; it
is a precise estimate with explicit hypotheses, while avoiding the false
impression that the hypotheses themselves are automatic theorem-level
consequences of an arbitrary regulated Lagrangian.

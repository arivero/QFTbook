# Issue #325 Audit: Wilsonian Continuum-Limit Existence Theorem

## Concern

The Wilsonian chapter described continuum-limit removal as a dynamical
mechanism and gave an irrelevant-coordinate suppression estimate, but it did
not contain a labeled theorem stating that, under explicit hypotheses, the
tuned reference-scale Wilsonian coordinates have a limit as
\(\Lambda_0\to\infty\).

## Manuscript Changes

- Added a forward reference in the `Renormalizability as a Continuum Limit`
  section to the theorem-level statement, separating the Wilsonian mechanism
  from the proof of its hypotheses.
- Upgraded the finite-coordinate cutoff-removal estimate to
  `Theorem~\ref{thm:conditional-finite-coordinate-wilsonian-continuum-limit}`.
- The theorem assumes:
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
- The proof derives the limit from variation of constants, the boundary-memory
  suppression proposition, and the generated-integral remainder bound.
- The theorem also records that every continuous finite-coordinate projected
  low-energy quantity \(Q(z_R)\) converges, with the same power estimate when
  \(Q\) is Lipschitz.

## Logical Status After Fix

The monograph now distinguishes:

1. The finite-regulator Wilsonian flow identity.
2. The conditional finite-coordinate continuum-limit theorem, whose proof is
   self-contained once the stated estimates are assumed.
3. The separate analytic or constructive task of proving those estimates in a
   specific model and norm.

Thus the continuum-limit statement is no longer only a mechanism in prose; it
is a theorem with explicit hypotheses and a proof, while still avoiding the
false claim that arbitrary four-dimensional scalar Lagrangians have
non-Gaussian continuum limits.

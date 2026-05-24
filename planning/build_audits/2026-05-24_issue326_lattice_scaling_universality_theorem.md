# Issue #326 Audit: Lattice Scaling Limit and Universality Theorem

## Concern

The Ising universality chapter displayed the near-critical spin scaling-limit
formula and then treated the resulting continuum correlators as available for
the rest of the discussion.  The chapter also contained finite-coordinate
universality estimates and a warning that scaling-limit existence is separate,
but it did not state a theorem whose hypotheses imply continuum universality
of lattice scaling limits.

## Manuscript Changes

- Converted the displayed separated-point spin scaling formula into
  `Hypothesis~\ref{hyp:ising-separated-spin-scaling-limit}`.
- The hypothesis now states that thermodynamic-limit conventions and
  boundary/pure-phase choices are part of the assertion, and that convergence
  is assumed for pairwise distinct continuum insertion points along the
  chosen thermal scaling trajectory.
- Added
  `Theorem~\ref{thm:conditional-lattice-to-continuum-universality}`.
- The theorem assumes:
  - finite-coordinate RG convergence to the same continuum graph;
  - source-renormalized generating-functional representations with vanishing
    remainders;
  - sequential continuity of the coordinate-to-source-functional map at the
    continuum graph;
  - common normalization of the leading scaling fields;
  - convergence of reflection-positive Osterwalder--Schrader quadratic forms
    and the Euclidean covariance, locality, regularity, and clustering
    hypotheses needed for reconstruction.
- The proof derives equality of separated-point Schwinger functions from
  finite-coordinate convergence plus sequential continuity, and explains why
  source-local polynomial differences affect only contact terms on collision
  diagonals.
- Updated the proof of local coordinate universality to invoke the labeled
  Wilsonian continuum-limit theorem from issue #325.

## Logical Status After Fix

The chapter now separates three levels:

1. A displayed lattice spin scaling limit is a hypothesis unless a model- and
   dimension-specific theorem supplies it.
2. Finite-coordinate Wilsonian universality controls the reference-scale RG
   coordinates after relevant tuning.
3. Continuum universality of normalized separated-point correlators follows
   only from the added source-functional convergence, sequential continuity,
   and OS positivity/reconstruction hypotheses.

Thus the title-level universality claim is now a conditional theorem with
operational hypotheses, not an unsupported assertion that every lattice model
in a proposed class has an existing CFT scaling limit.

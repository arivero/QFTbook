# Issue #327 Audit: Ising Thermodynamic Limits

## Concern

The Ising chapter used translation-invariant infinite-volume expectations and
pure ordered-phase states without first stating when those limits exist or
which hypotheses select pure phases.  The missing ingredients were the
ferromagnetic correlation inequalities and the monotonicity arguments behind
the plus/minus thermodynamic limits.

## Manuscript Changes

- Added
  `Theorem~\ref{thm:ising-ferromagnetic-thermodynamic-limits}` before the
  spin-correlator phase discussion.
- The theorem records the finite-volume ferromagnetic inequalities:
  - FKG positive association for increasing observables;
  - GKS nonnegativity and monotonicity of spin correlations under increasing
    ferromagnetic couplings and nonnegative fields;
  - GHS concavity of the magnetization as a function of a uniform positive
    field.
- The proof gives the finite-lattice FKG derivation from log-supermodularity
  of the ferromagnetic edge weight and uses the correlation inequalities to
  obtain bounded monotone nets of local expectations.
- The theorem states the existence of plus and minus infinite-volume limits
  for local observables along cofinal rectangular boxes.
- The theorem states the one-sided \(h\downarrow0\) limits and distinguishes
  boundary-condition independence when plus and minus states coincide from
  phase coexistence when they differ.
- The theorem defines the extra clustering condition needed for plus/minus
  boundary-selected Gibbs states to be pure/extremal.
- The subsequent phase discussion now refers back to this theorem before
  writing \(C_\beta(x_1,\ldots,x_n)\) and before calling the ordered states
  pure.

## Logical Status After Fix

The chapter no longer treats the thermodynamic limit as an unstated
background assumption.  It now separates:

1. finite-volume Ising probability measures;
2. ferromagnetic monotonicity and plus/minus infinite-volume Gibbs limits;
3. one-sided symmetry-breaking-field limits;
4. the additional clustering hypothesis that makes a selected limiting Gibbs
   state pure;
5. the later and separate scaling limit to continuum Schwinger functions.

# Issue #324 Audit: Bethe--Salpeter Fredholm Existence Criterion

## Concern

The Bethe--Salpeter chapter stated the homogeneous equation
\[
  (\mathbf 1-\widehat V_P)\Psi_B=0
\]
as the pole-residue equation for an existing bound state, but the converse
from an eigenvalue-one condition to an actual pole was only described
informally.  The open gap was the absence of an operational theorem specifying
the function space, compactness, analyticity, invertibility, and channel
overlap hypotheses under which analytic Fredholm theory applies.

## Manuscript Changes

- Added
  `Theorem~\ref{thm:bethe-salpeter-fredholm-pole-criterion}` to
  `volume_ii/chapter05_composite_bound_states_and_bethe_salpeter_amplitudes.tex`.
- The theorem now assumes:
  - a Banach space \(\mathcal X\) for amputated relative-momentum test
    functions;
  - analytic compact-operator dependence of
    \(\widehat V(z)=\mathcal K_z\mathcal G_z\);
  - invertibility of \(\mathbf 1-\widehat V(z)\) at one point of the analytic
    neighborhood;
  - absence of threshold or competing singularities in that neighborhood;
  - analytic external-channel maps \(\mathcal E_z,\mathcal F_z\) through which
    the represented four-point block is seen.
- The proof now invokes the analytic Fredholm theorem explicitly, identifies
  the finite-rank principal part of the resolvent, and states exactly when
  external channel maps do or do not make the pole visible.
- The simple-root case now has an explicit rank-one residue formula in terms
  of a right eigenvector \(\psi\), a left eigenfunctional \(\chi\), and
  \(\lambda'(z_B)\).
- A follow-up remark separates the Fredholm pole criterion from the separate
  Hilbert-space spectral positivity needed to call a first-sheet
  below-threshold pole a stable particle.
- Volume II Chapter 3 now cross-references this theorem so that the
  below-threshold pole criterion is not misread as a general existence theorem
  for truncated or unspecified Bethe--Salpeter kernels.

## Logical Status After Fix

The manuscript now makes three distinct statements:

1. If an exact stable bound-state pole exists, its residue satisfies the
   homogeneous Bethe--Salpeter equation.
2. Under the analytic compact-operator Fredholm hypotheses, a nonzero
   root vector at eigenvalue one is equivalent, up to nonzero channel overlap,
   to a pole of the represented four-point block.
3. Identifying that analytic pole with a physical stable particle also
   requires the exact Hilbert-space spectral representation and positivity
   below the relevant threshold.

Thus the homogeneous equation is no longer presented as an unconditional
existence proof.

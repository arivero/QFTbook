# Volume III Chapter: EFTs Without Poincare-Invariant UV Completion

## Scope

- Compiled in Volume III after the Ising and universality discussion.
- Addresses GitHub issue #487.
- Separates critical scaling limits that construct continuum QFTs from
  finite-cutoff condensed-matter EFTs whose validity is observable- and
  cutoff-dependent.

## Definitions and Symbols

- Defines critical scaling limits with tuning, normalization, limiting
  correlators, positivity, locality, and reconstruction data.
- Defines finite-cutoff effective theory as a tuple containing cutoff,
  retained algebra/fields, regulated action/Hamiltonian, insertion
  prescription, observable class, and validity domain.
- Proves that an OS-positive Euclidean scaling limit reconstructs a continuum
  local QFT, with the OS linear-growth caveat stated.
- Defines validation maps for borrowing relativistic QFT technology.
- Gives a transfer table for Wilsonian integration, power counting,
  analyticity, LSZ, spin-statistics/CPT, modular theory, anomalies, and LSMOH
  constraints.
- Develops examples: Fermi liquids, Lifshitz fixed points, nonrelativistic
  Goldstone counting, and quantum Hall Chern--Simons response theory.
- States a controlled approximation for emergent relativistic EFT with an
  explicit error exponent and operator class.

## Figure Ledger

- No figures were added in this pass.  The key objects are definitions,
  validation maps, and examples whose equations are short enough to remain in
  text.  A later atlas pass may add diagrams only when they encode an actual
  map between regulator data, effective observables, and continuum limits.

## Claim Ledger

1. A lattice origin does not prevent a critical scaling limit from being a
   UV-complete relativistic QFT once the limit satisfies the reconstruction
   hypotheses.
2. A finite-cutoff EFT retains the cutoff as part of its definition and does
   not inherit relativistic QFT theorems without a validation map.
3. Wilsonian reasoning and power counting transfer broadly, but only after
   the correct scaling and blocking data are specified.
4. LSZ, spin-statistics, CPT, Wightman/OS analyticity, and
   Bisognano--Wichmann modular statements require separate hypotheses or
   replacement theorems outside relativistic local QFT.
5. LSMOH/anomaly language transfers to finite-cutoff EFTs only after the
   microscopic translation, filling or projective-cell datum, and background
   twist action have been mapped into the claimed infrared observables.
6. Nonrelativistic Goldstone counting transfers as an internal-symmetry,
   thermodynamic-phase statement using the commutator-density matrix,
   stiffness, susceptibility, and spectrum checks; it does not import
   Lorentz-invariant one-mode-per-generator counting or broken-spacetime
   inverse-Higgs bookkeeping.

## Audit Notes

- This chapter is methodological but not a wrapper: each section defines data
  or proves/constructs a validation statement.
- Keep the positive formulation: define the two regimes and their data before
  warning about non-transfer of relativistic theorems.
- 2026-06-05 issue #777 cross-reference pass: added LSMOH constraints to the
  validation table and stated the required microscopic-to-IR map.
- 2026-06-05 issue #775 cross-reference pass: added the nonrelativistic
  Goldstone-counting validation map, pointing finite-density and Hamiltonian
  systems to the internal commutator-density theorem in Volume II Chapter 21.

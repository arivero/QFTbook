# Issue #700: Supersymmetric Moduli-Space Datum

## Target

Volume VII, Chapter 8 was flagged in issue #700 because it described the
quantum moduli-space tuple in prose but had no defining-property block for
the central object.

## Edit

- Added `def:quantum-supersymmetric-moduli-space-datum` immediately after the
  chapter opening.
- The datum now distinguishes:
  - the reduced stratified vacuum space `M`;
  - the holomorphic branch-coordinate sheaf `O_M^hol`;
  - vacuum Hilbert spaces `H_p`;
  - low-energy local operator algebras `A_p`;
  - branch effective-theory data `E_p`;
  - background responses and anomaly data `G_p`.
- The definition states that classical scalar quotients are coordinate
  constructions for approximations to the quantum datum, not definitions of
  the quantum moduli space.
- Rewrote the later "Quantum Moduli Space Datum" section to refer back to the
  named datum and to identify smooth branches as strata with locally constant
  massless content, supersymmetry algebra, and background-response data.
- Updated the Chapter 8 dossier.

## Scope

This pass addresses the definition-locality failure.  It does not claim to
construct `mathfrak M` from Wightman or Kontsevich-Segal data; that remains
Open Problem `op:susy-nonperturbative-moduli-space-construction`.

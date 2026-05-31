# Build Audit: Hypersurface GLSM Phase Ledger

Date: 2026-05-31

## Trigger

Continuation of the stringbook Appendix K absorption program.  The existing
Volume VII hypersurface GLSM chamber analysis identified the positive and
negative FI chambers, but it still lacked the self-contained protected
geometric and algebraic ledgers needed to make the Calabi--Yau/Landau--
Ginzburg comparison precise inside the QFT monograph.

## Edits

- Expanded Volume VII, Chapter 09 with:
  - the adjunction derivation
    `c1(TY_G)=(N-d)H|_{Y_G}` and `K_{Y_G}=O(d-N)|_{Y_G}`;
  - the `d=N` Calabi--Yau condition for this hypersurface family;
  - the large-volume sigma-model central-charge target `3(N-2)`;
  - the Fermat Landau--Ginzburg protected central charge `3N(1-2/d)`;
  - the proof that these central charges agree precisely for `d=N`;
  - the residual `mu_d` finite-gauge action in the negative chamber and the
    untwisted invariant Jacobi-basis condition `sum_i a_i=0 mod d`;
  - the branch-dependent anomaly-free Coulomb-coordinate condition
    `exp(t)=C_branch`, equivalently `T=0` in a shifted additive FI
    coordinate.
- Rewrote the quintic example scope in positive QFT terms.
- Updated the Chapter 09 dossier, the stringbook crosswalk, and the
  calculation-check inventory.

## Checks

`calculation-checks/susy_2d_lg_glsm_checks.py` now checks the finite algebra
for the hypersurface phase ledger: adjunction signs, central-charge matching,
the residual finite-gauge invariant Jacobi monomial count, and the
Coulomb-coordinate singular signal.

The pass deliberately keeps the full infrared equivalence between the
positive-chamber sigma model and the negative-chamber finite-gauge
Landau--Ginzburg model as a construction problem requiring a regulator,
stress-tensor convergence, local-operator comparison, and finite-gauge
twisted-sector state-space matching.

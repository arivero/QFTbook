# Chapter 13: All-Loop Asymptotic Bethe Ansatz

## Source Position

This chapter follows the one-loop spin-chain construction and imports the
stringbook all-loop magnon-dispersion and asymptotic-Bethe-ansatz spine into
the monograph's proof-boundary language.

## Notation Inventory

- `J`: vacuum R-charge or spin-chain length in the BMN vacuum.
- `P,K,H`: central charges in the centrally extended residual algebra.
- `x^pm`: Zhukovsky variables.
- `q_r`: conserved magnon charges entering the dressing phase.
- `sigma`, `theta`: dressing factor and phase.
- `S_mat`, `S_0`: matrix and scalar parts of the two-body magnon S-matrix.
- `A_{12},...,L_{12}`: `su(2|2)_c` matrix S-matrix amplitudes.
- `y,w`: level-II and level-III nested Bethe roots.
- `E_Q,p`: bound-state energy and momentum.
- `f(g)`: large-spin cusp scaling function.

## Claim Ledger

- Derives the magnon dispersion relation from the shortening condition and
  central charges.
- Adds BMN scaling as a normalization check rather than a proof input.
- Defines the Zhukovsky variables and charge conventions used in the ABA.
- Separates the symmetry-fixed matrix part of the S-matrix from the scalar
  dressing factor, including the ten-amplitude intertwiner form.
- Adds a dressing-phase status ledger: AFS, Hernandez-Lopez, crossing, BES,
  and the weak `c_{2,3}` onset.
- States the BES/crossing scalar-factor input as a quoted theorem with its
  framework assumptions.
- Gives the `SU(2)` all-loop asymptotic Bethe equations and cyclicity.
- Displays the first nested Bethe step and level-III rational scattering.
- Proves weak-coupling reduction to the one-loop Bethe equation and dispersion
  normalization.
- Adds bound-state dispersion and the large-spin cusp-scaling function with
  status boundaries.

## Figure Ledger

No figure is included in this pass.  A future figure should show physical and
crossed Zhukovsky sheets.

## Calculation Checks

- `calculation-checks/planar_n4_integrability_checks.py` verifies the
  central-extension dispersion identity and the weak-coupling expansion.
- The same script now checks BMN scaling, bound-state dispersion, and weak
  coefficient arithmetic relevant to cusp/Bremsstrahlung comparisons.

# Chapter 14: Mirror TBA and the Y-System

## Source Position

This chapter follows the asymptotic Bethe ansatz and develops the finite-size
mirror-TBA and Y-system framework needed for wrapping interactions.

## Notation Inventory

- `E,p`: physical magnon energy and momentum.
- `tilde E, tilde p`: mirror energy and momentum.
- `x_Q^pm`: bound-state Zhukovsky variables.
- `epsilon_A`, `Y_A`: mirror pseudoenergies and Y-functions.
- `K_BA`: mirror scattering kernel.
- `Y_{a,s}`: T-hook Y-system variables.
- `u_j`: exact physical Bethe roots in excited-state TBA.
- `T_{a,s}`: Hirota T-functions.
- `Z_0^\vee`: mirror-sheet cut locus when inherited from the stringbook
  convention.

## Claim Ledger

- Defines the mirror transformation and emphasizes the non-relativistic
  difference from two-dimensional relativistic integrable QFT.
- Adds the sheet/branch status of physical versus mirror Zhukovsky variables.
- States the general mirror TBA equation with contours, kernels, chemical
  potentials, and signs as part of the data.
- Gives the excited-state energy formula with wrapping integral.
- States the T-hook Y-system relation, derives its local Hirota origin, and
  warns that Y-system equations alone do not define the spectrum.
- Uses Konishi as the first wrapping test and separates finite-length
  correction from magnon-dispersion correction.
- Adds the weak-coupling Konishi root expansion, ABA coefficient, wrapping
  correction, and resulting four-loop coefficient.

## Figure Ledger

No figure is included in this pass.  A future figure should show the T-hook
node domain.

## Calculation Checks

- `calculation-checks/planar_n4_integrability_checks.py` verifies a local
  Hirota-to-Y-system algebra identity.
- The same script verifies Konishi four-loop wrapping coefficient arithmetic.

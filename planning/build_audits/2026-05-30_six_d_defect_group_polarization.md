# Six-Dimensional Defect Group And Polarization Pass

## Scope

- Continued the Volume VII Chapter 11 development associated with issue #626.
- Targeted the part of six-dimensional \((2,0)\) data not visible in the
  local tensor-branch Lagrangian: finite defect/discriminant groups, finite
  fluxes, and polarization choices for self-dual finite sectors.

## Change

- Added the root lattice \(Q_{\mathfrak g}\), weight lattice
  \(P_{\mathfrak g}\), defect group \(A_{\mathfrak g}=P_{\mathfrak g}/Q_{\mathfrak g}\),
  and the induced \(\mathbb Q/\mathbb Z\)-valued pairing.
- Added the ADE defect-group table and stated its normalization through
  \(|A_{\mathfrak g}|=\det C_{\mathfrak g}\).
- Defined the finite flux group \(K_Y(\mathfrak g)=H^3(Y;A_{\mathfrak g})\)
  on a closed oriented six-manifold, the cup-product pairing, and the
  finite Heisenberg commutator controlled by that pairing.
- Separated the vector-valued self-dual finite-flux theory from the numerical
  partition function obtained only after choosing a maximal isotropic
  polarization.
- Worked out the cyclic \(A_{N-1}\) finite model
  \(K=\mathbb Z_N\oplus\mathbb Z_N\) with pairing
  \((ab'-ba')/N\) and polarization \(\mathbb Z_N\oplus0\).
- Updated the chapter dossier and calculation-check ledger.

## Verification

- `python3 calculation-checks/susy_abjm_6d_checks.py`
- `python3 -m py_compile calculation-checks/susy_abjm_6d_checks.py`

## Remaining Issue #626 Work

- This pass does not construct the interacting \((2,0)\) theory.
- The global category of genuine/non-genuine surface defects, compactification
  with boundaries, and the Pestun/localization proof-debt parts of issue #626
  remain open.

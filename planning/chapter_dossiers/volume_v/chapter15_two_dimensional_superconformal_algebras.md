# Chapter 15: Two-Dimensional Superconformal Algebras

## Source Position

This chapter absorbs the chiral-algebra portion of the stringbook Appendix J
material into the CFT volume while coordinating with the Volume VII
supersymmetric-QFT development.  The chapter is deliberately not a
Landau--Ginzburg/GLSM RG-flow chapter: it supplies the shared
superconformal-algebra infrastructure that such constructions must satisfy.

## Notation Inventory

- `C`: a two-dimensional spin CFT datum.
- `T(z)`: holomorphic stress tensor.
- `G(z)`: odd `N=1` supercurrent of weight `3/2`.
- `G^+(z), G^-(z)`: odd `N=2` supercurrents of weights `3/2` and `U(1)`
  charges `+1,-1`.
- `J(z)`: holomorphic `U(1)_R` current.
- `L_n,J_n,G_r,G_r^pm`: modes in the NS or R sector.
- `c`: holomorphic central charge.
- `eta`: `N=2` spectral-flow parameter.
- `h,q`: simultaneous `L_0,J_0` eigenvalues.
- `W`: quasihomogeneous Landau--Ginzburg polynomial used only as a protected
  chiral-algebra test.
- `q_i`: rational weights of the variables in `W`.
- `Jac(W)`: Jacobi ring `C[X_i]/(partial_i W)`.

## Claim Ledger

- Defines spin two-dimensional CFT sector data, including NS/R chiral state
  spaces and the monodromy-dependent mode expansion.
- Defines the `N=1` chiral superconformal datum by the `T T`, `T G`, and
  `G G` singular OPEs.
- Derives the `N=1` mode algebra from contour residues.
- Derives the Ramond zero-mode bound `L_0-c/24 >= 0` in unitary
  representations.
- Defines the `N=2` chiral superconformal datum by the `T,J,G^pm` OPEs.
- Derives the `N=2` mode algebra, including the mixed
  `G^+ G^-` anticommutator and its `(r-s)J_{r+s}` coefficient.
- Proves the `N=2` spectral-flow automorphism and the induced shifts of
  `h` and `q`.
- Proves the NS unitarity bound `h >= |q|/2` and identifies chiral and
  antichiral primary shortening conditions.
- Shows that spectral flow by `eta=-1/2` maps an NS chiral primary to a
  Ramond state with `h=c/24`.
- Defines quasihomogeneous LG chiral data only as a protected algebraic test
  for supersymmetric dynamics, not as an RG-flow construction.
- Computes the `A`-series Jacobi ring, central charge, and chiral weights.
- Computes the quintic central charge `c=9` as an algebraic `U(1)_R` anomaly
  check, while excluding Calabi--Yau phase interpretation from this chapter.
- Records a small `N=4` boundary and states the need for a full OPE tensor
  before using small-`N=4` multiplet classification.
- Adds an open problem requiring coordination with Volume VII for intrinsic
  `N=(2,2)` LG/GLSM RG construction.

## Claims To Verify

1. The NS/R mode sets follow from the monodromy convention
   `a(z)=sum a_r z^{-r-h}`.
2. The `N=1` residue calculation gives
   `[L_m,G_r]=(m/2-r)G_{m+r}`.
3. The cubic pole in `G G` gives
   `c/3(r^2-1/4) delta_{r+s,0}`.
4. The Ramond zero-mode anticommutator is
   `{G_0,G_0}=2(L_0-c/24)`.
5. In the `N=2` algebra, the double pole and derivative term in
   `G^+G^-` combine to `(r-s)J_{r+s}`.
6. Spectral flow preserves all `N=2` brackets with the central shifts
   `eta^2 c/6` and `eta c/3`.
7. The chiral-primary norm identities are
   `||G^+_{-1/2}v||^2=(2h-q)||v||^2` and
   `||G^-_{-1/2}v||^2=(2h+q)||v||^2`.
8. For `h=q/2`, spectral flow by `eta=-1/2` gives `h'=c/24`.
9. The `A`-series central charge from `W=X^{k+2}` is `3k/(k+2)`.
10. The quintic protected algebraic central charge is `9`.

## Figures

No figures were added.  A later pass could add a sector-flow diagram showing
NS chiral primaries and Ramond ground states, if it clarifies the algebraic
map without turning into a supersymmetric dynamics chapter.

## Checks

- `calculation-checks/superconformal_algebra_checks.py` verifies the
  `N=1` Ramond zero-mode shift, `N=2` chiral-primary norm identities,
  spectral-flow automorphism, NS-to-R ground-state shift, and protected LG
  central-charge arithmetic in exact rational arithmetic.

## Remaining Obligations

- Coordinate with the Volume VII supersymmetric-QFT lane before developing
  `N=(2,2)` Landau--Ginzburg or GLSM dynamics, Witten phase structure,
  topological twists, or any IR-flow theorem.
- Develop the full small-`N=4` OPE tensor and representation theory only if
  a later QFT chapter needs it.
- Add theorem-level sewing/modular statements for spin SCFTs only after the
  relevant spin-surface and modular-functor hypotheses are stated.

## Audit Notes

- 2026-05-26 Appendix-J coordination pass: added a dedicated Volume V chapter
  for two-dimensional superconformal algebra, with explicit coordination
  boundaries to Volume VII and a calculation-check companion.

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
- `k`: supersymmetric WZW level for the rank-one coset interfaces.
- `K`: usual compact `N=2` minimal-model level, `K=k-2`.
- `K^3,J^3`: total Cartan currents in the supersymmetric `SU(2)_k` and
  `SL(2,R)_k` parent data.
- `Psi^{su}_{j,m,bar m}`, `Psi^{sl}_{j,m,bar m}`: compact and cigar coset
  primaries after the Cartan vertex has been factored out.
- `n,w`: asymptotic cigar momentum and winding labels after spectral flow.

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
- Adds the compact supersymmetric `SU(2)_k/U(1)` rank-one coset interface:
  parent `SU(2)_{k-2}` plus three fermions, removal of the `N=1` Cartan
  sector, `N=2` generators, central charge `3(k-2)/k`, primary weights and
  `R`-charges, spectral-flowed labels, simple-current identifications, and
  the residual `Z_k` action.
- Identifies the compact coset chiral-primary values with the protected
  `A`-series Landau--Ginzburg chiral data for `K=k-2`, while explicitly not
  claiming an RG-flow construction.
- Adds the noncompact supersymmetric `SL(2,R)_k/U(1)` cigar interface:
  parent `SL(2,R)_{k+2}` plus three fermions, removal of the Cartan
  `N=1` sector, `N=2` generators, central charge `3(k+2)/k`, primary
  weights and `R`-charges, continuous/discrete spectrum status boundary,
  spectral-flowed labels, momentum/winding bookkeeping, and the noncompact
  field-identification rule.
- Separates the `N=2` cigar/Liouville mirror relation as a Volume VII GLSM
  and duality theorem target from the exact coset chiral data proved here.
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
11. The compact supersymmetric coset central charge is
    `3(k-2)/k` after adding three fermions and removing the `N=1`
    abelian Cartan sector.
12. The compact coset primary formulas
    `h=(j(j+1)-m^2)/k`, `q=-2m/k` spectral-flow to
    `h=(j(j+1)-(m+eta)^2)/k+eta^2/2`,
    `q=-2(m+eta)/k+eta`.
13. The compact chiral primaries `m=-j` have `h=q/2` and match the
    `A`-series protected values with minimal level `K=k-2`.
14. The noncompact cigar central charge is `3(k+2)/k`, and the primary
    formulas `h=(-j(j-1)+m^2)/k`, `q=2m/k` spectral-flow to the displayed
    cigar formulas.
15. The compact and noncompact endpoint field-identification formulas
    preserve the displayed `h,q` values, and the cigar momentum/winding
    labels satisfy `n=M-Mbar`, `w=(M+Mbar)/k` for flowed Cartan labels.

## Figures

No figures were added.  A later pass could add a sector-flow diagram showing
NS chiral primaries and Ramond ground states, if it clarifies the algebraic
map without turning into a supersymmetric dynamics chapter.

## Checks

- `calculation-checks/superconformal_algebra_checks.py` verifies the
  `N=1` Ramond zero-mode shift, `N=2` chiral-primary norm identities,
  spectral-flow automorphism, NS-to-R ground-state shift, protected LG
  central-charge arithmetic, and the compact/noncompact supersymmetric
  rank-one coset central charges, chiral-primary identities,
  field-identification identities, spectral-flow formulas, and cigar
  momentum/winding bookkeeping in exact rational arithmetic.

## Remaining Obligations

- Coordinate with the Volume VII supersymmetric-QFT lane before developing
  `N=(2,2)` Landau--Ginzburg or GLSM dynamics, Witten phase structure,
  topological twists, cigar/Liouville mirror duality, or any IR-flow theorem.
- Develop the full small-`N=4` OPE tensor and representation theory only if
  a later QFT chapter needs it.
- Add theorem-level sewing/modular statements for spin SCFTs only after the
  relevant spin-surface and modular-functor hypotheses are stated.

## Audit Notes

- 2026-05-26 Appendix-J coordination pass: added a dedicated Volume V chapter
  for two-dimensional superconformal algebra, with explicit coordination
  boundaries to Volume VII and a calculation-check companion.
- 2026-05-26 supersymmetric rank-one coset pass: added compact minimal-coset
  and noncompact cigar chiral-algebra interfaces, expanded the Appendix J
  coset material beyond the stringbook formulas with stated hypotheses,
  self-contained central-charge/weight/flow derivations, and exact
  calculation-check coverage.

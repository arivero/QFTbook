# Chapter 15: Two-Dimensional Superconformal Algebras
Source-File: monograph/tex/volumes/volume_v/chapter15_two_dimensional_superconformal_algebras.tex

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
- `Z=(z,theta)`: local holomorphic superspace coordinate.
- `D_theta`: flat odd derivative `partial_theta+theta partial_z`.
- `Q_theta`: flat supercharge `partial_theta-theta partial_z`.
- `V`: local `N=1` contact supervector encoded by a superfunction
  `mathbb V=v+theta eta`.
- `Z_ij`: `N=1` superdistance `z_i-z_j-theta_i theta_j`.
- `Theta_123`: odd three-point `OSp(1|2)` invariant.
- `kappa`: `c/3`, the level of the `U(1)_R` current algebra.
- `eta`: `N=2` spectral-flow parameter.
- `h,q`: simultaneous `L_0,J_0` eigenvalues.
- `varphi`: chiral boson used to exponentiate the `U(1)_R` current when a
  charge-lattice extension is part of the CFT datum.
- `X_eta`, `X^pm`, `Y^pm`: spectral-flow vertex, integer spectral-flow
  generators, and their opposite superdescendants in the extended `N=2`
  chiral algebra.
- `varphi_C(tau,z)`: elliptic genus of a compact unitary `N=(2,2)` spin CFT
  under the stated Ramond trace hypotheses.
- `m_ell`: elliptic genus index `c/6`.
- `chi_y^LG`: finite Landau--Ginzburg Ramond charge polynomial obtained from
  the Jacobi ring after NS-to-R spectral flow.
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
- `Phi_ell`: compact-coset NS chiral primary
  `Psi^{su}_{ell/2,-ell/2}`.
- `R_ch`: protected NS chiral-primary fusion ring.
- `n,w`: asymptotic cigar momentum and winding labels after spectral flow.
- `J(z,y),G(z,y),Gtilde(z,y)`: auxiliary-variable packaging of the small
  `N=4` `sl_2` current triplet and two supercurrent doublets.
- `k`: small-`N=4` affine `SU(2)_R` level, with `c=6k` in that section.
- `j`: `SU(2)_R` highest weight/spin for small-`N=4` representations.
- `mathfrak S_j(q,a,x)`: global short-multiplet character used for the
  local `c=6` example.

## Claim Ledger

- Defines spin two-dimensional CFT sector data, including NS/R chiral state
  spaces and the monodromy-dependent mode expansion.
- Defines flat `(1,1)` superspace, the real scalar multiplet, the
  superspace action, its component action with auxiliary field, and the
  supercharge variation as a local QFT laboratory rather than a string
  background construction.
- Defines local `N=1` superconformal maps intrinsically as automorphisms of
  the rank-`0|1` distribution spanned by `D_theta`, derives the finite
  component conditions `z'=f+theta g h`, `theta'=g+theta h`,
  `h^2=partial f+g partial g`, and identifies the square-root branch as the
  local spin-structure shadow.
- Derives the infinitesimal `N=1` contact vector field, verifies that its
  supercommutator with `D_theta` is proportional to `D_theta`, packages
  `T` and `G` into the super stress tensor, and writes the superspace Ward
  charge.
- Defines primary superfields, their finite and infinitesimal
  transformation laws, the superdistance `Z_ij`, the odd three-point
  invariant `Theta_123`, and the two-/three-point superfield correlator
  structures with Grassmann parity bookkeeping.
- Defines the `N=1` chiral superconformal datum by the `T T`, `T G`, and
  `G G` singular OPEs.
- Derives the `N=1` mode algebra from contour residues.
- Derives the Ramond zero-mode bound `L_0-c/24 >= 0` in prose from the
  \(r=s=0\) Ramond anticommutator and positivity of \(G_0^2\) in unitary
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
- Separates abstract `N=2` spectral flow from the stronger claim that a
  spectral-flow vertex is present in the chiral algebra.
- Defines the Heisenberg/lattice realization of the `U(1)_R` current by
  `J=i sqrt(kappa) partial varphi`, including the charge-lattice/locality
  hypothesis.
- Derives the spectral-flow vertex OPE with a charged field and recovers the
  shifts `q -> q+eta kappa` and `h -> h+eta q+eta^2 kappa/2`.
- Derives the integer spectral-flow operator weights/charges, their
  chiral/antichiral shortening, the `Y^pm` descendant weights/charges, and
  the first terms in the `X_eta X_-eta` OPE.
- Records the `c=3n` Calabi-Yau-type charge-lattice values for integer and
  half-integer spectral-flow fields as algebraic data rather than a
  sigma-model construction.
- Defines the elliptic genus under compact/discrete Ramond trace hypotheses,
  proves right-moving Ramond-ground-state localization from the zero-mode
  anticommutator, derives the elliptic spectral-flow law and index `c/6`,
  records spin modular covariance of the Ramond trace as the full spin-CFT
  sewing hypothesis, derives the weak Jacobi-form conclusion from that
  hypothesis together with spectral flow, displays the determinant-line
  mechanism behind the modular quadratic factor from the `J J` OPE
  coefficient, derives the Fourier-coefficient spectral-flow orbit relation
  and fixed-discriminant invariant, and records the finite LG `chi_y` charge
  polynomial as a protected shadow rather than an RG-flow theorem.
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
- Derives the compact coset protected chiral ring from chiral-primary charge
  additivity and the truncated parent `SU(2)_{k-2}` fusion rule:
  `R_ch ~= C[x]/(x^(K+1))`, with `x^ell` mapped to `Phi_ell`.
- Adds the noncompact supersymmetric `SL(2,R)_k/U(1)` cigar interface:
  parent `SL(2,R)_{k+2}` plus three fermions, removal of the Cartan
  `N=1` sector, `N=2` generators, central charge `3(k+2)/k`, primary
  weights and `R`-charges, continuous/discrete spectrum status boundary,
  spectral-flowed labels, momentum/winding bookkeeping, and the noncompact
  field-identification rule.
- Separates the `N=2` cigar/Liouville mirror relation as a Volume VII GLSM
  and duality theorem target from the exact coset chiral data proved here.
- Defines the small `N=4` algebra in a complete auxiliary-`y` OPE
  convention with stress tensor, `sl_2` currents, and two supercurrent
  doublets, and records the equivalent compact `SU(2)_R` component mode
  algebra.
- Derives the small-`N=4` inner spectral-flow formulas and checks that the
  Cartan `J_N2=2J^3` subalgebra reproduces the `N=2` spectral-flow
  shifts.
- Derives the unitary NS BPS bound `h>=j` from the embedded `N=2` bound and
  affine `SU(2)_k` integrability, then shows half-unit flow sends
  `h=j` states to Ramond ground states of weight `k/4=c/24`.
- Works out the `c=6`, `k=1`, `j=1/2` global short-multiplet character and
  explains how it supplies the local multiplet test for `N=(4,4)`
  symmetric-product marginal operators in Chapter 11.
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
9. In a Heisenberg realization with `kappa=c/3`, the spectral-flow vertex
   `X_eta=exp(i eta sqrt(kappa) varphi)` has
   `h=eta^2 kappa/2` and `q=eta kappa`.
10. The OPE `X_eta O_q` has branch exponent `eta q` and shifts the
    Heisenberg weight by `eta q+eta^2 kappa/2`.
11. The opposite-generator OPE `X_eta X_-eta` has pole order
    `eta^2 kappa`, first `J` coefficient `eta`, and second-order
    coefficients `eta/2` for `partial J` and `eta^2/2` for `:JJ:`.
12. The integer generators `X^pm` have `h=c/6`, `q=pm c/3`, while
    `Y^pm` have `h=c/6+1/2`, `q=pm(c/3-1)`.
13. The elliptic genus spectral-flow law has Jacobi index `c/6`; the elliptic
    shift multipliers and the modular quadratic factor obey the Jacobi-group
    cocycle before any spin-modular-functor theorem is invoked.  At the
    Fourier-coefficient level, spectral flow identifies
    `c(n,r)` with `c(n+lambda r+m lambda^2,r+2m lambda)` and preserves the
    discriminant `4mn-r^2`; the weak condition is the Ramond-spectrum lower
    bound on the normalized exponent.
14. The `A`-series LG `chi_y` Ramond charges are
    `(2 ell-k)/(2(k+2))`, sum to zero, and give Witten index `k+1`.
15. The `A`-series central charge from `W=X^{k+2}` is `3k/(k+2)`.
16. The quintic protected algebraic central charge is `9`.
17. The compact supersymmetric coset central charge is
    `3(k-2)/k` after adding three fermions and removing the `N=1`
    abelian Cartan sector.
18. The compact coset primary formulas
    `h=(j(j+1)-m^2)/k`, `q=-2m/k` spectral-flow to
    `h=(j(j+1)-(m+eta)^2)/k+eta^2/2`,
    `q=-2(m+eta)/k+eta`.
19. The compact chiral primaries `m=-j` have `h=q/2` and match the
    `A`-series protected values with minimal level `K=k-2`.
20. The compact coset chiral ring multiplication is
    `Phi_a Phi_b=Phi_(a+b)` for `a+b<=K` and zero for `a+b>K`; the
    nilpotence boundary is equivalent to exceeding the maximal chiral charge
    `c/3`.
21. The noncompact cigar central charge is `3(k+2)/k`, and the primary
    formulas `h=(-j(j-1)+m^2)/k`, `q=2m/k` spectral-flow to the displayed
    cigar formulas.
22. The compact and noncompact endpoint field-identification formulas
    preserve the displayed `h,q` values, and the cigar momentum/winding
    labels satisfy `n=M-Mbar`, `w=(M+Mbar)/k` for flowed Cartan labels.
23. The local `N=1` contact vector fields preserve the odd distribution:
    `[V_mathbbV,D_theta]=-(partial mathbbV/2)D_theta`.
24. The finite superconformal-map component equations imply
    `D z'=theta' D theta'` and hence covariance of `D_theta`.
25. The `N=1` superfield two- and three-point exponents have the correct
    scaling weight, while the `Theta_123` structure carries the opposite
    Grassmann parity.
26. The small-`N=4` auxiliary-`y` OPE convention has central charge
    `c=6k` and induces an `N=2` Cartan current of level `c/3`.
27. Small-`N=4` half-unit spectral flow sends every NS BPS highest-weight
    state with `h=j` to `h_R=k/4=c/24`.
28. For `c=6`, the `j=1/2` short-character numerator is
    `q^(1/2)(a+a^-1)+q(x+x^-1)`, with the denominator supplying ordinary
    `L_-1` descendants.

## Figures

No figures were added.  A later pass could add a sector-flow diagram showing
NS chiral primaries and Ramond ground states, if it clarifies the algebraic
map without turning into a supersymmetric dynamics chapter.

## Checks

- `calculation-checks/superconformal_algebra_checks.py` verifies the
  `N=1` local superderivative algebra, contact-vector preservation of the
  odd distribution, primary-superfield scaling and parity ledgers, the
  `N=1` Ramond zero-mode shift, `N=2` chiral-primary norm identities,
  spectral-flow automorphism, NS-to-R ground-state shift, extended `N=2`
  spectral-flow vertex weights, charges, Heisenberg OPE exponents,
  `X^pm/Y^pm` descendant charges, protected LG central-charge arithmetic,
  elliptic-genus spectral-flow Jacobi multipliers and coefficient
  discriminants, LG `chi_y` charge polynomials and Witten-index counts,
  compact-coset chiral-ring
  multiplication, associativity, nilpotence, and Ramond charge matching, and
  the compact/noncompact supersymmetric rank-one coset central charges,
  chiral-primary identities, field-identification identities, spectral-flow
  formulas, cigar momentum/winding bookkeeping, the small-`N=4`
  Cartan-`N=2` level relation, BPS spectral-flow shift to `c/24`, and the
  `c=6`, `j=1/2` short-character numerator/denominator ledger in exact
  rational arithmetic.

## Reference Intake

- Local stringbook source consulted:
  `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`, lines
  `22157--22461`, for the missing Appendix-J superconformal topics.  The
  monograph repair rebuilds the relevant local QFT and chiral-algebra
  mechanisms rather than importing the string-context exposition.
- External small-`N=4` convention cross-check: Bonetti--Meneghelli,
  `arXiv:2506.15678`, Appendix A.1.1, for the compact auxiliary-`y` OPE
  packaging of the small `N=4` super Virasoro algebra.  The chapter uses the
  convention as a normalization check and derives the Cartan `N=2`,
  spectral-flow, BPS-bound, and `c=6` short-character consequences locally.
- External representation-status cross-check: Eguchi--Taormina character and
  unitary-representation records, used only to confirm the standard
  distinction between massless/BPS and massive/non-BPS small-`N=4`
  representations.  Full affine character formulas and modular completions
  remain outside the local character example.

## Remaining Obligations

- Coordinate with the Volume VII supersymmetric-QFT lane before developing
  `N=(2,2)` Landau--Ginzburg or GLSM dynamics, Witten phase structure,
  topological twists, cigar/Liouville mirror duality, or any IR-flow theorem.
- Full affine small-`N=4` character formulas, null-state resolutions, and
  modular completions remain representation-theoretic boundary material
  unless a later QFT argument uses them directly.  The chapter now contains
  the local OPE tensor, BPS bound, spectral flow, and global short-character
  test needed by the current symmetric-product construction.
- Broader spin-SCFT sewing/modular statements beyond the elliptic-genus
  theorem boundary require the corresponding spin-surface and modular-functor
  hypotheses to be stated first.

## Audit Notes

- 2026-06-04 issue #814 supergeometry/small-`N=4` pass: added the flat
  `(1,1)` superspace QFT laboratory, local `N=1` superconformal map
  derivation, primary-superfield two-/three-point structures with parity
  bookkeeping, and the small-`N=4` auxiliary-`y` OPE tensor, component mode
  algebra, inner spectral flow, BPS bound, and `c=6` short-character
  example.  Chapter 11's symmetric-product marginal tangent now explicitly
  uses the small-`N=4` `h=j=1/2` BPS test rather than treating spin-field
  dressing as a standalone weight adjustment.
- 2026-05-26 Appendix-J coordination pass: added a dedicated Volume V chapter
  for two-dimensional superconformal algebra, with explicit coordination
  boundaries to Volume VII and a calculation-check companion.
- 2026-05-26 supersymmetric rank-one coset pass: added compact minimal-coset
  and noncompact cigar chiral-algebra interfaces, expanded the Appendix J
  coset material beyond the stringbook formulas with stated hypotheses,
  self-contained central-charge/weight/flow derivations, and exact
  calculation-check coverage.
- 2026-05-26 extended `N=2` spectral-flow operator pass: separated the
  mode-algebra automorphism from the stronger local-operator assertion,
  added the charge-lattice/Heisenberg realization, derived spectral-flow
  vertex OPE data and `X^pm/Y^pm` charges, and extended the exact check
  companion.
- 2026-05-27 elliptic-genus coordination pass: added compact Ramond-trace
  hypotheses, right-moving localization, spectral-flow/Jacobi covariance,
  the full spin-CFT modular theorem boundary, finite LG `chi_y` charge
  polynomials, and exact rational checks for the index, cocycle, and
  Witten-index ledgers.
- 2026-05-30 elliptic-genus proof-boundary pass: expanded the local mechanism
  behind the Jacobi modular factor by treating the elliptic genus as a section
  of the \(U(1)_R\) anomaly determinant line over elliptic curves with flat
  \(R\)-background.  The calculation check now verifies the modular quadratic
  cocycle in addition to the elliptic spectral-flow cocycle.
- 2026-06-02 elliptic-genus coefficient-orbit pass: added the coefficient
  meaning of weak Jacobi covariance under the compact/discrete Ramond-trace
  hypotheses.  The chapter now derives the spectral-flow orbit relation on
  Fourier coefficients, isolates the discriminant \(4m_{\rm ell}n-r^2\), and
  keeps the full spin modular-functor covariance as the theorem boundary.
- 2026-06-02 elliptic-genus dequote pass: replaced the Jacobi-form
  `quotedtheorem` wrapper by a spin modular-covariance hypothesis.  The
  chapter now states the modular transport of the Ramond trace as the
  full-CFT sewing input and treats the weak Jacobi-form statement as the
  definitional consequence of that hypothesis plus the locally derived
  spectral-flow law, determinant-line quadratic factor, and coefficient
  orbit arithmetic.
- 2026-05-27 compact chiral-ring pass: promoted the compact
  supersymmetric `SU(2)_k/U(1)` interface from matching chiral-primary
  weights to deriving the protected `A`-series ring
  `C[x]/(x^(K+1))`, with exact checks of multiplication, associativity,
  nilpotence, and Ramond charge matching.
- 2026-05-29 seventh anti-wrapper pass: corrected and strengthened the
  `N=2` NS chiral-primary bound by stating the common-domain hypothesis and
  the full equality condition; for primary states the condition reduces to the
  usual single lowering-mode shortening.  The elliptic-genus right-moving
  localization proof now displays the supertrace cyclicity and positive-energy
  Ramond zero-mode pairing explicitly.

# Chapter 13: All-Loop Asymptotic Bethe Ansatz

## Source Position

This chapter follows the one-loop spin-chain construction and imports the
stringbook all-loop magnon-dispersion and asymptotic-Bethe-ansatz spine into
the monograph's proof-boundary language.

## Notation Inventory

- `J`: vacuum R-charge or spin-chain length in the BMN vacuum.
- `h_stringbook`: stringbook integrability coupling, identified here with
  monograph `g=sqrt(lambda)/(4 pi)`.
- `P,K,H`: central charges in the centrally extended residual algebra.
- `x^pm`: Zhukovsky variables.
- `x(u)`: physical-branch Zhukovsky map with short cut `[-2g,2g]`.
- `q_r`: conserved magnon charges entering the dressing phase.
- `sigma`, `theta`: dressing factor and phase.
- `chi(x,y)`: BES contour-integral kernel for the dressing phase.
- `S_mat`, `S_0`: matrix and scalar parts of the two-body magnon S-matrix.
- `A_{12},...,L_{12}`: `su(2|2)_c` matrix S-matrix amplitudes.
- `y,w`: level-II and level-III nested Bethe roots.
- `f(y,p)`, `S^{II,I}(y,p)`: one-defect nesting coefficient and the
  level-II/level-I scattering factor in the stringbook spin-chain basis.
- `v(y)=y+1/y`: rational rapidity entering level-II and level-III nested
  scattering.
- `M(y_1,y_2), N(y_1,y_2)`: `SU(2)`-invariant level-II matrix amplitudes.
- `gamma(w,y)`, `S^{III,II}(w,y)`: one-defect level-III coefficient and
  level-III/level-II scattering factor.
- `K^I,K^II,K^III`: nesting numbers for physical, level-II, and level-III
  excitations in one `su(2|2)_c` copy.
- `S_str`: string-basis nesting factor after absorbing half of the
  length-changing marker into bosons.
- `E_Q,p`: bound-state energy and momentum.
- `f(g)`: large-spin cusp scaling function.

## Claim Ledger

- Derives the magnon dispersion relation from the shortening condition and
  central charges.
- Adds a convention ledger aligning the chapter with the stringbook
  integrability convention and warning about reciprocal scalar-factor
  conventions in the literature.
- Adds BMN scaling as a normalization check rather than a proof input.
- Defines the Zhukovsky variables and charge conventions used in the ABA.
- Corrects and proves the Zhukovsky energy formula
  `H=1+2ig(1/x^+-1/x^-)`, including the physical branch and cut
  reciprocal relation.
- Separates the symmetry-fixed matrix part of the S-matrix from the scalar
  dressing factor, including the ten-amplitude intertwiner form.
- Adds the BES `chi(x,y)` contour-integral representation with its
  sheet-domain caveat.
- Adds a dressing-phase status ledger: AFS, Hernandez-Lopez, crossing, BES,
  and the weak `c_{2,3}` onset.
- Adds the explicit crossing scalar-factor equation and warns that the
  crossing path winds around shifted Zhukovsky branch points rather than
  acting as a sheet-free substitution.
- States the BES/crossing scalar-factor input as a quoted theorem with its
  framework assumptions.
- Adds an explicit asymptotic Bethe-Yang regime assumption: the ABA is a
  long-chain quantization rule for fixed-magnon or controlled high-density
  root configurations as `L -> infinity`, with wrapping/mirror winding
  suppressed.  This is deliberately distinguished from thermodynamic Bethe
  ansatz.
- Gives the `SU(2)` all-loop asymptotic Bethe equations and cyclicity.
- Proves the first single-defect nested Bethe step in the stringbook
  orientation: the mixed `su(2|2)_c` amplitude ratios imply
  `f(y,p)=a(p)/(y-x^+(p))` and
  `S^{II,I}(y,p)=(y-x^-(p))/(y-x^+(p))` by the two adjacent-transposition
  coefficient equations.
- Adds the two-defect level-II scattering datum: the `M,N` amplitudes, the
  `M+N=-1` ungraded fermion sign, the rational `M-N` eigenvalue, and the
  same-site `phi_2 Z^+` contact coefficient.
- Proves the single level-III nesting step from the `M,N` amplitudes after
  accounting for the fermionic exchange sign, deriving
  `S^{III,II}(w,y)=(w-v(y)-i/(2g))/(w-v(y)+i/(2g))`.
- Displays the level-III rational self-scattering factor following this
  nesting step.
- Proves the single-copy closed-chain nested Bethe-Yang equations by
  transporting level-I, level-II, and level-III excitations around their
  corresponding ZF chains; records the nesting numbers
  `K^I=N_1+N_2+N_3+N_4`, `K^II=2N_2+N_3+N_4`, and `K^III=N_2+N_4`.
- Adds a string-basis frame ledger for `S^{I,I}`, `S^{II,I}`,
  `S^{III,II}`, and `S^{III,III}`, and states the reciprocal auxiliary
  insertion for the alternative `SL(2)` vacuum nesting.
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
- The same script checks the Zhukovsky defining equation, large-`u`
  expansion, cut reciprocal boundary values, `x^pm` shortening relation, and
  corrected energy formula.
- It also checks that the stringbook-orientation crossing RHS is not
  invariant under a naive sheet-free `x -> 1/x` substitution.
- It checks the single level-II nesting step by evaluating the two local
  coefficient equations and their cleared polynomial identities for
  non-singular complex samples.
- It checks the two-defect level-II matrix eigenvalues and unitarity, the
  graded conversion of `M+N=-1` to trivial level-III vacuum scattering, the
  two level-III local coefficient equations, and their cleared rational
  identities.
- It checks closed-chain nesting frame conventions: string-basis level-I and
  level-II frame ratios, reciprocal `SU(2)`/`SL(2)` auxiliary factors,
  level-III inverse orientation, and the nesting-number bookkeeping.
- The same script now checks BMN scaling, bound-state dispersion, and weak
  coefficient arithmetic relevant to cusp/Bremsstrahlung comparisons.

## External References Used In Current Pass

- Downloaded local study copies under
  `references/planar_n4_integrability/` for convention comparison only:
  Bajnok--Janik `0807.0399`, Arutyunov--Frolov `0901.1417` and `0903.0141`,
  and Arutyunov--Frolov--Suzuki `1002.1711`.
- The monograph text does not import a claim solely by citation.  The
  downloaded sources were used to check convention-sensitive wording about
  ABA, mirror branches, and wrapping assumptions against the stringbook spine.

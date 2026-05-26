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
- The same script checks the Zhukovsky defining equation, large-`u`
  expansion, cut reciprocal boundary values, `x^pm` shortening relation, and
  corrected energy formula.
- It also checks that the stringbook-orientation crossing RHS is not
  invariant under a naive sheet-free `x -> 1/x` substitution.
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

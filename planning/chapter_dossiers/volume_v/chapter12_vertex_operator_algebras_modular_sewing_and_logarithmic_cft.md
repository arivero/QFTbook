# Chapter 12: Vertex Operator Algebras, Modular Sewing, and Logarithmic CFT

## Source Position

This chapter is the first dedicated Volume V algebraic two-dimensional CFT
chapter after the sigma-model, WZW, Narain, orbifold, and twist-field chapter.
It absorbs the non-ghost chiral-algebra and modular-sewing material required
by the stringbook crosswalk while excluding bc and beta-gamma systems from the
current QFT scope.

## Notation Inventory

- `V`: vertex operator algebra.
- `Y(a,z)`: state-field map \(\sum_m a_m z^{-m-1}\).
- `1`: vacuum vector.
- `omega`: conformal vector whose modes are \(L_n\).
- `c`: chiral central charge.
- `M_i`: simple ordinary \(V\)-module.
- `chi_M(tau)`: character \(\operatorname{Tr}_M q^{L_0-c/24}\).
- `CB_{g,n}`: space of chiral conformal blocks.
- `q`: sewing parameter in \(zw=q\).
- `S,T`: genus-one modular matrices.
- `N_{ij}{}^k`: fusion coefficient.
- `d_i`: quantum dimension \(S_{i0}/S_{00}\).
- `M_{ij}`: full-CFT modular-invariant multiplicity matrix.

## Claim Ledger

- Gives a self-contained VOA definition with grading, vacuum, state-field
  map, conformal vector, translation, and locality axioms.
- Derives the chiral OPE expansion from VOA locality and lower truncation.
- Defines ordinary modules, characters, and chiral conformal blocks as Ward
  identity functionals on pointed Riemann surfaces.
- Defines sewing of blocks through dual bases of a module and its dual, with
  the annulus propagation factor \(q^{h_a+n-c/24}\).
- States explicit rationality/sewing hypotheses before invoking modular
  tensor category language.
- States character modularity as a quoted theorem, separating the theorem
  input from the linear-algebraic Verlinde derivation.
- Proves the Verlinde formula from simultaneous diagonalization by the
  modular \(S\)-matrix.
- Works the Ising chiral theory explicitly: \(c=1/2\), three simple modules,
  \(S_{\rm Ising}\), quantum dimensions, and fusion rules.
- Defines rational full-CFT torus partition functions and the modular
  invariance constraints \(MS=SM\), \(MT=TM\).
- Derives the leading Cardy high-temperature partition-function asymptotic
  from modular invariance and a unique vacuum hypothesis.
- Defines logarithmic CFT by nonsemisimple \(L_0\) action, explains the
  appearance of logarithms, and identifies pseudo-traces and finite tensor
  category data as the replacement for semisimple modular data.

## Figure Ledger

- No figures in the initial chapter pass.  Sewing and modular moves are
  currently carried by equations and categorical data.

## Calculation Checks

- `calculation-checks/cft_voa_modular_checks.py` verifies the Ising modular
  \(S\)-matrix, Verlinde fusion coefficients, quantum dimensions, and
  character exponent shifts in \(\mathbb Q(\sqrt2)\).

## Audit Notes

- 2026-05-26 issue #584 pass: added the VOA/modular-sewing/logarithmic-CFT
  chapter, included it in Volume V, and added the Ising modular-data
  calculation check.

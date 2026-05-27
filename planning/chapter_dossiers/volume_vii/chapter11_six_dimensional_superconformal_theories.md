# Chapter 11: Six-Dimensional Superconformal Theories

## Source Position

This chapter follows three-dimensional supersymmetric gauge theories by
introducing supersymmetric QFTs whose fixed points are often specified
through representation data, tensor branches, anomalies, strings, and
compactification tests rather than microscopic Lagrangians.  The current pass
addresses the six-dimensional part of issue #588.

Reviewed source spine:

- `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`,
  lines 14506 onward: six-dimensional `(2,0)` theory, absence of ordinary
  Lagrangian, tensor branch, BPS strings, and compactification to 5D maximally
  supersymmetric Yang-Mills.
- `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`,
  lines 13955-14019: external motivation only.  The monograph definition and
  all logical uses in this chapter are QFT data, not string-theoretic
  constructions.
- GitHub issue #588: request for six-dimensional `(2,0)` theory data and
  compactification/normalization boundaries.

## Notation Inventory

- `Spin(1,5)`: six-dimensional Lorentz spin group.
- `G_R`: R-symmetry group, either `SU(2)_R` or `USp(4)_R` in the chapter.
- `OSp(8^*|2)`, `OSp(8^*|4)`: six-dimensional superconformal algebras for
  `(1,0)` and `(2,0)`.
- `phi^I`, `phi`: tensor-branch scalar coordinates.
- `B^I`, `H^I`: two-form gauge potentials and self-dual field strengths.
- `mathfrak g`, `mathfrak t_g`, `W_g`: simply laced Lie algebra, Cartan
  algebra, and Weyl group of a `(2,0)` theory.
- `I_8`, `I_8(1)`: interacting and free-tensor anomaly polynomials.
- `N_R`: rank-five `SO(5)_R` background bundle for `(2,0)` anomalies.
- `Omega^{IJ}`, `X_I^{(4)}`: tensor pairing and Green-Schwarz four-forms.
- `q`, `alpha`: BPS string charge vector and root-lattice charge.
- `g_5`, `R`: five-dimensional trace-delta Yang-Mills coupling and circle
  radius.

## Claim Ledger

- Separates six-dimensional superconformal representation data from
  branch-EFT field variables.
- Proves that a six-dimensional Yang-Mills coupling has negative mass
  dimension and therefore is not a marginal conformal coordinate.
- Defines `(1,0)` and `(2,0)` tensor multiplet variables while marking
  self-dual field actions as formulation-dependent.
- Defines tensor-branch coordinates and Green-Schwarz couplings.
- Gives the `(2,0)` tensor-branch quotient
  `(R^5 tensor t_g)/W_g`, with the type `A_{N-1}` chart as an example.
- States anomaly matching as an equality involving `I_8` and quadratic
  Green-Schwarz terms.
- Records the `(2,0)` anomaly polynomial as a quoted theorem, with all
  coefficients and characteristic classes named.
- Defines BPS string charges, tensions, and inflow data, including
  root-lattice strings for `(2,0)` theories.
- Proves the trace-delta compactification normalization
  `g_5^2 = 4 pi^2 R` from the BPST instanton mass and KK momentum.
- Records compactification on Riemann surfaces as a test requiring twist,
  defect, anomaly, and descendant data.

## Calculation Checks

- `calculation-checks/susy_abjm_6d_checks.py` verifies the six-dimensional
  Yang-Mills coupling dimension, type `A_{N-1}` `(2,0)` rank/dimension/anomaly
  coefficient arithmetic, tensor-branch dimension, and the trace-delta
  five-dimensional instanton/Kaluza-Klein normalization.

## Proof Obligations And Boundaries

- The interacting `(2,0)` theory remains a non-Lagrangian object; the chapter
  gives protected and effective data, not a construction.
- The `(2,0)` anomaly polynomial is quoted theorem status because a
  first-principles construction of the interacting six-dimensional local QFT
  and its anomaly functional is not reproduced here.  External geometric or
  string-theoretic arguments can motivate the formula but are not used as
  foundations.
- Compactification to 5D maximally supersymmetric Yang-Mills is treated as a
  protected test/effective description, not as a definition of the parent
  six-dimensional local QFT.
- Future passes should add a fuller self-dual-field formalism, line/surface
  defect categories, anomaly descent calculations for string worldsheets, and
  class-`S` anomaly reductions.

## Figure Ledger

No figure is included in this pass.  Future figures should show a tensor
branch cone, root-lattice BPS string walls, and compactification maps to
lower-dimensional protected data.

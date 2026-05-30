# Volume IV Chapter 03 — Algebraic QFT, Local Nets, and States

## Source Position

This chapter builds the operator-algebraic presentation of a QFT after the
Wightman and OS reconstruction chapters.  It introduces local \(C^*\)- and
von Neumann nets, perturbative algebraic QFT as a formal local-net
construction, states and the GNS representation, vacuum represented nets,
Haag duality, the precise Wightman-to-net bridge, interacting constructive
local-net examples, Reeh--Schlieder cyclicity, and locally covariant
functorial QFT.

## Notation Inventory

- `\mathcal A(\mathcal O)`: local \(C^*\)-algebra attached to a spacetime
  region \(\mathcal O\).
- `\mathcal R(\mathcal O)`: represented local von Neumann algebra.
- `\omega`: state on a \(C^*\)-algebra.
- `(\Hilb_\omega,\pi_\omega,\Omega_\omega)`: GNS Hilbert space,
  representation, and cyclic vector.
- `\Omega`, `\vac`: vacuum vector in a represented net.
- `U`: unitary implementation of spacetime symmetries.
- `\Phi_\alpha(f)`: Wightman smeared fields used as unbounded local
  coordinates.
- `E_{\overline{\Phi(f)}}(\Delta)`: spectral projection of the self-adjoint
  closure of a real smeared field.
- `\mathcal F_P(\mathcal O)`: constructive \(P(\phi)_2\) local field net.
- `\mathcal R_P(\mathcal O)=\mathcal F_P(\mathcal O)^\Gamma`: fixed-point
  observable net for a finite internal symmetry group \(\Gamma\).
- `\Theta_{\beta,\mathcal O}`: energy-damped local phase-space map
  \(A\mapsto e^{-\beta H}A\Omega\).
- `\Loc`, `\Alg`: source and target categories for locally covariant QFT.

## Claim Ledger

- Defines Haag--Kastler \(C^*\)-nets and represented vacuum nets with isotony,
  covariance, locality, spectrum, and vacuum-state data kept distinct.
- Constructs the perturbative interacting local net from relative
  \(S\)-matrices under the causal-factorization and interaction-cutoff
  independence hypotheses.
- Proves the GNS construction, including the null quotient, representation,
  cyclic vector, and uniqueness.
- Proves unitary implementation of an invariant state by the GNS universal
  property.
- Defines Haag duality and operator affiliation without identifying unbounded
  fields with bounded local observables.
- Proves the conditional Wightman-to-net theorem: spectral projections of
  self-adjoint closures generate a represented local net only when strong
  locality of closures is available.
- Adds Lemma `lem:analytic-vector-strong-locality`, proving that joint entire
  analytic-vector estimates plus domain commutativity imply strong
  commutation of self-adjoint closures.
- Expands the massive \(P(\phi)_2\) checkpoint into a model-specific AQFT
  verification route: OS reconstruction gives fields and the Hilbert space;
  essential self-adjointness and analytic-vector bounds give bounded local
  algebras; strong commutation gives locality; finite internal fixed points
  give observables; nuclearity, split inclusions, Haag duality, and DHR
  reconstruction require separate estimates or category constructions.
- Proves the Reeh--Schlieder theorem for a weakly additive vacuum net from
  the spectral condition, translated analyticity, weak additivity, and vacuum
  cyclicity.
- Defines the locally covariant \(C^*\)-algebraic QFT functor and separates
  functorial covariance from the existence problem for a concrete model.

## Figure Ledger

- `fig:aqft-local-net`: categorical/local-net assignment of regions,
  inclusions, spacelike commutation, and symmetry covariance.
- `fig:gns-representation`: state-to-GNS construction showing null quotient,
  cyclic vector, representation, and expectation recovery.
- `fig:reeh-schlieder-cyclicity`: local algebra action on the vacuum and its
  dense Hilbert-space orbit under the spectral/weak-additivity hypotheses.

## Calculation Checks

- No numerical calculation script is attached to this chapter.  Verification
  is by LaTeX build, proof-substance audit, figure audit, and local
  theorem-boundary review.

## Audit Notes

- 2026-05-28 proof-substance audit: retained the Wightman-to-AQFT theorem
  only in its conditional form; the statement requires essential
  self-adjointness and strong commutativity of closures rather than claiming a
  general Wightman-to-net theorem.
- 2026-05-30 constructive AQFT example pass: added the analytic-vector
  strong-locality lemma and expanded the massive \(P(\phi)_2\) checkpoint so
  the example distinguishes OS/Wightman reconstruction, spectral-projection
  net construction, internal fixed-point observables, phase sectors, and the
  separate estimates needed for nuclearity, split, Haag duality, and DHR
  reconstruction.

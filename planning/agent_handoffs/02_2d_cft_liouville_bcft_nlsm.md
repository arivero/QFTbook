# Agent Handoff: 2D CFT, Liouville, BCFT, Sigma Models, Orbifolds

## Primary Scope

Issues: #600, #601, #602, plus the CFT items in #606.
Main files:

- `monograph/tex/volumes/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.tex`
- `monograph/tex/volumes/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`
- possible new Volume V chapter files if the existing chapters become too
  large, with corresponding updates to `volume_v_current.tex`;
- `planning/chapter_dossiers/volume_v/*.md`;
- relevant CFT calculation checks.

## Objective

Develop Volume V into a serious 2D CFT volume rather than a collection of
thin topics.  This lane should handle Liouville CFT, BCFT, NLSM
renormalization/T-duality, orbifolds and twist fields, VOA/conformal-net
relations, and logarithmic CFT status in a way consistent with the
monograph's foundational-rebuild standard.

## Non-Negotiable Exclusions

- Do not add black-hole entropy applications.
- Do not add Hartman-Keller-Stoica material.
- Do not add Saad-Shenker-Stanford or JT-gravity/matrix-model material.
- The Cardy formula may appear only as a CFT-internal theorem about modular
  covariance and asymptotic density of states, not as a black-hole bridge.

## Required Development Targets

### Liouville CFT

1. Define the classical Liouville action, background metric, curvature term,
   stress tensor, and classical equation of motion.
2. Derive the central charge formula \(c=1+6Q^2\) within the chosen
   normalization, including the improvement term.
3. Define exponential vertex operators, the Seiberg bound, reflection
   relation, and the domain of probabilistic construction.
4. Develop Gaussian multiplicative chaos enough to state precisely what
   measure-theoretic object Liouville path integration means.
5. State the DOZZ formula with all special functions defined and convention
   checks supplied.  If proof is not reproduced, use `quotedtheorem` and
   record the exact proof boundary.
6. Derive BPZ equations for degenerate insertions and show how recursion
   constrains correlators.
7. State the higher-genus and K-S functorial closure status precisely; do not
   imply more than is known.

### Boundary CFT

1. Define a BCFT as a CFT on bordered Riemann surfaces with boundary
   conditions, Hilbert spaces on intervals/circles, and sewing constraints.
2. Derive Ishibashi states from representation-theoretic gluing conditions.
3. Derive Cardy states and the annulus consistency condition, including the
   modular S transform and open-channel spectrum.
4. Work out free boson Neumann/Dirichlet boundary conditions and zero-mode
   treatment.
5. Work out Majorana/Ising boundary conditions and NS/R sector bookkeeping.
6. State Cardy-Lewellen sewing constraints and what is known/proved.

### NLSM, Orbifolds, Twist Fields

1. Define the 2D NLSM path integral with target data
   \((M,G,B,\Phi)\), including worldsheet topology and regulator status.
2. Derive one-loop beta functions with clear convention choices.
3. Develop Buscher T-duality rules by gauging an isometry and integrating out
   fields:
   \(G'_{00}\), \(G'_{0i}\), \(B'_{0i}\), \(G'_{ij}\), \(B'_{ij}\), and
   dilaton shift.
4. Discuss order-by-order preservation of beta functions as a formal
   perturbative statement, not a nonperturbative theorem.
5. Define orbifold sectors, twisted Hilbert spaces, projection, and modular
   covariance.
6. Derive twist-field conformal weights in free examples.
7. Develop twist-field deformations as local operators, with OPE and
   marginality status stated carefully.

### VOA / Conformal Nets

1. Strengthen the VOA definitions with module categories, Zhu algebra,
   characters, modular transformations, and fusion rules.
2. Add conformal-net definitions if feasible: intervals, von Neumann
   algebras, isotony, locality, covariance, vacuum, split property/status.
3. State the VOA/conformal-net equivalence status for suitable rational
   theories as `quotedtheorem` unless proved.

## Calculation Checks

Add or extend checks for:

- modular S matrices and Verlinde fusion in minimal/Ising examples;
- twist-field weights for cyclic orbifolds;
- Buscher-rule algebra in a finite symbolic example;
- BPZ null-vector coefficient arithmetic;
- Liouville special-function shift relations if tractable.

## Completion Standard

Do not close #600, #601, or #602 unless the corresponding material is
chapter-level, with definitions, derivations, examples, dossier updates,
calculation checks where relevant, and a clean build.  Partial work should
leave the issues open and comment with exact remaining obligations.

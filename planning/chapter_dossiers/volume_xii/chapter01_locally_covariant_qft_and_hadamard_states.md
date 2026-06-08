# Volume XII, Chapter 1 Dossier: Locally Covariant QFT And Hadamard States

## Logical Role

- Role in the monograph: after the microlocal spectrum-condition foundation,
  give the functorial curved-spacetime framework, the free Klein--Gordon
  model, and the Hadamard state class used by point splitting and
  perturbative AQFT.
- Printed predecessor: microlocal spectrum condition and Hadamard geometry.
- Printed successor: perturbative algebraic QFT on curved backgrounds.
- Downstream consumers: point-split stress tensors, trace anomalies, Unruh
  effect, Hawking effect, cosmological particle creation, and semiclassical
  backreaction.

## Definitions And Results

- Defines globally hyperbolic spacetime, causal future/past, causally convex
  open subset, the background category `Loc`, and Cauchy morphisms.
- Adds a Volume XII control-level matrix separating fixed-background free
  theory, perturbative interacting theory, conditional semiclassical theory,
  and nonperturbative interacting curved QFT, with the input data and
  controlled outputs for each level.
- Adds the explicit claim-control spine for the volume: free locally
  covariant/Hadamard statements, point-split stress-tensor and anomaly
  statements, fixed-background thermal/Hawking/cosmological claims,
  perturbative interacting pAQFT fields, interacting composite stress
  tensors, conditional semiclassical Einstein--Langevin statements, and
  nonperturbative interacting curved-QFT claims are separated by control level
  and by the missing physical inputs required to strengthen them.
- Defines a locally covariant QFT as a functor
  `A : Loc -> Alg_*` with injective algebra morphisms, Einstein causality,
  and the time-slice axiom.
- Defines kinematic local algebras
  `A^kin(M;O)=A(iota_{M;O})(A(O))` and proves isotony plus Einstein
  causality for the induced net.
- Defines locally covariant fields as natural transformations from compactly
  supported test-section functors to the algebra functor.
- Defines locally covariant state spaces as contravariant families of states.
- Constructs the free Klein--Gordon functor:
  `P_M=-nabla^mu nabla_mu+m^2+xi R`, retarded/advanced Green operators,
  causal propagator `E_M`, quotient
  `V(M)=C_c^\infty(M)/P_M C_c^\infty(M)`, symplectic form
  `sigma_M([f],[h])=int f E_M h`, and the CCR algebra.
- Proves the causal-propagator kernel identity
  `ker E_M = P_M C_c^\infty(M)`.
- Proves functoriality under causally convex isometric embeddings using the
  restriction identities
  \(\chi^*E_N^{\rm ret/adv}\chi_*=E_M^{\rm ret/adv}\), not a global
  zero-extension identity, and proves the time-slice property for Cauchy
  morphisms by an explicit cutoff between Cauchy surfaces.
- Defines quasifree states, their two-point distributions, positivity,
  equation of motion, and CCR antisymmetric part.
- Defines the local four-dimensional Hadamard parametrix, including Synge's
  world function, the \(i\epsilon\) boundary prescription, \(U=\Delta^{1/2}\),
  and the recursively determined \(V\)-coefficient.
- Proves that the difference of two Hadamard two-point functions for the
  same Klein--Gordon operator is smooth by combining local parametrix
  cancellation near the diagonal with the local-to-global
  propagation-of-singularities theorem.
- Connects the local Hadamard form to the microlocal Hadamard wavefront set,
  Wick square subtraction, and the local curvature freedom of the stress
  tensor.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \({\bf Loc}\) | category of oriented, time-oriented globally hyperbolic backgrounds |
| \(J_M^\pm(S)\) | causal future/past of \(S\subset M\) |
| \(\chi:M\to N\) | admissible causally convex isometric embedding |
| \(\mathfrak A\) | locally covariant algebra functor |
| \(\mathfrak A^{\rm kin}(M;O)\) | kinematic algebra of \(O\) inside \(M\) |
| \(P_M\) | curved Klein--Gordon operator |
| \(E_M^{\rm ret},E_M^{\rm adv}\) | retarded and advanced Green operators |
| \(E_M\) | causal propagator |
| \(\mathcal V(M)\) | equation-of-motion quotient of compactly supported test functions |
| \(\sigma_M\) | causal-propagator symplectic form |
| \(\omega_2\) | two-point distribution of a quasifree state |
| \(\sigma(x,y)\) | Synge world function |
| \(H_{\epsilon,\mu}\) | local Hadamard singular distribution |
| \(U,V,W_\omega\) | Hadamard geometric coefficients and smooth state-dependent part |
| claim-control spine | volume-level classification of theorem, perturbative construction, conditional semiclassical framework, and open nonperturbative boundary |

## Claim Ledger

1. The category `Loc` is closed under composition because causal convexity
   is stable under composition of admissible embeddings.
2. A locally covariant theory induces an isotone Einstein-causal net on each
   fixed background.
3. The free scalar CCR algebra depends on compactly supported test functions
   only through the quotient by the equation of motion.
4. The causal-propagator pairing descends to a nondegenerate symplectic form
   on the quotient.
5. Causally convex embeddings preserve the causal propagator after
   restriction to the embedded spacetime:
   \(\chi^*E_N^{\rm ret/adv}\chi_*=E_M^{\rm ret/adv}\).  The global target
   Green solution need not equal the zero extension of the source solution.
6. Cauchy morphisms induce isomorphisms because every compactly supported
   source is equivalent in the quotient to one supported in the Cauchy image.
7. Hadamard states have a state-independent singular part near the diagonal;
   global smoothness of differences of Hadamard two-point functions uses the
   bisolution property and the local-to-global Hadamard theorem.
8. Wick powers and the stress tensor require a locally covariant subtraction
   and retain finite local curvature-coordinate freedom.
9. The volume's curved-spacetime claims are organized by control level: free
   fixed-background, perturbative interacting, conditional semiclassical, and
   nonperturbative/open.  Crossing levels requires additional hypotheses.
10. The claim-control matrix makes the cross-chapter spine explicit: fixed
    background thermal or particle-creation statements do not imply
    interacting horizon results, pAQFT order-by-order constructions now use
    local/equicausal functional-space closure rather than unrestricted
    microcausal functionals, they do not provide nonperturbative state spaces,
    and finite response/noise checks become backreaction evidence only after
    the state, stress tensor, response, stability, and EFT-reduction data are
    fixed together.

## Calculation Checks

- `calculation-checks/locally_covariant_kg_checks.py` verifies the finite
  quotient algebra behind the CCR construction: descent of the
  causal-propagator form, vanishing of equation-of-motion generators,
  symplectic preservation under embeddings, restriction-versus-zero-extension
  functoriality, the Minkowski-diamond retarded-support negative control, the
  quotient distinction between Cauchy and non-Cauchy embeddings, and the
  diagonal-neighborhood product-cover negative control.

## Remaining Deepening Targets

- Add an explicit ultrastatic example connecting the Hadamard condition to a
  spectral decomposition of the spatial elliptic operator.
- Develop spinor and gauge-field Hadamard structures after the background
  gauge-field and index-theory chapters have been expanded.
- Later compare the locally covariant state-space definition with concrete
  constructive examples on static curved backgrounds.

## Figures

- Naturality square for locally covariant fields is included in the chapter.
- Future figures should include a causal-convex embedding diagram and a
  point-splitting diagram in a convex normal neighborhood.

## Anti-Wrapper Audit

- 2026-06-04: added the Volume XII control-level matrix for issue #729.  This
  is architectural claim-control content: it tells the reader which data
  support free, perturbative interacting, conditional semiclassical, and
  nonperturbative claims, and prevents formal adjacent chapters from being
  read as one continuous theorem chain.
- 2026-06-04: upgraded the control-level prose to an explicit claim-control
  spine with point-of-use curved-spacetime references.  The matrix separates
  the strong fixed-background and pAQFT claims from conditional
  semiclassical/backreaction claims and from genuinely open nonperturbative
  interacting curved-QFT statements.
- 2026-06-08 issue #729 printed-order pass: changed the dossier role from
  opening the volume to following the microlocal foundation, and changed the
  TeX cross-reference range to named chapter references.  The chapter remains
  the locally covariant free-field/Hadamard model; it no longer has to carry
  the wavefront-set foundation by abbreviation.
- 2026-06-08 issue #854 functional-space pass: updated the claim-control row
  for perturbative interacting fields so it no longer says the construction is
  based on unrestricted microcausal functionals.  Microcausality is recorded
  as the pairing test; equicausal or explicit polynomial/local domains carry
  the Peierls/star/time-slice closure claim.
- 2026-06-08 issue #902 pass: corrected two globalization errors by replacing
  the false causal-propagator zero-extension identity with the restriction
  identity used by the symplectic pairing and injectivity proof, and by
  replacing the diagonal-neighborhood Hadamard smoothness argument with an
  explicit local-to-global propagation-of-singularities theorem boundary.

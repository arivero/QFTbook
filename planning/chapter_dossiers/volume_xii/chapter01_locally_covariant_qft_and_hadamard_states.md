# Volume XII, Chapter 1 Dossier: Locally Covariant QFT And Hadamard States

## Logical Role

- Role in the monograph: open the curved-spacetime and background-field
  volume with precise functorial foundations, the free Klein--Gordon model,
  and the Hadamard state class used by point splitting and perturbative AQFT.
- Immediate predecessor: flat-spacetime local QFT, algebraic nets, stress
  tensors, anomalies, and thermal KMS theory.
- Immediate successor: point-split stress tensor, trace anomalies, Unruh
  effect, Hawking effect, microlocal spectrum condition, and perturbative
  algebraic QFT on curved backgrounds.

## Definitions And Results

- Defines globally hyperbolic spacetime, causal future/past, causally convex
  open subset, the background category `Loc`, and Cauchy morphisms.
- Adds a Volume XII control-level matrix separating fixed-background free
  theory, perturbative interacting theory, conditional semiclassical theory,
  and nonperturbative interacting curved QFT, with the input data and
  controlled outputs for each level.
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
- Proves functoriality under causally convex isometric embeddings and proves
  the time-slice property for Cauchy morphisms by an explicit cutoff between
  Cauchy surfaces.
- Defines quasifree states, their two-point distributions, positivity,
  equation of motion, and CCR antisymmetric part.
- Defines the local four-dimensional Hadamard parametrix, including Synge's
  world function, the \(i\epsilon\) boundary prescription, \(U=\Delta^{1/2}\),
  and the recursively determined \(V\)-coefficient.
- Proves that the difference of two Hadamard two-point functions for the
  same Klein--Gordon operator is smooth.
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

## Claim Ledger

1. The category `Loc` is closed under composition because causal convexity
   is stable under composition of admissible embeddings.
2. A locally covariant theory induces an isotone Einstein-causal net on each
   fixed background.
3. The free scalar CCR algebra depends on compactly supported test functions
   only through the quotient by the equation of motion.
4. The causal-propagator pairing descends to a nondegenerate symplectic form
   on the quotient.
5. Causally convex embeddings preserve the causal propagator and hence the
   CCR commutator.
6. Cauchy morphisms induce isomorphisms because every compactly supported
   source is equivalent in the quotient to one supported in the Cauchy image.
7. Hadamard states have a state-independent singular part; differences of
   Hadamard two-point functions are smooth.
8. Wick powers and the stress tensor require a locally covariant subtraction
   and retain finite local curvature-coordinate freedom.
9. The volume's curved-spacetime claims are organized by control level: free
   fixed-background, perturbative interacting, conditional semiclassical, and
   nonperturbative/open.  Crossing levels requires additional hypotheses.

## Calculation Checks

- `calculation-checks/locally_covariant_kg_checks.py` verifies the finite
  quotient algebra behind the CCR construction: descent of the
  causal-propagator form, vanishing of equation-of-motion generators,
  symplectic preservation under embeddings, and the quotient distinction
  between Cauchy and non-Cauchy embeddings.

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
  is architectural theorem-status content: it tells the reader which data
  support free, perturbative interacting, conditional semiclassical, and
  nonperturbative claims, and prevents formal adjacent chapters from being
  read as one continuous theorem chain.

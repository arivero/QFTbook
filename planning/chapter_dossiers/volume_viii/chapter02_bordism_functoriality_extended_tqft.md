# Volume VIII, Chapter 2 Dossier: Bordism Functoriality And Extended TQFT
Source-File: monograph/tex/volumes/volume_viii/chapter02_bordism_functoriality_extended_tqft.tex

## Logical Role

- Role in the monograph: state the functorial target of topological field
  theory after the cohomological metric-independence mechanism, with one
  completely worked ordinary example rather than only abstract packaging.
- Immediate predecessor: metric variation and \(Q\)-cohomological observables.
- Immediate successor: BF theory, Chern--Simons theory, cohomological gauge
  theory, and twists.

## Definitions And Results

- Tangential structure as a map \(\theta_\xi:B_\xi\to BO(D)\) and
  stabilized lower-stratum \(\xi\)-structures.
- Collared \(\xi\)-bordisms, collar gluing, identity cylinders, and disjoint
  union as symmetric monoidal product.
- Symmetric monoidal Atiyah--Segal TQFT functor.
- Honest versus relative/anomalous functorial theories.
- State spaces from closed \((D-1)\)-manifolds and numbers from closed
  \(D\)-manifolds.
- Pairing from evaluation bordism; proposition that finite-dimensional honest
  TQFTs assign dual vector spaces to reversed hypersurfaces.
- Complete ordinary \(2D\) theorem: finite-dimensional oriented TQFTs are
  equivalent to finite-dimensional commutative Frobenius algebras.
- Explicit Frobenius tensor \(C=\sum_i e_i\otimes e^i\),
  comultiplication \(\Delta(a)=\sum_i e_i\otimes e^ia\), cylinder identity,
  neck-exchange/Frobenius identity, and genus-\(g\) semisimple partition
  function.
- Extended TQFT as a higher functor from an extended bordism category.
- Cobordism hypothesis through fully \(D\)-dualizable objects: duals,
  adjoints for evaluation/coevaluation, and iterated adjoints through level
  \(D\), recorded as an external classification boundary rather than a local
  theorem.
- Defines the finite-dimensional Morita \(2\)-category and proves that a
  finite-dimensional separable algebra is fully \(2\)-dualizable there, using
  the separability idempotent to split \(A^e\to A\).
- Semisimple Morita example: \(A=\Bbbk^r\), separability element
  \(\sum_\alpha p_\alpha\otimes p_\alpha\), Calabi-Yau trace
  \(\epsilon(p_\alpha)=\lambda_\alpha\), and \(HH_0(A)=A\).
- Functorial extraction criterion from regulated local QFT amplitudes.
- Extraction problem from local QFT protected sectors.
- Witten--Donaldson theory as a four-dimensional cohomological gauge-theory
  test case.
- Donaldson/Seiberg--Witten comparison as an RG comparison between the twisted
  non-Abelian \(\mathcal N=2\) theory and the Abelian monopole effective
  theory, with explicit gap ledger.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\xi\) | tangential structure |
| \(\operatorname{Bord}_D^\xi\) | \(D\)-dimensional bordism category |
| \(Z\) | topological field theory functor |
| \(\Sigma\) | closed spatial \((D-1)\)-manifold |
| \(M:\Sigma_{\rm in}\to\Sigma_{\rm out}\) | bordism |
| \(\mathcal L\) | invertible anomaly theory/anomaly-line system |
| \(A\) | commutative Frobenius algebra, often \(Z(S^1)\) |
| \(\epsilon\) | Frobenius trace/counit |
| \(\eta(a,b)\) | Frobenius pairing \(\epsilon(ab)\) |
| \(C\) | inverse pairing tensor \(\sum_i e_i\otimes e^i\) |
| \(\Delta\) | comultiplication adjoint to multiplication |
| \(E\) | Euler/handle element \(m\Delta(1_A)\) |
| \(\mathcal C\) | higher-categorical target for extended theories |
| \(X\) | fully \(D\)-dualizable object classifying a framed extended TQFT |
| \(A^e\) | enveloping algebra \(A\otimes A^{\rm op}\) |
| \(e=\sum_r x_r\otimes y_r\) | separability idempotent |
| \(HH_0(A)\) | Hochschild trace \(A/[A,A]\), the circle value in Morita \(2D\) examples |
| \(u\) | Coulomb-branch Wilsonian coordinate in the Seiberg--Witten comparison |
| \(\tau(u)\) | low-energy Abelian gauge coupling coordinate |

## Claim Ledger

1. Functorial TQFT requires collar-gluing laws beyond metric-independent
   correlation functions.
2. Reversal of a hypersurface gives the dual state space in any honest
   finite-dimensional TQFT; the proof is the cap/cup zig-zag identity.
3. Reflection positivity/unitarity is extra structure on the functor.
4. The \(2D\) oriented case is not merely illustrative: the full gluing law is
   exactly the commutative Frobenius algebra identities, including the
   cylinder inverse-pairing identity and Frobenius neck exchange.
5. Extended theories assign data to lower-dimensional strata and require a
   higher-categorical target.
6. The cobordism hypothesis is an external classification boundary; the
   chapter locally proves the finite Morita \(2\)-dualizability mechanism used
   by the semisimple example.
7. A local QFT gives a TQFT only after state-space limits, metric-choice
   independence/anomaly-line data, gluing convergence, and cylinder/tensor
   laws are proved.
8. The Donaldson/Seiberg--Witten relation is an RG comparison problem whose
   current mathematical status must be separated into differential-geometric
   moduli-space theorems, finite-dimensional localization or gluing inputs, and
   still-unproved QFT RG statements.

## Anti-Wrapper Audit

- 2026-05-29 ninth pass: retained the cap/cup state-space duality proposition
  because it is a structural consequence of the Atiyah-Segal gluing law, but
  expanded the proof from the phrase "triangular identities" to the explicit
  finite-dimensional maps \(W\otimes V\to\Bbbk\), \(1\mapsto c\in V\otimes W\),
  injectivity arguments, dimension comparison, and inverse-tensor conclusion.
- 2026-05-30 anti-wrapper pass: demoted the former "Cylinder and Frobenius
  identities" lemma to a calculation paragraph.  The cylinder and neck
  equations remain labelled because they are used in the \(2D\)
  TQFT/Frobenius classification proof, but the dual-basis verification is now
  presented as supporting algebra rather than as a standalone theorem-family
  result.
- 2026-05-30 cobordism-boundary pass: removed the cobordism-hypothesis
  `quotedtheorem` wrapper, retained the fully extended classification theorem
  as an external boundary, and proved the finite-dimensional Morita
  two-dualizability statement for separable algebras that the chapter actually
  uses.

## Figures

- Collar-gluing diagram for \(M_{12}\circ M_{01}\).
- Frobenius generator diagram showing pair of pants, cap/cup tensor, and
  comultiplication.

## Calculation Checks

- `calculation-checks/tqft_frobenius_gluing_checks.py` verifies the
  semisimple Frobenius algebra formulas with exact rational arithmetic:
  cylinder identity, neck-exchange identity, associativity/commutativity, and
  \(\Sigma_g\) partition function; it also checks the semisimple
  separability idempotent, the splitting of \(A^e\to A\), and
  \(HH_0(\Bbbk^r)=\Bbbk^r\).

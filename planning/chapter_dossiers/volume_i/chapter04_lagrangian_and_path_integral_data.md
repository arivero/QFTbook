# Volume I, Chapter 4 Dossier: Hamiltonian Evolution And Time-Sliced Path Integrals

## Status

Current status: source-certified against handwritten 253a pp. 10--14 after
the 2026-05-22 derivation and figure pass; tightened on 2026-05-23 so the
position/momentum kernels explicitly use the rigged-Hilbert-space convention
and the continuum path-integral symbol is tied to finite regulators; tightened
again on 2026-05-24 for GitHub issue #298 by adding the Wiener-measure and
Feynman--Kac existence theorem for Euclidean Schrödinger quantum mechanics,
with an explicit warning that Borel measures are not a general foundation for
fermionic, gauge, theta-angle, or perturbative QFT path integrals.
Formalization upgraded on 2026-05-27 for issue #615.  Upgraded again on
2026-06-04 for issue #813 by adding intrinsic Hermitian matrix quantum
mechanics, radial/Vandermonde fermionization, non-singlet sectors, and the
large-`N` collective-field coordinate, while keeping `c=1` string
interpretations as comparison boundaries.

## Logical Role

This chapter introduces the path integral in ordinary finite-dimensional
quantum mechanics as a regulated construction of transition amplitudes and
time-ordered Green functions. It prepares the later field-theoretic path
integral without using scattering language.

## Framework

Working framework:

- finite-dimensional configuration space \(\mathcal Q=\mathbb R^d\), with
  later remarks on curved configuration spaces;
- classical configuration manifold \(Q\), tangent data \((q,\dot q)\), and
  cotangent data \((q,p)\);
- regular Legendre transform between \(L:TQ\to\mathbb R\) and \(H:T^*Q\to
  \mathbb R\);
- Hilbert space \(L^2(\mathcal Q,\dd^dq)\);
- canonical coordinate and momentum operators;
- self-adjoint Hamiltonian \(\widehat H\);
- unitary time-evolution group \(U(T)=\exp(-\ii T\widehat H/\hbar)\);
- Hermitian matrix configuration spaces `Herm_N`, their flat Lebesgue measure,
  global or gauged `U(N)` action, and singlet/Gauss-law projection;
- eigenvalue-angle coordinates on the regular matrix locus, the
  Vandermonde measure, collision hyperplanes, radial Laplacian, and the
  unitary map from singlet wavefunctions to antisymmetric eigenvalue
  wavefunctions;
- large-`N` eigenvalue density and Fermi-surface collective-field
  coordinates as a controlled hydrodynamic approximation to the singlet
  fermion system;
- generalized position and momentum eigenstates used as a distributional
  resolution of identity in
  \(\mathcal S(\mathbb R^d)\subset L^2(\mathbb R^d)\subset\mathcal S'(\mathbb R^d)\);
- finite time partition \(0=t_0<t_1<\cdots<t_N=T\);
- finite-dimensional phase-space integrals at fixed \(N\).

## Primary Source Anchors

- `transcription/tex/253a/foundations.tex`, Lagrangian formalism and
  time-evolution/path-integral measure.
- `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`, section
  "The path integral", subsection "Path integral formulation of quantum
  mechanics", including the trace boundary-condition check.
- `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`,
  lines `24414--24663`, used as source intake for one-matrix quantum
  mechanics, Vandermonde fermionization, collective fields, and non-singlet
  sectors; string-duality interpretations were not imported as proof.

## External Reference Needs

- Trotter product formula and oscillatory-integral convergence references for
  future mathematical interludes.
- Feynman--Kac/Wiener-measure references for further sharpening of the
  Euclidean Schrödinger theorem; the chapter now contains the theorem and its
  proof infrastructure at the level needed for the monograph.

## Notation Inventory

| Symbol | Type | Framework |
| --- | --- | --- |
| \(d\) | number of quantum-mechanical degrees of freedom | finite-dimensional QM |
| \(Q\) | smooth classical configuration manifold | classical mechanics |
| \(\mathcal Q\) | configuration space, initially \(\mathbb R^d\) | QM |
| \(q^a,p_a\) | canonical coordinates and momenta | phase space |
| \(L,S,H\) | Lagrangian, action, and Hamiltonian | classical mechanics and path integral |
| \(\{\cdot,\cdot\}_{\rm P}\) | canonical Poisson bracket on \(T^*Q\) | Hamiltonian mechanics |
| \(\widehat q^a,\widehat p_a\) | coordinate and momentum operators | Hilbert space |
| \(\widehat H\) | self-adjoint Hamiltonian | time evolution |
| \(h(q,p)\) | chosen symbol of \(\widehat H\) in a specified ordering | time slicing |
| \(h'(q,p)\) | alternative ordering symbol for the same operator | time slicing |
| \(\epsilon\) | time step \(T/N\) | regulator |
| \(K_N\) | finite-\(N\) regulated phase-space integral | path integral |
| \(S_N\) | discrete phase-space action | regulator |
| \(G_{ab}(q)\) | positive-definite configuration-space metric | Lagrangian form |
| \(J(t)\) | external source | generating functional |
| \(\beta_{\mathrm T}\) | Euclidean inverse temperature in trace kernels | thermal trace |
| \(\mathcal S\subset L^2\subset\mathcal S'\) | Gelfand triple | position/momentum kernels |
| \(\mathbb W_x^\tau\) | Wiener probability measure | Feynman--Kac representation |
| \(\mathbb W_{x,y}^\tau\) | Brownian-bridge measure | fixed endpoints |
| \(k_s^0(x,y)\) | heat kernel with diffusion \(\hbar/m\) | Wiener distributions |
| \(\Herm_N\) | real vector space of \(N\times N\) Hermitian matrices | matrix QM |
| \(X,P\) | Hermitian matrix coordinate and conjugate momentum | matrix QM |
| \(\Delta(\lambda)\) | Vandermonde determinant \(\prod_{i<j}(\lambda_i-\lambda_j)\) | eigenvalue coordinates |
| \(\Hilb_N^{\rm sing}\) | `U(N)`-invariant/gauged singlet matrix Hilbert space | matrix QM |
| \(\rho(x)\) | eigenvalue density \(\sum_i\delta(x-\lambda_i)\) | large-`N` matrix QM |
| \(p_\pm(x)\) | upper/lower Fermi-surface branches | collective field |
| \(v(x)\) | hydrodynamic velocity \((p_++p_-)/2\) | collective field |

## Definition Ledger

- `def:regular-classical-lagrangian-datum`: regular Legendre transform from
  classical Lagrangian to Hamiltonian data.
- `def:schrodinger-representation-datum`: canonical Schrödinger Hilbert-space
  representation and self-adjoint Hamiltonian time evolution.
- `def:position-momentum-rigging-kernel-notation`: weak position/momentum
  resolutions of identity with the \(\hbar\)-Fourier normalization.
- Paragraph `par:finite-phase-space-time-sliced-kernel`: finite time-sliced
  phase-space construction and discrete phase-space action, recorded as a
  regulated insertion calculation rather than proposition-level content.
- `qthm:trotter-product-formula-qm`: local theorem-level operator Trotter
  formula used to interpret continuum limits, now with explicit real-time
  essential-self-adjoint-sum hypotheses, Euclidean closed-form-sum hypotheses,
  and the bounded norm plus unbounded closed-form/resolvent proof mechanisms.
- `def:kato-schrodinger-euclidean-datum`: Kato/local Kato hypotheses and
  Friedrichs Schrödinger Hamiltonian.
- `thm:wiener-feynman-kac-qm`: Wiener measure, Brownian bridge, and
  Feynman--Kac representation.
- `qthm:faris-lavine-essential-self-adjointness`: local theorem-level
  sufficient essential-self-adjointness criterion, with the
  comparison-Hamiltonian and Nelson commutator mechanism included in the
  proof.
- `def:regulated-phase-space-path-integral-datum`: ordering-dependent symbols
  and local \(O(\hbar)\) counterterms.
- Paragraph "Gaussian elimination of quadratic momenta": Lagrangian form after
  Gaussian momentum integration.
- `def:finite-slice-time-ordered-insertions-source`: source-dependent
  generating functional at finite cutoff.
- `def:hermitian-one-matrix-qm`: matrix Hilbert space, global `U(N)` action,
  canonical matrix commutators, invariant Hamiltonian, and self-adjointness
  status.
- Section `sec:hermitian-matrix-quantum-mechanics`: singlet/Gauss projection,
  eigenvalue coordinates, Vandermonde measure, radial Laplacian,
  free-fermion map, non-singlet angular sectors, large-`N` collective fields,
  and inverted-oscillator comparison boundary.
- Paragraph "Trace and periodic Euclidean boundary conditions": Euclidean
  trace boundary condition for bosonic paths.
- Paragraph "Euclidean long-time projection to a gapped ground state": vacuum
  projection by Euclidean time evolution, treated as spectral-projection
  prose rather than theorem-family content.

## Claim Ledger

- A regular classical Lagrangian determines Hamiltonian data through the
  Legendre transform \(p_a=\partial L/\partial\dot q^a\),
  \(H=p_a\dot q^a-L\).
- Schrödinger and Heisenberg time evolution are two representations of
  \(U(t)=e^{-\ii t\widehat H/\hbar}\), with the usual commutator equation on
  the relevant domain.
- Position and momentum kets are distributional vectors in a Gelfand triple;
  their resolutions of identity are weak Fourier-inversion identities.
- Paragraph `par:finite-phase-space-time-sliced-kernel` derives the
  finite-dimensional phase-space expression for time evolution at fixed
  partition; its status is a regulated construction, not an independent
  theorem.
- The continuum path-integral notation is shorthand for a regulator and
  limiting procedure.
- `thm:wiener-feynman-kac-qm` constructs the Wiener-measure/Feynman--Kac
  representation under locally Kato bounded-below Schrödinger hypotheses.
- The Trotter theorem boundary is expanded in place: the bounded case is
  explained by norm Taylor expansion plus telescoping, while the unbounded
  Schrödinger case is identified as a closed-form theorem whose proof passes
  through variational characterization of the resolvent and strong semigroup
  convergence, with real-time convergence requiring the corresponding
  Stone--Chernoff/self-adjoint-sum input.
- The Faris--Lavine theorem boundary is expanded in place: after reducing to
  \(V\ge-|x|^2\), the comparison operator
  \(N=p^2+V+2|x|^2\), the form inequalities \(\pm A\le N\), the oscillator
  graph estimate, the commutator
  \(\ii[N,A]=-4(x\cdot p+p\cdot x)\), and the Nelson commutator-theorem
  mechanism are displayed.
- The Feynman--Kac theorem supplies one positive-measure bosonic entry in a
  broader typed path-integral taxonomy.
- Distinct time-lattice orderings define distinct symbols \(h\) and \(h'\),
  differing by local \(O(\hbar)\) terms.
- Paragraph "Gaussian elimination of quadratic momenta" derives the Lagrangian form and
  determinant measure for quadratic momentum dependence.
- `def:finite-slice-time-ordered-insertions-source` records how source
  derivatives generate time-ordered insertions.
- Hermitian one-matrix quantum mechanics is an intrinsic finite-dimensional
  Hamiltonian system with Hilbert space `L^2(Herm_N,dX)`, global `U(N)`
  conjugation action, and a gauged singlet sector obtained by Gauss-law
  projection.
- On the regular eigenvalue locus, `dX = C_N Delta(lambda)^2 d lambda
  dmu(U/T)` and singlet wavefunctions see the radial Laplacian
  `Delta^-2 sum_i partial_i Delta^2 partial_i`.
- Multiplication by the Vandermonde maps symmetric singlet wavefunctions in
  the radial measure to antisymmetric eigenvalue wavefunctions and conjugates
  the radial kinetic operator to the free `N`-fermion kinetic operator away
  from collision hyperplanes.
- Non-singlet matrix-QM sectors contain representation-dependent angular
  inverse-square terms; long-string language is not part of the intrinsic
  Hamiltonian statement.
- The large-`N` collective Hamiltonian follows from integrating the
  one-particle energy over the filled phase-space strip between `p_-` and
  `p_+`; finite-`N` Jacobian, gradient, and edge corrections remain part of
  the validity regime.
- The inverted-oscillator/double-scaling example is recorded as a matrix-QM
  scattering and collective-field laboratory; `c=1` string, leg-factor,
  particle-hole, and ZZ-instanton interpretations are comparison boundaries.
- The trace-boundary-condition paragraph derives that a bosonic Euclidean trace
  identifies \(q_N=q_0\), hence periodic paths.
- Under Feynman--Kac hypotheses, the Euclidean trace path integral is a
  Brownian-loop integral with endpoint constraint \(q(\beta_{\mathrm T})=q(0)\).
- Infinite-volume thermal equilibrium is formulated by the KMS analytic
  boundary condition on the quasilocal algebra, not by a literal full-Hilbert
  trace.
- The Euclidean long-time projection paragraph derives ground-state
  projection under a spectral gap and nonzero overlap, and records that the
  substantive hypotheses are the ground state, overlap, and gap.

The formalized version labels the time-slicing, Kato/Feynman--Kac,
essential-self-adjointness, ordering, Gaussian momentum, matrix-QM radial
reduction, and trace statements, while the vacuum-projection step is kept as
prose because the argument is the spectral theorem plus a gap estimate.

## Calculation Checks

- `calculation-checks/matrix_quantum_mechanics_checks.py` verifies the
  radial Laplacian, Vandermonde conjugation to the free-fermion kinetic
  operator, collision antisymmetry, wrong-Vandermonde-power negative control,
  and collective-field Hamiltonian identity used in
  Section~`sec:hermitian-matrix-quantum-mechanics`.

## Audit Notes

- 2026-05-24, issue #298: added Theorem
  `thm:wiener-feynman-kac-qm`, its proof, and the conceptual restriction that
  path-integral notation must specify its mathematical object, such as a
  measure, oscillatory integral, Berezin functional, gauge-fixed/BV
  construction, lattice or holonomy construction, or formal perturbative
  expansion.
- 2026-05-27, issue #615: upgraded the chapter with labeled definitions,
  propositions, and theorem-boundary entries for the Hamiltonian, rigging,
  time-slicing, Trotter/Kato, Feynman--Kac, ordering, Gaussian momentum,
  source, trace, and vacuum-projection steps.
- 2026-05-30 anti-wrapper pass: demoted the finite phase-space time-sliced
  kernel from proposition/proof form to a labelled construction paragraph.
  The formulas and regulator assumptions were preserved, while the status now
  correctly reflects that the step is insertion of finite resolutions of
  identity and symbol bookkeeping.
- 2026-05-30 dequotation pass: promoted the Trotter product formula from a
  quoted wrapper to local theorem/proof form, replaced the vague hypothesis
  "suppose the hypotheses hold" by explicit real-time essential-self-adjoint
  algebraic-sum hypotheses and Euclidean closed-form-sum hypotheses, and kept
  the bounded telescoping and unbounded form/resolvent mechanisms in the proof.
- 2026-05-30 dequotation pass: promoted the Faris--Lavine criterion from a
  quoted wrapper to local theorem/proof form, with the comparison-Hamiltonian
  and Nelson commutator estimate kept as the proof mechanism preventing hidden
  boundary conditions at infinity.
- 2026-06-04 issue #813: added Hermitian matrix quantum mechanics as an
  intrinsic \(0+1\)-dimensional QFT layer.  The repair reverses the old
  crosswalk classification that treated double-scaled matrix quantum
  mechanics as merely contextual: the radial/Vandermonde, non-singlet, and
  collective-field mechanisms are now incorporated, while string
  interpretations remain boundary comparisons.

## Figure Ledger

Included figures:

- classical Lagrangian/Hamiltonian data and the regular Legendre transform;
- finite time slicing of the interval \([0,T]\), with endpoints and
  intermediate positions labelled.

The time-slicing figure is exact as a discretization diagram, not a continuum
path configuration.

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
Formalization upgraded on 2026-05-27 for issue #615.

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

## Definition Ledger

- `def:regular-classical-lagrangian-datum`: regular Legendre transform from
  classical Lagrangian to Hamiltonian data.
- `def:schrodinger-representation-datum`: canonical Schrödinger Hilbert-space
  representation and self-adjoint Hamiltonian time evolution.
- `def:position-momentum-rigging-kernel-notation`: weak position/momentum
  resolutions of identity with the \(\hbar\)-Fourier normalization.
- `prop:finite-phase-space-time-sliced-kernel`: finite time-sliced
  phase-space integral and discrete phase-space action.
- `qthm:trotter-product-formula-qm`: operator-level Trotter formula used to
  interpret continuum limits.
- `def:kato-schrodinger-euclidean-datum`: Kato/local Kato hypotheses and
  Friedrichs Schrödinger Hamiltonian.
- `thm:wiener-feynman-kac-qm`: Wiener measure, Brownian bridge, and
  Feynman--Kac representation.
- `qthm:faris-lavine-essential-self-adjointness`: sufficient
  essential-self-adjointness criterion.
- `def:regulated-phase-space-path-integral-datum`: ordering-dependent symbols
  and local \(O(\hbar)\) counterterms.
- `prop:gaussian-elimination-quadratic-momenta`: Lagrangian form after
  Gaussian momentum integration.
- `def:finite-slice-time-ordered-insertions-source`: source-dependent
  generating functional at finite cutoff.
- Paragraph "Trace and periodic Euclidean boundary conditions": Euclidean
  trace boundary condition for bosonic paths.
- `prop:euclidean-long-time-ground-state-projection`: vacuum projection by
  Euclidean time evolution.

## Claim Ledger

- A regular classical Lagrangian determines Hamiltonian data through the
  Legendre transform \(p_a=\partial L/\partial\dot q^a\),
  \(H=p_a\dot q^a-L\).
- Schrödinger and Heisenberg time evolution are two representations of
  \(U(t)=e^{-\ii t\widehat H/\hbar}\), with the usual commutator equation on
  the relevant domain.
- Position and momentum kets are distributional vectors in a Gelfand triple;
  their resolutions of identity are weak Fourier-inversion identities.
- `prop:finite-phase-space-time-sliced-kernel` derives the finite-dimensional
  phase-space expression for time evolution at fixed partition.
- The continuum path-integral notation is shorthand for a regulator and
  limiting procedure.
- `thm:wiener-feynman-kac-qm` constructs the Wiener-measure/Feynman--Kac
  representation under locally Kato bounded-below Schrödinger hypotheses.
- The Feynman--Kac theorem supplies one positive-measure bosonic entry in a
  broader typed path-integral taxonomy.
- Distinct time-lattice orderings define distinct symbols \(h\) and \(h'\),
  differing by local \(O(\hbar)\) terms.
- `prop:gaussian-elimination-quadratic-momenta` derives the Lagrangian form and
  determinant measure for quadratic momentum dependence.
- `def:finite-slice-time-ordered-insertions-source` records how source
  derivatives generate time-ordered insertions.
- The trace-boundary-condition paragraph derives that a bosonic Euclidean trace
  identifies \(q_N=q_0\), hence periodic paths.
- Under Feynman--Kac hypotheses, the Euclidean trace path integral is a
  Brownian-loop integral with endpoint constraint \(q(\beta_{\mathrm T})=q(0)\).
- Infinite-volume thermal equilibrium is formulated by the KMS analytic
  boundary condition on the quasilocal algebra, not by a literal full-Hilbert
  trace.
- `prop:euclidean-long-time-ground-state-projection` proves ground-state
  projection under a spectral gap and nonzero overlap.

The formalized version labels the time-slicing, Kato/Feynman--Kac,
essential-self-adjointness, ordering, Gaussian momentum, trace, and vacuum
projection statements so later chapters can cite hypotheses rather than
informal path-integral slogans.

## Audit Notes

- 2026-05-24, issue #298: added Theorem
  `thm:wiener-feynman-kac-qm`, its proof, and the conceptual restriction that
  path-integral notation must specify its mathematical object, such as a
  measure, oscillatory integral, Berezin functional, gauge-fixed/BV
  construction, lattice or holonomy construction, or formal perturbative
  expansion.
- 2026-05-27, issue #615: upgraded the chapter with labeled definitions,
  propositions, and quoted theorems for the Hamiltonian, rigging,
  time-slicing, Trotter/Kato, Feynman--Kac, ordering, Gaussian momentum,
  source, trace, and vacuum-projection steps.

## Figure Ledger

Included figures:

- classical Lagrangian/Hamiltonian data and the regular Legendre transform;
- finite time slicing of the interval \([0,T]\), with endpoints and
  intermediate positions labelled.

The time-slicing figure is exact as a discretization diagram, not a continuum
path configuration.

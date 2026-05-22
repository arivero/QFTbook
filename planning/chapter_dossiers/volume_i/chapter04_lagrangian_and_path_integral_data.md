# Volume I, Chapter 4 Dossier: Hamiltonian Evolution And Time-Sliced Path Integrals

## Status

Current status: source-certified against handwritten 253a pp. 10--14 after
the 2026-05-22 derivation and figure pass; tightened on 2026-05-23 so the
position/momentum kernels explicitly use the rigged-Hilbert-space convention
and the continuum path-integral symbol is tied to finite regulators.

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
  future mathematical interlude.
- Feynman--Kac and Euclidean measure references for the later Wick-rotation
  chapter.

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
| \(\mathcal S(\mathbb R^d)\subset L^2\subset\mathcal S'\) | Gelfand triple | generalized position and momentum kernels |

## Definition Ledger

- regular Legendre transform from classical Lagrangian to Hamiltonian data;
- weak position/momentum resolutions of identity with the \(\hbar\)-Fourier
  normalization;
- finite time-sliced phase-space integral;
- discrete phase-space action;
- ordering-dependent Hamiltonian symbols and local \(O(\hbar)\) counterterms;
- Lagrangian form after Gaussian momentum integration;
- source-dependent generating functional at finite cutoff;
- Euclidean trace boundary condition for bosonic paths;
- vacuum projection by Euclidean time evolution.

## Claim Ledger

| Claim | Status | Certification |
| --- | --- | --- |
| A regular classical Lagrangian determines Hamiltonian data through the Legendre transform \(p_a=\partial L/\partial\dot q^a\), \(H=p_a\dot q^a-L\). | Construction with hypothesis | Added before the quantum time-slicing construction and checked against handwritten p. 10 |
| Schrödinger and Heisenberg time evolution are two representations of \(U(t)=e^{-\ii t\widehat H/\hbar}\), with \(\dot{\widehat O}(t)=\ii[\widehat H,\widehat O(t)]/\hbar\) on the relevant domain. | Operator identity | Restored from handwritten p. 11 |
| Position and momentum kets are distributional vectors in a Gelfand triple; their resolutions of identity are weak Fourier-inversion identities. | Definition/construction | 2026-05-23 rigor pass |
| Inserting position and momentum resolutions gives a finite-dimensional phase-space expression for time evolution at fixed partition. | Construction | Derived in chapter |
| The continuum path-integral notation is shorthand for a regulator and limiting procedure. | Framework statement | Definition of \(K_N\) and limiting convention |
| Distinct time-lattice orderings define distinct operator symbols \(h\) and \(h'\), differing by local \(O(\hbar)\) terms. | Regulator statement | Explicit finite-slice comparison patched from handwritten p. 13 |
| Quadratic momentum dependence yields a Lagrangian form with a determinant measure. | Derivation | Gaussian integration in chapter |
| Source derivatives generate time-ordered insertions. | Construction | Derived from discrete source insertion |
| The Euclidean trace of a bosonic quantum-mechanical system identifies the endpoints \(q_N=q_0\), hence produces periodic paths. | Construction | Derived by inserting the position resolution into \(\operatorname{Tr} e^{-\beta_{\mathrm T}\widehat H/\hbar}\) |
| Euclidean long-time evolution projects onto the ground state under a spectral gap/overlap assumption. | Proposition | Derived from spectral decomposition |

## Figure Ledger

Included figures:

- classical Lagrangian/Hamiltonian data and the regular Legendre transform;
- finite time slicing of the interval \([0,T]\), with endpoints and
  intermediate positions labelled.

The time-slicing figure is exact as a discretization diagram, not a continuum
path configuration.

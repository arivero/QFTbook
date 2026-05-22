# Volume I, Chapter 4 Dossier: Hamiltonian Evolution And Time-Sliced Path Integrals

## Status

Current status: first mature draft prepared for inclusion after audit and
build.

## Logical Role

This chapter introduces the path integral in ordinary finite-dimensional
quantum mechanics as a regulated construction of transition amplitudes and
time-ordered Green functions. It prepares the later field-theoretic path
integral without using scattering language.

## Framework

Working framework:

- finite-dimensional configuration space \(\mathcal Q=\mathbb R^d\), with
  later remarks on curved configuration spaces;
- Hilbert space \(L^2(\mathcal Q,\dd^dq)\);
- canonical coordinate and momentum operators;
- self-adjoint Hamiltonian \(\widehat H\);
- unitary time-evolution group \(U(T)=\exp(-\ii T\widehat H/\hbar)\);
- generalized position and momentum eigenstates used as a distributional
  resolution of identity;
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
| \(\mathcal Q\) | configuration space, initially \(\mathbb R^d\) | QM |
| \(q^a,p_a\) | canonical coordinates and momenta | phase space |
| \(\widehat q^a,\widehat p_a\) | coordinate and momentum operators | Hilbert space |
| \(\widehat H\) | self-adjoint Hamiltonian | time evolution |
| \(h(q,p)\) | chosen symbol of \(\widehat H\) in a specified ordering | time slicing |
| \(\epsilon\) | time step \(T/N\) | regulator |
| \(K_N\) | finite-\(N\) regulated phase-space integral | path integral |
| \(S_N\) | discrete phase-space action | regulator |
| \(G_{ab}(q)\) | positive-definite configuration-space metric | Lagrangian form |
| \(J(t)\) | external source | generating functional |
| \(\beta_{\mathrm T}\) | Euclidean inverse temperature in trace kernels | thermal trace |

## Definition Ledger

- finite time-sliced phase-space integral;
- discrete phase-space action;
- Lagrangian form after Gaussian momentum integration;
- source-dependent generating functional at finite cutoff;
- Euclidean trace boundary condition for bosonic paths;
- vacuum projection by Euclidean time evolution.

## Claim Ledger

| Claim | Status | Certification |
| --- | --- | --- |
| Inserting position and momentum resolutions gives a finite-dimensional phase-space expression for time evolution at fixed partition. | Construction | Derived in chapter |
| The continuum path-integral notation is shorthand for a regulator and limiting procedure. | Framework statement | Definition of \(K_N\) and limiting convention |
| Quadratic momentum dependence yields a Lagrangian form with a determinant measure. | Derivation | Gaussian integration in chapter |
| Source derivatives generate time-ordered insertions. | Construction | Derived from discrete source insertion |
| The Euclidean trace of a bosonic quantum-mechanical system identifies the endpoints \(q_N=q_0\), hence produces periodic paths. | Construction | Derived by inserting the position resolution into \(\operatorname{Tr} e^{-\beta_{\mathrm T}\widehat H/\hbar}\) |
| Euclidean long-time evolution projects onto the ground state under a spectral gap/overlap assumption. | Proposition | Derived from spectral decomposition |

## Figure Ledger

Included figure:

- finite time slicing of the interval \([0,T]\), with endpoints and
  intermediate positions labelled.

The figure is exact as a discretization diagram, not a continuum path
configuration.

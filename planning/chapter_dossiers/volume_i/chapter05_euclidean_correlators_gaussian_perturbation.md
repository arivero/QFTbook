# Volume I, Chapter 5 Dossier: Euclidean Correlators, Gaussian Integrals, and Quantum-Mechanical Perturbation Theory

## Status

Current status: ready for TeX rewrite.

## Logical Role

This chapter converts the regulated time-sliced path integral of Chapter 4
into a concrete calculus for Green functions. The order of ideas is:

1. spectral decomposition of vacuum correlation functions;
2. analytic continuation to Euclidean time;
3. Euclidean path-integral representation of correlation functions;
4. exact Gaussian evaluation and Wick contractions;
5. perturbative expansion of Euclidean Green functions in a quantum-mechanical
   interacting model;
6. connected diagrams, one-particle-irreducible insertions, and regulator
   dependent counterterms.

The chapter remains entirely about Green functions and spectral data. It does
not introduce scattering amplitudes.

## Primary Source Anchors

- `transcription/tex/253a/foundations.tex`, lines around "Correlation
  Functions and Wick Rotation", "Harmonic Oscillator Example", "Gaussian
  Integrals and Wick Contractions", "Gaussian Functional Integrals",
  "Anharmonic Oscillator", "Ground State Energy from Vacuum Diagrams", "The
  Two-Point Function and One-Particle-Irreducible Graphs", and "Derivative
  Interactions and the Measure".
- `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`, section
  "The path integral", for the regulated path-integral and counterterm
  perspective.
- `references/253a_notes.tex`, sections on correlation functions, harmonic
  oscillator, Gaussian integrals, anharmonic oscillator, and derivative
  interactions. This is a comparison layer only, not an authority.

## Framework

Working framework:

- a one-dimensional quantum-mechanical example unless a vector index is
  explicitly introduced;
- Hilbert space with self-adjoint Hamiltonian \(\widehat H\);
- normalized ground state \(\ket 0\) with energy \(E_0\);
- complete orthonormal energy eigenbasis in examples with discrete spectrum;
- Euclidean time \(\tau\) defined from real time \(t\) by \(t=-\ii\tau\);
- Euclidean action \(S_E\) defined from the Lagrangian after analytic
  continuation;
- regulated functional integrals understood as mode-cutoff or time-sliced
  limits.

## Notation Inventory

| Symbol | Type | Meaning |
| --- | --- | --- |
| \(\widehat H\) | self-adjoint operator | Hamiltonian |
| \(\ket n,E_n\) | eigenstate/eigenvalue | energy basis |
| \(\omega_n\) | nonnegative number | \((E_n-E_0)/\hbar\), or \(E_n-E_0\) after \(\hbar=1\) |
| \(G(t)\) | distribution/function | real-time two-point function in a specified ordering |
| \(G_E(\tau)\) | Euclidean Green function | analytic continuation of \(G(t)\) for \(\tau>0\), extended by Euclidean ordering |
| \(S_E,L_E\) | Euclidean action/Lagrangian | weight \(\exp(-S_E/\hbar)\) |
| \(A\) | positive operator/matrix | Gaussian quadratic kernel |
| \(A^{-1}\) | covariance | propagator/Green function |
| \(J\) | source | generates insertions |
| \(G_0\) | free covariance | harmonic oscillator propagator |
| \(\Sigma(k)\) | self-energy | sum of amputated 1PI two-point insertions |
| \(\Lambda\) | cutoff | frequency regulator |
| \(C\) | counterterm coefficient | regulator-dependent local term |

## Definition Ledger

- Euclidean two-point function for \(\tau>0\) by spectral analytic
  continuation.
- Euclidean ordered \(r\)-point function.
- Gaussian expectation and covariance.
- Wick contraction and complete pairing.
- Gaussian functional integral with Green function kernel.
- Connected vacuum graph and linked-cluster exponentiation.
- Connected two-point function.
- One-particle-irreducible two-point insertion/self-energy.
- Cutoff-dependent counterterm in derivative-interaction quantum mechanics.

## Claim Ledger

| Claim | Status | Certification |
| --- | --- | --- |
| The vacuum two-point function has a lower-half-plane analytic continuation under spectral positivity and suitable convergence hypotheses. | Derived | Spectral expansion |
| Wick rotation \(t=-\ii\tau\) gives exponential Euclidean decay \(e^{-(E_n-E_0)\tau/\hbar}\). | Derived | Spectral expansion |
| Long Euclidean time projects onto the ground state under overlap and gap assumptions. | Derived | Spectral decomposition |
| The harmonic oscillator Euclidean two-point function is \(\hbar(2\omega)^{-1}e^{-\omega|\tau|}\). | Derived | Mode expansion and contour integral |
| Gaussian moments are sums over complete pairings. | Derived | Source differentiation |
| The logarithm of the partition function is the sum of connected vacuum diagrams. | Derived | Partition combinatorics |
| Normalized two-point functions retain diagrams connected to the external insertions. | Derived | Vacuum factor cancellation |
| The full two-point function is obtained from the self-energy by a geometric series in momentum space. | Derived | 1PI decomposition |
| Derivative interactions require a regulator and local counterterm data to define the path-integral expression. | Framework/construction | Explicit cutoff computation |

## Figure Ledger

Figures to include:

- complex-time Wick rotation and Euclidean projection interval;
- harmonic-oscillator path with Dirichlet endpoints;
- contour integral in the complex \(k\)-plane;
- Wick pairings for a four-point Gaussian moment;
- connected/disconnected vacuum graph schematic;
- cancellation of vacuum bubbles in a normalized two-point function;
- 1PI self-energy chain;
- derivative-interaction vertex schematic with derivative marks.

## Audit Targets

- Every use of \(Dq\), \(Z\), \(G\), \(A\), \(J\), \(\Sigma\), and \(\Lambda\)
  must be defined before use.
- Perturbative diagrams must be explicitly identified as Green-function
  diagrams, not scattering amplitudes.
- Counterterms must be presented as part of the regulated definition, not as a
  slogan about removing infinities.
- The chapter must end at the threshold of relativistic fields; the transition
  to fields is for the next chapter.

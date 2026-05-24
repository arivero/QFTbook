# Volume I, Chapter 5 Dossier: Euclidean Correlators, Gaussian Integrals, and Quantum-Mechanical Perturbation Theory

## Status

Current status: spectral/Wick-rotation opening block certified against
handwritten 253a pp. 15--18 on 2026-05-22; harmonic-oscillator Euclidean
propagator certified against handwritten 253a pp. 19--23 on 2026-05-22;
finite and functional Gaussian integral block certified against handwritten
253a pp. 24--29 on 2026-05-22;
anharmonic-oscillator vacuum/two-point/self-energy block certified against
handwritten 253a pp. 30--43 on 2026-05-22;
derivative-interaction/regulator counterterm block also certified on
2026-05-22 after handwritten source and rendered-figure audit; tightened on
2026-05-24 for GitHub issue #298 so the Euclidean quantum-mechanical
path-integral notation refers to Wiener/Brownian-bridge measure precisely when
Chapter 4's Feynman--Kac theorem applies, and otherwise remains a stated
regulator or perturbative construction.

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
- Handwritten source visual trace:
  253a pp. 30--43 rendered for the 2026-05-22 source pass from
  `references/253a lectures 2022.pdf`; derivative-interaction trace
  `monograph/tex/build/source_visual_trace/253a_trace-043.png` through
  `monograph/tex/build/source_visual_trace/253a_trace-051.png`.

## Framework

Working framework:

- a one-dimensional quantum-mechanical example unless a vector index is
  explicitly introduced;
- Hilbert space with self-adjoint Hamiltonian \(\widehat H\);
- normalized ground state \(\ket 0\) with energy \(E_0\);
- complete orthonormal energy eigenbasis in examples with discrete spectrum;
- projection-valued spectral measure \(P_{\widehat H}\) and the positive
  two-point spectral measure \(\mu_q\) when continuous spectrum is allowed;
- Euclidean time \(\tau\) defined from real time \(t\) by \(t=-\ii\tau\);
- complex-time vacuum-projection contour with endpoint wavefunctions included
  in the regulated path-integral data;
- Euclidean action \(S_E\) defined from the Lagrangian after analytic
  continuation;
- regulated functional integrals understood as mode-cutoff or time-sliced
  limits.
- for Schrödinger operators satisfying Chapter 4's Feynman--Kac hypotheses,
  finite-interval Euclidean path integrals are Brownian-bridge expectations
  with potential weight; this is not generalized to fermionic, gauge,
  complex-weight, or perturbative QFT path integrals.

## Notation Inventory

| Symbol | Type | Meaning |
| --- | --- | --- |
| \(\widehat H\) | self-adjoint operator | Hamiltonian |
| \(\ket n,E_n\) | eigenstate/eigenvalue | energy basis |
| \(P_{\widehat H}\) | projection-valued measure | spectral theorem for \(\widehat H\) |
| \(\eta_q\) | vector | \(\widehat q\ket0\) |
| \(\mu_q\) | positive Borel measure | \(\mu_q(B)=\langle\eta_q,P_{\widehat H}(B)\eta_q\rangle\) |
| \(\omega_n\) | nonnegative number | \((E_n-E_0)/\hbar\), or \(E_n-E_0\) after \(\hbar=1\) |
| \(G(t)\) | distribution/function | real-time two-point function in a specified ordering |
| \(G_E(\tau)\) | Euclidean Green function | analytic continuation of \(G(t)\) for \(\tau>0\), extended by Euclidean ordering |
| \(S_E,L_E\) | Euclidean action/Lagrangian | weight \(\exp(-S_E/\hbar)\) |
| \(\Gamma_{T,t}\) | complex-time contour | vacuum projection and real-time insertion contour |
| \([Dq]_{\Gamma,\psi}\) | regulated contour path-integral data | includes endpoint wavefunctions of \(\ket\psi\) |
| \(\mathbb W_{x,y}^\tau\) | Brownian-bridge measure | rigorous Euclidean Schrödinger path integral when Chapter 4 hypotheses hold |
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
- spectral-measure representation of the two-point function.
- Euclidean ordered \(r\)-point function.
- complex-contour path-integral representation of the projected real-time
  correlator.
- Wiener/Brownian-bridge interpretation of \([Dq]\) in the Schrödinger cases
  covered by Chapter 4, separated from Gaussian regulator and perturbative
  uses of the same notation.
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
| The vacuum two-point function has a lower-half-plane analytic continuation under spectral positivity and suitable convergence hypotheses. | Derived | Spectral expansion and positive spectral-measure representation |
| Wick rotation \(t=-\ii\tau\) gives exponential Euclidean decay \(e^{-(E_n-E_0)\tau/\hbar}\). | Derived | Spectral expansion |
| Long Euclidean time projects onto the ground state under overlap and gap assumptions. | Derived | Spectral decomposition |
| The projected correlator has a regulated complex-time path-integral representation with endpoint wavefunctions included in the contour measure. | Construction | Patched from handwritten pp. 16--17 and rendered on physical PDF page 65 |
| In Euclidean Schrödinger quantum mechanics satisfying Chapter 4's Feynman--Kac theorem, finite-interval \([Dq]\) denotes Brownian-bridge/Wiener expectation with potential weight. | Theorem application | Explicit paragraph after the Euclidean path-integral formula; distinguishes this from later Gaussian regulator and perturbative meanings |
| The harmonic oscillator Euclidean two-point function is \(\hbar(2\omega)^{-1}e^{-\omega|\tau|}\). | Derived; source-certified 2026-05-22 | Dirichlet sine-mode expansion, \(k_n=n\pi/(2T)\) Riemann-sum limit, endpoint image term, and contour integral |
| Gaussian moments are sums over complete pairings. | Derived; source-certified 2026-05-22 | Finite source differentiation, explicit two- and four-point calculations, and \(4!\)-assignment grouping |
| The Gaussian functional integral has two-point function equal to the Green kernel \(A^{-1}\). | Derived; source-certified 2026-05-22 | Regulated functional integration by parts and Fourier-space diagonalization |
| The logarithm of the partition function is the sum of connected vacuum diagrams. | Derived; source-certified 2026-05-22 | Component-counting formula with \(m_\ell\), linked-cluster exponentiation, and counted three-vertex topology |
| Normalized two-point functions retain diagrams connected to the external insertions. | Derived; source-certified 2026-05-22 | Vacuum factor cancellation in \(Z_g^{-1}\langle q(\tau)q(0)\cdots\rangle_0\) |
| The full two-point function is obtained from the self-energy by a geometric series in momentum space. | Derived; source-certified 2026-05-22 | Amputated 1PI convention, second-order topologies, and \(\widetilde G(k)=1/(k^2+1-\Sigma(k))\) |
| Derivative interactions require a regulator and local counterterm data to define the path-integral expression. | Framework/construction | Explicit cutoff computation; 2026-05-22 handwritten source/figure audit |

## Figure Ledger

Figures to include:

- complex-time Wick rotation and Euclidean projection interval;
- harmonic-oscillator path with Dirichlet endpoints, certified against
  handwritten pp. 19--23 on 2026-05-22;
- contour integral in the complex \(k\)-plane, certified against handwritten
  pp. 22--23 on 2026-05-22;
- Wick pairings for a four-point Gaussian moment;
- connected/disconnected vacuum graph schematic;
- second-order connected vacuum topologies and counted three-vertex connected
  vacuum graph, certified against handwritten pp. 30--43 on 2026-05-22;
- cancellation of vacuum bubbles in a normalized two-point function;
- connected two-point graph series and second-order two-point topologies,
  certified against handwritten pp. 30--43 on 2026-05-22;
- 1PI self-energy chain;
- complex \(k\)-plane pole-extraction contour for the anharmonic oscillator
  two-point function, certified against handwritten pp. 30--43 on 2026-05-22;
- derivative-interaction vertex schematic with derivative marks.
- derivative-interaction contraction figure separating the linearly divergent
  loop-derivative term, the finite wavefunction term, and the parity-odd
  vanishing term. Certified on rendered manuscript physical PDF pages 63--65
  (printed pages 47--49) against handwritten pp. 43--51.

## Audit Notes

- 2026-05-24, issue #298: added the Chapter 5 cross-reference to
  Theorem `thm:wiener-feynman-kac-qm` and recorded that the Borel-measure
  interpretation is only the Euclidean Schrödinger case, not a general QFT
  path-integral foundation.

## Audit Targets

- Every use of \(Dq\), \(Z\), \(G\), \(A\), \(J\), \(\Sigma\), and \(\Lambda\)
  must be defined before use.
- Perturbative diagrams must be explicitly identified as Green-function
  diagrams, not scattering amplitudes.
- Counterterms must be presented as part of the regulated definition, not as a
  slogan about removing infinities.
- The derivative-coupled oscillator block is certified to retain the classical
  \(q\mapsto y\) coordinate check, the cutoff self-energy, the local
  \(Cg\hbar q^2/2\) counterterm, and the first-pole energy-gap interpretation
  of the finite counterterm part.
- The chapter must end at the threshold of relativistic fields; the transition
  to fields is for the next chapter.
- The harmonic-oscillator source block is certified to retain the finite
  interval before taking \(T\to\infty\): sine modes, coefficient covariance,
  Riemann-sum conversion, image contribution from Dirichlet endpoints, and the
  contour suppression criterion.
- The Gaussian-integral source block is certified to retain the source
  derivative convention, the explicit four-point combinatorics, the
  contraction-value definition, the functional derivative normalization, the
  integration-by-parts derivation of \(G(\tau_1,\tau_2)\), and the
  Fourier-space covariance.
- The anharmonic-oscillator source block is certified to retain the regulated
  coefficientwise meaning of the perturbative expansion, first-order vacuum
  graph, second-order connected/disconnected vacuum topologies,
  linked-cluster component counting, ground-state-energy interpretation,
  normalized two-point vacuum-bubble cancellation, order-\(g\) Fourier tadpole
  computation, second-order two-point graph row, amputated self-energy
  convention, \(g^2\) self-energy expression, complex-\(k\)-plane contour, and
  first gap \(E_1-E_0=1+g/8-g^2/32+O(g^3)\).

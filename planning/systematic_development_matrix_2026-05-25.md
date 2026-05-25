# Systematic Development Matrix, 2026-05-25

## Scope

This matrix records the next-stage development plan across all compiled
volumes after the launch of Volumes VI--XII.  It is not a substitute for
chapter dossiers; it is the cross-volume control sheet for topic order,
proof infrastructure, and frontier-gap development.

## Global Standards

- Every chapter must introduce its primitive objects before using derived
  structures.
- Framework changes must be explicit: Wightman, OS, AQFT, constructive,
  perturbative, functorial, factorized, BV, and lattice formulations compare
  objects only through stated maps.
- External references are to be downloaded and converted to readable sidecars
  when detailed local analysis is needed.
- Frontier gaps should be formulated as construction or comparison problems
  with precise objects, not as vague literature comments.
- Calculation-check scripts are required when convention-sensitive algebra
  controls a formula.

## Volume Tracks

| Volume | Immediate development track | Proof or example infrastructure |
| --- | --- | --- |
| I Foundations | OS reconstruction proof, Wightman/AQFT bridge, rigged Hilbert-space distributional states | OS-II growth estimates, local-net examples from fields, source-note coverage audit |
| II Scattering | charged-sector Haag--Ruelle/LSZ, polynomial boundedness, Froissart refinements, resonance sheets | wave-packet estimates, spectral support lemmas, partial-wave counting checks |
| III Renormalization | BPHZ finiteness, BPHZ--Polchinski map, operator regularization versus renormalization, Borel/Lefschetz theory | forest-formula appendices, finite coordinate maps, asymptotic-analysis examples |
| IV Gauge Theory | global form bridge, QCD string, large \(N\), anomaly convention checks, BRST/BV refinements | color/gamma/anomaly scripts, lattice plaquette checks, Wilson-loop examples |
| V CFT | rigorous conformal representation theory, conformal blocks from tensor products, radial OPE convergence, light-ray operator domains, modern two-dimensional CFT from chiral algebras through modular/sewing data; entanglement and replica topics remain outside the CFT spine and belong, if developed, to AQFT/local-algebraic foundations | Gram-matrix/block scripts, Hilbert-space radial estimates, conformal group appendices, Virasoro/Kac determinant and modular-character checks |
| VI Integrable QFT | factorized S-matrices, form-factor bootstrap, TBA, exact integrable RG flows, mirror-channel finite-size effects, sine-Gordon, affine Toda, \(O(N)\), Gross--Neveu, sigma-model examples, bridges to nonintegrable 2D QFT and 2D CFT | rapidity-strip diagrams, residue/fusion checks, form-factor convergence examples, TBA kernel and UV/IR central-charge checks |
| VII Supersymmetric QFT | Hilbert-space particle multiplets versus off-shell field-variable multiplets, superspace geometry, supersymmetric Wilsonian schemes, \(4D\) \(\mathcal N=1\) and \(\mathcal N=2\) gauge dynamics, \(2D\) LG/CY/GLSM models, \(3D\) Chern-Simons-matter theories, \(6D\) SCFTs, holomorphy and nonrenormalization with regulator caveats, localization from regulated localization data | spinor/superfield calculation checks, stringbook convention comparison, auxiliary-field closure checks, Wilsonian-coordinate and anomaly-matching ledgers, dimensional example status ledgers, JK-residue and instanton-moduli-space boundary audits |
| VIII TQFT | BF theory, Chern--Simons, extended functors, BV quantization of topological gauge theories, Witten--Donaldson theory, Donaldson/Seiberg--Witten RG comparison | bordism diagrams, finite-dimensional BV/Stokes proofs, anomaly-line examples, instanton/monopole moduli-space and RG-gap ledgers |
| IX Global Structure | line/surface operators, confinement and screening, discrete theta terms, anomaly inflow | charge-lattice calculations, defect fusion examples, gauge-group global form tables |
| X Thermal/Hydrodynamic | Schwinger--Keldysh, Kubo formulae, hydrodynamic EFT, thermal gauge theory, kinetic limits | spectral/KMS derivations, transport formula checks, SK contour sign tables |
| XI Constructive/Lattice/Numerical | Glimm--Jaffe scalar models, lattice reflection positivity, SPDE quantization, numerical methods | OS data tables, lattice positivity proofs, reproducible benchmark scripts |
| XII Curved Backgrounds | stress tensors, trace anomalies, Unruh/Hawking effects, background gauge fields, index theory, eta invariants, and global anomalies | point-splitting calculations, curvature counterterm tables, Hadamard wavefront appendices, determinant-line holonomy checks |

## Current Second-Chapter Pass

The second-chapter pass develops the first local object after each new
volume's opening chapter:

- Volume VI: rapidity-plane analytic bootstrap data.
- Volume VII: superspace as locally super-ringed geometry.
- Volume VIII: bordism functoriality and extended TQFT target.
- Volume IX: extended operators and topological defects.
- Volume X: Euclidean thermal path integrals from the Gibbs trace.
- Volume XI: constructive scalar models and OS data.
- Volume XII: point splitting and stress-tensor renormalization.

## Current Third-Chapter Pass

The third-chapter pass develops the first nontrivial consistency mechanism or
worked structure in each launched special volume:

- Volume VI: Yang--Baxter consistency from three-particle factorization and
  internal-symmetry projectors.
- Volume VII: supersymmetric gauge theory with trace, coupling, field-strength,
  matter, moment-map, and anomaly conventions fixed.
- Volume VIII: BF theory as an explicit cohomological gauge theory with
  reducible gauge symmetry and BV obligations.
- Volume IX: line, surface, and domain-wall operators as defect data with
  global-form and fusion inputs.
- Volume X: Schwinger--Keldysh real-time generating functionals and retarded
  response.
- Volume XI: lattice reflection positivity with a nearest-neighbor scalar
  proof, now supplemented by Xi's lattice-fermion mid-link reflection
  positivity note.
- Volume XII: trace anomalies as Weyl variations of background generating
  functionals.

## Current Fourth-Chapter Pass

The fourth-chapter pass adds the first operator, response, or continuum
completion layer after the initial consistency mechanisms:

- Volume VI: form factors as local-operator matrix elements, including
  exchange, cyclicity, kinematic-pole, and bound-state-pole equations.
- Volume VII: supersymmetric Wilsonian schemes as finite-cutoff data with BV
  pushforward, local \(F\)- and \(D\)-term coordinates, and holomorphic scheme
  hypotheses.
- Volume VIII: Chern--Simons theory, including level quantization, phase
  space, Wilson lines, framing, and boundary data.
- Volume IX: confinement, screening, and oblique confinement through
  renormalized line operators and electric/magnetic charge lattices.
- Volume X: spectral functions, fluctuation--dissipation, Kubo formulae, and
  the theorem boundary from response to hydrodynamics.
- Volume XI: continuum limits and scaling windows as distributional limits
  satisfying reconstruction hypotheses.
- Volume XII: the Unruh effect through wedge modular theory and the
  Bisognano--Wichmann theorem boundary.

## Current Fifth-Chapter Pass

The fifth-chapter pass adds the first thermodynamic, cohomological,
topological-sector, hydrodynamic, lattice-gauge, and horizon-radiation layer:

- Volume VI: thermodynamic Bethe ansatz from Bethe--Yang quantization,
  rapidity densities, constrained entropy, pseudoenergies, and finite-size
  ground-state energy.
- Volume VII: nonrenormalization and holomorphy as Wilsonian chiral-coordinate
  statements, including the perturbative superpotential theorem, spurion
  selection rules, holomorphic gauge coupling, and rescaling anomaly.
- Volume VIII: cohomological field theories from a regulated \(Q\)-complex,
  metric-independence proof, \(Q\)-exact deformation invariance, and
  finite-dimensional localization boundary.
- Volume IX: discrete theta terms as cohomology-valued topological actions,
  including one-form backgrounds, Pontryagin-square terms, and line-lattice
  effects.
- Volume X: hydrodynamics from stress-tensor and current Ward identities,
  thermodynamic closure, entropy-current algebra, first-order transport, and
  linearized shear/sound poles.
- Volume XI: Wilson lattice gauge theory with link variables, plaquettes,
  Wilson action, continuum expansion, Wilson loops, transfer matrix, and
  fermion/chiral-regulator boundary.
- Volume XII: Hawking radiation from Euclidean horizon regularity,
  near-horizon Bogoliubov analyticity, state distinctions, greybody factors,
  and interacting-QFT theorem boundary.

## Current Sixth-Chapter Pass

The sixth-chapter pass adds the first exact-flow, supersymmetric-dynamics,
sigma-model, inflow, hydrodynamic-action, numerical, and index-theoretic
layers after the basic examples and theorem boundaries:

- Volume VI: integrable RG flows from relevant CFT perturbations, finite-size
  scaling functions, TBA ultraviolet limits, massless-flow TBA, and
  form-factor normalization obligations.
- Volume VII: four-dimensional \(\mathcal N=1\) gauge dynamics with SQCD
  chiral coordinates, holomorphic scale matching, gaugino condensation,
  ADS superpotentials, and the quantum modified constraint.
- Volume VIII: topological sigma models with A-model and B-model BRST
  complexes, holomorphic-map localization, and continuum-QFT construction
  boundary.
- Volume IX: anomaly inflow as anomaly lines and invertible bulk theories,
  including descent, one-form symmetry backgrounds, and the gauging
  trivialization criterion.
- Volume X: Schwinger--Keldysh hydrodynamic effective actions for diffusion,
  including doubled sources, hydrodynamic phases, positivity, retarded poles,
  and dynamical KMS.
- Volume XI: Monte Carlo finite-regulator expectations, detailed balance,
  autocorrelation, reweighting, fermion determinants, and sign-problem
  continuum interpretation.
- Volume XII: background gauge fields and index theory, including coupled
  Dirac operators, Atiyah--Singer formulae, zero-mode insertion rules,
  anomaly polynomials, and determinant-line global anomalies.

## Current Seventh-Chapter Pass

The seventh-chapter pass adds finite-size, exact-dynamics, twisting, phase,
screening, rigorous-RG, and global-anomaly layers:

- Volume VI: mirror-channel TBA from equality of torus Hamiltonian
  decompositions, large-circumference expansion, excited-state finite-size
  corrections, and relativistic wrapping effects.
- Volume VII: four-dimensional \(\mathcal N=2\) gauge dynamics, including
  Coulomb-branch coordinates, special geometry, Seiberg-Witten period data,
  pure gauge-algebra \(\mathfrak{su}(2)\) monodromies, and local Abelian
  dynamics near singular fibers.
- Volume VIII: twists of supersymmetric theories as homomorphisms from
  rotations to R-symmetry, scalar supercharge cohomology, metric-independence
  proof, Donaldson twist data, and two-dimensional A/B twist placement.
- Volume IX: phases of gauge theories defined by infinite-volume local and
  extended-operator data, Wilson-loop potentials, higher-form symmetry
  realization, gauge-Higgs analytic corridors, and topological sectors.
- Volume X: thermal gauge theory screening, including static correlators,
  Debye mass conventions, magnetic infrared scale, Polyakov loops, and
  dimensionally reduced static effective theory.
- Volume XI: rigorous RG maps on Banach spaces, covariance decomposition,
  linearization, local stable manifolds, polymer estimates, and a precise
  definition of universality class.
- Volume XII: eta invariants and global anomalies, including APS boundary
  formulae, determinant-line holonomy, Dai-Freed phases, and the interacting
  anomaly-line problem.

## Current Eighth-Chapter Pass

The eighth-chapter pass adds the first concrete model, moduli-space,
cohomological-gauge, defect, kinetic, lattice-continuum, and cosmological
development layers:

- Volume VI: sine-Gordon, massive Thirring, and affine Toda theories with
  declared normalizations, soliton sectors, breather kinematics, Coleman
  coupling convention, affine-root potentials, and model-comparison tests.
- Volume VII: supersymmetric moduli spaces as vacuum families with chiral
  rings, quotient coordinates, branch metrics, singular strata, and low-energy
  QFT data.
- Volume VIII: Witten-Donaldson theory and the Seiberg-Witten comparison,
  including the ASD deformation complex, descent observables, Coulomb-branch
  RG mechanism, monopole equations, and a QFT gap ledger.
- Volume IX: boundaries and defects as local submanifold-supported QFT data,
  including boundary expansions, interfaces, fusion, anomaly inflow, gauge
  boundary choices, and defect-refined phase invariants.
- Volume X: kinetic theory as a controlled limit from quasiparticle Wigner
  data, Boltzmann collision terms, entropy production, hydrodynamic moments,
  linearized collision operators, and gauge-theory soft-scale ledgers.
- Volume XI: lattice-to-continuum local QFT through scaling maps,
  distributional Schwinger limits, reflection positivity, local-algebra
  approximation, gauge-invariant operator mixing, and reconstruction data.
- Volume XII: cosmological spacetimes and particle creation through
  Robertson-Walker modes, complex structures, Bogoliubov transformations,
  adiabatic states, detector response, de Sitter states, and backreaction
  boundaries.

## Current Ninth-Chapter Pass

The ninth-chapter pass adds nonabelian integrable examples,
lower-dimensional supersymmetric models, categorical topological data,
categorical symmetry, anomalous transport, stochastic constructive machinery,
and microlocal curved-background analysis:

- Volume VI: \(O(N)\), Gross--Neveu, and sigma-model families through
  internal-symmetry scattering channels, projectors, asymptotic freedom,
  auxiliary-field mass-gap analysis, and bootstrap matching conditions.
- Volume VII: two-dimensional \(\mathcal N=(2,2)\) Landau--Ginzburg,
  sigma-model, and GLSM data, including chiral rings, residue pairings,
  B-type sectors, quotient phases, and infrared comparison problems.
- Volume VIII: boundaries, defects, and categories in topological QFT,
  including interval composition, defect fusion, braided line categories,
  Chern--Simons boundary data, and the BV-BFV boundary mechanism.
- Volume IX: categorical symmetry and defect fusion, including defect action
  on local operators, junction spaces, algebra-object condensation, and
  anomaly obstructions.
- Volume X: anomalous and topological transport through source variations,
  anomaly equations, Kubo definitions, equilibrium Chern--Simons terms,
  entropy constraints, and contact-term dependence.
- Volume XI: stochastic quantization and singular SPDE through Langevin
  invariant-measure identities, regularized field equations, Wick
  subtractions, \(\Phi^4_3\) dynamics, and OS-data obligations.
- Volume XII: microlocal spectrum condition and Hadamard geometry through
  wavefront sets, Hadamard parametrices, propagation of singularities, Wick
  products, and time-ordered extension freedom.

## Current Tenth-Chapter Pass

The tenth-chapter pass adds integrability-breaking bridges, lower-dimensional
supersymmetric gauge dynamics, finite-dimensional BV localization, duality
and gauging operations, nonequilibrium states, Hamiltonian numerical
regulators, and perturbative algebraic QFT on curved backgrounds:

- Volume VI: bridges to nonintegrable two-dimensional QFT and CFT through
  regulated Hamiltonian deformations, broken higher-charge conservation,
  form-factor perturbation, finite-volume widths, and truncated conformal
  space.
- Volume VII: three-dimensional supersymmetric Chern--Simons--matter theories
  through \(3D\) \(\mathcal N=2\) algebras, level quantization, vector
  multiplets, matter moment maps, parity anomaly, and monopole operators.
- Volume VIII: BV integration and finite-dimensional localization through odd
  symplectic data, Lagrangian gauge fixing, BV Laplacian identities,
  \(Q\)-exact deformation invariance, one-loop normal forms, and boundary
  terms.
- Volume IX: duality defects, gauging, and orbifold data through finite
  background fields, Dijkgraaf--Witten twists, gauging interfaces, twisted
  sectors, and charge-lattice duality walls.
- Volume X: nonequilibrium steady states and open-system limits through
  invariant positive functionals, reservoir limits, entropy production,
  weak-coupling Markovian limits, influence functionals, and hydrodynamic
  relaxation.
- Volume XI: Hamiltonian truncation, DLCQ, and benchmark protocols through
  projected Hamiltonians, Rayleigh--Ritz bounds, TCSA, light-front
  discretization, zero-mode obligations, and certified benchmark ledgers.
- Volume XII: perturbative algebraic QFT on curved backgrounds through
  microcausal functionals, Hadamard star products, time-ordered extensions,
  causal factorization, interacting fields, and local renormalization maps.

## Current Eleventh-Chapter Pass

The eleventh-chapter pass adds finite-volume spectral reconstruction,
six-dimensional supersymmetric fixed-point data, finite state-sum TQFTs,
higher-group and symmetry-TQFT organization, hydrodynamic fluctuation theory,
lattice fermion/chiral-symmetry regulators, and semiclassical backreaction:

- Volume VI: finite-volume form factors and spectral expansions through
  Bethe--Yang states, Gaudin determinants, off-diagonal and diagonal matrix
  elements, connected diagonal form factors, zero-temperature correlator
  sums, and TBA-compatible thermal series.
- Volume VII: six-dimensional superconformal theories through
  superconformal representation data, tensor-branch EFTs, anomaly
  polynomials, Green--Schwarz matching, BPS strings, and compactification
  tests.  During this pass Chapters 5 and 6 were also deepened with the NSVZ
  coordinate derivation and the finite-volume Witten-index logic for pure
  four-dimensional \(\mathcal N=1\) Yang--Mills.
- Volume VIII: finite gauge theory and state-sum TQFT through field
  groupoids, Dijkgraaf--Witten twists, triangulated cocycle weights,
  groupoid-sum state spaces, extended defects, and anomaly boundaries.
- Volume IX: higher-group symmetry and symmetry TQFT through two-group
  backgrounds, Postnikov constraints, combined gauge transformations,
  anomaly functionals, condensation, and gauging.
- Volume X: hydrodynamic fluctuations and long-time tails through stochastic
  noise, Schwinger--Keldysh diffusion actions, mode-coupling integrals,
  transport-coordinate renormalization, and microscopic theorem boundaries.
- Volume XI: lattice fermions and chiral symmetry through finite Berezin
  integrals, doubling, Wilson fermions, mid-link reflection positivity,
  Ginsparg--Wilson symmetry, overlap fermions, and determinant-line
  obligations for chiral gauge theories.
- Volume XII: semiclassical backreaction and stress-tensor fluctuations
  through renormalized stress tensors, curvature counterterm coordinates,
  linear response, noise kernels, Einstein--Langevin equations, and validity
  ledgers.

## Next Frontier After This Pass

- Add proof appendices where current chapters state theorem boundaries.
- Download and locally analyze references for factorizing models,
  superspace/supergeometry, cobordism hypothesis, constructive \(\phi^4_3\),
  singular SPDE, Schwinger--Keldysh effective actions, and locally covariant
  stress-tensor renormalization.
- Add calculation checks for superspace component expansion signs, thermal
  Matsubara sums, and simple curvature counterterm variations.

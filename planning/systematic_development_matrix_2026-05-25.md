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
| XII Curved Backgrounds | stress tensors, trace anomalies, Unruh/Hawking effects, background gauge fields and index theory | point-splitting calculations, curvature counterterm tables, Hadamard wavefront appendices |

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

## Next Frontier After This Pass

- Add proof appendices where current chapters state theorem boundaries.
- Download and locally analyze references for factorizing models,
  superspace/supergeometry, cobordism hypothesis, constructive \(\phi^4_3\),
  singular SPDE, Schwinger--Keldysh effective actions, and locally covariant
  stress-tensor renormalization.
- Add calculation checks for superspace component expansion signs, thermal
  Matsubara sums, and simple curvature counterterm variations.

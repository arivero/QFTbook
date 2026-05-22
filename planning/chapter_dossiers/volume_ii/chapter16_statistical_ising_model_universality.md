# Volume II, Chapter 16 Dossier: Statistical Ising Model And Universality

## Source Position

- Primary local source: second-sequence handwritten material, pages 136--146.
- Immediate predecessor: Wilson-Fisher fixed point and the first scaling
  operators.
- Immediate successor in the source order: Wilsonian effective actions with a
  floating cutoff.
- Role in the monograph: connect the fixed-point and scaling-operator
  construction to statistical spin systems by defining the Ising ensemble,
  its scaling limit, and the RG meaning of universality.

## Source And Reference Controls

- `SRC-QFT-PDF`: `references/253b lecture notes 2023.pdf`, pages 136--146;
  checked against rendered page images in
  `monograph/tex/build/source_visual_trace/`.
- `SRC-BEN-COMPARISON`: `references/253b transcribed lecture notes.tex`,
  corresponding Ising-universality section, used only as a comparison layer.
- `SRC-EXTERNAL`: Rosten's exact-RG review for Wilsonian terminology and
  Simmons-Duffin's bootstrap lectures for CFT scaling-operator language.
  External sources orient theorem boundaries; the chapter follows the local
  logical order.

## Construction Task

The chapter must define and derive:

- the finite-volume statistical Ising ensemble on a \(D\)-dimensional lattice;
- the role of boundary conventions in \(E(\Lambda)\) and thermodynamic
  limits;
- the equivalent finite-dimensional diagonal-operator trace notation;
- the canonical Boltzmann distribution and its maximum-entropy role;
- thermal spin correlators and the distinction among ordered, disordered, and
  critical long-distance regimes;
- spontaneous magnetization as an infinite-volume pure-phase limit;
- the correlation length and its divergence near the critical temperature;
- the critical exponents \(\Delta_\sigma\) and \(\nu\), including the
  quoted \(D=2\) and \(D=3\) values from the local source;
- the scaling limit in which lattice spin correlators become correlators of a
  continuum Ising field theory;
- the signed thermal scaling parameter \(\mathfrak m\), whose absolute value
  is the continuum inverse correlation length and whose sign records the
  high- or low-temperature side;
- the magnetic scaling coordinate and the restriction to zero magnetic
  deformation in the displayed scaling limit;
- the critical \(\mathfrak m=0\) Ising fixed point and the assumptions under
  which it is interpreted as the Ising CFT;
- the operator dictionary as a leading scaling-field expansion, with
  \(s_x\) having leading field \(\sigma\) and the subtracted lattice energy
  density having leading field \(\varepsilon\);
- the scalar-coordinate statement that \(\phi\) represents \(\sigma\) and the
  identity-subtracted mass operator \([\phi^2]\) represents \(\varepsilon\);
- the generalized Ising model with a single-site potential and continuous
  spin variable;
- the rewriting of the generalized Ising partition function as a lattice
  scalar path integral;
- the Brillouin-zone cutoff, the derivative expansion of the lattice kinetic
  term, and the lattice-anisotropic irrelevant corrections;
- universality classes as fixed-point basins after tuning relevant
  coordinates;
- the relation \(\nu=1/(D-\Delta_\varepsilon)\) from the energy deformation;
- the distinction between nonuniversal metric factors, such as the coefficient
  relating \(T-T_c\) to the thermal scaling coordinate, and universal
  exponents.

## Claim Ledger

1. A finite Ising model is a classical probability measure on spin
   configurations; diagonal-operator notation is exact finite-dimensional
   bookkeeping.
2. Canonical weights arise from maximizing entropy at fixed expected energy.
3. The low-temperature ordered phase is defined by infinite-volume limits with
   boundary conditions or a symmetry-breaking field before the thermodynamic
   limit.
4. Critical spin correlators define the spin scaling dimension
   \(\Delta_\sigma\).
5. The scaling limit of near-critical lattice correlators produces Euclidean
   correlators of a continuum Ising field theory.
6. At criticality the inverse correlation length vanishes; with the usual
   rotation, scale, and stress-tensor assumptions the limiting fixed point is
   the Ising CFT.
7. The generalized Ising model can be written as a scalar lattice path
   integral with a finite UV cutoff and many local couplings.
8. Lattice anisotropy and higher-derivative terms are irrelevant at the Ising
   fixed point in \(D=2,3\).
9. The temperature perturbation couples to the energy operator, whose dimension
   determines the correlation-length exponent.
10. In the \(\mathbb Z_2\)-even slice, only the thermal relevant coordinate
    must be tuned; without the symmetry, the magnetic coordinate is also
    relevant.

## Figure Requirements

- Lattice-spin ensemble and finite-volume trace representation.
- Spin correlator regimes below, at, and above the critical temperature.
- Scaling-limit map from lattice spin insertions to continuum Ising-field
  correlators, with the signed thermal scaling parameter recorded.
- Generalized Ising model as a cutoff scalar path integral with Brillouin-zone
  support and a lattice derivative expansion.
- RG universality diagram showing Ising lattice actions and scalar
  \(\phi^4\)-type actions flowing to the same critical fixed point in the
  \(\mathbb Z_2\)-even slice after tuning the thermal relevant direction.

## Audit Notes

- Do not state or imply that the statistical spin Hilbert space is the
  Lorentzian QFT Hilbert space.
- Do not present universality as microscopic equality.
- Do not identify a microscopic lattice observable literally with a continuum
  field; use the scaling-field expansion and state nonuniversal normalizations.
- Do not erase the sign of the thermal deformation in the massive scaling
  limit.
- Keep Wilsonian cutoff-flow equations for the next chapter.
- No reader-facing source-page references or course-note references.

# Volume IX, Chapter 2 Dossier: Extended Operators And Topological Defects
Source-File: monograph/tex/volumes/volume_ix/chapter02_extended_operators_and_topological_defects.tex

## Logical Role

- Role in the monograph: develop extended operators immediately after global
  forms and higher-form symmetry, before the analytic construction of line,
  surface, and wall operators.
- Immediate predecessor: global form, genuine line operators, and linking
  action of higher-form symmetry.
- Immediate successor: confinement, screening, anomaly inflow, and phases.

## Definitions And Results

- Extended operator as renormalized correlation-functional datum supported on
  an embedded submanifold with tubular-neighborhood normal model, defect
  fields, counterterms, and bulk-to-defect OPE.
- Genuine defects, higher-dimensional bounding defects, endpoints, and
  junctions as lower-dimensional Hom objects.
- Displacement operator from the stress-tensor Ward identity in the presence
  of a defect.
- Shape-variation proposition deriving the displacement insertion formula.
- Topological defect as isotopy-invariant defect insertion, with the
  displacement criterion and the cohomological `Q`-exact variant.
- Fusion through tubular-neighborhood collision, including group-like finite
  symmetry defects and associativity data.
- Higher-form Ward operators acting on charged defects by local integer
  linking, with the global action separated into degree-\(p\)
  holonomy/transgression data, background characteristic classes, and torsion
  \(\mathbb Q/\mathbb Z\) linking where applicable.
- Defect locality and braiding, including Wilson/'t Hooft electric-magnetic
  pairing.
- Defect-completion data as part of a full nonperturbative QFT definition.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(M\) | spacetime |
| \(\Sigma^p\) | \(p\)-dimensional support of an extended operator |
| \(N_{\Sigma/M}\) | normal bundle of the support |
| \(T_\varepsilon(\Sigma)\) | tubular neighborhood of the support |
| \(W(\Sigma)\) | extended operator |
| \(D_1,D_2\) | topological defects |
| \(\mathcal D^i\) | displacement operator |
| \(U_a(N^{D-p-1})\) | higher-form symmetry defect |
| \(q\in\widehat A\) | character associated to charge \(q\) |
| \(\operatorname{Link}_{\rm loc}(N,\Sigma)\) | local or controlled-chart integer linking number |
| \([B]\in H^{p+1}(M;A)\) | characteristic class of a finite \(p\)-form background, evaluable on \((p+1)\)-cycles |
| \(\check B\) | cochain or differential-cohomology representative with declared \(p\)-cycle holonomy |
| \(B\in Z^{p+1}(M;A)\) | cocycle representative of the finite \(p\)-form background before quotienting by coboundaries |
| \(\xi\in C^p(M;A)\) | arbitrary background gauge cochain, with \(B\mapsto B+\delta\xi\) |
| \(\alpha\in Z^p(M;A)\) | closed global higher-form symmetry parameter acting at fixed background |
| \(\tau_a\) | relative/Thom class of a codimension-\((p+1)\) symmetry defect before transgression |
| \(\lambda_{\rm tor}\) | torsion linking pairing with values in \(\mathbb Q/\mathbb Z\) |

## Claim Ledger

1. Extended-operator definitions include support, normal data, singular
   behavior, defect fields, counterterms, correlators, and bulk-to-defect OPE.
2. The displacement operator is the defect-local term in the normal
   stress-tensor Ward identity.
3. Shape variation of a defect correlator equals the integrated displacement
   insertion under explicit boundary and insertion-separation assumptions.
4. Vanishing or `Q`-exact displacement gives isotopy invariance in the
   corresponding physical or cohomological sector.
5. Fusion is a correlation-function limit inside a tubular neighborhood, with
   associators and unit defects included in the defect data.
6. Screening is an operator statement about allowed endpoints.
7. Higher-form symmetry acts on charged defects through local integer linking
   only in a ball, \(S^D\), \(\mathbb R^D\) with compact support, or a declared
   bounding-chain chart whose ambiguity vanishes.  On general \(M\), the
   characteristic class \([B]\in H^{p+1}(M;A)\) is not evaluated directly on a
   charged \(p\)-cycle.  Operator phases use a declared \(p\)-cycle holonomy,
   an arbitrary gauge cochain \(\xi\) for background-gauge covariance, a closed
   fixed-background symmetry cocycle \(\alpha\), or a transgressed complement
   datum, with torsion wrapping data valued in \(\mathbb Q/\mathbb Z\).
8. Defect completion data record the genuine extended operators, boundaries,
   junctions, and fusion limits included in the theory.

## Calculation Checks

- `calculation-checks/extended_defect_ward_checks.py` verifies finite
  `Z_N` group-like fusion, Ward phase multiplicativity, orientation and charge
  reversal, dimension bookkeeping for linking/intersection, local meridian
  integer recovery, nonbounding \(T^3\) loop and bounding-chain ambiguity
  negative controls, torsion \(\mathbb Q/\mathbb Z\) linking bilinearity, the
  degree/type rejection of \(H^{p+1}\) evaluation on an \(H_p\) cycle,
  degree-\(p\) holonomy evaluation on noncontractible cycles, separation of
  arbitrary gauge cochains from closed symmetry cocycles, transgression of a
  codimension-\((p+1)\) defect class to the local linking action, and junction
  charge conservation.

## Audit Notes

- 2026-06-08 issue #880 pass: restricted the linking-number Ward formula to
  local/spherical or explicitly controlled bounding-chain charts.  The chapter
  now records the bounding-chain independence condition, treats nonbounding
  global cycles by higher-form background evaluation, and separates torsion
  linking as a \(\mathbb Q/\mathbb Z\) pairing rather than an integer.  The
  companion check now includes the requested \(T^3\), bounding-chain ambiguity,
  and local meridian negative/positive controls.
- 2026-06-08 issue #961 pass: corrected the global higher-form action typing.
  A background characteristic class \([B]\in H^{p+1}(M;A)\) is now separated
  from evaluable \(p\)-cycle holonomy data, degree-\(p\) action data, and
  transgressed defect-complement data.  The companion check rejects direct
  evaluation of an \(H^{p+1}\) class on an \(H_p\) charged cycle.
- 2026-06-08 issue #964 cochain/cocycle split: separated the background gauge
  cochain \(\xi\in C^p(M;A)\), which can have \(\delta\xi\ne0\) and shifts a
  representative \(B\), from the closed global symmetry cocycle
  \(\alpha\in Z^p(M;A)\), which has \(\delta\alpha=0\), leaves \(B\) fixed, and
  acts on charged \(p\)-cycles by evaluation.  The companion now checks a finite
  cochain Stokes covariance example and rejects treating a closed cocycle as a
  nonzero background coboundary shift.

## Figures

- The chapter includes a TikZ figure showing tubular-neighborhood support, a
  defect-local insertion on \(\Sigma\), defect fusion, and a linking
  configuration.

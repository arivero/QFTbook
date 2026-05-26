# Volume IX, Chapter 2 Dossier: Extended Operators And Topological Defects

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
- Higher-form Ward operators acting on charged defects by linking, with a
  proof from crossing and character evaluation.
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
| \(\operatorname{Link}(N,\Sigma)\) | linking number |

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
7. Higher-form symmetry acts on charged defects through the linking number and
   the character pairing.
8. Defect completion data record the genuine extended operators, boundaries,
   junctions, and fusion limits included in the theory.

## Calculation Checks

- `calculation-checks/extended_defect_ward_checks.py` verifies finite
  `Z_N` group-like fusion, Ward phase multiplicativity, orientation and charge
  reversal, dimension bookkeeping for linking/intersection, and junction
  charge conservation.

## Figures

- The chapter includes a TikZ figure showing tubular-neighborhood support,
  defect fusion, and a linking configuration.

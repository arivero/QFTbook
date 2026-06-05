# Volume II, Lattice Yang-Mills as a Nonperturbative Formulation Dossier

## Source Position

- Manuscript file:
  `monograph/tex/volumes/volume_ii/chapter17b_lattice_yang_mills_nonperturbative_definition.tex`.
- Logical insertion point: after the classical local Yang--Mills construction
  and before covariant gauge fixing, ghosts, BRST, BV, and QCD perturbation
  theory.
- Role in the monograph: provide the finite-dimensional compact Haar integral
  formulation of pure Yang--Mills theory, state exactly what is rigorous at
  finite lattice spacing, state the central pure Yang--Mills conjecture by
  separating continuum existence, vacuum structure, mass gap, line-sector
  confinement, and spectral sectors, and frame
  covariant BRST/BV material as perturbative and cohomological machinery to be
  matched to gauge-invariant lattice observables.

## Source And Reference Controls

- `SRC-ISSUE-263`: GitHub issue #263, including Xi's directive that lattice
  Yang--Mills belongs in the Yang--Mills volume as the primary
  nonperturbative regulator-level formulation.
- `SRC-LOCAL`: classical Yang--Mills conventions from
  `chapter17_yang_mills_theory_and_matter_fields.tex`, especially Hermitian
  generators, \(F_{\mu\nu}\), and the \(SU(N)\) trace normalization.
- `SRC-LOCAL-OS`: Osterwalder--Schrader reconstruction chapter, used for the
  reflection-positivity bridge from finite lattice measures to Hilbert-space
  reconstruction.
- External literature to consult in later proof passes: Wilson lattice gauge
  theory, Osterwalder--Seiler reflection positivity, strong-coupling character
  expansions, Symanzik improvement, Nielsen--Ninomiya, Ginsparg--Wilson, and
  Ba{\l}aban's multiscale construction program.  These references are
  guardrails; finite-cutoff definitions and status distinctions are written
  explicitly in the manuscript.

## Construction Task

The chapter must define and derive:

- the periodic hypercubic lattice \(\Lambda_{a,L}\), oriented links, inverse
  orientations, and the finite configuration space \(G^{E^+(\Lambda)}\);
- the lattice gauge group \(G^\Lambda\) and its endpoint action on link
  variables;
- the oriented plaquette variable \(U_{\mu\nu}(x)\) and its conjugation
  covariance under lattice gauge transformations;
- the Wilson action
  \(S_W=(\beta/N)\sum_P\operatorname{Re}\operatorname{tr}(1-U_P)\) with
  \(\beta=N/g_0^2\) in the monograph/stringbook trace normalization
  \(\operatorname{tr}(t^a t^b)=\delta^{ab}\);
- the finite compact Haar integral for \(Z_\Lambda(\beta)\) and expectation
  values of gauge-invariant observables;
- the smooth-field expansion of the plaquette and the recovery of
  \((4g_0^2)^{-1}\int\operatorname{tr}F_{\mu\nu}F_{\mu\nu}\);
- Wilson-loop observables, character expansion, Haar orthogonality, and the
  leading tiled-surface mechanism for the strong-coupling area law;
- the finite-lattice reflection-positivity theorem and its transfer-matrix
  consequence;
- the finite-temperature lattice, exact thermal center symmetry of pure
  \(SU(N)\), the Polyakov loop, its \(N\)-ality transformation, the
  infinite-volume order-parameter limit, static-source free-energy
  interpretation, and the distinction from the zero-temperature Wilson-loop
  area law;
- the asymptotic-scaling relation
  \(a\Lambda_L=\exp[-1/(2\beta_0g_0^2)]
  (\beta_0g_0^2)^{-\beta_1/(2\beta_0^2)}(1+O(g_0^2))\);
- the operator-basis/tuning analysis for pure CP-even \(SU(N)\) Yang--Mills,
  including the identity term, \(F^2\), and the separate \(\theta\)-parameter;
- Symanzik improvement as a classification of irrelevant lattice artifacts;
- lattice topological charge and the distinction among plaquette, geometric,
  gradient-flow, and Ginsparg--Wilson definitions;
- naive fermion doubling, the Nielsen--Ninomiya obstruction, Wilson,
  staggered, domain-wall, and overlap/Ginsparg--Wilson responses;
- the precise central conjecture needed for the four-dimensional continuum
  limit, theta-dependent vacuum structure, positive local mass gap,
  line-sector confinement, and glueball/flux-tube spectra.

## Claim Ledger

1. A finite Wilson lattice gauge theory is a finite-dimensional compact
   integral with exact gauge invariance and normalized Haar measure.
2. The plaquette is the lattice curvature: it transforms by conjugation at its
   basepoint and has classical expansion
   \(U_{\mu\nu}=\exp(i a^2F_{\mu\nu}+O(a^3))\).
3. The Wilson action recovers the Euclidean Yang--Mills action on smooth
   fields up to \(O(a^2)\) corrections.
4. Osterwalder--Seiler reflection positivity for the Wilson action gives a
   positive finite-lattice transfer matrix and a Hilbert-space interpretation
   at finite cutoff.
5. Pure thermal \(SU(N)\) Wilson lattice gauge theory has an exact
   \(\mathbb Z_N\) center symmetry acting on temporal links crossing one time
   slice; the fundamental Polyakov loop carries the fundamental center
   character and is a sharp order parameter only after the infinite spatial
   volume and small source limits are taken in the correct order.
6. The Polyakov loop computes the free energy of a static external source up
   to its line self-energy renormalization, and the Polyakov-loop pair
   correlator computes the static source-antisource free energy.
7. Dynamical matter with nonzero \(N\)-ality explicitly breaks the
   corresponding center subgroup, so the fundamental Polyakov loop ceases to
   be an exact order parameter in QCD with fundamental quarks.
8. The strong-coupling character expansion yields a rigorous area-law bound
   for sufficiently small \(\beta\) in the finite-cutoff lattice theory.
9. The central pure Yang--Mills conjecture separates continuum local-QFT
   existence, theta-dependent vacuum structure, a positive local mass gap,
   confinement for nonzero \(N\)-ality line sectors, and glueball/flux-tube
   spectral sectors.
10. A mass gap in the gauge-invariant local Hilbert space does not by itself
   prove line-operator confinement, and the small-\(\beta\) strong-coupling
   area-law theorem does not prove the weak-coupling continuum conjecture.
11. Pure CP-even \(SU(N)\) Yang--Mills on an isotropic Wilson lattice has one
   running parameter, \(g_0(a)\), after vacuum-energy normalization; \(\theta\)
   is a separate topological parameter when included.
12. Different gauge-invariant lattice actions with the same symmetries differ
   by irrelevant operators and by scale matching, with Symanzik improvement
   organizing the power of \(a\) at which artifacts enter.
13. Lattice definitions of the \(\theta\)-term require regulator choices beyond
   the plaquette action because naive topological charge is not integer-valued
   at finite cutoff.
14. Chiral fermions require care on the lattice because locality,
    translational invariance, Hermiticity, and exact naive chiral symmetry
    imply species doubling.
15. BRST and BV chapters are perturbative/cohomological frameworks whose
    relation to the nonperturbative Yang--Mills theory is through
    gauge-invariant observable matching and the central pure Yang--Mills
    conjecture.

## Figure Requirements

- Plaquette covariance figure showing endpoint gauge transformations, the
  ordered plaquette product, and conjugation at the basepoint.
- Thermal center-symmetry/Polyakov-loop figure showing a time-slice center
  transformation, plaquette invariance, and the center phase of a winding
  Polyakov loop.
- Fermion-doubling figure showing Brillouin-zone zeros of the naive lattice
  derivative.
- Future expansion target: scaling-trajectory figure relating strong coupling,
  weak coupling, lattice artifacts, and the central pure Yang--Mills
  conjecture.
- Future expansion target: table or flow diagram for lattice fermion
  formulations and their symmetry/tuning tradeoffs.

## Audit Notes

- 2026-05-24 issue #263 pass: added the chapter as the foundational
  finite-cutoff Yang--Mills formulation in Volume IV's current assembly.
- The chapter deliberately separates finite-lattice theorems from the
  four-dimensional continuum-limit, mass-gap, and confinement conjecture.
- The phase-structure paragraph avoids upgrading numerical or action-dependent
  evidence into a theorem and flags bulk lattice-artifact transitions.
- The BRST and QCD chapters now cross-reference this chapter for the
  nonperturbative regulator-level formulation and for the strong-coupling
  Wilson-loop area-law result.
- 2026-05-25 issue #467 pass: added the finite-temperature center-symmetry
  and Polyakov-loop framework, including the finite-lattice symmetry proof,
  infinite-volume order parameter, static-source free-energy interpretation,
  center-breaking by nonzero \(N\)-ality matter, and a calculation check for
  center phases.
- 2026-06-05 issue #798 pass: replaced the old continuum-limit hypothesis
  with the named central pure Yang--Mills conjecture, separating continuum
  existence, theta-vacuum data, local mass gap, line-sector confinement, and
  glueball/flux-tube spectra.  The dossier now records explicitly that
  mass gap does not imply confinement and that the strong-coupling area law is
  evidence at finite cutoff rather than a continuum proof.
